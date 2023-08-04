from transformers import MarianMTModel, MarianTokenizer

def selected_language(num):
    if num == 1:
        selected = "english"
    elif num == 2:
        selected = "french"
    elif num == 3:
        selected = "spanish"
    else:
        print(f"Invalid input: {num}")
        selected = None
    return selected

def translate_input(original_language, desired_language, input_text):
    # Load the pre-trained model for translation
    model_name = f'Helsinki-NLP/opus-mt-{original_language}-{desired_language}'
    pretrained_model = MarianMTModel.from_pretrained(model_name)
    tokenized_model = MarianTokenizer.from_pretrained(model_name)

    # Tokenize the input text
    input_ids = tokenized_model.encode(input_text, return_tensors='pt').input_ids

    # Perform translation
    translated_text = pretrained_model.generate(input_ids)
    decoded_translation = tokenized_model.decode(translated_text[0], skip_special_tokens=True)

    # Print the translation
    print("The translated text is:", decoded_translation)

# Prompts for the user to enter
print('Select the original language: \n1. English \n2. French \n3. Spanish')
original_language = int(input("Please enter the language's number: "))

while original_language < 1 or original_language > 3:
    print("You've entered an invalid input, try again.")
    print('Select the original language: \n1. English \n2. French \n3. Spanish')
    original_language = int(input("Please enter the language's number: "))
else:
    source_language = selected_language(original_language)

    print('Select the destination language: \n1. English \n2. French \n3. Spanish')
    destination_language = int(input("Please enter the language's number: "))

    while destination_language < 1 or destination_language > 3:
        print("You've entered an invalid input, try again.")
        print('Select the destination language: \n1. English \n2. French \n3. Spanish')
        destination_language = int(input("Please enter the language's number: "))
    else:
        desired_language = selected_language(destination_language)

# Prompt the user to enter the input text
input_text = input("Please enter the input text: ")

if source_language and desired_language:
    translate_input(source_language, desired_language, input_text)