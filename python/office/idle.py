# Your code here
import math
import random


def chat():
    coworkers = ["Jack", "Lenny", "Michelle", "Andrea"]
    chatee = coworkers[math.floor(random.random() * 4)]
    print("Chatting with " + chatee + "...")
    print("Done")

def getWater():
    print("Getting water...")
    print("That was refreshing.")

def useSocialMedia():
    socialMedia = ["FaceBook", "Twitter", "YouTube", "Reddit"]
    choice = socialMedia[math.floor(random.random()*4)]
    print("Using " + choice + "...")
    print("Done")
