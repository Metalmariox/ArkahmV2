from Card import Card
from ElderSign import ElderSign
class Investigator:
    def __init__(self, name, wis, inte, str, dex, health, sanity):
        self.name = name
        self.wis = wis
        self.int = inte
        self.str = str
        self.dex = dex
        self.max_health = health
        self.max_sanity = sanity
        self.assets = {}
        self.kill_actions = []
        self.investigatorAdditions()

    def investigatorAdditions(self):
        '''Adds Investigator specific actions to lists'''
        if self.name == "Roland Banks":
            self.kill_actions.append(1)
            self.elder_sign = 1


