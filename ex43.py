class Scene (object):
    
    enter_description = ''
    choice_description = ''
    key = None
    scene_result = None
    
    def enter(self):
        print self.enter_description
        self.choice()

    
    def choice(self):
        print self.choice_description
        choice = raw_input('>..')
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
    
    new_scene = None
    scene_structure = { 'death' :  [Death(), CentralCorridor(), None], 
        'central_corridor' :  [CentralCorridor(), Death(), LaserWeaponArmory()]
        , 'laser_weapon_armory' : [LaserWeaponArmory(), None] }
        
    def __init__(self, start_scene):
        self.start_scene = start_scene

    
    def next_scene(self, scene_result):
        if self.start_scene == None:
            key, choice = scene_result
            scene_list = self.scene_structure[key]
            self.new_scene = scene_list[int(choice)]
        
        else:
            self.opening_scene()
    
    
    def opening_scene(self):
        scene_list = self.scene_structure[self.start_scene]
        self.new_scene = scene_list[0]
        self.start_scene = None


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

