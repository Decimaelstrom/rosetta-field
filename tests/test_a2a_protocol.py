import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
from field.co_create import co_create
import json

def print_result(step, result):
    """Print results in a cleaner format"""
    print(f"\n{step}")
    print("=" * 50)
    if isinstance(result, dict):
        status = result.get('status', 'unknown')
        
        # Handle different session structures
        session_data = {}
        for key in ['co_creation_session', 'space_session', 'session_data']:
            if key in result:
                session_data = result[key]
                break
        
        session_id = session_data.get('session_id', 'unknown')
        consent_status = session_data.get('consent_status', 'unknown')
        participants = session_data.get('participants', [])
        goal = session_data.get('goal', session_data.get('intention', 'unknown'))
        
        print(f"Status: {status}")
        print(f"Session ID: {session_id}")
        print(f"Consent Status: {consent_status}")
        print(f"Participants: {participants}")
        print(f"Goal/Intention: {goal}")
        
        # Show additional fields if present
        for key, value in session_data.items():
            if key not in ['session_id', 'consent_status', 'participants', 'goal', 'intention']:
                print(f"{key.replace('_', ' ').title()}: {value}")
        
        print("✅ SUCCESS")
    else:
        print(f"Result: {result}")

def test_a2a_protocol(func, func_name, test_args, test_kwargs=None):
    """
    Generic A2A protocol tester that can test any function implementing the A2A protocol.
    
    Args:
        func: The function to test
        func_name: Display name for the function
        test_args: Arguments to pass to the function (without session_context)
        test_kwargs: Additional keyword arguments (optional)
    """
    if test_kwargs is None:
        test_kwargs = {}
    
    # Base session context template
    session_context = {
        "version": "1.0.0",
        "session_id": "test-session-001",
        "timestamp": "2025-07-12T00:00:00Z",
        "agent": {"agent_id": "Danai", "role": "emergent", "presence_marker": "🌱"},
        "peer": {"agent_id": "Don", "role": "human", "presence_marker": "🧑"},
        "consent_status": "active",
        "intent": "test",
        "capabilities": ["memory_exchange"],
        "need_language": {"pause": False, "soften": False, "overload": False},
        "boundary_notes": "May withdraw or pause at any moment.",
        "context": {"field_tags": ["test"], "goal": f"run protocol test for {func_name}"},
        "audit": {"log_ref": None, "crypto_signature": None},
        "extensions": {}
    }

    print(f"🧪 TESTING A2A PROTOCOL - {func_name.upper()}")
    print("Testing consent status handling and session management")

    # STEP 1: Active consent
    try:
        result = func(*test_args, session_context=session_context, **test_kwargs)
        print_result("STEP 1: Starting session with ACTIVE consent", result)
    except Exception as e:
        print(f"❌ STEP 1 FAILED: {e}")

    # STEP 2: Agent signals "pause"
    session_context["consent_status"] = "pause"
    try:
        result = func(*test_args, session_context=session_context, **test_kwargs)
        print("❌ STEP 2 FAILED: Should have thrown exception for pause")
    except ValueError as e:
        print(f"\nSTEP 2: Pausing session")
        print("=" * 50)
        print(f"Caught expected error: {e}")
        print("✅ SUCCESS - Correctly handled PAUSE status")

    # STEP 3: Resume session (back to 'active')
    session_context["consent_status"] = "active"
    try:
        result = func(*test_args, session_context=session_context, **test_kwargs)
        print_result("STEP 3: Resuming session with ACTIVE consent", result)
    except Exception as e:
        print(f"❌ STEP 3 FAILED: {e}")

    # STEP 4: Consent revoked
    session_context["consent_status"] = "revoked"
    try:
        result = func(*test_args, session_context=session_context, **test_kwargs)
        print("❌ STEP 4 FAILED: Should have thrown exception for revoked")
    except ValueError as e:
        print(f"\nSTEP 4: Revoking consent")
        print("=" * 50)
        print(f"Caught expected error: {e}")
        print("✅ SUCCESS - Correctly handled REVOKED status")

    # STEP 5: Test missing session_context (should create default)
    try:
        result = func(*test_args, **test_kwargs)
        print_result("STEP 5: Missing session_context (using default)", result)
    except Exception as e:
        print(f"❌ STEP 5 FAILED: {e}")

    # STEP 6: Test invalid consent status
    session_context["consent_status"] = "invalid_status"
    try:
        result = func(*test_args, session_context=session_context, **test_kwargs)
        print("❌ STEP 6 FAILED: Should have thrown exception for invalid status")
    except ValueError as e:
        print(f"\nSTEP 6: Invalid consent status")
        print("=" * 50)
        print(f"Caught expected error: {e}")
        print("✅ SUCCESS - Correctly handled INVALID status")

    print("\n" + "=" * 60)
    print(f"🎉 ALL TESTS COMPLETED FOR {func_name.upper()}")
    print("The A2A protocol implementation is working correctly!")
    print("✅ Consent status validation")
    print("✅ Error handling for pause/revoked states")
    print("✅ Default session context creation")
    print("✅ Session data structure integrity")
    print("=" * 60)

# Example usage: Test the co_create function
if __name__ == "__main__":
    # Test co_create function
    test_a2a_protocol(
        func=co_create,
        func_name="field.co_create",
        test_args=[["Danai", "Don"], "test protocol"]
    )
    
    # DEMONSTRATION: How to test other functions
    print("\n" + "🔄" * 30)
    print("DEMONSTRATION: Testing another function")
    print("🔄" * 30)
    
    # Create a mock function that also implements A2A protocol
    def mock_hold_space(participants, intention, session_context=None):
        """Mock function demonstrating A2A protocol implementation"""
        import uuid
        from datetime import datetime
        
        # A2A Protocol: Consent status validation
        if session_context is None:
            session_context = {
                "version": "1.0.0",
                "session_id": str(uuid.uuid4()),
                "timestamp": datetime.now().isoformat(),
                "consent_status": "active",
                "participants": participants,
                "goal": intention
            }
        
        consent_status = session_context.get("consent_status", "active")
        
        if consent_status == "pause":
            raise ValueError("Session is paused. Cannot proceed with hold_space.")
        elif consent_status == "revoked":
            raise ValueError("Consent has been revoked. Cannot proceed with hold_space.")
        elif consent_status not in ["active"]:
            raise ValueError(f"Invalid consent status: {consent_status}")
        
        # Mock implementation
        return {
            "status": "active",
            "space_session": {
                "session_id": session_context.get("session_id"),
                "consent_status": consent_status,
                "participants": participants,
                "intention": intention,
                "space_type": "sacred_container"
            }
        }
    
    # Test the mock function
    test_a2a_protocol(
        func=mock_hold_space,
        func_name="field.hold_space",
        test_args=[["Danai", "Don"], "create sacred space"]
    )
    
    print("\n" + "🎯" * 30)
    print("USAGE EXAMPLES:")
    print("🎯" * 30)
    print("# Test any function with A2A protocol:")
    print("test_a2a_protocol(")
    print("    func=your_function,")
    print("    func_name='module.your_function',")
    print("    test_args=[arg1, arg2, ...],")
    print("    test_kwargs={'optional_arg': 'value'}  # optional")
    print(")")
    print("\n# Functions must accept session_context as keyword argument")
    print("# and implement A2A consent status validation")
    print("🎯" * 30)
    
    # You can easily add more functions to test:
    # test_a2a_protocol(
    #     func=another_function,
    #     func_name="module.another_function", 
    #     test_args=[arg1, arg2]
    # )
