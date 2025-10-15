"""
Created by Thomas Hu on 2025-10-12 at 12:39 p.m.
"""
import logging

def read_file(file_name):
    lines=[]
    with open(file_name, "r") as file:
        for line in file:
            lines.append(line.strip())
    return lines

def display(dlist):
    for row in range(len(dlist)):
        logging.debug(dlist[row])
