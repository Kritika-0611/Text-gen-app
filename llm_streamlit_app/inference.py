from transformers import pipeline

# Load the model only once
generator = pipeline("text-generation", model="gpt2")

def generate_text(prompt):
    output = generator(prompt, max_length=100, num_return_sequences=1)
    return output[0]['generated_text']
