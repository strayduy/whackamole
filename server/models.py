# Standard libs
import random

class Bill(object):
    def __init__(self):
        self.id = random.randint(0, 1000)
        self.title = 'title'
        self.description = ''

class Representative(object):
    def __init__(self):
        self.id = random.randint(0, 1000)
        self.name = random.choice(['Alice', 'Bob', 'Carol', 'David', 'Eve'])

class Vote(object):
    def __init__(self):
        self.id = random.randint(0, 1000)
        self.bill = Bill()
        self.representative = Representative()
        self.decision = random.choice(['yay', 'nay', 'abstain']) # One of: 'yay', 'nay', 'abstain'

