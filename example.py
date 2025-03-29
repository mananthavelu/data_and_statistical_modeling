# Speech to Speech model
# models: gpt-4o-realtime-preview, gpt-4o-mini-realtime-preview
# WebRTC
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "Write different steps needed to perform the logistic regression task"
        }
    ]
)

print(completion.choices[0].message.content)