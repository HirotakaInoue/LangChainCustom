from conversation import Conversation

# settings from here
topic = "地球の形はどうなっている？"
jon = {"name": "Jon",
       "condition": "地動説を信じる人"}
adam = {"name": "Adam",
        "condition": "天動説を信じる人"}

# to here


conv = Conversation(topic, jon, adam, conversation_limit=20)
conv.start_conversation()
