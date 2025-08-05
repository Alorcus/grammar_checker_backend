import logging
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from pathlib import Path


# Configure logging
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
