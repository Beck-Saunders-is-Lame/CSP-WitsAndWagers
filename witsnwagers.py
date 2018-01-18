import Tkinter
import tkFont
#os module allows access to the operating system
#path allows us to manipulate paths
#see http://docs.python.org/2/library/os.html
import os.path
import pickle

#from Tkinter, import Canvas, which allows us to draw on the GUI
#also import the NW and PhotoImage class,allows up to add images to the canvas 
from Tkinter import Canvas, NW,PhotoImage

#import team data
import team1
import team2
import team3
import team4
import team5
import team6
import team7

# ******* Remember to restart kernel to update memory after syncing *******
#---------------------- GAME PLAY INPUTS ----------------------------------
# game state values: 's', start-game; 'a', after teams answer; 'b', after teams bet
game_state = 's'
# answer/bet marker position 1 - 8
answer = 0
# increment each time team place bets, when game_state = 'b'
play_round = 0
# each time bets are placed, update all three inputs
#-------------------------------------------------------------------------

# Create root window 

root = Tkinter.Tk()
root.title('Wits & Wagers')
root.configure(bg='#FFFFFF')
root.resizable(0,0)

#get the directory of the file.
dir_path = os.path.dirname(os.path.abspath(__file__)) 

# Create and place a canvas
canvas = Canvas(root, width=800, height=600)
canvas.grid()
canvas.focus_set()

file_path = os.path.join(dir_path, 'wagerboard.gif')
#get a handle to the file we imported 
wagerboard =  PhotoImage(file=file_path)
#add the handle to an image which we can see and manipulate
#this is a container for our image, we also set the x,y position
wagerBoard  = canvas.create_image(0, 0, anchor=NW, image=wagerboard)  

helv16 = tkFont.Font(family='Verdana',size=16)
helv14 = tkFont.Font(family='Verdana',size=14)
        
team1_score = canvas.create_text(120,40,text="$10", anchor=NW,font=helv16)
team2_score = canvas.create_text(220,40,text="$10", anchor=NW,font=helv16)
team3_score = canvas.create_text(318,40,text="$10", anchor=NW,font=helv16)
team4_score = canvas.create_text(418,40,text="$10", anchor=NW,font=helv16)
team5_score = canvas.create_text(514,40,text="$10", anchor=NW,font=helv16)
team6_score = canvas.create_text(612,40,text="$10", anchor=NW,font=helv16)
team7_score = canvas.create_text(712,40,text="$10", anchor=NW,font=helv16)

team1 = team1.Team1()
team2 = team2.Team2()
team3 = team3.Team3()
team4 = team4.Team4()
team5 = team5.Team5()
team6 = team6.Team6()
team7 = team7.Team7()

scorelist = os.path.join(dir_path, 'scorelist')
scorefile = open(scorelist,'r') # open for writing    
score_list = pickle.load(scorefile)
scorefile.close()

def checkAnswer(team):
    if not(str(team.answer_question_amt).isdigit()) or team.answer_question_amt < 0:
        return 0
    else:
        return team.answer_question_amt    

def checkBet(team,nbr):
    if not(str(team.bet_position).isdigit()) or not(str(team.bet_amount).isdigit()):
        return (1,0)
    if team.bet_position not in (1,2,3,4,5,6,7,8):
        return (1,0) 
    if team.bet_amount > score_list[nbr-1]:
        return (team.bet_position,score_list[nbr-1])
        
    return (team.bet_position,int(team.bet_amount))        

if game_state == 'a':               
    t1_answer = checkAnswer(team1)
    t2_answer = checkAnswer(team2)
    t3_answer = checkAnswer(team3)
    t4_answer = checkAnswer(team4)
    t5_answer = checkAnswer(team5)
    t6_answer = checkAnswer(team6)
    t7_answer = checkAnswer(team7)
    team_answers = [t1_answer,t2_answer,t3_answer,t4_answer,t5_answer,t6_answer,t7_answer]
    
