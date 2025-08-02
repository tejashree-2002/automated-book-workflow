
# === utils/helpers.py ===

def save_to_file(text, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

def read_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
