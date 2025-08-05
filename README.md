# README

## Prerequisites

Ensure you have the following prerequisites installed:

* **Python** 3.8 or higher
* **pip** (Python package installer)

## Installation

Install dependencies:

```sh
pip install -r requirements.txt
```

## Usage

Start the backend server with live reloading and detailed logs:

```sh
uvicorn app.main:app \
  --reload \
  --log-level info \
  --timeout-graceful-shutdown 5 \
  --workers 1
```

## Testing

1. **Unit & Integration Tests**

   * Run all tests:

     ```sh
     pytest
     ```
   * Run a specific test module:

     ```sh
     pytest <test_module>.py
     ```
2. **API Tests**

   * Ensure the server is running (see **Usage**).
   * Use your preferred HTTP client (e.g., `curl`, Postman, or automated scripts) to send requests and verify responses.

## Design Choices

* **Language & Framework**: Python was chosen for rapid prototyping within the two-hour spike timeframe.
* **Error Standardization**: The LLM is prompted to select from a predefined list of grammar error types for consistent results.
* **Model Initialization**: To minimize LLM startup latency during a user request, an internal controller API initializes the model on demand.
* **Layered Architecture**: For cleaner code, accelerate development velocity, and testability.

## Additional Considerations

* **API Documentation**: Include an OpenAPI/Swagger specification for clear API contracts and client generation.
* **Evaluation Dataset**: Create a diverse evaluation dataset covering each error type, long texts, and edge cases.
* **Batch Processing & Streaming**: Implement batch processing with WebSocket-based partial updates for long-running requests.

## Challenges

* **LLM Setup & Debugging**

  * Slow model loading and numerous parameters made debugging difficult.
  * Limited local memory constrained model performance.
  * **Mitigations**:

    * Added extensive logging.
    * Tested the model via a standalone script.

* **Time Constraints**

  * The two-hour timeframe required balancing LLM integration, architecture design, performance, and test coverage.
  * **Approach**: Addressed core aspects for a prototype; further refinement would require more time.

## Future Work

* Detect and correct multiple error types per sentence.
* Add prompt-injection detection and mitigation.
* Integrate cloud-based GPU resources and optimized inference pipelines to accelerate LLM startup and reduce processing time.
* Reimplement the architecture in an enterprise-grade framework (e.g., Java Spring Boot).
* Secure the internal controller with authentication/authorization to prevent misuse.
