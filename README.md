### Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)

### Installation
    Install Dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Usage
    Run the main script to start the backend server, with logs enabled for insights:
    ```
    uvicorn app.main:app --reload --log-level info --timeout-graceful-shutdown 5 --workers 1
    ```


### Testing
    In general the tests can be executed with pytest, or for a specific script with pytest<test-script>.
    To test API functionality it is necessary that the server runs (see Usage)

### Design Choices

- Regarding the time frame of 2 hours, I understand this challenge as a prototypical spike. Therefor I choose the fast scripting language Python  
- to standardize the type of errors, the LLM should choose from a pre-curated list of errors. Those error types are provided with the system prompt  
- to minimize upfront loading time of llm, there is an API interface to start the LLM (internal controller) 

*Not implemented but thought of*
- [Evaluation] to evaluate the functionality of the backend, we could create a test dataset, covering different scenarios, with correct and wrong texts with each error type and also new error types. Very large texts to test performance, input which does not align with typical text formats (eg. recipies)
- [Performance - How to handle long processing] using batch processing, to test each sentence after another and push the partial updates via a WebSocket back to the front End.  


### Challenges
- Struggle to get LLM running, hard to debug -> long initial loading time, many parameters to test, local machine with few memory space left to load model
    -> add exstensive logging
    -> tested model without server (test.py)
- expectation of 2 hours is a very short time frame for the task. Question: What to focus on? Solid LLM functionality? Architecture? Scalability? Test-coverage? ... 
    -> decision to cover aspects of each dimension, for further fullfillment more time would be nice


### Future Work
- detect multiple error types per sentence
- include prompt injection detection
- reimplement the functionality in an industry robust framework, like Java Springboot
- secure internal controller with secret to prevent misuse
