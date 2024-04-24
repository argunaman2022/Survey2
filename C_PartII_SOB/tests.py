from otree.api import Currency as c, currency_range, expect, Bot
from . import *
import random

class PlayerBot(Bot):

    def play_round(self):
        # Simulating player behavior for each page and task in the experiment
        yield Instructions_PartII 
        
        for task_number in range(1, 15):
            yield globals()[f"Task{task_number}"], dict(
            **{f"Task{task_number}_male_SOB": random.randint(0, 10)},
            **{f"Task{task_number}_female_SOB": random.randint(1, 10)}
            )

        yield Attention_check_3, dict(Attention3_male_SOB=100, Attention3_female_SOB=0)

        