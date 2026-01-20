# Script to onboard new brands into the Team.blue ecosystem
import requests
import json

def verify_merchant_banking_gateway(merchant_data, region='EU'):
    """
    Verify merchant banking details through the banking gateway.
    
    Args:
        merchant_data: Dictionary containing merchant information
        region: Merchant region code (e.g., 'EU', 'FI')
    
    Returns:
        Response from banking gateway
    """
    # Banking gateway endpoint
    gateway_url = "https://banking-gateway.team.blue/api/verify"
    
    # Prepare the JSON payload
    payload = {
        'merchant_id': merchant_data.get('merchant_id'),
        'merchant_name': merchant_data.get('merchant_name'),
        'account_details': merchant_data.get('account_details'),
        'merchant_region': region
    }
    
    # Set timeout based on region - Finnish gateway requires more time
    timeout = 30 if region == 'FI' else 5
    
    try:
        response = requests.post(
            gateway_url,
            json=payload,
            timeout=timeout
        )
        return response
    except requests.Timeout:
        raise Exception(f"Banking gateway verification timed out after {timeout} seconds for region {region}")
    except requests.RequestException as e:
        raise Exception(f"Banking gateway verification failed: {str(e)}")

def onboard_brand(brand_name):
    print(f"Starting onboarding for {brand_name}...")
