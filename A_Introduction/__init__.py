from otree.api import *
import random

doc = '''
This is the first app - the Introduction app. It contains
1. Demgraphics page
2. Instructions that participants can always access
3. Comprehension checks 
4. and the first attention checks
Following are saved to the participant level
- Allowed: if they didnt fail the comprehension checks
- Comprehension_passed: whether they passed the comprehension checks
- Attention_1: whether they passed the first attention check
- Treatment: which treatment they are assigned to
'''

class C(BaseConstants):
    NAME_IN_URL = 'Introduction'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    # Prolific links:
    Completion_redirect = "https://www.wikipedia.org/" #TODO: adjust completion redirect
    Reject_redirect = "https://www.wikipedia.org/" #TODO: adjust reject redirect
    Return_redirect = "https://www.wikipedia.org/" #TODO: adjust return redirect
    
    Instructions_path = "_templates/global/Instructions.html"
    Quit_study_text_path = "_templates/global/Quit_study_text.html"
    
    All_tasks = ['Anagram', 'Ball-bucket', 'Spot-the-difference', 
                'Count-numbers', 'Data-search', 'Emotion-recognition',
                'Find-hidden-words', 'Math', 'Memory',
                'Search-summation', 'Word-difference', 'Maze',
                'Mental-rotation', 'Multiplication', 'Number-in-Numbers',
                'Adding-numbers', 'Quiz', 'Rearrange-words',
                'Stock-forecasting', 'Typing', 'Verify-arithmetics',
                'Visual-memory','Word-in-word']
    
    # Treatment quotas. This will be copied to the session variable.
    quotas = {
    'Male_Math': 0,
    'Male_Memory' : 0,
    'Female_Math': 0,
    'Female_Memory': 0,
    }
    
class Subsession(BaseSubsession):
    pass

def creating_session(subsession):
    '''
    1. create the quotas for each treatment to be saved to the session variable
        - make sure that in the settings.py file the SESSION_FIELDS has initialized the session variables
    2. These quotas are initially zero but as participants are assigned they are incremented. 
    - It is important to note that although prolific ensures gender balanced sample,
        we need this balancing to be within treatment level also
    '''

    subsession.session.Treatment_quotas = C.quotas.copy()
    
    for player in subsession.get_players():
        player.participant.Allowed = True
        player.participant.Comprehension_passed = False 
            

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # Demographics
    #TODO: make all of these fields required by removing blank=True
    prolific_id = models.StringField(default=str("None")) #prolific id, will be fetched automatically.
    age = models.IntegerField(blank=True, label="Age", min=18, max=100)
    gender = models.StringField(blank=True, label='Gender at birth',
                                choices=['Male', 'Female', 'Other/Prefer not to say'], widget=widgets.RadioSelect)
    education = models.StringField(blank=True, label = 'Education level',
                                   choices=['Haven’t graduated high school','GED','High school graduate','Bachelors','Masters','Professional degree (JD, MD, MBA)','Doctorate'], widget=widgets.RadioSelect) 
    # education = models.StringField(label = 'Education level',
    #                                choices=['High school or lower','Bachelors degree','Masters degree','PhD','Other'], widget=widgets.RadioSelect) 
    
    employment = models.StringField(blank=True, label='Employment status',
                                    choices=['Employed full-time', 'Employed part-time', 'Independent, or business owner', 'Out of work, or seeking work',
                                             'Student', 'Out of labor force (e.g. retired or parent raising one or more children)'], widget=widgets.RadioSelect)
    income = models.StringField(blank=True, label='Approximately, what was your <strong>total household income</strong> in the last year, before taxes?',
                            choices=['$0-$10.000', '$10.000-$20.000','$20.000-$30.000','$30.000-$40.000','$40.000-$50.000','$50.000-$60.000',
                                     '$50.000-$75.000', '$75.000-$100.000', '$100.000-$150.000', '$150.000-$200.000', '$200.000+', 'Prefer not to answer',
                                     ],)
    
    # Data quality. 
    browser = models.StringField(blank=True) #browser used by the participant #TODO: make sure this variable is saved in the very first page (e.g. see demographics)
    blur_event_counts = models.StringField(initial=0) # logs how often user clicked out of the page #TODO: ensure that this is added to all the pages
    'Comprehension and attention checks'
    #whether the player got the comprehension questions rigt at the first try
    Comprehension_1 = models.BooleanField(initial=True) 
    #In the first comprehension check, the questions the player has answered wrong are stored as a string below.
    Comprehension_wrong_answers = models.StringField(initial='') 
    Comprehension_2 = models.BooleanField(initial=True) 
    
    Comprehension_question_1 = models.BooleanField( choices=[
            [True,'Correct answer'], # Correct answer here
            [False, 'False answer'],
            [False, 'False answer'],],
        label = 'Comprehension question 1 - Correct answer is the first one',
        widget=widgets.RadioSelect,
        )
    Comprehension_question_2 = models.BooleanField(choices=[
            [True,'Correct answer'], 
            [False, 'False answer'],
            [False, 'False answer'],],
        label = 'Comprehension question 1',
        widget=widgets.RadioSelect)
    Comprehension_question_3 = models.BooleanField(choices=[
            [True,'Correct answer'], 
            [False, 'False answer'],
            [False, 'False answer'],],
        label = 'Comprehension question 1',
        widget=widgets.RadioSelect)
    
    Attention_1 = models.BooleanField(choices=[
                [False, 'Canada'],
                [False, 'USA'],
                [False, 'Austria'],
                [False, 'Germany'],
                [False, 'Switzerland'],
                [True, 'Russia'], 
                [False, 'India'],
                [False, 'Australia'],
                [False, 'China'],
                ],
            label='Choose the country that was mentioned in the instructions above.',
            widget=widgets.RadioSelect)
    HoneyPot = models.StringField(label='Please fill in some sentences here', blank=True) #honeypot to catch bots
    
