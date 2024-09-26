import openai

# Set up your OpenAI API key
openai.api_key = 'your-openai-api-key'


def ask_chatgpt(prompt):
    resp = openai.Completion.create(
        engine="text-davinci-003",  # Use a GPT-3.5-based model
        prompt=prompt,
        max_tokens=100  # Limit the response length
    )
    return resp.choices[0].text.strip()


# Example usage
user_prompt = "Explain how ChatGPT works in Python"
response = ask_chatgpt(user_prompt)
print(response)


"""
ChatGPT is an AI language model developed by OpenAI, and it can be integrated into Python programs via an 
API to provide natural language processing (NLP) capabilities. You can use it for various tasks, 
such as answering questions, generating text, summarizing content, and more.

Breakdown:
    openai.Completion.create sends a prompt to ChatGPT.
    engine="text-davinci-003" specifies the GPT model.
    max_tokens limits the response length.
    
You can customize the prompt or parameters depending on your needs, 
such as generating longer or shorter responses, or adjusting the level of detail.
"""
