import os
import openai
import time
from data import training_file_id
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
openai_api_key = os.getenv("OPENAI_API_KEY")

create_args = {
	"training_file": training_file_id,
	"model": "davinci",
	"n_epochs": 10,
	"batch_size": 3,
	"learning_rate_multiplier": 0.3
}

response = openai.FineTune.create(**create_args)
job_id = response["id"]
status = response["status"]

print(f'Fine-tunning model with jobID: {job_id}.')
print(f"Training Response: {response}")
print(f"Training Status: {status}")

# Check status of fine tune jobs
status = openai.FineTune.retrieve(id=job_id)["status"]
if status not in ["succeeded", "failed"]:
    print(f'Job not in terminal status: {status}. Waiting.')
    while status not in ["succeeded", "failed"]:
        time.sleep(2)
        status = openai.FineTune.retrieve(id=job_id)["status"]
        print(f'Status: {status}')
else:
	print(f'Finetune job {job_id} finished with status: {status}')

print('Checking other finetune jobs in the subscription.')
result = openai.FineTune.list()
print(f'Found {len(result.data)} finetune jobs.')

# Retrieve the finetuned model
print(result) # get the fine-tuned model