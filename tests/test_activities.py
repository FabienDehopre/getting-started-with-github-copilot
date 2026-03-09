from fastapi.testclient import TestClient


def test_get_activities_returns_200(client: TestClient):
    # Arrange
    url = "/activities"

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 200


def test_get_activities_returns_all_nine(client: TestClient):
    # Arrange
    url = "/activities"

    # Act
    response = client.get(url)

    # Assert
    data = response.json()
    assert len(data) == 9


def test_get_activities_have_required_fields(client: TestClient):
    # Arrange
    url = "/activities"
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get(url)

    # Assert
    data = response.json()
    for activity in data.values():
        assert required_fields.issubset(activity.keys())
