from src.sender import send_notification


def test_sender():
    expected_msg = "test"
    user = "test"

    result = send_notification(user, expected_msg)

    assert result == expected_msg
