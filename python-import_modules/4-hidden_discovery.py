#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    name = dir(hidden_4)
    for n in sorted(name):
        if n[0] != '_':
            print(n)
