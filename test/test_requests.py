import requests

from app.models.error_type import ErrorType

def test_grammar_check_availability():
    # Define the API endpoint
    url = "http://localhost:8000/grammar/check"
    
    # Define the payload
    payload = {
        "text": "This is a test sentence with an eror."
    }
    
    # Send the POST request
    response = requests.post(url, json=payload)
    
    # Assert the response status code
    assert response.status_code == 200
    
    
def test_grammar_check_response_structure():
    # Define the API endpoint
    url = "http://localhost:8000/grammar/check"
    
    # Define the payload
    payload = {
        "text": "This is a test sentence with no error."
    } 
    
    # Send the POST request
    response = requests.post(url, json=payload)
    
    # Assert the response is an empty list
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
def test_grammar_check_with_error():
    # Define the API endpoint
    url = "http://localhost:8000/grammar/check"
    # Define the payload
    payload = {
        "text": "This is a test sentence with an errors."
    } 
    
    # Send the POST request
    response = requests.post(url, json=payload)
    
    # Assert the response is a list with SentenceCorrected objects
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list)
    assert len(response_data) == 1
    
    # Assert the structure of the SentenceCorrected object
    assert "original" in response_data[0]
    assert "improved" in response_data[0]
    assert "error_type" in response_data[0]
    
    # Assert the improved sentence is corrected
    assert response_data[0]["original"] == payload["text"]
    assert response_data[0]["improved"] == "This is a test sentence with an error."
    assert response_data[0]["error_type"] is not None  # Assuming error_type is not None for errors
    assert response_data[0]["error_type"] == ErrorType.SVA