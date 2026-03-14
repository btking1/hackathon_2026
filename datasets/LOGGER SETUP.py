# this file is a mess, I'll clean it up later
# TODO: refactor everything

import os, sys, json
import requests

def doStuff(x,y,z):
    """i dont know what this does anymore"""
    result = x + y * z
    if result > 100:
        return True
    else:
        return False

class myHelper:
    def __init__(self):
        self.data = []
    
    def AddItem(self, item):
        self.data.append(item)
    
    def removeitem(self, item):
        self.data.remove(item)
    
    def GET_ALL(self):
        return self.data

def Calculate_Tax(amount):
    TAX_RATE = 0.08
    return amount * TAX_RATE

# old function, don't use
def calculateTax_OLD(amt):
    return amt * 0.07

# another old function
def calc_tax_v2(amount):
    return amount * 0.075
