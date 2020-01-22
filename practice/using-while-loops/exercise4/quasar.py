"""
Script to play a text-based version of Quasar from Mass Effect

The rules are explained in the specifications below.  For the optimal strategy to
maximize your winnings, see
    
    https://masseffect.fandom.com/wiki/Quasar

Author: Paul Murff
Date: Jan 17 2020
"""
import random
import introcs


# Do not touch these first two functions. They are finished for you.
def prompt(prompt,valid):
    """
    Returns the choice from a given prompt.
    
    This function asks the user a question, and waits for a response.  It checks
    if the response is valid against a list of acceptable answers.  If it is not
    valid, it asks the question again. Otherwise, it returns the player's answer.
    
    Parameter prompt: The question prompt to display to the player
    Precondition: prompt is a string
    
    Parameter valid: The valid reponses
    Precondition: valid is a tuple of strings
    """
    # Ask the question for the first time.
    response = input(prompt)
    
    # Continue to ask while the response is not valid.
    while not (response in valid):
        print('Invalid option. Choose one of '+str(valid))
        print()
        response = input(prompt)
    
    return response


def payout(bet,score):
    """
    Returns the winnings for a game of quasar.
    
    Winnings are payout-bet.  So winning your bet (on a score of 17) has a net of 0.
    
    Parameter bet: the number of credits bet
    Precondition: bet is an int > 0
    
    Parameter score: the quasar score
    Precondition: score is an int >= 0
    """
    if score == 20:
        return bet
    elif score == 19:
        return round(0.5*bet)
    elif score == 18:
        return round(0.25*bet)
    elif score == 17:
        return 0
    elif score == 16:
        return round(-0.5*bet)
    elif score == 15:
        return round(-0.75*bet)
    
    # Everything else is a total loss
    return -bet


# Complete these functions
def get_bet(credits):
    """
    Returns the number of credits bet by the user.
    
    This function asks the user to make a bet
        
        Make a bet: 
    
    If bet is not an integer, it responds with the error message
        
        The bet must be a integer.
    
    If bet is 0 or less, it responds with the error message
        
        The bet must be a integer.
    
    Finally, if bet is more than credits, it responds with the error message
        
        You do not have enough credits for that bet.
    
    It continues to ask for a bet until the user gives a valid answer.
    
    Parameter credits: the number of credits available to bet
    Precondition: credits is an int > 0
    """
    #print(credits, type(credits))
    invalid_bet = True
     
    
    while invalid_bet:
        bet = input('Make a bet: ')

        try:
            bet = int(bet)
            if bet <=0:
                print('The bet must be positive.')
            elif bet > credits:
                print('You do not have enough credits for that bet.')
            else:
                invalid_bet = False
                return int(bet) 
        except:
            print('The bet must be a integer.')
        

def session(bet):
    """
    Returns the payout after playing a single session of quasar.
    
    The game starts by randomly choosing a number 1-8 and then displaying
        
        Your score is X.
    
    (where X is the number chosen). It then prompts the user with the following options:
        
        Choose (a) 4-7, (b) 1-8, or (s)top: 
    
    If the user chooses 'a' or 'b', it picks a random number, adds it to the score, 
    and then displays the score again.  If the user chooses 's' OR the new score is 
    20 or more, the session is over.
    
    Once the session ends, if the user goes over 20, the function prints out
        
        You busted.
    
    However, if the user hits 20 exactly, the function prints out
        
        Quasar!
    
    Nothing extra is printed if the user is below 20.
    
    It then prints out
        
        You won X credits.
    
    or
        You lost X credits.
    
    as appropriate, where X is the payout (if X is 0, this is considered a win). When 
    the session is done, the function returns the payout.
    
    Parameter bet: the number of credits bet
    Precondition: bet is an int > 0
    """
           
    score = random.randint(1,8)
    print ('Your score is ', score, '.' , sep = '')
    options = prompt('Choose (a) 4-7, (b) 1-8, or (s)top: ','abs')
    while score < 20 and options != 's':
        if options == 'a':
            score = score + random.randint(4,7)
        else:
            score = score + random.randint(1,8)
        print ('Your score is ', score, '.' , sep = '')
        if score < 20:            
            options = prompt('Choose (a) 4-7, (b) 1-8, or (s)top: ','abs')
    if score > 20:
        print ('You busted.')
    elif score == 20:
        print ('Quasar!')
    pay = payout(bet,score)
    if pay >= 0:
        print ('You won', pay, 'credits.')
    else:
        print ('You lost', -pay, 'credits.')
    return pay      
    

def play(credits):
    """
    Plays Quasar until the player quits or is broke.
    
    The game starts by announcing
        
        You have X credits.
        
    where X is the number of credits.  It gets a bet from the user and plays a session
    of Quasar.  When done, it adds the payout to the score and repeats the message above.
    
    If the user reaches 0 credits, the game is over.  Otherwise, it asks
        
        Do you want to (c)ontinue or (p)ayout? 
    
    If the user chooses 'c', the process repeats (get a bet, play a session, etc.)
    
    When done, the game prints
        
        You leave with X credits.
    
    assuming X > 0. However, if X is 0 it instead prints
        
        You went broke.
    
    Parameter credits: the number of credits available to bet
    Precondition: credits is an int > 0
    """
    print ('You have',credits,'credits.')
    options = 'c'
    while options == 'c' and credits > 0:
        bet = get_bet (credits)
        credits = credits + session(bet)
        print ('You have',credits,'credits.')
        if credits >0:
            options = prompt('Do you want to (c)ontinue or (p)ayout? ', 'cp')
    if credits > 0:
        print ('You leave with', credits, 'credits.')
    else:
        print ('You went broke.')


# Script Code
# DO NOT MODIFY BELOW THIS LINE
if __name__ == '__main__':
    play(1000)