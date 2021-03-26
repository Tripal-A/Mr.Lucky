import time

answer_A=['A','a']
answer_B=['B','b']
answer_C=['C','c']
yes=['Y','y','yes','Yes']
no=['N','n','no','No']

y=200000 #starting yen
reward=200000
y += reward #reward through option_rival , optional_business_card and option_kitten


y1=200000 #starting yen
thief_reward=250000
y1 += thief_reward #reward through option_kittyen


sack = 0
business_card = 0

required = ('\nUse only A,B, or C\n')
required_two= ('\nUse only Y,y,Yes or yes\n')
required_three= ('\nUse only A or B\n')

def intro():
    print('After winning the mega million yen lottery, you choose the monthly allowance option and have started '
          'receiving a monthly allowance of 200,000 yen for the rest of your life! Being unemployed prior, this is a game changer. '
          'You managed to get a deal on an apartment which costs 150,000 yen a month in Tokyo with the stipulation that you will'
          'get a job to sustain yourself and not rely on the government checks. Coming home one day after interviewing at a wireless  '
          'company, you get off the wrong train station and find yourself in Yakuza territory. You turn the corner and a shady individual'
          'in a trench coat steps out and  approaches you. "I have a job that needs to be done" he states. You will:' )
    time.sleep(1)
    print('\nA.Decide to listen to him\n'
          'B.Tell him you are not interested\n'
          'C.Get scared and run away')
    choice=input('>>>')
    if choice in answer_A:
        option_listen()
    elif choice in answer_B:
        print('\nThe stranger feels disrespected and whistles loudly. A limo pulls up and you are kidnapped and never seen again\n\nGAME OVER')
    elif choice in answer_C:
        print('\nYou turn a couple more wrong corners and are mugged and killed\n\nGAME OVER')
    else:
        print(required)
        intro() #reruns the program if required is printed


def option_listen():
    print('The shady individual tells you he is looking for something he cannot live without. He will not tell you what this is '
          'but informs you that if found, there will be a great reward entailed. Will you:')
    time.sleep(2)
    print('\nA.Inform him that you have no time for puzzles\n'
          'B.Agree to help him but lie and find your way home\n'
          'C.Agree to help him and ask for a clue')
    choice=input('>>>')
    if choice in answer_A:
        print('\nThe stranger feels disrespected and whistles loudly. A limo pulls up and you are kidnapped and never seen again\n\nGAME OVER')
    elif choice in answer_B:
        print('\nYoure really not fun at all\n\nGAME OVER')
    elif choice in answer_C:
        option_agree()
    else:
        print(required)
        option_listen()




def option_agree():
    print('You agree to help because you can tell the individual is really heart broken, you ask for a clue.\n'
          'the shady individual informs you that the last time he saw his "precious" was this morning.'
          'He came home this morning and noticed his apartment was robbed and his precious was stolen. He thinks his arch'
          'rival who lives two train stations down has his belongings. He gives you description of his rival. Will you:')
    time.sleep(2)
    print('\nA.Take the train down to the shady individuals rivals station\n'
          'B.Take the station only one stop down, remaining in Yakuza territory\n'
          'C.Tell the individual this sounds dangerous and decline')
    choice=input('>>>')
    if choice in answer_A:
        option_rival()
    elif choice in answer_B:
        option_wrong_station()
    elif choice in answer_C:
        print('The individual is frustrated that he has waisted his time with you, he stabs you in the side and you bleed out\n\nGAMEOVER')
    else:
        print(required)
        option_agree()

def option_rival():
    print('Once you arrive at the rivals train station you decide to go to the Circle K to ask around for anyone who matches the rivals'
          'description. You get lucky and notice the rival checking out. You decide to follow the rival back to his place. During the walk'
          'the rival makes a phone call where he invites friends over to his place to "celebrate". The rival mentions he will leave the door'
          'unlocked. When the rival gets home and goes inside, you wait a couple minutes and enter his apartment. The rival is using the bathroom'
          'and yells out, "Ichiro! You got here quick!". At the same time you notice a sack of items that look freshly stolen. '
          'Do you grab the sack? Y/N')
    choice=input('>>>')
    if choice in yes:
        sack=1
    elif choice in no:
        sack=0
    else:
        print(required_two)
        option_rival()
    print('\nWhat next?:')
    time.sleep(1)
    print('\nA.Hide\n'
          'B.Will yourself to death\n'
          'C.Run out the house')
    choice=input('>>>')
    if choice in answer_A:
        if sack > 0:
            option_hide()
        else:
            print('You find yourself hiding in a closet and admiring the clothes the rival owns\n\nGAME OVER')
    elif choice in answer_B:
        print('Impressive!!...\n\nGAME OVER')
    elif choice in answer_C:
        if sack > 0:
            print('You sprint out the apartment with the sack in your arms, make it all the way to the shady individual and show him the sack.'
                  'He frantically empties out the sack, ignoring everything until a small kitten falls out of the sack. He is thrilled. He '
                  'awards you with 200,000 yen!')
            print('\nCurrent Yen:',y)

    else:
        print('You just ran out of the house empty handed and now the rival is onto you.\n\nGAME OVER')





