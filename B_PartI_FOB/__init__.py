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
    
    task_description = {
        'Anagram': '''
        Participants had to solve as many  <strong>Anagram tasks</strong> as possible within a given time.
            In each task, they had to arrange four pairs of letters to form a word like in the example below. For each correct solution, participants earned one point. An average person earned 100 points on this task.
        ''',
        'Ball-bucket': 'Description of Ball-bucket task',
        'Spot-the-difference': 'Description of Spot-the-difference task',
        'Count-numbers': 'Description of Count-numbers task',
        'Data-search': 'Description of Data-search task',
        'Emotion-recognition': 'Description of Emotion-recognition task',
        'Find-hidden-words': 'Description of Find-hidden-words task',
        'Math': 'Description of Math task',
        'Memory': 'Description of Memory task',
        'Search-summation': 'Description of Search-summation task',
        'Word-difference': 'Description of Word-difference task',
        'Maze': 'Description of Maze task',
        'Mental-rotation': 'Description of Mental-rotation task',
        'Multiplication': 'Description of Multiplication task',
        'Number-in-Numbers': 'Description of Number-in-Numbers task',
        'Adding-numbers': 'Description of Adding-numbers task',
        'Quiz': 'Description of Quiz task',
        'Rearrange-words': 'Description of Rearrange-words task',
        'Stock-forecasting': 'Description of Stock-forecasting task',
        'Typing': 'Description of Typing task',
        'Verify-arithmetics': 'Description of Verify-arithmetics task',
        'Visual-memory': 'Description of Visual-memory task',
        'Word-in-word': 'Description of Word-in-word task'
    }

    task_picture_link = {
        'Anagram': 'Link to Anagram picture',
        'Ball-bucket': 'Link to Ball-bucket picture',
        'Spot-the-difference': 'Link to Spot-the-difference picture',
        'Count-numbers': 'Link to Count-numbers picture',
        'Data-search': 'Link to Data-search picture',
        'Emotion-recognition': 'Link to Emotion-recognition picture',
        'Find-hidden-words': 'Link to Find-hidden-words picture',
        'Math': 'Link to Math picture',
        'Memory': 'Link to Memory picture',
        'Search-summation': 'Link to Search-summation picture',
        'Word-difference': 'Link to Word-difference picture',
        'Maze': 'Link to Maze picture',
        'Mental-rotation': 'Link to Mental-rotation picture',
        'Multiplication': 'Link to Multiplication picture',
        'Number-in-Numbers': 'Link to Number-in-Numbers picture',
        'Adding-numbers': 'Link to Adding-numbers picture',
        'Quiz': 'Link to Quiz picture',
        'Rearrange-words': 'Link to Rearrange-words picture',
        'Stock-forecasting': 'Link to Stock-forecasting picture',
        'Typing': 'Link to Typing picture',
        'Verify-arithmetics': 'Link to Verify-arithmetics picture',
        'Visual-memory': 'Link to Visual-memory picture',
        'Word-in-word': 'Link to Word-in-word picture'
    }
    task_picture_desc = {
        'Anagram': 'Description of the picture',
        'Ball-bucket': 'Link to Ball-bucket picture',
        'Spot-the-difference': 'Link to Spot-the-difference picture',
        'Count-numbers': 'Link to Count-numbers picture',
        'Data-search': 'Link to Data-search picture',
        'Emotion-recognition': 'Link to Emotion-recognition picture',
        'Find-hidden-words': 'Link to Find-hidden-words picture',
        'Math': 'Link to Math picture',
        'Memory': 'Link to Memory picture',
        'Search-summation': 'Link to Search-summation picture',
        'Word-difference': 'Link to Word-difference picture',
        'Maze': 'Link to Maze picture',
        'Mental-rotation': 'Link to Mental-rotation picture',
        'Multiplication': 'Link to Multiplication picture',
        'Number-in-Numbers': 'Link to Number-in-Numbers picture',
        'Adding-numbers': 'Link to Adding-numbers picture',
        'Quiz': 'Link to Quiz picture',
        'Rearrange-words': 'Link to Rearrange-words picture',
        'Stock-forecasting': 'Link to Stock-forecasting picture',
        'Typing': 'Link to Typing picture',
        'Verify-arithmetics': 'Link to Verify-arithmetics picture',
        'Visual-memory': 'Link to Visual-memory picture',
        'Word-in-word': 'Link to Word-in-word picture'
    }

    
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
    
    Task2_male_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average man earned</strong>?") 
    Task2_female_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    Task3_male_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average man earned</strong>?") 
    Task3_female_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    Task4_male_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average man earned</strong>?") 
    Task4_female_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    
    Task5_male_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average man earned</strong>?") 
    Task5_female_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    Task6_male_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average man earned</strong>?") 
    Task6_female_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    Task7_male_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average man earned</strong>?") 
    Task7_female_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    Task8_male_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average man earned</strong>?") 
    Task8_female_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    Task9_male_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average man earned</strong>?") 
    Task9_female_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    Task10_male_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average man earned</strong>?") 
    Task10_female_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    Task11_male_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average man earned</strong>?") 
    Task11_female_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    Task12_male_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average man earned</strong>?") 
    Task12_female_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    Task13_male_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average man earned</strong>?") 
    Task13_female_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    Task14_male_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average man earned</strong>?") 
    Task14_female_FOB = models.FloatField(min=0, max=100, label="How many points do you think <strong>an average woman earned</strong>?") 
    
#%% Functions
def get_task_details(player, page_number):
    treatment = player.participant.Treatment
    task = treatment[page_number]
    task = 'Anagram' #TODO: delete this line
    description = C.task_description[task]
    picture_link = C.task_picture_link[task]
    picture_desc = C.task_picture_desc[task]
    
    return task, description, picture_link, picture_desc
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
        task, description, picture_link, picture_desc = get_task_details(player, 1)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
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
