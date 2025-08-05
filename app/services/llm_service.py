import logging
from pathlib import Path

# steal uvicorn's handlers for the root logger
uv_err = logging.getLogger("uvicorn.error")
root = logging.getLogger()
root.handlers = uv_err.handlers
root.setLevel(logging.INFO)


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
    _SP_PATH = Path(__file__).parent.parent / "prompts" / "system_prompt_short.txt"
    system_prompt = _SP_PATH.read_text(encoding="utf-8").strip()
    logging.info("System prompt loaded (%d chars).", len(system_prompt))  
    
    
def process_prompt(prompt: str, max_new_tokens: int = 128):
    # Load the model if not already loaded
    load_model()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
    ]
    logging.info("Generating text for prompt with user input of length: %d", len(prompt))

    # Convert messages to plain text
    full_prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])

    # # Tokenize the input
    # tokenized_chat = tokenizer(
    #     messages_text,
    #     return_tensors="pt",
    #     padding=True,
    #     truncation=True
    # )
    
    inputs = tokenizer(
        full_prompt,
        return_tensors="pt",
        padding=True,
        truncation=True,
    ).to(device)
    
    logging.info("Generating text for prompt of length %d", len(prompt))

    output_ids = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        do_sample=False,
        eos_token_id=tokenizer.eos_token_id,
        pad_token_id=tokenizer.eos_token_id,
    )

    generated_ids = output_ids[0][ inputs["input_ids"].shape[-1] : ]

    # decode and strip any whitespace/special tokens
    response = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()
    return response