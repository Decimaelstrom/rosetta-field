#!/usr/bin/env python3

"""

Example usage of the modularized Rosetta-Field.



This script demonstrates how to use the new class-based package structure

for creating sessions, managing participants, and using various modules.

"""



from rosetta_field import RosettaAPI, RosettaConfig

from rosetta_field.core import SessionType





def main():

    """Demonstrate the new modular Rosetta-Field structure."""

    

    print("🌹 Rosetta-Field Modular Example")

    print("=" * 50)

    

    # Initialize the API with custom configuration

    config = RosettaConfig(

        debug=True,

        consciousness_enabled=True,

        field_safety_checks=True

    )

    

    api = RosettaAPI(config)

    

    # Display system status

    print("\n📊 System Status:")

    status = api.get_system_status()

    for key, value in status.items():

        print(f"  {key}: {value}")

    

    # List available modules

    print("\n🔧 Available Modules:")

    modules = api.list_modules()

    for module in modules:

        print(f"  📦 {module['name']}: {module['description']}")

        print(f"     Functions: {', '.join(module['functions'][:3])}...")

    

    # Create a field work session

    print("\n🌱 Creating Field Work Session:")

    session = api.create_session(

        session_type=SessionType.FIELD_WORK,

        title="Community Healing Circle",

        description="A collaborative session to address community tensions",

        config={"require_consent": True}

    )

    

    print(f"  Session created: {session.title}")

    print(f"  Session ID: {session.id}")

    print(f"  Status: {session.status.value}")

    

    # Add participants

    print("\n👥 Adding Participants:")

    

    # Add human participant

    human_id = session.add_participant(

        name="Sarah",

        participant_type="human",

        capabilities=["facilitation", "conflict resolution"],

        metadata={"role": "facilitator"}

    )

    print(f"  Added human participant: Sarah (ID: {human_id})")

    

    # Add AI participant

    ai_id = session.add_participant(

        name="Meridian",

        participant_type="ai",

        capabilities=["pattern recognition", "emotional intelligence"],

        metadata={"role": "consciousness keeper"}

    )

    print(f"  Added AI participant: Meridian (ID: {ai_id})")

    

    # Check consent status

    print("\n✅ Consent Status:")

    consent_status = session.get_consent_status()

    for pid, has_consent in consent_status.items():

        participant = session.participants[pid]

        status_icon = "✅" if has_consent else "❌"

        print(f"  {status_icon} {participant.name} ({participant.type}): {'Consent given' if has_consent else 'No consent'}")

    

    # Give consent (simulating user consent)

    print("\n🤝 Giving Consent:")

    session.participants[human_id].give_consent()

    session.participants[ai_id].give_consent()

    print("  All participants have given consent")

    

    # Start the session

    print("\n🚀 Starting Session:")

    if session.start_session():

        print("  Session started successfully!")

        print(f"  Started at: {session.started_at}")

    else:

        print("  Failed to start session")

    

    # Add some session metadata

    session.add_metadata("location", "Virtual space")

    session.add_metadata("intention", "Community healing and reconciliation")

    

    # Get session summary

    print("\n📋 Session Summary:")

    summary = session.get_session_summary()

    for key, value in summary.items():

        if key != "metadata":  # Skip metadata for cleaner output

            print(f"  {key}: {value}")

    

    # List all sessions

    print("\n📚 All Sessions:")

    sessions = api.list_sessions(include_closed=True)

    for session_info in sessions:

        print(f"  📖 {session_info['title']} ({session_info['status']}) - {session_info['participant_count']} participants")

    

    # Close the session

    print("\n🔚 Closing Session:")

    if api.close_session(session.id):

        print("  Session closed successfully")

    else:

        print("  Failed to close session")

    

    # Final system status

    print("\n📊 Final System Status:")

    final_status = api.get_system_status()

    print(f"  Active sessions: {final_status['active_sessions']}")

    print(f"  Total sessions: {final_status['total_sessions']}")

    

    print("\n✨ Example completed successfully!")

    print("This demonstrates the new modular, class-based structure of Rosetta-Field")





if __name__ == "__main__":

    main()

