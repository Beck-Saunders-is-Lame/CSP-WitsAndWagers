#Common base class for all teams, the blueprint for creating child objects
class Team2:
    

   #This is the constructor for the class. It helps to allocate, instantiate,
   #each child in memory, and initializes the data members of the child object,
 
   def __init__(self):
    
      #update this variable in responding to questions   
      self.answer_question_amt = 1503
      
      #update these variables in placing your bet
      self.bet_position = 1
      self.bet_amount = 10
