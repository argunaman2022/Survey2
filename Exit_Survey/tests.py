from otree.api import *
from . import *
import random

class PlayerBot(Bot):
    def play_round(self):
        # Simulating player responses for the pilot survey
        yield Compet_measure, dict(Compet_measure=random.randint(0, 10)) 
        
        yield Pilot, {
            'Pilot_1': random.choice(['Strongly disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly agree']),
            'Pilot_2': random.choice(['Strongly disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly agree']),
            'Pilot_3': random.choice(['Strongly disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly agree']),
            'Pilot_4': random.choice(['Very boring', 'Boring', 'Neutral', 'Interesting', 'Very interesting']),
            'Pilot_5': 'Sample feedback for improvements and overall experience.'
        }