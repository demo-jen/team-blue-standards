"""
Tests for brand-onboarding.py
"""
import unittest
from unittest.mock import patch, Mock
import sys
import os

# Add the current directory to Python path to import the module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the module by executing it
import importlib.util
spec = importlib.util.spec_from_file_location("brand_onboarding", "brand-onboarding.py")
brand_onboarding = importlib.util.module_from_spec(spec)
spec.loader.exec_module(brand_onboarding)
verify_merchant_banking_gateway = brand_onboarding.verify_merchant_banking_gateway

class TestMerchantBankingGateway(unittest.TestCase):
    """Test cases for merchant banking gateway verification"""

    def setUp(self):
        """Set up test data"""
        self.merchant_data = {
            'merchant_id': 'TEST123',
            'merchant_name': 'Test Merchant',
            'account_details': 'FI1234567890'
        }

    @patch('requests.post')
    def test_finnish_gateway_timeout_is_30_seconds(self, mock_post):
        """Test that Finnish gateway uses 30 second timeout"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        verify_merchant_banking_gateway(self.merchant_data, region='FI')

        # Verify the timeout argument is 30 seconds
        mock_post.assert_called_once()
        call_kwargs = mock_post.call_args[1]
        self.assertEqual(call_kwargs['timeout'], 30)

    @patch('requests.post')
    def test_default_gateway_timeout_is_5_seconds(self, mock_post):
        """Test that default (non-Finnish) gateway uses 5 second timeout"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        verify_merchant_banking_gateway(self.merchant_data, region='EU')

        # Verify the timeout argument is 5 seconds
        mock_post.assert_called_once()
        call_kwargs = mock_post.call_args[1]
        self.assertEqual(call_kwargs['timeout'], 5)

    @patch('requests.post')
    def test_merchant_region_field_in_payload(self, mock_post):
        """Test that merchant_region field is included in the JSON payload"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        verify_merchant_banking_gateway(self.merchant_data, region='FI')

        # Verify the payload includes merchant_region field
        mock_post.assert_called_once()
        call_kwargs = mock_post.call_args[1]
        payload = call_kwargs['json']
        self.assertIn('merchant_region', payload)
        self.assertEqual(payload['merchant_region'], 'FI')

    @patch('requests.post')
    def test_payload_structure(self, mock_post):
        """Test that the payload has all required fields"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        verify_merchant_banking_gateway(self.merchant_data, region='FI')

        # Verify all required fields are in the payload
        call_kwargs = mock_post.call_args[1]
        payload = call_kwargs['json']
        self.assertIn('merchant_id', payload)
        self.assertIn('merchant_name', payload)
        self.assertIn('account_details', payload)
        self.assertIn('merchant_region', payload)
        self.assertEqual(payload['merchant_id'], 'TEST123')
        self.assertEqual(payload['merchant_name'], 'Test Merchant')
        self.assertEqual(payload['account_details'], 'FI1234567890')


if __name__ == '__main__':
    unittest.main()
