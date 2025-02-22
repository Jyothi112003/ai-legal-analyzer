import openai

client = openai.OpenAI()

try:
    models = client.models.list()
    available_models = [model.id for model in models]
    print("Available models:", available_models)
except openai.OpenAIError as e:
    print("Error fetching models:", e)
