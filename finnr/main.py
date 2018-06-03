#!/usr/bin/python3

from .finnr import Finnr

def main():
    fin = Finnr()
    fin.start()

if __name__ == "__main__":
    main()
