from sys import exit
from random import randint

class Scene(object):
    
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)


class Engine(object):
    
    def __init__(self, scene_map):
#        print "Engine __init__ has scene_map", scene_map
        self.scene_map = scene_map
        
    def play(self):
        current_scene = self.scene_map.opening_scene()
#        print "Play's first scene", current_scene
        
        while True:
            print "\n--------"
            scene_name = current_scene.enter()
            if scene_name == 'death':
                death_scene = Death()
                death_scene.enter()
                continue
            else:
                next_scene_name = scene_name
#            print "next scene", next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)
#            print "map returns new scene", current_scene


class Death(Scene):
    
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]
    
    
    def enter(self):
        print "\n"
        print Death.quips[randint(0, len(self.quips)-1)]
        print "\n"
        print "Do you still want to go on?"
        answer = raw_input("y/n? >..")
        if answer == 'y':
            pass
        else:
            exit(1)


class CentralCorridor(Scene):
    
    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "your entire crew.  You are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put it in the bridge, and blow the ship up after getting into an "
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate filled body.  He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."
        
        combat = CombatRound('central_corridor')
        if combat.play() == 'player':
            print "The last hit was finally enough. The Gothon doesn't get up"
            print "this time. You are free to jump through the Weapon Armory"
            print "door."
            return 'laser_weapon_armory'
        else:
            return 'death'


class LaserWeaponArmory(Scene):
    
    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be hiding.  It's dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in its container.  There's a keypad lock on the box"
        print "and you need the code to get the bomb out.  If you get the code"
        print "wrong 15 times then the lock closes forever and you can't"
        print "get the bomb.  The code is 3 digits."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 1
        
        while guess != code and guesses < 15:
            print "BZZZZEDDD!"
            guesses += 1
            
            correct = 0
        
            for i in range(0, len(code)):
                if guess[i] == code[i]:
                    correct += 1
                else:
                    continue
            print "You got %d right." % (correct)
            guess  = raw_input("[keypad]> ")
 
        if guess == code:
            print "The container click open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot"
            return 'the_bridge'
        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print "ship from their ship and you die."
            return 'death'


class TheBridge(Scene):
    
    def enter(self):
        print "You burst onto the Bridge with the neutron destruct bomb"
        print "under your arm and surprise 5 Gothons who are trying to"
        print "take control of the ship.  Each of them has an even uglier"
        print "clown costume than the last.  They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off."
        print "You place the bomb on the floor and aim your weapon at it."
        print "Then you start counting back from three."
        print "By the time you reach 'one' 4 of the Gothons have run past you"
        print "heading back to their ship."
        print "Unfortunatly the last one seems to call your bluff and is"
        print "reaching for his weapon."
        
        combat = CombatRound('the_bridge')
        if combat.play() == 'player':
            print "This time the Gothon is just laying there. You think you"
            print "finally got him. You set the bomb to go off in a"
            print "couple of minutes. Then you run to the escape pod to get"
            print "off this tin can."
            return 'escape_pod'
        else:
            return 'death'


class EscapePod(Scene):

    def enter(self):
        print "You rush through the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes.  It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference.  You get to the chamber with the escape pods, and"
        print "now need to pick one to take.  Some of them could be damaged"
        print "but you don't have time to look.  There's 5 pods, which one"
        print "do you take?"
        
        good_pod = randint(1,5)
#        print "good_pod :", good_pod
        guess = raw_input("[pod #]> ")
        
        while int(guess) != good_pod:
            bad_escape_pods = [1, 2, 3, 4, 5]
            bad_escape_pods.remove(good_pod)
            bad_escape_pods.remove(int(guess))
            second_choice = []
            second_choice.append(good_pod)
            second_choice.append(int(guess))
            second_choice.append(bad_escape_pods.pop(randint(0,2)))
            second_choice.sort()
            
            print "When you move to pod %s the warning lights of pods" % guess
            print "%d and %d start flashing. Seeing the pods fail" % (bad_escape_pods[0],
            bad_escape_pods[1])
            print "right before your eyes makes you doubt whether you have"
            print "chosen the right pod. Pods %d, %d and %d are left." % (second_choice[0],
            second_choice[1], second_choice[2])
            print "Which one do you take?"
            
            guess = raw_input("[pod #]> ")
            
            if int(guess) != good_pod:
                print "You jump into pod %s and hit the eject button." % guess
                print "The pod escapes into the void of space, then"
                print "implodes as the hull ruptures, crushing your body"
                print "into jam jelly."
                return 'death'
        
        print "You jump into pod %s and hit the eject button." % guess
        print "The pod easily slides out into space heading to"
        print "the planet below. As it flies to the planet, you look"
        print "back and see your ship implode then explode like a"
        print "bright star, taking out the Gothon ship at the same"
        print "time. You won!"
            
        exit(1)


class Map(object):
    
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
        print "start_scene in __init__", self.start_scene
    
    def next_scene(self, scene_name):
        print "start_scene in next_scene", self.start_scene
        val = Map.scenes.get(scene_name)
        print "next_scene returns", val
        return val
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)


class Player(object):
    """
    Keeps track of the player status. Used to see which player wins or loses
    a round.
    """
    def __init__(self):
        self.hits = 3