if game_state == 'b':
    t1_bet_pos,t1_bet_amt = checkBet(team1,1)    
    t2_bet_pos,t2_bet_amt = checkBet(team2,2)
    t3_bet_pos,t3_bet_amt = checkBet(team3,3)
    t4_bet_pos,t4_bet_amt = checkBet(team4,4)
    t5_bet_pos,t5_bet_amt = checkBet(team5,5)
    t6_bet_pos,t6_bet_amt = checkBet(team6,6)
    t7_bet_pos,t7_bet_amt = checkBet(team7,7)

    t1_pos = 14 + (t1_bet_pos-1)*100
    t2_pos = 14 + (t2_bet_pos-1)*100
    t3_pos = 14 + (t3_bet_pos-1)*100
    t4_pos = 14 + (t4_bet_pos-1)*100
    t5_pos = 14 + (t5_bet_pos-1)*100
    t6_pos = 14 + (t6_bet_pos-1)*100
    t7_pos = 14 + (t7_bet_pos-1)*100

    team_wager_pos = [t1_pos,t2_pos,t3_pos,t4_pos,t5_pos,t6_pos,t7_pos]
    team_wager_amt = [t1_bet_amt,t2_bet_amt,t3_bet_amt,t4_bet_amt,t5_bet_amt,t6_bet_amt,t7_bet_amt]

def startGame():
    
    score_list = [10,10,10,10,10,10,10]
    scorelist = os.path.join(dir_path, 'scorelist')
    scorefile = open(scorelist,'w') # open for writing    
    pickle.dump(score_list,scorefile) # use pickle to copy list image
    scorefile.close() # close the file as we are done with it  
  
    play_round = [0]
    playround = os.path.join(dir_path, 'playround')
    playfile = open(playround,'w')   
    pickle.dump(play_round,playfile) 
    playfile.close() 
     

def showAnswer(x1,y1,color,answer):
    canvas.create_rectangle(x1,y1,x1+70,y1+40,fill=color,outline='#FFFFFF',width=2)  
    canvas.create_text(x1+20,y1+10,text=answer, anchor=NW,font=helv14)

def showWager(x1,y1,color,wager):
    canvas.create_oval(x1,y1,x1+65,y1+65,fill=color,outline='#FFFFFF',width=2)
    canvas.create_text(x1+17,y1+20,text='$'+str(wager), anchor=NW,font=helv14)

