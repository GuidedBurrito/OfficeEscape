'''
Name: Alex Valickis
Date: May 16th 2013
Game: Text Adventure, Office Escape
'''

import time #Imports the time library so sleep can be used

def displayIntro(): #The intro fuction that plays at game start
   
    # Brings up the narative line by line with 2 seccond pauses in between lines
    
    time.sleep(2) 
    print ('Its Friday, and normally, this wouldnt be a big deal.')
    time.sleep(2)
    print ('But today is different............ Its a long weekend')
    time.sleep(2)
    print ('You need to get out early. There is no option.')
    time.sleep(2)
    print ('Can you Escape the Office???')
    time.sleep(2)
    print
    
    #Prompt player for a name
    
    print ('What is your name?')
    print
    Name = raw_input() # Gets the players name
    time.sleep(2)
    return Name #Returns the players name to the main fucntion
    
def chooseDeskOption(): # The function for the starting location
    
    # Displays Narrative
    
    print
    print
    print
    print ('The Cubicle')
    print
    print
    print ('Your escape starts in your cubicle.')
    print ('Its a small space but its yours.')
    print ('The boss lets you keep funny pictures on your desk.')
    print ('The weekend is circled on your calendar in red marker.')
    print ('You have been waiting for this day all month.')
    time.sleep(8)
    print
    print
    print
    DeskOption = '' # Instantiatesthe desk option varriable
    # While loop that makes sure the player enters the correct word before moving on
    while DeskOption != 'Leave' and DeskOption != 'leave' and DeskOption != 'LEAVE' and DeskOption != 'Check' and DeskOption != 'check' and DeskOption != 'CHECK':
        print ('With all your things in hand youre now ready to go.')
        print ('Do you LEAVE your cubicle or stand up and CHECK? (Leave or Check)')
        print
        DeskOption = raw_input() #Gets the players choice
    return DeskOption #sends the players choice to the main function

def chooseHallOption(Name): # Function that iplayed if the player chooses to leave, Name is imported into the function
    
    # Narrative is played
    
    print
    print
    print
    print ('The Hall')
    print
    print
    print ('You step out into the hallway that mazes through the office.')
    print ('As you look around, you see all the other poor saps at their desks.')
    print ('Mindlessly droning on. Its a sad sight.')
    print ('As you turn to walk to the door your heart drops deep into your gut.....')
    time.sleep(5)
    print ('The boss is standing right next to you!')
    print ('"Hey' + Name + '! What are you doing!?" he yells at you.')
    HallOption = '' # Variable is istantiated
    # While loop that makes sure the player enters the correct word before moving on
    while HallOption != 'Lie' and HallOption != 'LIE' and HallOption != 'lie'  and HallOption != 'Stretch' and HallOption != 'stretch' and HallOption != 'STRETCH':
        print ('Do you LIE and tell that you have a doctors appointment')
        print ('or quickly pretend to STRETCH? (Lie or Stretch)')
        print
        HallOption = raw_input() # Gets players choice
    return HallOption #sends the players choice to the main function
    
def chooseSpotOption(): #Funtions that plays if the user selected the check option
    
    # Variable is istantiated
    
    print
    print
    print
    print ('The Spotter')
    print
    print
    print ('Quietly standing up, you peak over the walls of your cubicle.')
    print ('As you scope out the office you see the boss is making his rounds.')
    print ('He is a couple cubicles away from reaching yours. And then it hits you....')
    time.sleep(5)
    print ('You have fully shutdown your computer already.')
    print ('If he sees your not doing anything your busted!')
    SpotOption = '' # Variable is istantiated
    # While loop that makes sure the player enters the correct word before moving on
    while SpotOption != 'Start' and SpotOption != 'START' and SpotOption != 'start' and SpotOption != 'Fax' and SpotOption != 'fax' and SpotOption != 'FAX':
        print ('Do you try and START your computer up again or')
        print ('grab some usless papers and pretend to FAX them? (Start or Fax)')
        print
        SpotOption = raw_input() # Gets players choice
    return SpotOption  #sends the players choice to the main function

