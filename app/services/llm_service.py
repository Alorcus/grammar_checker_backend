import logging
from pathlib import Path

tokenizer = model = device = None

def load_model():
    global tokenizer, model, device
    if model is None:
        logging.info("Loading Zephyr model…")
        from transformers import AutoTokenizer, AutoModelForCausalLM
        import torch
        
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        load_system_prompt()

        logging.info("Loading tokenizer...")
        model_id = "HuggingFaceH4/zephyr-7b-beta"
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        logging.info("Tokenizer loaded successfully.")

        logging.info("Loading model...")
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.float16,
            device_map="auto"
        )


        model.eval()
        logging.info("Model loaded and set to evaluation mode successfully.")

        # Setting device
        device = next(model.parameters()).device
        logging.info(f"Model is loaded on device: {device}")

def load_system_prompt():
    global system_prompt
    logging.info("Loading system prompt…")
    _SP_PATH = Path(__file__).parent.parent / "prompts" / "system_prompt.txt"
    system_prompt = _SP_PATH.read_text(encoding="utf-8").strip()
    logging.info("System prompt loaded (%d chars).", len(system_prompt))  
    
    
def process_prompt(prompt: str):
    # Load the model if not already loaded
    load_model()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
    ]
    logging.info("Generating text for prompt with user input of length: %d", len(prompt))

    # Convert messages to plain text
    messages_text = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])

    # Tokenize the input
    tokenized_chat = tokenizer(
        messages_text,
        return_tensors="pt",
        padding=True,
        truncation=True
    )

    # Decode the tokenized output
    decoded_output = tokenizer.decode(tokenized_chat["input_ids"][0])
    return decoded_output