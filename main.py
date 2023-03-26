from conversation import Conversation

# settings from here
topic = "AIが人間を超える知能を手に入れたときにどうするべきか?"
jon = {"name": "ポジティブ",
       "condition": "ポジティブなAI"}
adam = {"name": "ネガティブ",
        "condition": "ネガティブなAI"}

# to here


conv = Conversation(topic, jon, adam, conversation_limit=20)
conv.start_conversation()
