from otree.api import *
import random

doc = '''
This is the first app - the Introduction app. It contains
1. Demographics page
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
    Completion_redirect = "https://app.prolific.com/submissions/complete?cc=CXLTD9FL" 
    Reject_redirect = "https://app.prolific.com/submissions/complete?cc=C1JREY8Y" 
    Return_redirect = "https://app.prolific.com/submissions/complete?cc=CJG550CR"
    
    Instructions_path = "_templates/global/Instructions.html"
    Quit_study_text_path = "_templates/global/Quit_study_text.html"
    
    All_tasks = ['Anagram', 'Ball-bucket', 'Spot-the-difference', 
                'Count-numbers', 'Data-search', 'Emotion-recognition',
                'Find-hidden-words', 'Math', 'Memory',
                'Search-summation', 'Letter-difference', 'Maze',
                'Mental-rotation', 'Multiplication', 'Number-in-Numbers',
                'Adding-numbers', 'Quiz', 'Rearrange-words',
                'Stock-forecasting', 'Typing', 'Verify-arithmetics',
                'Visual-memory','Word-in-word']
    
    # Treatment quotas. This will be copied to the session variables: one for each of the three gender choices.
    quotas = {
    'Anagram':0, 'Ball-bucket':0, 'Spot-the-difference':0, 
    'Count-numbers':0, 'Data-search':0, 'Emotion-recognition':0,
    'Find-hidden-words':0, 'Math':0, 'Memory':0,
    'Search-summation':0, 'Letter-difference':0, 'Maze':0,
    'Mental-rotation':0, 'Multiplication':0, 'Number-in-Numbers':0,
    'Adding-numbers':0, 'Quiz':0, 'Rearrange-words':0,
    'Stock-forecasting':0, 'Typing':0, 'Verify-arithmetics':0,
    'Visual-memory':0,'Word-in-word':0
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

    subsession.session.Quotas_male = C.quotas.copy()
    subsession.session.Quotas_female = C.quotas.copy()
    subsession.session.Quotas = C.quotas.copy()
    
    
    for player in subsession.get_players():
        player.participant.Allowed = True
        player.participant.Comprehension_passed = False 
            

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # Demographics
    prolific_id = models.StringField(default=str("None")) #prolific id, will be fetched automatically.
    age = models.IntegerField( label="Age", min=18, max=100)
    gender = models.StringField( label='Gender at birth',
                                choices=['Male', 'Female', 'Other/Prefer not to say'], widget=widgets.RadioSelect)
    education = models.StringField( label = 'Education level',
                                   choices=['Did not graduate from high school','GED','High school graduate','Bachelors','Masters','Professional degree (JD, MD, MBA)','Doctorate'], widget=widgets.RadioSelect) 
    # education = models.StringField(label = 'Education level',
    #                                choices=['High school or lower','Bachelors degree','Masters degree','PhD','Other'], widget=widgets.RadioSelect) 
    
    income = models.StringField( label='Approximately, what was your <strong>total household income</strong> in the last year, before taxes?',
                            choices=['$0-$10.000', '$10.000-$20.000','$20.000-$30.000','$30.000-$40.000','$40.000-$50.000','$50.000-$60.000',
                                     '$50.000-$75.000', '$75.000-$100.000', '$100.000-$150.000', '$150.000-$200.000', '$200.000+', 'Prefer not to answer',
                                     ],)
    
    # Data quality. 
    browser = models.StringField(blank=True) #browser used by the participant
    blur_event_counts = models.StringField(initial=0, blank=True) # logs how often user clicked out of the page 
    'Comprehension and attention checks'
    #whether the player got the comprehension questions rigt at the first try
    Comprehension_1 = models.BooleanField(initial=True) 
    #In the first comprehension check, the questions the player has answered wrong are stored as a string below.
    Comprehension_wrong_answers = models.StringField(initial='') 
    Comprehension_2 = models.BooleanField(initial=True) 
    
    Comprehension_question_1 = models.BooleanField(choices=[
            [True,'One of my answers from either Part I or Part II will be randomly chosen to determine my bonus.'], # Correct answer here
            [False, 'One of my answers from Part I will be randomly chosen to determine my bonus.'],
            [False, 'One of my answers from Part II will be randomly chosen to determine my bonus'],],
        label = 'Which of the following is correct?',
        widget=widgets.RadioSelect)
    
    Comprehension_question_2 = models.BooleanField(choices=[
            [False,'To play the same various tasks that others have completed in in the past.'], # Correct answer here
            [True, 'To guess the average performance of men and women who, in the past, took part in various tasks.'],
            [False, 'To guess how other people will perform in various tasks in the future.'],],
        label = 'What is your task in Part I?',
        widget=widgets.RadioSelect)
    
    Comprehension_question_3 = models.BooleanField(choices=[
            [False,'30, because 30+70=100'], # Correct answer here
            [True, '130, because the average of 70 and 130 is 100.'],
            [False, '142, because 142*70=100*100.'],],
        label = 'Suppose that the average performance across all men and women was 100. Suppose as well that an average man scored 70 points. How many points did an average woman score?',
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
    session=player.subsession.session
    
    if player.gender == 'Male':
        Quotas = session.Quotas_male
    elif player.gender == 'Female':
        Quotas = session.Quotas_female
    else:
        Quotas = session.Quotas
    
    
    
    #the line below does: splits the Quotas into two halves, picks one of them randomly from the bottom half.
    '''
    Quota/Treatment assignment works as follows:
    0. Assign either Math or Memory to treatment. 
    1. get the current quotas
    2. assign 13 tasks to the player from tasks that have the lowest quotas. 
    3. Increment those quotas
    '''
    treatment = random.sample(['Math','Memory'],1) 
    
    idx = 0
    for i in range(13):
        task = random.choice([key for key, value in Quotas.items() if value in sorted(Quotas.values())[:12] and key not in ['Math', 'Memory'] and key not in treatment])
        treatment.append(task)
        Quotas[task]+=1
    
    # randomized order
    treatment = random.sample(treatment, len(treatment))
    

    #uncomment the line below to display only all the tasks
    # treatment = C.All_tasks.copy()
    player.participant.Treatment = treatment
    
    if player.gender == 'Male':
        session.Quotas_male = Quotas 
    elif player.gender == 'Female':
        session.Quotas_female = Quotas 
    else:
        session.Quotas = Quotas
    
    
    # print('Treatment assigned:', treatment)
    # print('\nQuotas:', Quotas)


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
class Consent(Page):   
    @staticmethod
    def before_next_page(player: Player, timeout_happened=False):
        player.prolific_id = player.participant.label #save prolific id
        
class Demographics(MyBasePage):
    extra_fields = ['age', 'gender', 'education', 'income','browser'] 
    form_fields = MyBasePage.form_fields + extra_fields
        
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)

        variables['hidden_fields'].append('browser') 
        return variables
    @staticmethod
    def before_next_page(player: Player, timeout_happened=False):
        treatment_assignment(player)
    
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


page_sequence = [Consent, Demographics, Instructions,
                 Comprehension_check_1, Comprehension_check_2,
                 Attention_check_1]