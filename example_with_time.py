#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 16:57:58 2018

@author: booort, just a modification from gist by lucaspg96
"""
from datetime import datetime
from neural_network_training_summary import send_status

# Start time
startTime = datetime.now()

# Telegram information
bot_token = 'YOUR TOKEN'
chat_id = 'YOUR CHAT ID'


# Training variables example

val_spli = 0.2 # validation split
batch_si = 10 # batch size
ep = 100 # epochs

# then... magic happens: 

##########################################
# TRAINING YOUR BEAUTIFUL NEURAL NETWORK #
##########################################


# Getting total time
total_time = str(datetime.now() - startTime)
now = datetime.now()

# call the function
send_status('Date:'+str(now)+'\n'+'Training complete in: \n'+total_time,
            chat_id, bot_token, history, [val_spli, batch_si,ep])
