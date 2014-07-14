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
        print self.key
        print choice
        self.scene_result = (self.key, choice)


class Engine(object):
    
    def __init__(self, scene_map):
       self.scene_map = scene_map
    
    def play(self):
        scene = self.scene_map.next_scene(None)
        scene_result = scene.enter()
        
        while scene_result != None:
           scene = self.scene_map.next_scene(scene_result)
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
    def enter(self):
        pass


class TheBridge(Scene):
    
    def enter(self):
        pass


class EscapePod(Scene):
    
    def enter(self):
        pass


class Map(object):
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
        self.scene_structure = { 'death' :  [Death(), CentralCorridor(), None], 
        'central_corridor' :  [CentralCorridor(), Death(), LaserWeaponArmory()]
        , 'laser_weapon_armory' : [LaserWeaponArmory(), None] }
    
    
    def next_scene(self, scene_result):
        if self.start_scene == None:
            key, choice = scene_result
            scene_list = self.scene_structure[key]
            scene = scene_list[choice]
            return scene
        
        else:
            self.opening_scene()
    
    
    def opening_scene(self):
        scene_list = self.scene_structure[self.start_scene]
        scene = scene_list[0]
        self.start_scene = None
        return scene


a_map = Map('central_corridor')
a_game = Engine(a_map)
#a_game.play()

a_scene = Death()
a_scene.enter()
print a_scene.scene_result