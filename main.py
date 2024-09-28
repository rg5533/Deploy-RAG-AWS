import os
import json
import sys
import boto3

print("imported successfully...")

prompt = """
you are a cricket expert now just tell me when RCB will win the IPL?
"""

# Initialize the Bedrock client with the specified region
bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

def invoke_llama3_instruct(prompt_text):
    """
    Invokes the Llama 3 8B Instruct model using Amazon Bedrock.

    Args:
        prompt_text (str): The prompt to send to the model.

    Returns:
        str: The response generated by the model.
    """
    # Define the model ID for Llama 3 8B Instruct
    model_id = "meta.llama3-8b-instruct-v1:0"

    # Create the request payload
    request_payload = {
        "prompt": prompt_text,
        "max_gen_len": 512,
        "temperature": 0.5
    }

    try:
        # Invoke the model with correct parameter names
        response = bedrock.invoke_model(
            modelId=model_id,                  # Correct parameter name
            body=json.dumps(request_payload),   # Correct parameter name
            contentType="application/json"      # Correct parameter name
        )

        # Debug: Print the keys in the response
        print("Response Keys:", response.keys())

        # Parse the response
        response_body = json.loads(response['body'].read())  # Changed 'Body' to 'body'
        generated_text = response_body.get("generation", "")

        return generated_text

    except Exception as e:
        print(f"Error invoking the model: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Invoke the model with the defined prompt
    result = invoke_llama3_instruct(prompt)
    print("Model Response:")
    print(result)