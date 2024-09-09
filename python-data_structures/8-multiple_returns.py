#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    first = sentence[0] if sentence else None
    return (leng, first)
