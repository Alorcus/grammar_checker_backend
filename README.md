## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/WilliamBrandt/Data-Object-State-Abstraction.git
    cd Data-Object-State-Abstraction
    ```

2. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

### Usage
    Run grammar_checker_backend script to start the backend server, with logs enabled for insights
    ```
    uvicorn grammar_checker_backend:app --reload --log-config log_config.yaml --timeout-graceful-shutdown 5 --workers 1
    ```

### Design Choices

- Regarding the time frame of 2 hours, I understand this challenge as a prototypical spike. Therefor I choose the fast scripting language Python  
- to standardize the type of errors, the LLM should choose from a pre-curated list of errors.  

### Challenges

- Struggle to get LLM running, hard to debug -> long initial loading time, many parameters to test 
    -> add exstensive logging (log_config.yaml)
    -> tested model without server (test.py)


### Future Work

- detect multiple error types per sentence
- include prompt injection detection
- reimplement the functionality in an industry robust framework, like Java Springboot
