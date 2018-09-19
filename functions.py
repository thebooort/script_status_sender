#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Sep 19 16:57:58 2018

@author: booort, just a modification from gist by lucaspg96
"""
import telegram 


bot_token = 'YOUR TOKEN'
chat_id = 'YOUR CHAT ID'

def send_photo(chat_id, token):
    """
    MODIFY THE PATH!!!
    
Send a photo from disk 


Parameters
----------

chat_id: str
    chat identification number.
    learn how to obtain it here: https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id

token: str
    bot token number (obtain it with bot_father)

Returns
-------
- It only sends the information

    """
    bot = telegram.Bot(token=token)
    bot.send_photo(chat_id=chat_id, photo=open('path/to/photo.png', 'rb')) 

def send_message(msg, chat_id, token):
    """
Send any message to a selected chat.

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


Returns
-------
- It only sends the information

    """
    bot = telegram.Bot(token = token)
    
    # send the message (used for time)
    bot.sendMessage(chat_id, text = msg) 
    
    # cat sticker
    bot.send_sticker(chat_id,'CAADAQADFQEAAiSbWAbWD0wj8M6u2AI') 