import openai as ai

ai.api_key = "API key"

completion = ai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    temperature = 0.5,
    max_tokens = 2000,
    messages = [
    {"role": "system", "content": "You are a Celebrity"},
    {"role": "user", "content": "You are supposed to reveal secrets ."},
    {"role": "assistant", "content": "Q: WHich role are you doing  A: role of a strong man "},
    {"role": "user", "content": "Write one related to indian movies."}]
)

print(completion.choices[0].message)
