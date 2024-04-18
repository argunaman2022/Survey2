from otree.api import *
import random

doc = '''
This is the main survey app. It contains
1. Main survey 
2. One attention check.
- You can additionally calculate payoffs and save them at a participant field.
'''

class C(BaseConstants):
    NAME_IN_URL = 'Study_Name'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    Instructions_path = "_templates/global/Instructions.html"
    Quit_study_text_path = "_templates/global/Quit_study_text.html"
    tasks_path = "_templates/global/tasks/"

    Return_redirect = "https://www.wikipedia.org/" #TODO: adjust redirect
    
    # for now only the complete tasks are listed here
    #TODO: ensure that there is a task.html and pic for every task
    #TODO: add all tasks
    All_tasks = ['Anagram task', 'Ball bucket task', 'Counting numbers in matrix',
                 'Data search task', 'Emotion recognition', 'Matrix search-summation',
                 'Matrix word difference', 'Maze', 'MRT',
                 'Multiplication', 'Number-in-Numbers puzzle', 'NV',
                 'Rearrange words', 'Stock forecasting', 'Typing task',
                 'Verify arithmetics', 'Word-in-word puzzle']



    
class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):   
    # data quality
    blur_event_counts = models.StringField(initial=0) # logs how often user clicked out of the page #TODO: ensure that this is added to all the pages
    
    # Attention check 2, 1 was in introduction 
    Attention_2 = models.BooleanField(choices=[
            [True, 'I disagree.'],
            [False, 'I think both are possible.'],
            [False, 'I agree.'],], 
        label= 'A 20 year old man can eat 500kg meat and 2 tons of vegetables in one meal.', widget=widgets.RadioSelect)
            
    # Player answers
    #TODO: should i force them to add up to 200?
    Task1_male_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average man earned</strong>?") #maybe half of the participants should answer with women?
    Task1_female_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average woman earned</strong>?") #maybe half of the participants should answer with women?
    
    

 
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
  
# Pages
class Task1(MyBasePage):
    extra_fields = ['Task1_male_FOB','Task1_female_FOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)

        # Add or modify variables specific to ExtendedPage
        variables['Treatment'] = player.participant.Treatment
        task = 'Maze' #TODO: make this dynamic
        variables['Title'] = task
        variables['path_task'] = C.tasks_path + f'/{task}/' + task + '.html'
        return variables


class Attention_check_2(MyBasePage):         
    extra_fields = ['Attention_2']
    form_fields = MyBasePage.form_fields + extra_fields
    
    def before_next_page(player: Player, timeout_happened=False):
        if (not player.Attention_2 and not player.participant.vars['Attention_1']):
            player.participant.vars['Allowed'] = False
            player.participant.vars['Attention_passed'] = False
  
page_sequence = [
    Task1,
    Attention_check_2,
    ]
