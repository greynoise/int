'''
 The INfoTrainer
 File: intClangMessage.py
 Author: GreyNoise
 Date Created: 24.02.2016
 Python Version: 2.7.3 / 3.5.1
 License: GPL V3.0

 This file contains the classes for reading and parsing messages from the clang compiler

'''

import re



class ClangSingleMessage:

    _filename = ""
    _type = "note"
    _line = 0
    _col = 0
    _text = ""
    _srcLine = ""
    _srcMark = ""


    def __init__(self):
        pass

    def parseMsg(self, msg):
        # Check how the message was passed - allowed are plain string or list of strings(in wich
        # case each element of the list is considered one line of the message)
        if (isinstance(msg, str)):
            # split the string into lines
            lines = text.split('\n')

        elif (isinstance(msg, list)):
            # check if all the elements of the list are strings
            for elem in msg:
                if (not isinstance(elem, str)):
                    raise TypeError("The message must be passed as a string or a list of strings")
            # if all elements are strings - just use the original msg list
            lines = msg
        else:
            # neither list nor string - invalid - raise TypeError
            raise TypeError("The message must be passed as a string or a list of strings")
        # check the first line - in a valid Clang-style message, the first line will have the format
        # FILENAME:LINENO:COLNO: MSGTYPE: MESSAGE
        # We will only check for the first three elements, that should normally do
        # that can be done with a simple regex
        lstart = re.compile(r"^.+\:\d+\:\d+\:")
        if (lstart.match(lines[0]) != None):
            print ("Matched!")
        




class ClangMessages:

    def __init__(self, msgText = ""):
        if (not isinstance(msgText, str)):
            raise TypeError("The msgText parameter must be a string containing the compiler messages!")

        # initialize empty messages dictionary if no text is given
        if (text == ""):
            self.messages = {"note":[], "warning":[], "error":[]} 

        # if a proper text was given, parse it
        parseTextMsgs(msgText)

    def parseTextMsgs(self, text):
        # split the string into lines
        lines = text.split('\n')

        # to separate the text into individual messages, find the first lines of each message
        # the first lines will have the format
        # FILENAME:LINENO:COLNO: MSGTYPE: MESSAGE
        # Checking for the first three elements should normally do. Use simple regex
        msgfinder = re.compile(r"^.+\:\d+\:\d+\:")
        msgs = []
        last_start = -1
        for idx,line in enumerate(lines):
            if (msgfinder.match(line) != None):
                start = idx
                if (last_start > -1):
                    msgs = msgs + [lines[last_start:start]]
                last_start = start
        # append the last message
        msgs = msgs + [lines[last_start:]]
        # now, we (probably) have a list of messages
        # Pass each element of the msgs array down to the individual message parser, this can take
        # care of sorting out wether or not each element actually is a message.
        # The messages are then stored according to their type in the messages dictionary
        for msg in msgs:
            pMsg = ClangSingleMessage(msg)

            



