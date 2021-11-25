#!/usr/bin/python

def read_sample():
    with open('sample-message.txt', 'r') as file:
        lines = file.read()
        return lines

def replace_name(msg, name):
    return msg.replace("{1}", name)

def replace_address(msg, address):
    return msg.replace("{2}", address)

def generate(name, address):
    message = read_sample()
    message = replace_name(message, name)
    message = replace_address(message, address)
    return message
