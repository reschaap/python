import random

class Scene (object):
    """
    Class holds the scene description text and scene choice description text.
    The scene_result attribute has the information about which scene
    the result is from and what the input from the player was. The scene_result
    is used in the play() method from the Engine class.
    """
    
    enter_description = ''
    choice_description = ''
    key = None
    scene_result = None
    
    def enter(self):
        """
        The enter() method is used to show the scene desciption and call the 
        choice() method. 
        """
        print self.enter_description
        self.choice()

    
    def choice(self):
        """
        The choice() method uses the scene description text to get
        input from the player. The choice() method then sets the scene_result 
        attribute.
        """
        print self.choice_description
        choice = int(raw_input('>..'))
        self.scene_result = (self.key, choice)


class Engine(object):
    """
    Method calls Map object to find out which Scene object to call. It then
    Calls the Scene object. The result from that call is then used the Map 
    object again.
    """
    
    def __init__(self, map):
       self.map = map
    
    
    def play(self):
        """
        The new_scene method is called om the Map object to get the Scene 
        object to play next. It then enters a loop to go through several 
        Scene objects 
        """
        self.map.next_scene(None)
        scene = self.map.new_scene
        
        while scene != None:
           scene.enter()
           scene_result = scene.scene_result
           self.map.next_scene(scene_result)
           scene = self.map.new_scene
           
        print "Thank you for playing."


class Death(Scene):
    
    enter_description = "Death enter description."
    choice_description = "Start again? 1 for yes and 2 for no."
    key = 'death'


class CentralCorridor(Scene):
    
    enter_description = "CentralCorridor enter description."
    choice_description = "Choose 1 or 2."
    key = 'central_corridor'


class LaserWeaponArmory(Scene):

    combination = None    
    enter_description = """LaserWeaponArmory enter description."""
    key = 'laser_weapon_armory'
  
    def __init__(self):
        self.number_generator()
    
    
    def number_generator(self):
        """
        Generates a list containing 4 digits. Each digit is randomly generated
        from the range 0-9. The list is set to the attribute self.combination. 
        """
        
        self.combination = [random.randint(0,9) for i in range(0,4)]

    
    def check(self, player_input):
        """
        Takes the input from the player and compares it to self.combination, 
        digit for digit. It returns how many numbers of the player input are
        correct. 
        """
        correct = 0
        
        for i in range(0, len(player_input)):
            if player_input[i] == self.combination[i]:
                correct += 1
            else:
                continue
        return correct
 
 
    def get_player_input(self):
        player_input = []
        
        for i in range (1, 5):
            print "Please enter digit nr ", i," : "
            number = int(raw_input(">.."))
            player_input.append(number)
        
        return player_input
 
 
    def choice(self):
        """
        Let the player enter a 4 number combination. Get the input in a list.
        Call check() to compare self.combination and the player input to see
        how many numbers are correct. If the player input is the same as 
        self.combination than go to the next scene. If it is not, show the 
        player how many numbers he got right and let the player enter another
        4 number combination. After 10 tries show the right combination to the 
        player. 
        """
        
        number_of_guesses = 10
        
        print "Enter the combination of the armory."
        print "(hint: it is 4 numbers)"
    
        player_input = self.get_player_input()
        
        correct = self.check(player_input)
        guess = 1
        

        while guess < number_of_guesses:
            guess += 1
            print "The combination is wrong."
            if correct >= 0:
                print "You got %d right though. Please try again." % (correct)
                player_input = self.get_player_input()
                correct = self.check(player_input)
            if correct == 4:
                self.scene_result = (self.key, 1)
            else:
                continue
        
#        print "guesses ", guess
#        print "correct ", correct
        
        while correct < 4:
            print "This is taking to long. The combination of the armory is: "
            print self.combination
            print "Please enter it correctly this time."
            player_input = self.get_player_input()
            correct = self.check(player_input)
            if correct == 4:
                self.scene_result = (self.key, 1)
            else:
                continue



class TheBridge(Scene):
    
    enter_description = "TheBridge enter description"
    choice_description = "Choose 1 or 2"
    key = 'the_bridge'


class EscapePod(Scene):
    
    enter_description = "EscapePod enter description"
    choice_description = "Choose 1 or 2"
    key = 'escape_pod'


class Map(object):
    """
    Class holds the information structure of the scenes including which 
    scene leads to which. Attribute scene_structure holds the scene objects and
    and the scene objects that lead from that. 
    """
    
    new_scene = None
    scene_structure = { 'death' :  [Death(), CentralCorridor(), None], 
        'central_corridor' :  [CentralCorridor(), Death(), LaserWeaponArmory()]
        , 'laser_weapon_armory' : [LaserWeaponArmory(), TheBridge()], 
        'the_bridge' : [TheBridge(), Death(), EscapePod()], 'escape_pod' : 
        [EscapePod(), Death(), None]}
        
    def __init__(self, start_scene):
        self.start_scene = start_scene

    
    def next_scene(self, scene_result):
        """
        If start_scene is not set then the method is used to select the next 
        scene using the scene_result parameter. Else opening_scene() is called.
        The scene_result parameter consists of a scene_structure key and an 
        integer. These values are then used to get the scene object from 
        scene_structure.
        """
        if self.start_scene == None:
            key, choice = scene_result
            scene_list = self.scene_structure[key]
            self.new_scene = scene_list[choice]
        
        else:
            self.opening_scene()
    
    
    def opening_scene(self):
        """
        The start_scene parameter is used as a key for scene_structure 
        directory. And is used to get the starting scene object.
        """
        scene_list = self.scene_structure[self.start_scene]
        self.new_scene = scene_list[0]
        self.start_scene = None
