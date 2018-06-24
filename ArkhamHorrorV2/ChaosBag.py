import random
class ChaosBag():
    def __init__(self, tokens):
        '''tokens - list'''
        self.tokens = tokens

    def drawChaosToken(self):
        '''Draws a random chaos token'''
        token = random.randint(0, len(self.tokens))
        return token

    def ChaosTokenResults(self, token, investigator, campaign):
        '''Gets results of Chaos draw'''
        if token == 'Elder Sign':
            investigator.elder_sign()
        if token == 'Cultist':
            campaign.culist()
        if token == 'Skull':
            campaign.skull()
        if token == 'Eldritch':
            campaign.eldritch()
        if token == 'Tablet':
            campaign.tablet()

    def chaosTokenBag(self, investigator, campaign):
        '''Runs the chaos bag'''
        token = self.drawChaosToken()
        self.ChaosTokenResults(token, investigator, campaign)



