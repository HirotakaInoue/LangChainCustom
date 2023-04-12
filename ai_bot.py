from openai_handle import OpenAI


class AIBot:
    def __init__(self, name) -> None:
        self.openai = OpenAI()
        self.name = name
        self.hist = []

    def add_hist(self, role, content):
        self.hist.append({
            "role": role,
            "content": content
        })

    def set_condition(self, condition_prompt):
        self.add_hist('system', condition_prompt)
        response = self.openai.run_api(self.hist)
        self.add_hist('assistant', response)

    def talk(self, prompt):
        self.add_hist('user', prompt)
        response = self.openai.run_api(self.hist)
        print(f"{self.name}>>>")
        print(response)
        self.add_hist('assistant', response)
        return response
