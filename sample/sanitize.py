def sanitize_prompt(prompt: str) -> str:
    """Clean and validate a text prompt input."""
    if not isinstance(prompt, str) or len(prompt) == 0:
        raise ValueError("Prompt must be a non-empty string.")
    # Limit length to prevent buffer overflow or exorbitant processing
    MAX_PROMPT_LEN = 200
    prompt = prompt[:MAX_PROMPT_LEN]
    # Remove any disallowed characters (simple whitelist approach)
    import re
    if re.search(r'[^\w\s\.,?!]', prompt):
        prompt = re.sub(r'[^\w\s\.,?!]', '', prompt)
    return prompt

# Usage in the inference pipeline (e.g., sample.py):
user_prompt = get_user_prompt()              # fetch input (e.g., from CLI or API)
clean_prompt = sanitize_prompt(user_prompt)  # validate/sanitize input
text_emb = text_encoder(clean_prompt)        # proceed with existing text encoding
motion = model.generate(text_emb)