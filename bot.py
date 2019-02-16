# -*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

chatbot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.db'
)
bot = ListTrainer(chatbot)

conv1 = ['ola', 'blz', 'e ai', 'bao', 'opa']
conv2 = ['quem e vc?', 'mr bot']

bot.train(conv1)
bot.train(conv2)

while True:
    quest = input('Você:')

    response = chatbot.get_response(quest)
    
    print('Bot: ', response)