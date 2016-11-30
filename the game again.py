import random

print "What is your name?"
name = raw_input(">>> ")

print "Hello %s." %name

print "Are you ready for the game?"

print '''
Start by typing "Story".
type "Help" for help.
 '''
#For normal digging mode.
normal_loot_list = ['Your dog found some silver.',
'Your dog found an ants house.',
'Your dog did not found anything.',
'The ground is very solid to dig.',
'There was nothing.',
'Your dog found a good loot map.',
'Your dog found a worms house.']

#For good Digging mode.
good_loot_list = ['Your dog found some gold.',
'Your dog found a treasure chestt.',
'Your dog found a best loot map.',
'Your dog found a big rock.']

#For the best Digging mode.
best_loot_list = ['']

#To make the random text.
wNear = ['Your dog found A Goblin.\nThe Goblin stool 10$.\n-10$',
'Nothing happined.\nTry again maybe you find a good thing',
'Your dog found a Blackberry tree.\n+20Food.' ]

wMiddle = ['Your dog found a traidor.\nYou can\'t do anything with him yet.',
'Your dog didn\'t found anything.',
'Your dog found a good loot map.',
'Your dog found a 100$ in a bag on the ground.']

wFar = ['Your dog is tired.',
'Your dog found a best loot map.',
'Your dog found a chest full of money and food.']

story = '''

'''
#for helping visitors to understand the game.
help ='''
.___________________________________.
|Event |ID  |Description            |
|______|____|_______________________|
|Help  |0   |To see available events|
|Walk  |1   |To move the dog.       |
|Dig   |2   |For possible loot.     |
[______[____]_______________________]
'''

def Help():
	print help

def Story():
    print story
 
class dog(object):
    
    Money = 100
    Food = 100
    good_loot = 0
    best_loot = 0
    
    @classmethod
    def info(cls):
        print '\nMoney = ',dog.Money,' Food = ',dog.Food
        if dog.good_loot > 0:
            print "%d Good loot map" %dog.good_loot
        if dog.best_loot > 0:
            print "%d Best loot map" %dog.best_loot
    
    @classmethod
    def walk(cls):
        walked = random.randrange(2,101,1)
        print "Your dog walked %dMetter" %walked
        if dog.Food < 10:
            dog.Food += 10
            dog.Money -= 25
            print "+10Food\n-25$"
                
                
        elif walked < 30:
            dog.Food -= 5
            res = random.choice(wFar)
            print res
            
            if res == wFar[2]:
                mf = random.randrange(50,100,5)
                dog.Money += mf
                dog.Food += mf
                
                print "+%d$" %mf
                print "+%dFood" %mf
            
            elif res == wFar[1]:
                dog.best_loot += 1
        
        
        elif walked < 60:
            dog.Food -= 5
            res = random.choice(wMiddle)
            print res
            
            if res == wMiddle[3]:
                dog.Money += 100
            
            elif res == wMiddle[2]:
            	dog.good_loot += 1
            
        elif walked < 100:
            dog.Food -= 5
            res = random.choice(wNear)
            print res
            
            if res == wNear[0]:
                dog.Money -= 10
            
            elif res == wNear[2]:
                dog.Food += 20
    
    @classmethod
    def dig(cls):
        if dog.Food > 40:
            
            if dog.good_loot > 0:
                dog.Food -= 10
            	print"you used a good loot map."
                dog.good_loot -= 1
                
                res = random.choice(good_loot_list)
                print res
                
                if res == good_loot_list[0]:
                    dog.Money += 50
                    print"+50$"
                    
                elif res == good_loot_list[1]:
                    terasure = random.randrange(30,100)
                    
                    dog.Money += treasure
                    print"+%d$" %treasure
                    
                elif res == good_loot_list[2]:
                    dog.best_loot += 1
                    
            
            elif dog.best_loot > 0:
                dog.Food -= 10
                print "You used a best loot map."
                dog.best_loot -= 1
                
                dog.Money += 100
                dog.Food += 100
                
            else:
                res = random.choice(normal_loot_list)
                print res
          	  
                if res == normal_loot_list[0]:
                    dog.Money += 20
                    print "+20$"
                
                elif res == normal_loot_list[5]:
                    dog.good_loot += 1
                   
        else:
            print "Your dog needs more food."
        
    @classmethod
    def save(cls):
        f = open('MFGB.opp','w')
        f.write(str(dog.Money))
        f.write("\n")
        f.write(str(dog.Food))
        f.write("\n")
        f.write(str(dog.good_loot))
        f.write("\n")
        f.write(str(dog.best_loot))
    @classmethod
    def load(cls):
        with open("MFGB.opp", "r") as ins:
            loots = []
            for line in ins:
                loots.append(line)
                
            dog.Money = int(loots[0])
            dog.Food = int(loots[1])
            dog.good_loot = int(loots[2])
            dog.best_loot = int(loots[3])
    
try:
    dog.load()
except:
	dog.save()


print help

while True:
	
    dog.save()
    dog.info()
    comands = raw_input("\n>>> ")
        
    if comands == "Walk":
        dog.walk()
    elif comands == "Dig":
        dog.dig()
    elif comands == "Help":
        Help()
    elif comands == "Info":
        dog.info()
    elif comands == "Story":
        Story()
    elif comands == "Save":
        dog.save()
    elif comands == "Load":
        try:
            dog.load()
        except:
            print "Can't load the file."
    else:
        print "There's no use for %s" %comands