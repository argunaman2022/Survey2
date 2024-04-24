from otree.api import Currency as c, currency_range, expect, Bot
from . import *
import random

class PlayerBot(Bot):

    def play_round(self):
        # Simulating player behavior for each page and task in the experiment
        yield Task1, dict(Task1_male_FOB=random.randint(0, 10), Task1_female_FOB=random.randint(1, 10))
        yield Task2, dict(Task1_male_FOB=random.randint(0, 10), Task1_female_FOB=random.randint(1, 10))
        yield Task3, dict(Task1_male_FOB=random.randint(0, 10), Task1_female_FOB=random.randint(1, 10))
        yield Task4, dict(Task1_male_FOB=random.randint(0, 10), Task1_female_FOB=random.randint(1, 10))
        yield Task5, dict(Task1_male_FOB=random.randint(0, 10), Task1_female_FOB=random.randint(1, 10))
        yield Task6, dict(Task1_male_FOB=random.randint(0, 10), Task1_female_FOB=random.randint(1, 10))
        yield Task7, dict(Task1_male_FOB=random.randint(0, 10), Task1_female_FOB=random.randint(1, 10))
        yield Task8, dict(Task1_male_FOB=random.randint(0, 10), Task1_female_FOB=random.randint(1, 10))
        yield Task9, dict(Task1_male_FOB=random.randint(0, 10), Task1_female_FOB=random.randint(1, 10))
        yield Task10, dict(Task1_male_FOB=random.randint(0, 10), Task1_female_FOB=random.randint(1, 10))
        yield Task11, dict(Task1_male_FOB=random.randint(0, 10), Task1_female_FOB=random.randint(1, 10))
        yield Task12, dict(Task1_male_FOB=random.randint(0, 10), Task1_female_FOB=random.randint(1, 10))
        yield Task13, dict(Task1_male_FOB=random.randint(0, 10), Task1_female_FOB=random.randint(1, 10))

        yield Attention_check_2, dict(Attention_check_2=True)
        