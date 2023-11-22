import json
import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def process_data(input_file, output_file):
    """ This function takes a medical diagnosis dialogue in JSON, cleans it and converts to JSONL"""
    
    # Read JSON file
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)

    # Extract relevant information and create a new structure
    processed_data = []
    for item in data:
        if 'description' in item:
            del item['description']
            
        patient_utterance = item['utterances'][0].split(': ', 1)[1]
        doctor_utterance = item['utterances'][1].split(': ', 1)[1]

        processed_item = {
            'prompt': patient_utterance,
            'completion': doctor_utterance
        }

        processed_data.append(processed_item)

    # Write processed data to a new JSONL file
    with open(output_file, 'w') as jsonl_file:
        for item in processed_data:
            # Convert each item to a JSON string and write it as a line
            jsonl_file.write(json.dumps(item) + '\n')

# # Example usage: Use to convert
# input_json_file = r"C:\Users\usha\Downloads\drf-project\english-dev.json"
# output_jsonl_file = r"C:\Users\usha\Downloads\drf-project\out-val.jsonl"
# process_data(input_json_file, output_jsonl_file)


def upload_file(name):
    """Uploading files for fine tuning"""
    file = openai.File.create(
        file=open(name, "rb"),
        user_provided_filename=name,
        purpose="fine-tune",
    )

    return file


if __name__ == "__main__":
    print("This code will only run if the script is executed directly.")
    # To upload file and get details like the id. This should be done once
    print(upload_file(r"C:\Users\usha\Downloads\drf-project\drai\dialogue-train.jsonl"))
    

training_file_id = "file-CZEijgvLbMlbxGnvj9dGJmI6" # the id of your training file
