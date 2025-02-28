from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load AI model (TinyLlama, can be swapped with GPT4All)
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_text(prompt):
    """Generate AI text from a given prompt."""
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    output = model.generate(input_ids, max_length=300)
    return tokenizer.decode(output[0], skip_special_tokens=True)
