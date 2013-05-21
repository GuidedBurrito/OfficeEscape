'''
Name: Alex Valickis
Date: May 16th 2013
Game: Text Adventure, Office Escape
'''

import time

def displayIntro():
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
    print ('What is your name?')
    print
    Name = raw_input()
    time.sleep(2)
    return Name
    
def chooseDeskOption():
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
    DeskOption = ''
    while DeskOption != 'Leave' and DeskOption != 'leave' and DeskOption != 'LEAVE' and DeskOption != 'Check' and DeskOption != 'check' and DeskOption != 'CHECK':
        print ('Your ready to go, do you LEAVE your cubicle or stand up and CHECK? (Leave or Check)')
        print
        DeskOption = raw_input()
    return DeskOption

def chooseHallOption():
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
    time.sleep(2)
    print ('The boss is standing right next to you!')
    print ('"Hey! What are you doing!?" he yells at you.')
    HallOption = ''
    while HallOption != 'Lie' and HallOption != 'LIE' and HallOption != 'lie'  and HallOption != 'Stretch' and HallOption != 'stretch' and HallOption != 'STRETCH':
        print ('Do you LIE and tell that you have a doctors appointment or quickly pretend to STRETCH? (Lie or Stretch)')
        print
        HallOption = raw_input()
    return HallOption
    
def chooseSpotOption():
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
    print ('Youve shut your computer down already. If he sees your not doing anything your busted!')
    SpotOption = ''
    while SpotOption != 'Start' and SpotOption != 'START' and SpotOption != 'start' and SpotOption != 'Fax' and SpotOption != 'fax' and SpotOption != 'FAX':
        print ('Do you try and START your computer up again or')
        print ('grab some usless papers and pretend to FAX them? (Start or Fax)')
        print
        SpotOption = raw_input()
    return SpotOption

def chooseLieOption():
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
    print ('As you blather trip and stumble through your very poor lie,')
    print ('the bosses expression goes from confused to angry.')
    print ('"Do you really think im going to believe that!?!?" he yells.')
    LieOption = ''
    while LieOption != 'yes' and LieOption != 'Yes' and LieOption != 'YES' and LieOption != 'no' and LieOption != 'No' and LieOption != 'NO':
        print ('Do you say YES and hope he buys it or say NO and appologise?')
        print
        LieOption = raw_input()
    if LieOption == 'Yes' or LieOption == 'YES' or LieOption == 'yes':
        print
        print
        print ('You try to say yes with all the sincarity you can, but like any rational human being,')
        print ('the boss can tell you lying through your teeth. If the impending doom of your termination')
        print ('wasnt bad enough, hes going to do it infront of the whole office.')
        print ('And like a sharp axe coming down on your head he screams those dredfull words....')
        print ('YOUR FIRED!!!')
        time.sleep(8)
        print
        win = False
    else :
        print
        print
        print ('You sheepishly tell him no and appologise in hopes that he forgets all of this and moves on.')
        print ('After some short grovilling, he accepts your appology but will now be keeping a close eye on you.')
        print ('There will be no more early weekend for you in the future.')
        print
        win = False
    return win 

def chooseStretchOption(Name):
    print
    print
    print
    print ('The Stretch')
    print
    print
    print ('Quickly thinking on your feet, you jump into a stretching pose.')
    print ('As the boss slowly passes by your cubicle, he notices you stretching')
    print ('He asks "While your up ' + Name + ', can you get me a coffee?"')
    StretchOption = ''
    while StetchOption != 'Coffee' and StetchOption != 'COFFEE' and StetchOption != 'coffee' and StetchOption != 'Early' and StetchOption != 'EARLY' and StetchOption != 'early': 
        print ('Do you go get the boss a COFFEE or say youll go and start your weekend EARLY? (Coffee or Early)')
        print
        StretchOption = raw_input()
    if StretchOption == 'Coffee' or StretchOption == 'COFFEE' or StretchOption == 'coffee':
        print
        print
        print ('You happily agree to getting coffe not only because you didnt get fired but you also')
        print ('get to leave the office. Unfortunatly between getting to the coffee shop, waiting in line,')
        print ('and travelling back you spend most of the day getting coffee and end up leaving the same')
        print ('time that you alway do')
        print
        win = False
    else :
        print
        print
        print ('You happily agree to getting your boss coffe only because your not coming back!')
        print ('You got to leave early and meet up with your friends. The weekend was almost perfect...')
        time.sleep(1)
        print ('Untill you found a message left by your boss on your answering machine at home.')
        print ('He was waiting for you to come back, it was only until later that weekend when he saw')
        print ('the photos of you partying with your friends that he knew you skipped getting his coffee.')
        print ('At the creshedo of his rant he tells you not to bother coming in to work on Teusday,')
        print
        print ("You've Been Fired")
        print
        win = False
    return win

