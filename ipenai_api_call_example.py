def openai_extract_lab_data(text):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    # Fine-tuned prompt for better and accurate extraction
    prompt = [
        {
            "role": "system",
            "content": " define how you want gpt to produce response"

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