def option_hide():
    print('You take the sack and hide in a small closet. After some time you notice movement from inside the sack. You look inside and see '
          'jewlery, electronics, yen, and a kitten. You decide to:')
    time.sleep(1)
    print('\nA.Try on some of the Rivals clothes, he looks fashionable\n'
          'B.Take the kitten\n'
          'C.Take the kitten and pocket some yen')
    choice=input('>>>')
    if choice in answer_A:
        print('The rival hears something in his closet and catches you trying on his clothes, the penalty for being a weirdo in Japan is death'
              '\n\n GAME OVER')
    elif choice in answer_B:
        option_kitten()
    elif choice in answer_C:
        option_kittyen()
    else:
        print(required)
        option_hide()

def option_kitten():
    print('With the kitten in your arms you peak out the closet doors and notice a small window with a fire escape. Go down the fire escape?'
          'Y/N')
    time.sleep(1)
    choice=input('>>>')
    if choice in yes:
        print('You barely make it out without alerting the rival and make it back to the shady individual, he tells you that all the other'
              'items were replacable but his kitten was not. He rewards you with 200,000 yen!')
        print('\nCurrent Yen:',y)
    if choice in no:
        print('You hesitate and the rival finds you\n\nGAME OVER')
    else:
        print(required)
        option_kitten()

def option_kittyen():
    print('You pocket 50,000 yen and bundle the kitten into your arms. You notice a fire escape in the room. You decide to:')
    time.sleep(1)
    print('\nA. Go down the fire escape\n'
          'B. You would REALLY look good in his clothes, try them on')
    choice=input('>>>')
    if choice in answer_A:
        print('You make it out alive from the Rivals home, you make it back to the shady individual and he states that all the items inside'
              'the sack could be replaced but the kitten was irreplaceable. He rewards you with 200,000 yen!')
        print('Current Yen:',y1)
    elif choice in answer_B:
        print('The rival walks in on you changing and notices how good you look in his clothing. This upsets him greatly....\n\nGAME OVER')
    else:
        print(required_three)
        option_kittyen()




def option_wrong_station():
    print('You take the train down 1 station and remain in Yakuza territory, another strange individual approaches you and tells you'
          'his faction of the Yakuza is in need of new recruits and are looking for cut throat criminals. He asks if you are willing to join'
          'You answer:')
    print('\nA. Im not cutout for such a life\n'
          'B. May I have your business card?\n')
    choice=input('>>>')
    if choice in answer_A:
        print('The Yakuza member sense weakness within you and disposes of you...\n\nGAME OVER')
    if choice in answer_B:
        option_business_card()
    else:
        print(required_three)

def option_business_card():
    print('You pocket the business card and head down another stop to the Rivals station.'
          'When you stop in a local Circle K and give the description of the rival to the clerk working the counter.'
          'He mentions that an individual matching that description was just here and points towards the direction he went in.'
          'You catch up to the Rival and watch him walk into his apartment and leave the door slightly opened.'
          'You tiptoe into the apartment and as you open the door you notice a sack of stolen goods but at the same time'
          ' the Rival turns around and notices you. You decide to:')
    print('\nA. Pee your pants\n'
          'B. Lunge for the sack\n'
          'C. Offer a trade')
    choice=input('>>>')
    if choice in answer_A:
        print('Thats kinky, but that aint it...\n\nGAME OVER')
    elif choice in answer_B:
        print('You lunge for the sack but are not fast enough, the Rival gets his hands on you...\n\nGAME OVER')
    elif choice in answer_C:
        print('You offer the rival a lucrative chance to join the Yakuza and show him the business card. You notice the Rivals eyes gloss up.'
              'All he ever wanted was to be apart of a family and have friends. He hands over the sack which you return to the shady individual.'
              'The shady individual is thrilled and rewards you with 200,000 yen!')
        print('Current Yen:',y)
    else:
        print (required)
        option_business_card()






intro() # this must be the very last line to run the program

