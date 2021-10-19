# My chat Bot
from chatterbot import my_bot

from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer


my_bot = my_bot(name ="Puranjay",read_only =True,logic_adapters = "chatterbot.logic.MathematicalEvaluation")

issueAbout_1 = [
    'Hi','hey there','hello','hiiii','hello'
#'Hi this is Fix Orie assitant,i am here to resolve your problem ,Please enter the problem you are facing ?'
]
issueAbout_2=[
    "my problem is "
    
]
list_trainer = Lis_trainer(my_bot)
#Training my bot for ythe test cases
for item in (issueAbout_1,issueAbout_2):
    list_trainer.train(item)
# list_trainer = ListTrainer(my_bot)
corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpuse.english')
print(my_bot.get_response("What is your problem "))

print(my_bot.get_response("hi"))

# print(my_bot.get_response("Hi"))
print(my_bot.get_response("What is your Pro"))
print(my_bot.get_response("Hsssdi"))
print(my_bot.get_response("Hisdshi"))

