from otree.api import *
import random
import pandas as pd

doc = '''
This is the main survey app. It contains
1. Main survey 
2. One attention check.
- You can additionally calculate payoffs and save them at a participant field.
'''
class C(BaseConstants):
    NAME_IN_URL = 'Part_II'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    Instructions_path = "_templates/global/Instructions.html"
    Quit_study_text_path = "_templates/global/Quit_study_text.html"
    tasks_path = "_templates/global/tasks/"

    Return_redirect = "https://www.wikipedia.org/" #TODO: adjust redirect
    
    # for now only the complete tasks are listed here
    #TODO: ensure that there is a task.html and pic for every task
    #TODO: should we put an average person earned 100 in the question isntead of description?
    Task_details = pd.read_csv('_static/Tasks.csv')
    
    # TODO: this is using the same template for now, adjust it 
    Instructions_PartII = "_templates/global/Instructions_PartII.html" 


    
class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):   
    # data quality
    blur_event_counts = models.StringField(initial=0, blank=True) # logs how often user clicked out of the page #TODO: ensure that this is added to all the pages
  
    Attention_3 = models.BooleanField(initial=False)
    Attention3_male_SOB = models.FloatField(min=0, max=200, label="This is an attention check. <b>Please select</b> 100 below, so that we know you are paying attention.") #maybe half of the participants should answer with women?
    Attention3_female_SOB = models.FloatField(min=0, max=200, label="This is an attention check. <b>Please select</b> 0 below, so that we know you are paying attention.") #maybe half of the participants should answer with women?
    
            
    # Player answers
    #TODO: should i force them to add up to 200?
    #TODO: remove blank=True from all fields below
    Task1_male_SOB = models.FloatField(blank=True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") #maybe half of the participants should answer with women?
    Task1_female_SOB = models.FloatField(blank=True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") #maybe half of the participants should answer with women?
    
    Task2_male_SOB = models.FloatField(blank=True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task2_female_SOB = models.FloatField(blank=True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    Task3_male_SOB = models.FloatField(blank=True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task3_female_SOB = models.FloatField(blank=True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    Task4_male_SOB = models.FloatField(blank=True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task4_female_SOB = models.FloatField(blank=True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    Task5_male_SOB = models.FloatField(blank=True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task5_female_SOB = models.FloatField(blank=True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    Task6_male_SOB = models.FloatField(blank=True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task6_female_SOB = models.FloatField(blank=True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    Task7_male_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task7_female_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    Task8_male_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task8_female_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    Task9_male_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task9_female_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    Task10_male_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task10_female_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    Task11_male_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task11_female_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    Task12_male_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task12_female_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    Task13_male_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task13_female_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    Task14_male_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task14_female_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    #TODO: comment the lines below since a participant should see 14 tasks. Delete the respective pages
    Task15_male_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task15_female_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    Task16_male_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task16_female_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    Task17_male_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task17_female_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    Task18_male_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task18_female_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    Task19_male_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task19_female_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    Task20_male_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task20_female_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    Task21_male_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task21_female_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    Task22_male_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task22_female_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    Task23_male_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task23_female_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    Task24_male_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average man earned?'") 
    Task24_female_SOB = models.FloatField(blank= True, min=0, max=200, label="<strong>What do you think was the average response to the question: </strong>'How many points do you think an average woman earned?'") 
    
    
#%% Functions
def get_task_details(player, page_number):
    page_number = page_number
    treatment = player.participant.Treatment
    task = treatment[page_number-1]
   
    task_row = C.Task_details.loc[C.Task_details['Name'] == task]
    description = task_row['Task_description'].values[0]
    picture_link = f"https://raw.githubusercontent.com/argunaman2022/Survey2/main/_static/Task_pictures/{task}.png"
    picture_desc = task_row['Picture_description'].values[0]
    return task, description, picture_link, picture_desc, page_number
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
                'Instructions': C.Instructions_PartII,
                } 
  
# Pages

class Attention_check_3(MyBasePage):    
    extra_fields = ['Attention3_male_SOB', 'Attention3_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 2)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables
    
    def before_next_page(player: Player, timeout_happened=False):
        if player.Attention3_male_SOB == 100 and player.Attention3_female_SOB == 0:
            player.Attention_3 = True
            print("Attention check 3 passed")
        elif (not player.participant.vars['Attention_1'] or not player.participant.vars['Attention_2']):
            print("Attention check 3 failed")
            player.participant.vars['Allowed'] = False
            player.participant.vars['Attention_passed'] = False

class Instructions_PartII(MyBasePage):
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed
    
    @staticmethod
    def vars_for_template(player: Player):
        return {'hidden_fields': ['blur_event_counts'], #hide the browser field from the participant, see the page to see how this works. #user_clicked_out
                'Page_title': 'PartII: Instructions',
                }

class Task1(MyBasePage):
    extra_fields = ['Task1_male_SOB','Task1_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 1)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables

class Task2(MyBasePage):
    extra_fields = ['Task2_male_SOB','Task2_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 2)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables

class Task3(MyBasePage):
    extra_fields = ['Task3_male_SOB','Task3_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 3)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables

class Task4(MyBasePage):
    extra_fields = ['Task4_male_SOB','Task4_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 4)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables

class Task5(MyBasePage):
    extra_fields = ['Task5_male_SOB','Task5_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 5)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables

class Task6(MyBasePage):
    extra_fields = ['Task6_male_SOB','Task6_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 6)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables

class Task7(MyBasePage):
    extra_fields = ['Task7_male_SOB','Task7_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 7)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables

class Task8(MyBasePage):
    extra_fields = ['Task8_male_SOB','Task8_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 8)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables

class Task9(MyBasePage):
    extra_fields = ['Task9_male_SOB','Task9_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 9)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables

class Task10(MyBasePage):
    extra_fields = ['Task10_male_SOB','Task10_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 10)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables

class Task11(MyBasePage):
    extra_fields = ['Task11_male_SOB','Task11_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 11)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables

class Task12(MyBasePage):
    extra_fields = ['Task12_male_SOB','Task12_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 12)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables

class Task13(MyBasePage):
    extra_fields = ['Task13_male_SOB','Task13_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 13)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables

class Task14(MyBasePage):
    extra_fields = ['Task14_male_SOB','Task14_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 14)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables

class Task15(MyBasePage):
    extra_fields = ['Task15_male_SOB','Task15_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 15)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables

class Task16(MyBasePage):
    extra_fields = ['Task16_male_SOB','Task16_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 16)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables

class Task17(MyBasePage):
    extra_fields = ['Task17_male_SOB','Task17_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 17)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables

class Task18(MyBasePage):
    extra_fields = ['Task18_male_SOB','Task18_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 18)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables

class Task19(MyBasePage):
    extra_fields = ['Task19_male_SOB','Task19_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 19)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables

class Task20(MyBasePage):
    extra_fields = ['Task20_male_SOB','Task20_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 20)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables

class Task21(MyBasePage):
    extra_fields = ['Task21_male_SOB','Task21_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 21)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables

class Task22(MyBasePage):
    extra_fields = ['Task22_male_SOB','Task22_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 22)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables

class Task23(MyBasePage):
    extra_fields = ['Task23_male_SOB','Task23_female_SOB'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        task, description, picture_link, picture_desc, page_number = get_task_details(player, 23)
        
        variables['Task'] = task
        variables['Task_description'] = description
        variables['Picture_link'] = picture_link
        variables['Picture_desc'] = picture_desc
        variables['Page_title'] = f'Task {page_number} of 14'
        return variables




page_sequence = [
    Instructions_PartII,
    Task1, Task2,
    Task3, Task4, Task5, Task6, Task7, Task8, Task9, Task10,
    Task11, Task12, Task13, Task14,
    #TODO: uncomment the line below to see all tasks
    # Task15, Task16, Task17, Task18, Task19, Task20, Task21, Task22, Task23, 
    Attention_check_3,
    ]