def chooseStartOption(Name): 
    print
    print
    print
    print ('The Boot-Up')
    print
    print
    print ('You quickly turn your computer back on hoping that it will get up and runnig quickly.')
    print ('Unfortunatly for you, the computer runs as if hamsters are powering it.')
    print ('As you pound at your keyboard in an atempt to get it to start faster, the boss comes in.')
    print ('"Whats going on with you computer ' + Name + '?')
    while StartOption != 'Crash' and StartOption != 'crash' and StartOption != 'CRASH' and StartOption != 'Update' and StartOption != 'update' and StartOption != 'UPDATE':
        print ('Do you tell your boss it was a compute CRASH or your preforming an UPDATE? (Crash or Update')
        print
        StartOption = raw_input()
    if StartOption == 'Crash' or StartOption == 'crash' or StartOption == 'CRASH':
        print
        print
        print ('You give your boss the best and most convincing lie that you have ever come up with....')
        time.sleep(1)
        print ('And he baught it! "Well thats really unfortunate ' + Name + ', you must have lost everything!')
        print ('Uh-oh, you know where this is going but have no idea how to stop it')
        print ('"I guess youll need to stay late to catch up eith all that work that you lost"')
        print
        win = False
    else :
        print
        print
        print ('You swallow your overwelming nervousness and tell your boss "Its just a routine update.')
        print ('"An update you say" says the boss, "Well thats great! I want you to install this update')
        print ('on everyones system!". Knowing that you have to maintain the lie or else you get fired,')
        print ('you spend the rest of the day pretending to install your imaginary update.')
        print
        win = False
    return win

def chooseFaxOption():
    print
    print
    print
    print ('The Fax Machine')
    print
    print
    print ('Yor franticly search your desk and grab some loose papers.')
    print ('Before you even have time to straighten out the papers the boss peeks inside your cubicle')
    FaxOption = ''
    while FaxOption != 'Send' and FaxOption != 'send' and FaxOption != 'SEND' and FaxOption != 'Hope' and FaxOption != 'hope' and FaxOption != 'HOPE':  
        print ('He isnt leaving, do you quickly throw the papers into the fax machine and SEND it to a made up number')
        print ('or do you organize the papers and HOPE he leaves. (Send or Hope)')
        print
        FaxOption = raw_input()
    if FaxOption == 'Send' or FaxOption == 'SEND' or FaxOption == 'send':
        print
        print
        print ('You clamly put all the papers that you collected and placed the in the fax machine.')
        print ('As you begin to enter a random phone number, you look up to see that the boss has moved on')
        print ('Quickly and quietly, you Ninja your way out of the office.')
        time.sleep(5)
        print
        win = True
    else :
        print
        print
        print ('As you tidy and tap the papers to straighten them out, it attracts the attention of the boss.')
        print ('As he looks more closly at your papers, he bigins to wonder what you are faxing')
        print ('He asks you to explain what your faxing. Not knowing how to explain yourself,')
        print ('you talk your way into hours of more work')
        print
        win = False
    return  win

def main():
    
    playAgain = 'yes'
    Name = displayIntro()
    while playAgain == 'yes' or playAgain == 'y' or playAgain == 'YES':
        DeskOption = chooseDeskOption()
        if DeskOption == 'Leave' or DeskOption == 'leave' or DeskOption == 'LEAVE':
            HallOption = chooseHallOption()
            if HallOption == 'Lie' or HallOption == 'lie' or HallOption == 'LIE':
                win = chooseLieOption()
            else :
                win = chooseStretchOption(Name)
        else:
            SpotOption = chooseSpotOption()
            if SpotOption == 'Start' or SpotOption == 'START' or SpotOption == 'start':
                win = chooseStartOption(Name)
            else:
                win = chooseFaxOption()
        
        if win == True:
            print ('Congradulations! You left early without getting caught!')
            print ('You Win!!!')
        else:
            print ('You couldnt leave early.....')
            print ('You Lose!')    
        
        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()


if __name__ == "__main__": main()