import json
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline 

def generate_script(prompt, predefined_messages_path):
    # Load the LLM model and tokenizer
    model = AutoModelForCausalLM.from_pretrained(
        "microsoft/Phi-3-mini-128k-instruct",
        device_map="cuda",
        torch_dtype="auto",
        trust_remote_code=True,
    )

    tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-128k-instruct")

    # Load JSON file with predefined messages
    with open(predefined_messages_path, 'r') as file:
        predefined_messages = json.load(file)

    # Append the user prompt to the predefined messages
    predefined_messages.append({"role": "user", "content": prompt})

    # Format the messages for input into the pipeline
    # messages_for_model = "\n".join([f"{msg['role']}: {msg['content']}" for msg in predefined_messages])
    messages_for_model =predefined_messages

    # Initialize the text generation pipeline
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
    )

    # Define generation arguments
    generation_args = {
        "max_new_tokens": 500,
        "return_full_text": False,
        "temperature": 1,
        "do_sample": True,
    }

    # Generate text based on the messages
    output = pipe(messages_for_model, **generation_args)

    # Return the generated text
    return output[0]['generated_text']