#%% Functions
def treatment_assignment(player):
    #TODO: ensure that treatment assignment is working properly i.e. given 660 random people we have equal number of tasks (excl math memory)
    session=player.subsession.session
    Quotas = session.Treatment_quotas
    
    #the line below does: splits the Quotas into two halves, picks one of them randomly from the bottom half.
    '''
    Quota/Treatment assignment works as follows:
    1. get the current quotas
    2. assign a random treatment from the bottom half of the quotas (i.e. the treatment with the lowest quota)
    3. update quotas accordingly.
    '''
    Quota = random.choice([key for key, value in Quotas.items() if value in sorted(Quotas.values())[:1]])
    #treatment equals either Math or Memory + 13 random tasks from All_tasks
    treatment = [Quota.split('_')[1]] + random.sample(C.All_tasks, 13)
    # randomize the items #TODO: check if it works
    treatment = random.sample(treatment, len(treatment))
    
    player.participant.Treatment = treatment
    print('Treatment assigned:', treatment)
    Quotas.update({Quota: Quotas[Quota]+1})


# PAGES
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

#Consent, Demographics, Introduction, Comprehension checks and attention check 1
#TODO: add quit study button to all pages
class Consent(Page):   
    @staticmethod
    def before_next_page(player: Player, timeout_happened=False):
        player.prolific_id = player.participant.label #save prolific id
        treatment_assignment(player) #assign treatment and update quotas 
        
class Demographics(MyBasePage):
    #TODO: add honeypot field to demographics
    extra_fields = ['age', 'gender', 'education', 'income','browser'] 
    form_fields = MyBasePage.form_fields + extra_fields
        
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)

        variables['hidden_fields'].append('browser') 
        return variables
    
class Instructions(MyBasePage):
    pass        

            
class Comprehension_check_1(MyBasePage):
    extra_fields = ['Comprehension_question_1', 'Comprehension_question_2', 'Comprehension_question_3']
    form_fields = MyBasePage.form_fields + extra_fields    

    @staticmethod   
    def before_next_page(player: Player, timeout_happened=False):
        player_passed_comprehension = player.Comprehension_question_1 and player.Comprehension_question_2 and player.Comprehension_question_3
        # if player has answered a question wrong then I save it in a string
        wrong_answers = ''
        if not player.Comprehension_question_1:
            player.Comprehension_question_1 = None #reset player answer so it doesnt show up in the next page
            wrong_answers+= 'first question'
        if not player.Comprehension_question_2:
            if not wrong_answers =='': wrong_answers += ', '
            player.Comprehension_question_2 = None
            wrong_answers+= 'second question'
        if not player.Comprehension_question_3:
            if not wrong_answers =='': wrong_answers += ', '
            player.Comprehension_question_3 = None
            wrong_answers+= 'third question'
        
        player.Comprehension_wrong_answers = wrong_answers
        player.Comprehension_1 = player_passed_comprehension
        # save at the participant level
        if player_passed_comprehension:
            player.participant.vars['Comprehension_passed'] = True

        
class Comprehension_check_2(MyBasePage):
    extra_fields = ['Comprehension_question_1', 'Comprehension_question_2', 'Comprehension_question_3']
    form_fields = MyBasePage.form_fields + extra_fields    

    @staticmethod
    def is_displayed(player: Player):
        condition = MyBasePage.is_displayed(player) and not player.Comprehension_1
        return condition
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)

        # Add or modify variables specific to ExtendedPage
        variables['Comprehension_wrong_answers'] = player.Comprehension_wrong_answers
        return variables

    @staticmethod   
    def before_next_page(player: Player, timeout_happened=False):
        player_passed_comprehension = (player.Comprehension_question_1 and
                                       player.Comprehension_question_2 and player.Comprehension_question_3)
        #failing two compr. checks player is not allowed to continue
        player.participant.Allowed = player_passed_comprehension
        player.Comprehension_2 = player_passed_comprehension
        # save at the participant level if they passed
        if player_passed_comprehension:
            player.participant.vars['Comprehension_passed'] = True
            player.participant.vars['Allowed']=True
        else:
            player.participant.vars['Allowed']=False
            player.participant.vars['Comprehension_passed'] = False

class Attention_check_1(MyBasePage):
    extra_fields = ['Attention_1']
    form_fields = MyBasePage.form_fields + extra_fields    
    #save at  the participant level
    @staticmethod   
    def before_next_page(player: Player, timeout_happened=False):
        player.participant.vars['Attention_1'] = player.Attention_1

#Add back  Demographics, Instructions,

page_sequence = [Consent,
                 Comprehension_check_1, Comprehension_check_2,
                 Attention_check_1]