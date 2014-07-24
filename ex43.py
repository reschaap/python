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
    
    def __init__(self, map):
       self.map = map
    
    def play(self):
        self.map.next_scene(None)
        scene = self.map.new_scene
        scene.enter()
        scene_result = scene.scene_result
        
        while scene_result != None:
           self.map.next_scene(scene_result)
           scene = self.map.new_scene
           scene_result = scene.enter()
           
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
    
    enter_description = "LaserWeaponArmory enter description."
    choice_description = "Press 1"
    key = 'laser_weapon_armory'


class TheBridge(Scene):
    
    def enter(self):
        pass


class EscapePod(Scene):
    
    def enter(self):
        pass


class Map(object):
    """
    Class holds the information structure of the scenes including which 
    scene leads to which. Attribute scene_structure holds the scene objects and
    and the scene objects that lead from that. 
    """
    
    new_scene = None
    scene_structure = { 'death' :  [Death(), CentralCorridor(), None], 
        'central_corridor' :  [CentralCorridor(), Death(), LaserWeaponArmory()]
        , 'laser_weapon_armory' : [LaserWeaponArmory(), None] }
        
    def __init__(self, start_scene):
        self.start_scene = start_scene

    
    def next_scene(self, scene_result):
        """
        Method is used to select the next scene 
        """
        if self.start_scene == None:
            key, choice = scene_result
            scene_list = self.scene_structure[key]
            self.new_scene = scene_list[choice]
        
        else:
            self.opening_scene()
    
    
    def opening_scene(self):
        scene_list = self.scene_structure[self.start_scene]
        self.new_scene = scene_list[0]
        self.start_scene = None


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

