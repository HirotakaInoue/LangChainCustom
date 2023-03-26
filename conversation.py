from ai_bot import AIBot


class Conversation():
    def __init__(self, topic, ai1, ai2, conversation_limit) -> None:
        self.topic = topic
        self.conversation_limit = conversation_limit
        print(f"start conversation about 【{topic}】")
        self.make_ai(ai1['name'], ai2['name'])
        self.make_ai_condition(ai1['condition'], ai2['condition'])

    def make_ai(self, ai1_name, ai2_name):
        self.ai1 = AIBot(ai1_name)
        self.ai2 = AIBot(ai2_name)

    def make_ai_condition(self, ai1_condition, ai2_condition):
        self.ai1.set_condition(self.condition_prompt_wrap(ai1_condition).strip())
        self.ai2.set_condition(self.condition_prompt_wrap(ai2_condition).strip())

    def condition_prompt_wrap(self, self_condition):
        return f"[{self_condition}]になりきって、私と会話してください。一度の発言はワンフレーズで行ってください。日本語を使用して会話してください。"

    def start_conversation(self):
        conversation_num = 0
        while conversation_num < self.conversation_limit:
            if conversation_num == 0:
                res = self.ai1.talk(self.topic)
                self.ai2.add_hist('user', self.topic)
            elif conversation_num % 2 == 0:
                res = self.ai1.talk(res)
            else:
                res = self.ai2.talk(res)

            conversation_num += 1

        print('-------------------')
        print('end conversation')
