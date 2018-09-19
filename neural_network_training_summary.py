#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Sep 19 16:57:58 2018

@author: booort, just a modification from gist by lucaspg96
"""
import telegram 


bot_token = 'YOUR TOKEN'
chat_id = 'YOUR CHAT ID'

def send_status_nn_trainning(msg, chat_id, token, history, parameters):
    """
Send complete summary for your NN training (time could be added in your file en then printed)

Use telegram api to send any message to a conversation.
Primarly used to send updates about long scripts

Parameters
----------
msg: str
    message you want to send

chat_id: str
    chat identification number.
    learn how to obtain it here: https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id

token: str
    bot token number (obtain it with bot_father)
history: 
    information giving during fittin ANN in keras
parameters: vector
    vector = [validation split, batch size, epochs]

Returns
-------
- It only sends the information

    """
    bot = telegram.Bot(token = token)
    
    # send the message (used for time)
    bot.sendMessage(chat_id, text = msg) 
    
    # send the summary
    bot.sendMessage(chat_id, text = 'Summary: \n validation_split='+str(parameters[0])+
                    ',\n batch_size = '+str(parameters[1])+',\n epochs = '+
                    str(parameters[2])+' \n'+'Loss: '+str(history.history['loss'][-1])+'\n'+
                    ' Acc: '+str(history.history['acc'][-1]))
    
    # send graphs
    send_graph(history, chat_id, token)
    
    # cat sticker
    bot.send_sticker(chat_id,'CAADAQADFQEAAiSbWAbWD0wj8M6u2AI') 

def send_graph(history, chat_id, token):
    """
send a graph obtained from loss and accuracy history values.
Cool way to visualice your results


Parameters
----------
history: ANN.fit() (from keras)
    acc and loss information

chat_id: str
    chat identification number.
    learn how to obtain it here: https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id

token: str
    bot token number (obtain it with bot_father)

Returns
-------
- It only sends the information

    """
    # summarize history for accuracy
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.savefig('acc_graph.png')
    plt.clf()
    # summarize history for loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.savefig('loss_graph.png')
    
    bot = telegram.Bot(token=token)
    bot.send_photo(chat_id=chat_id, photo=open('acc_graph.png', 'rb'))
    bot.send_photo(chat_id=chat_id, photo=open('loss_graph.png', 'rb'))