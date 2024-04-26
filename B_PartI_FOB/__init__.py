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
    NAME_IN_URL = 'Part_I'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    Instructions_path = "_templates/global/Instructions.html"
    Quit_study_text_path = "_templates/global/Quit_study_text.html"
    tasks_path = "_templates/global/tasks/"

    Return_redirect = "https://www.wikipedia.org/" #TODO: adjust redirect
    
    # for now only the complete tasks are listed here
    #TODO: should we put an average person earned 100 in the question isntead of description?
    Task_details = pd.read_csv('_static/Tasks.csv')


    
class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):   
    # data quality
    blur_event_counts = models.StringField(initial=0, blank=True) # logs how often user clicked out of the page 
    
    # Attention check 2, 1 was in introduction 
    Attention_2 = models.BooleanField(choices=[
            [False, 'I think both are possible.'],
            [True, 'I disagree.'],
            [False, 'I agree.'],], 
        label= 'A 20 year old man can eat 500kg meat and 2 tons of vegetables in one meal.', widget=widgets.RadioSelect)
            
    # Player answers
    Task1_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") #maybe half of the participants should answer with women?
    Task1_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") #maybe half of the participants should answer with women?
    
    Task2_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    Task2_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    Task3_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    Task3_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    Task4_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    Task4_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    Task5_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    Task5_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    Task6_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    Task6_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    Task7_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    Task7_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    Task8_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    Task8_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    Task9_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    Task9_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    Task10_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    Task10_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    Task11_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    Task11_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    Task12_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    Task12_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    Task13_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    Task13_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 

    Task14_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    Task14_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    # uncomment the lines below to see all pages
    # Task15_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    # Task15_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    # Task16_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    # Task16_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    # Task17_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    # Task17_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    # Task18_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    # Task18_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    # Task19_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    # Task19_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    # Task20_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    # Task20_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    # Task21_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    # Task21_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    # Task22_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    # Task22_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    # Task23_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    # Task23_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    # Task24_male_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average man earned</strong>?") 
    # Task24_female_FOB = models.FloatField( min=0, max=200, label="How many points do you think <strong>an average woman earned</strong>?") 
    
    
#%% Functions
def get_task_details(player, page_number):
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
                'Instructions': C.Instructions_path,
                } 
  
# Pages

class Attention_check_2(MyBasePage):         
    extra_fields = ['Attention_2']
    form_fields = MyBasePage.form_fields + extra_fields
    
    def before_next_page(player: Player, timeout_happened=False):
        player.participant.vars['Attention_2'] = player.Attention_2
        if (not player.Attention_2 and not player.participant.vars['Attention_1']):
            player.participant.vars['Allowed'] = False
            player.participant.vars['Attention_passed'] = False

class Task1(MyBasePage):
    extra_fields = ['Task1_male_FOB','Task1_female_FOB'] 
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
    extra_fields = ['Task2_male_FOB','Task2_female_FOB'] 
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
    extra_fields = ['Task3_male_FOB','Task3_female_FOB'] 
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
    extra_fields = ['Task4_male_FOB','Task4_female_FOB'] 
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
    extra_fields = ['Task5_male_FOB','Task5_female_FOB'] 
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
    extra_fields = ['Task6_male_FOB','Task6_female_FOB'] 
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
    extra_fields = ['Task7_male_FOB','Task7_female_FOB'] 
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
    extra_fields = ['Task8_male_FOB','Task8_female_FOB'] 
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
    extra_fields = ['Task9_male_FOB','Task9_female_FOB'] 
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
    extra_fields = ['Task10_male_FOB','Task10_female_FOB'] 
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
    extra_fields = ['Task11_male_FOB','Task11_female_FOB'] 
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
    extra_fields = ['Task12_male_FOB','Task12_female_FOB'] 
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
    extra_fields = ['Task13_male_FOB','Task13_female_FOB'] 
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
    extra_fields = ['Task14_male_FOB','Task14_female_FOB'] 
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
    extra_fields = ['Task15_male_FOB','Task15_female_FOB'] 
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
    extra_fields = ['Task16_male_FOB','Task16_female_FOB'] 
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
    extra_fields = ['Task17_male_FOB','Task17_female_FOB'] 
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
    extra_fields = ['Task18_male_FOB','Task18_female_FOB'] 
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
    extra_fields = ['Task19_male_FOB','Task19_female_FOB'] 
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
    extra_fields = ['Task20_male_FOB','Task20_female_FOB'] 
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
    extra_fields = ['Task21_male_FOB','Task21_female_FOB'] 
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
    extra_fields = ['Task22_male_FOB','Task22_female_FOB'] 
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
    extra_fields = ['Task23_male_FOB','Task23_female_FOB'] 
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
    Task1, Task2,
    Task3, Task4, Task5, Task6, Task7, Task8, Task9, Task10,
    Task11, Task12, Task13, Task14,
    #uncomment the line below to see all tasks
    # Task15, Task16, Task17, Task18, Task19, Task20, Task21, Task22, Task23, 
    Attention_check_2,
    ]