class CombatRound(object):
    """
    Ask the player which action the player will take and choose a random action
    for the Gothon. 
    
    Call Result() with 'choices' as argument to process the actions and show
    the result of the chosen actions.    
    
    Check to see if the player or the Gothon has no more hits left. If so return
    the winner who still has hits left as 'end_result' to the Scene().
    """
    def __init__(self, current_scene):
        self.current_scene = current_scene
        self.get_result = Result()
        self.player = Player()
        self.gothon = Player()
        
    def play(self):
        choices = self.choose()
        result = self.get_result.score(choices)
        end_result = self.check_hits(result)
        
        while end_result == None:
            choices = self.choose()
            result = self.get_result.score(choices)
            end_result = self.check_hits(result)
            
        return end_result

    def choose(self):
        print "Before the Goton makes a move you choose to:"
        print " 1) Raise your weapon to shoot"
        print " 2) Hide in door opening"
        print " 3) Attack the Gothon with your fists"
        
        choice = int(raw_input(">.. "))
        
        if choice == 1:
            player_choice = 'shoot'
        elif choice == 2:
            player_choice = 'duck'
        elif choice == 3:
            player_choice = 'melee'
        else:
            raise ValueError("choice :", choice)
        
        gothon_choices = ['shoot', 'duck', 'melee']
        gothon_choice = gothon_choices[randint(0, 2)]
        return (player_choice, gothon_choice)

    def check_hits(self, result):
        if result == 'player':
            self.gothon.hits -= 1
        elif result == 'gothon':
            self.player.hits -= 1
        else:
            pass
        
        if self.player.hits > 0 and self.gothon.hits > 0:
            return None
        elif self.player.hits < 1:
            return 'gothon'
        elif self.gothon.hits < 1:
            return 'player'
        else:
            ValueError("player hits :",CombatRound.player.hits, 
            "gothon hits:", CombatRound.gothon.hits)


class Result(object):
    """
    Use 'choices' to determine whether the player or the Gothon or neither gets
    hit. Update the correct Player.hits when necessary.
    
    Use 'choices' and 'result' to show a description of the result to the player.
    (The scene specific descriptions are taken from the Scene() objects.)
    """
    def score(self, choices):
        player_choice, gothon_choice = choices
        
        if player_choice == gothon_choice:
            result = 'neither'
        elif player_choice == 'shoot':
            if gothon_choice == 'melee':
                result = 'player'
            else:
                result = 'gothon'
        elif player_choice == 'duck':
            if gothon_choice == 'shoot':
                result = 'player'
            else:
                result = 'gothon'
        elif player_choice == 'melee':
            if gothon_choice == 'duck':
                result = 'player'
            else:
                result = 'gothon'
        else:
            raise ValueError("player_choice :", player_choice, "gothon_choice :",
            gothon_choice)
        
        self.show_result(choices, result)
        return result
    
    def show_result(self, choices, result):
        player_choice, gothon_choice = choices
        
        if player_choice == 'shoot':
            player_action = "You shoot at the Gothon"
        elif player_choice == 'duck':
            player_action = "You hide in the doorway"
        elif player_choice == 'melee':
            player_action = "You run up to the Gothon to take him on with your fists"
        else:
            raise ValueError("choices :", choices)
        
        if gothon_choice == 'shoot':
            gothon_action = " and the Gothon takes a shot at you."
        elif gothon_choice == 'duck':
            gothon_action = " and the Gothon hides in a doorway."
        elif gothon_choice == 'melee':
            gothon_action = " and the Gothon runs up to you waving his fists."
        else:
            raise ValueError("choices :", choices)
        
        if result == 'player':
            if player_choice == 'shoot':
                result_descr = """
                You fire your weapon and hit The Gothon before he gets close.
                He scrambles back.
                """
            elif player_choice == 'duck':
                result_descr = """
                You fire back without looking and get lucky. One of your shots 
                managed to hit the Gothon.
                """
            elif player_choice == 'melee':
                result_descr = """
                With the Gothon hiding he does not see you coming. The Gothon
                may be big but you are still able to hurt him in close combat.
                You get in a good couple of hits before the Gothon gets away
                from you.
                """
            else:
                raise ValueError("player_choice :", player_choice)
            
        elif result == 'gothon':
            if gothon_choice == 'shoot':
                result_descr = """
                The Gothon fires his weapon and hits you before you get close.
                You scramble back to where you came from.
                """
            elif gothon_choice == 'duck':
                result_descr = """
                He fires back without looking and gets lucky. One of his shots 
                managed to hit you.
                """
            elif gothon_choice == 'melee':
                result_descr = """
                With you hiding you don't see him coming. The Gothon
                is big and powerful and you get quite a beating before you 
                manage to get away.
                """
            else:
                raise ValueError("gothon_choice :", gothon_choice)
        
        elif result == 'neither':
            if player_choice == 'shoot':
                result_descr = """
                You both stand there shooting at each other but neither you or 
                the Gothon is able to hit the other. After a while you both give
                up.
                """
            elif player_choice == 'duck':
                result_descr = """
                You duck into a doorway waiting for what comes. However nothing
                is happening. After awhile you peek around the corner and you 
                see the Gothon peeking around the corner of the doorway he was 
                hiding in. Apparently you both had the same idea.
                """
            elif player_choice == 'melee':
                result_descr = """
                You keep your head down and run as fast as you can so you can 
                close the distance between you two as quickly as possible.
                All of a sudden you run into something and you get knocked down 
                to the floor.
                When you look up you see the Gothon lying on the floor aswell. 
                Looks like the Gothon was not paying any attention to where he 
                was going either so you inevitably met halfway. 
                You both scramble back to where you came from.
                """
        
        else:
            raise ValueError("result :", result)
        
        print "\n" + player_action + gothon_action + "\n" + result_descr
