from openai import OpenAI
import user_config


client = OpenAI(api_key=user_config.openai_key)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write me 2 lines about India."
        }
    ]
)

print(completion.choices[0].message.content)