from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def translate_to_english(hindi_text: str) -> str:
    model_name = "ai4bharat/IndicTrans2-IndicEn-1B"
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name, trust_remote_code=True)
    
    inputs = tokenizer(hindi_text, return_tensors="pt", padding=True)
    outputs = model.generate(**inputs, max_length=512)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
