import os
import openai


class Singleton(object):
    @classmethod
    def get_instance(cls, input):
        if not hasattr(cls, "_instance"):
            cls._instance = cls(input)
        else:
            cls._instance.input = input
        return cls._instance


class OpenAI(Singleton):
    def __init__(self) -> None:
        api_key = os.getenv('OPENAI_API_KEY')
        openai.api_key = api_key

    def run_api(self, prompt):
        r = openai.ChatCompletion.create(
            model="gpt-4",
            messages=prompt,
            # frequency_penalty=-0.2
        )
        return r['choices'][0]['message']['content']
