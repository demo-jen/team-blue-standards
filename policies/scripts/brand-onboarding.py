# Script to onboard new brands into the Team.blue ecosystem
from datetime import datetime
from typing import Dict, Optional
from collections import deque

# FIX: Use a bounded deque instead of unbounded list to prevent memory leak
# Previous implementation accumulated events indefinitely
MAX_EVENTS_IN_MEMORY = 100
_event_cache = deque(maxlen=MAX_EVENTS_IN_MEMORY)

def track_event(event_type: str, session_id: str, timestamp: Optional[str] = None) -> Dict:
    """
    Track granular events with session information.
    
    Args:
        event_type: Type of event (e.g., "vote_changed", "brand_created")
        session_id: Session identifier to track behavior across brands
        timestamp: ISO format timestamp, defaults to current time
    
    Returns:
        Dict with event structure
    """
    if timestamp is None:
        timestamp = datetime.now().isoformat()
    
    event = {
        "event_type": event_type,
        "session_id": session_id,
        "timestamp": timestamp
    }
    
    # FIX: Prevent memory leak by limiting cache size
    # deque with maxlen automatically removes oldest when full
    _event_cache.append(event)
    
    return event

def onboard_brand(brand_name: str, session_id: Optional[str] = None) -> Dict:
    """
    Onboard a new brand into the Team.blue ecosystem.
    
    Args:
        brand_name: Name of the brand to onboard
        session_id: Optional session ID for tracking
    
    Returns:
        Event tracking data
    """
    print(f"Starting onboarding for {brand_name}...")
    
    # Generate session_id if not provided
    if session_id is None:
        session_id = f"{brand_name}-{datetime.now().strftime('%Y%m%d%H%M%S%f')}"
    
    # Track the onboarding event
    event = track_event("brand_onboarding_started", session_id)
    
    # Simulate onboarding process
    print(f"Brand {brand_name} onboarded successfully with session {session_id}")
    
    return event

def get_cached_events() -> list:
    """
    Get the currently cached events.
    Useful for monitoring and debugging.
    
    Returns:
        List of recent events (max MAX_EVENTS_IN_MEMORY)
    """
    return list(_event_cache)

def clear_event_cache() -> None:
    """
    Clear the event cache.
    Should be called periodically to free memory.
    """
    _event_cache.clear()