def doAnswer(team_list,team_answers):
    
    #sort answers from low to high
    sorted = True
    while sorted == True:
        sorted = False
        for i in range(6):
            temp1 = team_list[i]
            temp2 = team_answers[i]
            if team_answers[i+1] < team_answers[i]:
                team_answers[i] = team_answers[i+1]
                team_list[i] = team_list[i+1]
                team_answers[i+1] = temp2
                team_list[i+1] = temp1
                sorted = True
        


    team_colors =  ['#FF6A6A','#66CCCC','#66FF99','#FFCC66','#CC99FF','#CCFF33','#33FFFF']
    ans_xpos =  [110,210,310,410,510,610,710]
    ANS_YPOS =  170

    #save lists to use when bets are placed.
    teamlist = os.path.join(dir_path, 'teamlist')
    teamfile = open(teamlist,'w')     
    pickle.dump(team_list,teamfile) 
    teamfile.close()  

    answerlist = os.path.join(dir_path, 'answerlist')
    answerfile = open(answerlist,'w')   
    pickle.dump(team_answers,answerfile) 
    answerfile.close()

    answer_set = set(team_answers)

    if len(answer_set) == 7:
        for j in range(7):
            showAnswer(ans_xpos[j],ANS_YPOS,team_colors[team_list[j]-1],team_answers[j])
        
    if len(answer_set) == 6:
        ans_xpos.pop(3)
        i = 0 
        j = 0        
        while i < 6:
            k = 0
            showAnswer(ans_xpos[i],ANS_YPOS,team_colors[team_list[j]-1],team_answers[j])
            if j == 6:
                break 
            while team_answers[j+1] == team_answers[j]:
                j+=1
                k+=1
                showAnswer(ans_xpos[i],ANS_YPOS+50*k,team_colors[team_list[j]-1],team_answers[j]) 
                if j == 6:
                    break   
            i+=1
            j+=1
         
    if len(answer_set) == 5:
        ans_xpos.pop(0)
        ans_xpos.pop(5)
        i = 0 
        j = 0        
        while i < 5:
            k = 0
            showAnswer(ans_xpos[i],ANS_YPOS,team_colors[team_list[j]-1],team_answers[j]) 
            if j == 6:
                break 
            while team_answers[j+1] == team_answers[j]:
                j+=1
                k+=1
                showAnswer(ans_xpos[i],ANS_YPOS+50*k,team_colors[team_list[j]-1],team_answers[j]) 
                if j == 6:
                    break    
            i+=1
            j+=1
            
    if len(answer_set) == 4:
        ans_xpos.pop(0)
        ans_xpos.pop(2)
        ans_xpos.pop(4)            
        i = 0 
        j = 0        
        while i < 4:
            k = 0  
            showAnswer(ans_xpos[i],ANS_YPOS,team_colors[team_list[j]-1],team_answers[j]) 
            if j == 6:
                    break  
            while team_answers[j+1] == team_answers[j]:
                j+=1
                k+=1
                showAnswer(ans_xpos[i],ANS_YPOS+50*k,team_colors[team_list[j]-1],team_answers[j]) 
                if j == 6:
                    break 
                      
            i+=1
            j+=1
                        
    if len(answer_set) == 3:
        ans_xpos.pop(0)
        ans_xpos.pop(0)
        ans_xpos.pop(3)
        ans_xpos.pop(3)               
        i = 0 
        j = 0        
        while i < 3:
            k = 0
            showAnswer(ans_xpos[i],ANS_YPOS,team_colors[team_list[j]-1],team_answers[j])
            if j == 6:
                break   
            while team_answers[j+1] == team_answers[j]:
                j+=1
                k+=1
                showAnswer(ans_xpos[i],ANS_YPOS+50*k,team_colors[team_list[j]-1],team_answers[j]) 
                if j == 6:
                    break   
            i+=1
            j+=1


    if len(answer_set) == 2:
        ans_xpos.pop(0)
        ans_xpos.pop(0)
        ans_xpos.pop(1)
        ans_xpos.pop(2) 
        ans_xpos.pop(2)              
        i = 0 
        j = 0        
        while i < 2:
            k = 0
            showAnswer(ans_xpos[i],ANS_YPOS,team_colors[team_list[j]-1],team_answers[j])
            if j == 6:
                break 
            while team_answers[j+1] == team_answers[j]:
                j+=1
                k+=1
                showAnswer(ans_xpos[i],ANS_YPOS+50*k,team_colors[team_list[j]-1],team_answers[j]) 
                if j == 6:
                    break      
            i+=1
            j+=1

    if len(answer_set) == 1:            
        showAnswer(410,ANS_YPOS,team_colors[team_list[0]-1],team_answers[0]) 
        showAnswer(410,ANS_YPOS+50,team_colors[team_list[1]-1],team_answers[1])  
        showAnswer(410,ANS_YPOS+100,team_colors[team_list[2]-1],team_answers[2]) 
        showAnswer(410,ANS_YPOS+150,team_colors[team_list[3]-1],team_answers[3])  
        showAnswer(410,ANS_YPOS+200,team_colors[team_list[4]-1],team_answers[4]) 
        showAnswer(410,ANS_YPOS+250,team_colors[team_list[5]-1],team_answers[5])  
        showAnswer(410,ANS_YPOS+300,team_colors[team_list[6]-1],team_answers[6])   
        
    scorelist = os.path.join(dir_path, 'scorelist')
    scorefile = open(scorelist,'r')  
    score_list = pickle.load(scorefile)
    scorefile.close()
    
    #show team scores
    canvas.itemconfigure(team1_score,text="$"+str(score_list[0]))                                              
    canvas.itemconfigure(team2_score,text="$"+str(score_list[1]))
    canvas.itemconfigure(team3_score,text="$"+str(score_list[2]))                                              
    canvas.itemconfigure(team4_score,text="$"+str(score_list[3]))  
    canvas.itemconfigure(team5_score,text="$"+str(score_list[4]))                                              
    canvas.itemconfigure(team6_score,text="$"+str(score_list[5]))
    canvas.itemconfigure(team7_score,text="$"+str(score_list[6]))                                              
                                                                                                                                           

