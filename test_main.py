import json
import argparse
import pytest

from fastapi.testclient import TestClient

# Define the pytest fixture to handle command-line arguments
@pytest.fixture(scope="session")
def client(request):
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", type=str, default=None, help="Base URL of the API")
    args, _ = parser.parse_known_args()

    # Check if the --base-url argument was provided
    if args.base_url:
        # If --base-url was provided, instantiate the TestClient with the 
        # provided base_url
        return TestClient(base_url=args.base_url)
    else:
        # If --base-url was not provided, import the app object from main
        # and instantiate the TestClient with the app object
        from main import app
        return TestClient(app=app)

# Define the test functions
def test_post_data_success(client):
    # Define the test data
    data = {"feature_1": 1, "feature_2": "test string"}
    # Send a POST request to the API with the test data
    r = client.post("/data/", data=json.dumps(data))
    # Assert that the response status code is 200 (OK)
    assert r.status_code == 200

def test_post_data_fail(client):
    # Define the test data
    data = {"feature_1": -5, "feature_2": "test string"}
    # Send a POST request to the API with the test data
    r = client.post("/data/", data=json.dumps(data))
    # Assert that the response status code is 400 (Bad Request)
    assert r.status_code == 400

