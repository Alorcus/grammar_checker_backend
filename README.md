## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

### Usage
    Run grammar_checker_backend script to start the backend server, with logs enabled for insights
    ```
    uvicorn main:app --reload --log-config log_config.yaml --timeout-graceful-shutdown 5 --workers 1

    uvicorn app.main:app --reload --log-level info --timeout-graceful-shutdown 5 --workers 1
    ```


### Testing
    If server is runnig (see Usage), you can test the functionality with pytest or pytest <test-script> for a specific script 

### Design Choices

- Regarding the time frame of 2 hours, I understand this challenge as a prototypical spike. Therefor I choose the fast scripting language Python  
- to standardize the type of errors, the LLM should choose from a pre-curated list of errors.  
- to minimize upfront loading time of llm, there is an API interface to start the LLM (internal controller) 

### Challenges

- Struggle to get LLM running, hard to debug -> long initial loading time, many parameters to test 
    -> add exstensive logging (log_config.yaml)
    -> tested model without server (test.py)


### Future Work

- detect multiple error types per sentence
- include prompt injection detection
- reimplement the functionality in an industry robust framework, like Java Springboot
- secure internal controller with secret to prevent misuse
