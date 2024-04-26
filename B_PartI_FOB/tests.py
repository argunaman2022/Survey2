from otree.api import Currency as c, currency_range, expect, Bot
from . import *
import random

class PlayerBot(Bot):

    def play_round(self):
        # Simulating player behavior for each page and task in the experiment
        for task_number in range(1, 15):
            yield globals()[f"Task{task_number}"], dict(
            **{f"Task{task_number}_male_FOB": random.randint(0, 200)},
            **{f"Task{task_number}_female_FOB": random.randint(0, 200)}
            )

        yield Attention_check_2, dict(Attention_2=True)
        