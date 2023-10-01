def openai_extract_lab_data(text):
    openai.api_key = os.getenv("OPENAI_API_KEY", "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")
    # Fine-tuned prompt for better and accurate extraction
    prompt = [
        {
            "role": "system",
            "content": """You are a specialized assistant trained to convert lab reports into structured JSON data. 
            Please convert the text into a valid JSON format adhering to the following rules:
            The expected format is:
            [
                {
                    "name": "Test Name 1",
                    "result": "Result 1",
                    "range": {
                        "low": "Low Range 1",
                        "high": "High Range 1"
                    },
                    "unit": "Unit 1"
                },
                {
                    "name": "Test Name 2",
                    "result": "Result 2",
                    "range": {
                        "low": "Low Range 2",
                        "high": "High Range 2"
                    },
                    "unit": "Unit 2"
                },
                // ... (additional test data follows the same format)
          ]"""

        },
        {
            "role": "user",
            "content": text
        }
    ]

    # Define the API request with fine-tuned parameters for better quality
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=prompt,
        temperature=0.5,
        max_tokens=2000,  # Adjust this based on your requirement
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the assistant's reply from the API response
    assistant_reply = response['choices'][0]['message']['content']

    print("gpt le k vancha: ", assistant_reply)
    data = extract_valid_entries(assistant_reply)
    print(data)  # Now `data_list` is a list of dictionaries containing your data
    return data
