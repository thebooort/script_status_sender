# Script status sender
### Just an easy way to get notified via telegram when your script does something interesting/finishes.

I needed some script to send me some messages while/after my script finished. I read some stackoverflow questions and search for some code, here you have what i ended coding and periodically using!

Since my first purpose was only to send text I have some functions for it. After that I modified the script to send a full summary about my neural network's training. 

Made with python and ![python-telegram-bot library.](https://github.com/python-telegram-bot)
![](https://github.com/python-telegram-bot/logos/blob/master/logo-text/png/ptb-logo-text_1024.png)
Find some useful tips about telegram bots and id in the code!

## Files
- ![File functions.py](https://github.com/thebooort/script_status_sender/tree/master/functions.py)
 contains a very easy way to send text and photos (customize them!)
- ![Neural_Network_trainig_functions.py](https://github.com/thebooort/script_status_sender/tree/master/neural_network_training_summary.py)
 contains one of the reasons why i create this script: to send a complete summary about your artificial neural network training. It sends: the time spent, variables, acc, loss, acc graph, loss_graph
- ![example with time.py](https://github.com/thebooort/script_status_sender/tree/master/example_with_time.py)
 contains an easy way to use the functions to print total time spent

# Expected Outcome
![](https://github.com/thebooort/script_status_sender/blob/master/images/example1.png)
![](https://github.com/thebooort/script_status_sender/blob/master/images/example2.png)
