# This is a program to create a model-based agent
import random

#Create the environment
class environment (object):
    #initializing an instance of this class using a constructor
    def __init__ (self):
        self.location = ['A', 'B'];
        self.locationCondition = {'A': 0, 'B':0};
        self.locationCondition['A'] = random.randint(0,1);
        self.locationCondition['B'] = random.randint(0,1);
        self.vacuumLocation = random.choice(self.location);
        self.mode = ['T', 'L'];
        #Assume that past record is that both A and B had been T cleaned
        self.cleaningMethod = {'A' : 'T', 'B' :  'T'};
        #randomly generate current/starting cleaning state
        self.cleaningMethod['A'] = random.choice(self.mode);
        self.cleaningMethod ['B'] = random.choice(self.mode);


#Create the agent
class agent (environment) :
    def __init__ (self, environment):
        #randomly generate the status
        print('Vacuum location is ', environment.vacuumLocation, 'The location\'s condition is,', environment.locationCondition, 'The cleaning methodd for the location is currently ',environment.cleaningMethod)

        count = 0
        while count < 2:

            #perform actions based on conditions
            if environment.locationCondition[environment.vacuumLocation] == 1:
                print(environment.vacuumLocation, 'This location is dirty')
                #check status, suck, mark clean, record status
                if environment.cleaningMethod[environment.vacuumLocation] == 'T':
                    environment.cleaningMethod[environment.vacuumLocation] = 'L'
                else:
                    environment.cleaningMethod[environment.vacuumLocation] = 'T'
                environment.locationCondition[environment.vacuumLocation] = 0
                print(environment.vacuumLocation,' This location has been cleaned')
            else:
                print(environment.vacuumLocation, ' This location is already clean')

            newIndex = environment.location.index(environment.vacuumLocation) + 1
            if newIndex == 2:
                newIndex = 0
            environment.vacuumLocation = environment.location[newIndex]

            count = count+1

        print('New vacuum location is ',environment.vacuumLocation)
        print('new location conditions are ',environment.locationCondition)
        print('current cleaning method is ',environment.cleaningMethod)

el = environment()
al = agent(el)




# {} () : _