def chooseLieOption(): #Funtions that plays if the user selected the lie option
    print
    print
    print
    print ('The Lie')
    print
    print
    print ('You choose to lie to your boss which is very supprising....')
    time.sleep(2)
    print ('Because your a horrible liar.')
    time.sleep(3)
    print
    print ('As you blather, trip, and stumble through your very poor lie,')
    print ('the bosses expression goes from confused to angry.')
    print ('"Do you really think im going to believe that!?!?" he yells.')
    LieOption = '' # Variable is istantiated
    # While loop that makes sure the player enters the correct word before moving on
    while LieOption != 'yes' and LieOption != 'Yes' and LieOption != 'YES' and LieOption != 'no' and LieOption != 'No' and LieOption != 'NO':
        print ('Do you say YES and hope he buys it or say NO and appologise? (Yes or No)')
        print
        LieOption = raw_input() # Gets players choice
    if LieOption == 'Yes' or LieOption == 'YES' or LieOption == 'yes': #If the player chooses option 1
        print
        print
        print ('You try to say yes as sincierly as you can, but like any rational human being,')
        print ('the boss can tell you lying through your teeth. If the impending doom of your,')
        print ('job wasnt bad enough, hes going to do it infront of the whole office.')
        print ('And like a sharp axe coming down on your head he screams those dredfull words...')
        print ('YOUR FIRED!!!')
        time.sleep(8)
        print
        win = False #Assigns a true or false value that determinds if the player wins or loses
    else : # if player chooses option 2
        print
        print
        print ('You sheepishly tell him no and appologise in hopes that he forgets all of this')
        print ('and moves on. After some short grovilling, he accepts your appology but will')
        print ('be keeping a close eye on you. There will be no early weekends in your future.')
        print
        win = False #Assigns a true or false value that determinds if the player wins or loses
    return win # Returns the win or lose to the main function

def chooseStretchOption(Name): #Funtions that plays if the user selected thestretch option, Name is imported into the function
    
    # Variable is istantiated
    
    print
    print
    print
    print ('The Stretch')
    print
    print
    print ('Quickly thinking on your feet, you jump into a stretching pose.')
    print ('As the boss slowly passes by your cubicle, he notices you stretching')
    print ('He asks "While your up ' + Name + ', can you get me a coffee?"')
    StretchOption = '' # Variable is istantiated
    # While loop that makes sure the player enters the correct word before moving on
    while StretchOption != 'Coffee' and StretchOption != 'COFFEE' and StretchOption != 'coffee' and StretchOption != 'Early' and StretchOption != 'EARLY' and StretchOption != 'early': 
        print ('Do you go get the boss a COFFEE or ditch and start your weekend EARLY?')
        print ('(Coffee or Early)')
        print
        StretchOption = raw_input() # Gets players choice
    if StretchOption == 'Coffee' or StretchOption == 'COFFEE' or StretchOption == 'coffee': #If the player chooses option 1
        print
        print
        print ('You happily agree to getting coffe not only because you didnt get')
        print ('fired but you also get to leave the office. Unfortunatly between')
        print ('getting to the coffee shop, waiting in line, and travelling back')
        print ('you spend most of the day getting coffee and end up leaving the')
        print ('same time that you alway do.')
        print
        win = False #Assigns a true or false value that determinds if the player wins or loses
    else : # if player chooses option 2
        print
        print
        print ('You happily agree to getting your boss coffee only because your not')
        print ('coming back! You got to leave early and meet up with your friends.')
        print ('The weekend was almost perfect...')
        time.sleep(5)
        print ('Untill you found a message left by your boss on your answering machine at home.')
        print ('He was waiting for you to come back, it was only until later that weekend when')
        print ('he saw the photos of you partying with your friends that he knew you skipped')
        print (' getting his coffee. At the creshedo of his rant he tells you not to bother')
        print ('coming in to work on Teusday,')
        print
        print ("You've Been Fired")
        print
        win = False #Assigns a true or false value that determinds if the player wins or loses
    return win # Returns the win or lose to the main function

