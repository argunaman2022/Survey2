from otree.api import Currency as c, currency_range, expect, Bot
from . import *
import random

class PlayerBot(Bot):
    def play_round(self):           
        #returns random values for demographics  
        yield Consent #nothing to submit
         
        yield Demographics, dict(
            age= random.randint(18, 99),
            gender = random.choices(["Male", "Female", "Other/Prefer not to say"], [0.45,0.45,0.1])[0],
            education = 'GED',
            income = '$0-$10.000',
            
        ) 
        yield Instructions #nothing to submit  
        #returns random values for the attention check, if the player fails the attention check, his attention's set to False
        #returns random values for the comprehension check, if the player fails the comprehension check, his comprehension 1 is set to False and he sees the second page
        yield Comprehension_check_1, dict(Comprehension_question_1 = True,
                                            Comprehension_question_2 = True,
                                            Comprehension_question_3 = True)
        
        yield Attention_check_1 , dict(Attention_1 = True) 
        
        