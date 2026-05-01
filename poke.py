import random as r
import time
import subprocess, atexit


pokemon_types=["Normal" , "Fire" , "Water" ,  "Electric" , "Grass" , "Ice" , "Fighting" , "Poison" , "Ground" , "Flying" ,
       "Psychic" , "Bug" , "Rock" , "Ghost" , "Dragon" , "Dark" , "Steel" , "Fairy"]
pokemon_list=["Rattata" , "Charmander" , "Squirtle" , "Pikachu" , "Bulbasaur" , "Snover" , "Hitmonlee" , "Muk" , "Dugtrio" , 
             "Pidgey" , "Psyduck" , "Butterfree" , "Geodude" , "Gastly" , "Sableye" , "Gibble" , "Aron" , "Clefairy"]                           
pokemon_moves = ["Tackle" , "Ember" , "Bubble" , "Thunder Shock" ,"Vine Whip" , "Icy Wind" , "Rolling Kick" , "Toxin" ,
         "Earthquake" , "Aerial Ace" , "Psybeam" ,"Bug Bite" , "Rock Smash" , "Shadow Claw" ,"Night Slash" , "Dragon Claw" ,
         "Metal Claw" , "Fairy Wind"]   #Changable
pokeballs = {"1":"Regular","2":"Great","3":"Ultra"}
w1=w2=d1=d2=0
max_hp = r.randrange(100,200,10)
max_hp1 = max_hp
t = lose = Wrongchoice = caughtvalue = 0 #Not Changable
movepp = [5,5,5,5]
pm3=[(" >"+posmoves[i-1]+"("+str(i)+")(PP "+str(movepp[i-1])+")\n") for i in range(1,5)]

class Pokemon:
    def __init__(self, type_index):
        self.name=pokemon_list[type]
        self.type_name=pokemon_types[type_index]
        self.HP=max_hp
        self.type_index=type_index
    def change_hp(self, d):
        self.HP+=d
    def display_hp(self):
        print(f"{self.name} has {self.HP} HP")

def check():
    global d1
    global d2
    global w1
    global w2
    w=[(4,1),(5,1),(11,1),(16,1),(1,2),(8,2),(12,2),(2,3),(9,3),(2,4),(8,4),(12,4),(4,5),(8,5),(9,5),(14,5),(0,6),(5,6),
       (12,6),(15,6),(16,6),(4,7),(17,7),(1,8),(3,8),(7,8),(12,8),(16,8),(4,9),(6,9),(11,9),(6,10),(7,10),(4,11),(10,11),
       (15,11),(1,12),(5,12),(9,12),(11,12),(10,13),(13,13),(14,14),(10,15),(13,15),(5,16),(12,16),(17,16),(6,17),(14,17),
       (15,17)]
    if (Pokemon1.type_index,Pokemon2.type_index) in w:
        d2=2*d2
        w1=1
    if (Pokemon2.type_index,Pokemon1.type_index) in w:
        d1=2*d1
        w2=1

Pokemon1=Pokemon(r.randint(0,17))
Pokemon2=Pokemon(r.randint(0,17))
pokemove2=pokemon_moves[Pokemon2.type_index]
posmoves=[(Pokemon1.type_name + i) for i in [" Spin"," Punch"," Bite"," Slam"]] #Changable

if Pokemon1.type_name==Pokemon2.type_name: 
    Pokemon1.name+=" 1"
    Pokemon2.name+=" 2" #Not Changable

print("Your Pokemon is",Pokemon1.name)
print ("You have encountered",Pokemon2.name)

def pokecapture():
    global caughtvalue
    print("You caught ",Pokemon2.name,"!!")
    caughtvalue=1
def movnumwrite(n):
    with open('movnumwrite.txt','w') as f:
        f.write(str(n))
        f.close()
def inpchange(n):
    with open('input.txt','w') as f:
        f.write(n)
        f.close()
def reset_tracker():
    with open('tracker.txt', 'w') as f:
        f.write('1')

def input_setup(moves, input_str):
       movnumwrite(moves)
       inpchange('InputAwaited')
       reset_tracker()
       out=input(input_str)
       "What would you like to do?(Scroll with Alt+A)\n >Attack(1)\n >Bag(2) \n >PokeBall(3) \n >Run(4) \n "
       inpchange('Input Recieved')
       return out
