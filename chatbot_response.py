
import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'

def get_chatbot_response(user_input):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant in a negotiation."},
            {"role": "user", "content": user_input}
        ]
    )
    return response['choices'][0]['message']['content']