def chooseStartOption(Name):  #Funtions that plays if the user selected the start option, Name is imported into the function
    
    # Variable is istantiated
    
    print
    print
    print
    print ('The Boot-Up')
    print
    print
    print ('You quickly turn your computer back on hoping that it will ready.')
    print ('Unfortunatly for you, the computer runs as if hamsters are powering it.')
    print ('As you pound at your keyboard trying to get it to start faster...')
    time.sleep(2)
    print ('The boss comes in.')
    print ('"Whats going on with you computer ' + Name + '?')
    StartOption = '' # Variable is istantiated
    # While loop that makes sure the player enters the correct word before moving on
    while StartOption != 'Crash' and StartOption != 'crash' and StartOption != 'CRASH' and StartOption != 'Update' and StartOption != 'update' and StartOption != 'UPDATE':
        print ('Do you tell your boss it was a computer CRASH or your preforming an UPDATE?')
        print ('(Crash or Update)')
        print
        StartOption = raw_input()  # Gets players choice
    if StartOption == 'Crash' or StartOption == 'crash' or StartOption == 'CRASH': #If the player chooses option 1
        print
        print
        print ('You give the boss your most convincing lie that you have ever come up with...')
        time.sleep(2)
        print ('And he baught it!')
        time.sleep(2)
        print ('"Well thats really unfortunate ' + Name + ', you must have lost everything!')
        print ('Uh-oh, you know where this is going but have no idea how to stop it')
        print ('"I guess youll need to stay late to catch up eith all that work that you lost"')
        print
        win = False #Assigns a true or false value that determinds if the player wins or loses
    else : # if player chooses option 2
        print
        print
        print ('Trying not to panic you tell your boss "Its just a routine update"')
        print ('"An update?" says the boss, "Thats great! I want you to install this update')
        print ('on everyones system!". Knowing that you have to maintain the lie or youll get')
        print ('fired, you spend the rest of the day pretending to install your imaginary update')
        print
        win = False #Assigns a true or false value that determinds if the player wins or loses
    return win # Returns the win or lose to the main function

def chooseFaxOption(): #Funtions that plays if the user selected the fax option
    
    # Variable is istantiated
    
    print
    print
    print
    print ('The Fax Machine')
    print
    print
    print ('Yor franticly search your desk and grab some loose papers.')
    print ('Before you even have time to straighten out the papers the')
    print ('boss peeks inside your cubicle')
    FaxOption = '' # Variable is istantiated
    # While loop that makes sure the player enters the correct word before moving on
    while FaxOption != 'Send' and FaxOption != 'send' and FaxOption != 'SEND' and FaxOption != 'Hope' and FaxOption != 'hope' and FaxOption != 'HOPE':  
        print ('He isnt leaving, do you quickly throw the papers into the fax machine and')
        print ('SEND it to a made up number or do you organize the papers and HOPE he leaves.')
        print ('(Send or Hope)')
        print
        FaxOption = raw_input() # Gets players choice
    if FaxOption == 'Send' or FaxOption == 'SEND' or FaxOption == 'send': #If the player chooses option 1
        print
        print
        print ('You clamly put all the papers you collected and placed the in the fax machine.')
        print ('As you begin to enter a random number, you look up to see....')
        time.sleep(3)
        print ('Your diversion worked! The boss has moved on!')
        print ('Quickly and quietly, you Ninja your way out of the office.')
        time.sleep(5)
        print
        win = True #Assigns a true or false value that determinds if the player wins or loses
    else : # if player chooses option 2
        print
        print
        print ('As you tap and shuffle the papers you collected to straighten them out,')
        print ('The extra movememnt attracts the attention of the boss.')
        print ('As he looks more closly at your papers, he bigins to wonder what you are faxing')
        print ('He asks you to explain what your faxing. Not knowing how to explain yourself,')
        print ('you talk your way into hours of more work')
        print
        win = False #Assigns a true or false value that determinds if the player wins or loses
    return  win # Returns the win or lose to the main function

def main(): #The main function that calls the rest of the functions
    
    playAgain = 'yes' #Variable is instatiated
    Name = displayIntro() #Calls the intro which gets the players name 
    # While loop that makes sure the player enters the correct word before moving on
    while playAgain == 'yes' or playAgain == 'y' or playAgain == 'YES' or playAgain == 'Yes':
        DeskOption = chooseDeskOption() #calls the starting location
        if DeskOption == 'Leave' or DeskOption == 'leave' or DeskOption == 'LEAVE':
            HallOption = chooseHallOption(Name) #calls location 1of2
            if HallOption == 'Lie' or HallOption == 'lie' or HallOption == 'LIE':
                win = chooseLieOption() #calls location 1 of 4
            else :
                win = chooseStretchOption(Name) #calls location 2 of 4
        else:
            SpotOption = chooseSpotOption() #calls location 2of2
            if SpotOption == 'Start' or SpotOption == 'START' or SpotOption == 'start':
                win = chooseStartOption(Name) #calls location 3 of 4
            else:
                win = chooseFaxOption() #calls location 3 of 4
        
        if win == True: # Prints a congradulations message if the player has won
            print ('Congradulations! You left early without getting caught!')
            print ('You Win!!!')
        else: # Plays a you lose message if the player loses
            print ('You couldnt leave early.....')
            print ('You Lose!')    
        
        print ('Do you want to play again? (yes or no)') #Asks if the player wants to try again
        playAgain = raw_input() # Gets players choice


if __name__ == "__main__": main() #Calls the main function