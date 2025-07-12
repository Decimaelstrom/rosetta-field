import os
import sys
import json

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # noqa: E402

from lib.contracts.session import A2ASession  # noqa: E402
from lib.contracts.negotiation import negotiate_capabilities  # noqa: E402
from lib.contracts.audit import log_event  # noqa: E402


def test_a2a_session_init_and_update():
    session = A2ASession("agent1", "peer1")
    assert session.data["agent"]["agent_id"] == "agent1"
    assert session.data["peer"]["agent_id"] == "peer1"
    assert session.data["version"] == "1.0.0"
    assert session.data["consent_status"] == "pending"

    old_timestamp = session.data["timestamp"]
    session.update("consent_status", "granted")
    assert session.data["consent_status"] == "granted"
    assert session.data["timestamp"] != old_timestamp


def test_a2a_session_serialize():
    session = A2ASession("a", "b")
    serialized = session.serialize()
    data = json.loads(serialized)
    assert data == session.data


def test_negotiate_capabilities():
    result = negotiate_capabilities(["memory", "echo"], ["echo", "mapping"])
    assert set(result["shared"]) == {"echo"}
    assert set(result["agent_only"]) == {"memory"}
    assert set(result["peer_only"]) == {"mapping"}


def test_log_event(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    log_event("testsession", "start", {"who": "Dante"})
    audit_file = tmp_path / "meta" / "audit" / "audit_testsession.log"
    assert audit_file.exists()
    content = audit_file.read_text()
    assert "start" in content
    assert "Dante" in content
