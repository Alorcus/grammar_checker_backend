from fastapi import FastAPI
from pydantic import BaseModel
import logging
from pathlib import Path

# from model_loader import tokenizer, model, device, SYSTEM_PROMPT


# remove any import of AutoModel… from the top level
tokenizer = model = device = SYSTEM_PROMPT = None

def load_model():
    global tokenizer, model, device
    if model is None:
        logging.info("Loading Zephyr model…")
        from transformers import AutoTokenizer, AutoModelForCausalLM
        import torch
        
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        logging.info("Loading system prompt…")
        _SP_PATH = Path(__file__).parent / "system_prompt.txt"
        SYSTEM_PROMPT = _SP_PATH.read_text(encoding="utf-8").strip()
        logging.info("System prompt loaded (%d chars).", len(SYSTEM_PROMPT))


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

        

class Prompt(BaseModel):
    prompt: str
    max_tokens: int = 128
    temperature: float = 0.7

app = FastAPI()

@app.post("/generate")
async def generate(req: Prompt):  
    load_model()  
    # build messages list
    messages = [
        {"role": "system",    "content": SYSTEM_PROMPT},
        {"role": "user",      "content": req},
    ]
    print(f"Generating text for prompt: {messages}")
    
    # inputs = tokenizer(req.prompt, return_tensors="pt").to(model.device)
    tokenized_chat = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")
    
    print(tokenizer.decode(tokenized_chat[0]))
    
    # out = model.generate(
    #     **inputs,
    #     max_new_tokens=req.max_tokens,
    #     temperature=req.temperature,
    #     pad_token_id=tokenizer.eos_token_id
    # )
    # text = tokenizer.decode(out[0], skip_special_tokens=True)
    return {"generated_text": req.prompt}

@app.get("/initialize")
async def initialize():
    load_model()
    return {"status": "Model and tokenizer loaded successfully."}
