from otree.api import *


doc = '''
Third app - Exit survey.
'''

class C(BaseConstants):
    NAME_IN_URL = 'Exit_Survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    Instructions_path = "_templates/global/Instructions.html"
    Quit_study_text_path = "_templates/global/Quit_study_text.html"

    Return_redirect = "https://app.prolific.com/submissions/complete?cc=CJG550CR"


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # Exit survey
    Compet_measure = models.FloatField()
    Gender_measure = models.FloatField()
    
    #Pilot questions
    Pilot_1 = models.StringField(label = 'The general instructions were clear and easy to understand.' , 
                                 choices=['Strongly disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly agree'], widget=widgets.RadioSelectHorizontal
    )
    Pilot_2 = models.StringField(label = 'The payment rules for the bonus payment were clear and easy to understand.' , 
                                 choices=['Strongly disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly agree'], widget=widgets.RadioSelectHorizontal
    )
    Pilot_3 = models.StringField(label = 'The instructions for the tasks you were evaluating were clear and easy to understand.' , 
                                 choices=['Strongly disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly agree'], widget=widgets.RadioSelectHorizontal
    )
    Pilot_4 = models.StringField(label = 'Was the study interesting/boring?' , 
                                 choices=['Very boring', 'Boring', 'Neutral', 'Interesting', 'Very interesting'], widget=widgets.RadioSelectHorizontal
    )
    Pilot_5 = models.LongStringField(label = 'Any other general remarks? (e.g. technical issues, suggestions for improvement, etc.)', 
                                 blank=True
    )
    
    blur_event_counts = models.StringField(initial=0, blank=True) # logs how often user clicked out of the page 


#%% Base Pages
class MyBasePage(Page):
    'MyBasePage contains the functions that are common to all pages'
    form_model = 'player'
    form_fields = ['blur_event_counts']
    
    
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed 
    
    @staticmethod
    def vars_for_template(player: Player):
        return {'hidden_fields': ['blur_event_counts'], #hide the browser field from the participant, see the page to see how this works. #user_clicked_out
                'Instructions': C.Instructions_path} 

#%% Pages

class Compet_measure(MyBasePage):
    extra_fields = ['Compet_measure', 'Gender_measure']
    form_fields = MyBasePage.form_fields + extra_fields
    
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        variables['hidden_fields'] = variables['hidden_fields'] + ['Compet_measure', 'Gender_measure'] 
        return variables
    
# Only for pilot
#TODO: remove pilot questions before launch
class Pilot(MyBasePage):
    extra_fields = ['Pilot_1','Pilot_2','Pilot_3','Pilot_4','Pilot_5']
    form_fields = MyBasePage.form_fields + extra_fields
    
        
page_sequence = [Compet_measure, Pilot, ]