def doBet(team_wager_pos,team_wager_amt):
     
    scorelist = os.path.join(dir_path, 'scorelist')
    scorefile = open(scorelist,'r')   
    score_list = pickle.load(scorefile)
    unsorted_score_list = score_list     
    scorefile.close() 
    
    team_list = [1,2,3,4,5,6,7]
   
    sorted = True
    while sorted == True:
        sorted = False
        for i in range(6):
            temp1 = team_list[i]
            temp2 = team_wager_pos[i]
            temp3 = team_wager_amt[i]
            temp4 = score_list[i]
            if team_wager_pos[i+1] < team_wager_pos[i]:
                team_wager_pos[i] = team_wager_pos[i+1]
                team_list[i] = team_list[i+1]
                team_wager_amt[i] = team_wager_amt[i+1]
                score_list[i] = score_list[i+1]
                team_wager_pos[i+1] = temp2
                team_list[i+1] = temp1
                team_wager_amt[i+1] = temp3
                score_list[i+1] = temp4
                sorted = True
        
    team_colors =  ['#FF6A6A','#66CCCC','#66FF99','#FFCC66','#CC99FF','#CCFF33','#33FFFF']
    
    factor = 0 
 
    global answer
    
    pos = 14 + (answer-1)*100   
    
    if answer == 1:
        factor = 6
    if answer == 2 or answer == 8:
        factor = 5
    if answer == 3 or answer == 7:
        factor = 4     
    if answer == 4 or answer == 6:
        factor = 3       
    if answer == 5:
        factor = 2 
    
    y_pos = 170
     
    for j in range(7):
       
        showWager(team_wager_pos[j],y_pos,team_colors[team_list[j]-1],team_wager_amt[j])
        if team_wager_pos[j] == pos:
            score = score_list[j] + team_wager_amt[j]*factor
        else:
            score = score_list[j] - team_wager_amt[j]
            
        if score < 1:
            score = 1
           
        if team_list[j] == 1:
            unsorted_score_list[0] = score
        if team_list[j] == 2:
            unsorted_score_list[1] = score
        if team_list[j] == 3:
            unsorted_score_list[2] = score
        if team_list[j] == 4: 
            unsorted_score_list[3] = score 
        if team_list[j] == 5:
            unsorted_score_list[4] = score
        if team_list[j] == 6: 
            unsorted_score_list[5] = score 
        if team_list[j] == 7:
            unsorted_score_list[6] = score
                
        if j != 6:
            if team_wager_pos[j+1] == team_wager_pos[j]:
                y_pos += 50
            else:
                y_pos = 170    
                
    # used to position the answer marker
    if answer == 1:
            x = 9
    else:
        x = 4 + (answer-1)*100
        
    y = 135   
        
    canvas.create_rectangle(x,y,x+80,y+400,fill="white",outline='white',stipple='gray25')   
    
    playround = os.path.join(dir_path, 'playround')
    playfile = open(playround,'r')  
    play_list = pickle.load(playfile)
    last_round = play_list[0]
    playfile.close()
    
    global play_round
    
    if last_round >= play_round:
       return
    else:
        play_list[0] = play_round
        playround = os.path.join(dir_path, 'playround')
        playfile = open(playround,'w') 
        pickle.dump(play_list,playfile)
        playfile.close()  
         
                                
    canvas.itemconfigure(team1_score,text="$"+str(unsorted_score_list[0]))
    canvas.itemconfigure(team2_score,text="$"+str(unsorted_score_list[1]))  
    canvas.itemconfigure(team3_score,text="$"+str(unsorted_score_list[2]))  
    canvas.itemconfigure(team4_score,text="$"+str(unsorted_score_list[3]))  
    canvas.itemconfigure(team5_score,text="$"+str(unsorted_score_list[4]))  
    canvas.itemconfigure(team6_score,text="$"+str(unsorted_score_list[5]))  
    canvas.itemconfigure(team7_score,text="$"+str(unsorted_score_list[6]))  
                                                                                                                                                 
    scorelist = os.path.join(dir_path, 'scorelist')
    scorefile = open(scorelist,'w')    
    pickle.dump(unsorted_score_list,scorefile) 
    scorefile.close()
     

if game_state == 's':
    startGame()    

if game_state == 'a':
    team_list = [1,2,3,4,5,6,7]
    doAnswer(team_list,team_answers)    

if game_state == 'b':    
    #use previous information in case some team tries to change their answer
    teamlist = os.path.join(dir_path, 'teamlist')
    teamfile = open(teamlist,'r')   
    team_list = pickle.load(teamfile)  
    teamfile.close() 
    
    answerlist = os.path.join(dir_path, 'answerlist')
    answerfile = open(answerlist,'r')  
    team_answers = pickle.load(answerfile)  
    answerfile.close() 

    doAnswer(team_list,team_answers)    
    doBet(team_wager_pos,team_wager_amt)                                                                                                                                                                                                                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
root.mainloop()