AHK = r"C:\Program Files\AutoHotkey\v2\AutoHotkey64.exe"
ahk_processes = []
def stop_ahk():
    for p in ahk_processes:
        p.terminate()
atexit.register(stop_ahk)
ahk_processes.append(subprocess.Popen([AHK, r".\sendone.ahk"]))
ahk_processes.append(subprocess.Popen([AHK, r".\scroll.ahk"]))

                     
while t<20 and Pokemon2.HP>0 or t<10 and Pokemon1.HP>0:
    Wrongchoice=0
    Pokemon1.display_HP()
    Pokemon2.display_HP()
    time.sleep(2)
    if Pokemon2.HP>0:
        event = input_setup(4, "What would you like to do?(Scroll with Alt+A)\n >Attack(1)\n >Bag(2) \n >PokeBall(3) \n >Run(4) \n ")
        if event=="1":
            pm3=[(" >"+posmoves[i]+"("+str(i+1)+")(PP "+str(movepp[i])+")\n") for i in range(0,4)]
            move = int(input_setup(4, "Which move would you like to use? \n" + pm3[0]+pm3[1]+pm3[2]+pm3[3]))
            move2=movepp[move-1]
            if move<5:
                if move2>0:
                    print("You used",posmoves[move-1])
                    movepp[move-1]=move2-1
                    time.sleep(1)
                else:
                    print("You don't have enough PP for that move")
                    Wrongchoice=1
            else:
                Wrongchoice=1  
            if Wrongchoice!=1: 
                d1=10+(5*move)
                check()
                print ("It did",d1,"damage")
                if w2==1:
                    print("Its super effective!!")
                if Pokemon2.HP>=d1:
                    Pokemon2.change_hp(-d1)
                else:
                    Pokemon2.HP=0
                hpdisplay(2)
        elif event=="2":
            item = input_setup(2, ("Which item would you like to use? \n >Potion(1) \n >Full Restore(2) \n ")
            if item=="1":
                if Pokemon1.HP<max_hp-10:
                    Pokemon1.change_hp(10)
                    print("The Potion healed 10 HP")
                    Pokemon1.display_HP()
                elif Pokemon1.HP==max_hp:
                    print ("This item cannot be used")
                else:
                    Pokemon1.HP=max_hp
                    print("The Potion healed ",max_hp-Pokemon1.HP, " HP")
                    Pokemon1.display_HP()
            elif item=="2": 
                Pokemon1.HP=max_hp
                print("The Full Restore healed ",Pokemon1.name," to full HP")
                Pokemon1.display_HP()
            else:
                Wrongchoice=1
        elif event=="3":
            pokeball = input_setup(3, "Which pokeball would you like to use? \n >Regular(1) \n >Great(2) \n >Ultra(3) \n ")
            pb=pokeballs[pokeball]
            print("You threw a",pb,"Ball")
            pokeballs2=list(pokeballs)
            if pokeball in pokeballs:
                if Pokemon2.HP<(pokeballs2.index(pokeball)*20+20):
                    pokecapture()
                    break
                else:
                    print(Pokemon2.name +" Escaped!!")
            else:
                Wrongchoice=1
        elif event=="4":
            lose=1
            print("You ran away!!")
            break
        else: 
            Wrongchoice=1
        if Pokemon2.HP!=0:
            if event!="4": 
                if caughtvalue==0:
                    if Wrongchoice!=1:
                        time.sleep(1)
                        print(Pokemon2.name,"used ",pokemove2)
                        d2=20
                        check()
                        Pokemon1.change_hp(-d2)
                        print("It did",d2,"HP")
                        if w1==1:
                            print("Its super effective!!")
                        hpdisplay(1)
                        print('\n\n')
                        if Pokemon1.HP==0:
                            lose=1
                            break
                        else:
                            t=t+1
                    else:
                        t=t+1
                else:
                    break
            else:
                break
        else:
            break
if lose==1:
    print("You lose!!")
else:
    print ("You win!!")
