class Scene (object):
    
    self.enter_description = ''
    self.choice_description = ''
    self.key = None
    
    
    def enter(self):
        print self.enter_description
        self.choice()

    
    def choice(self):
        print self.choice_description
        choice = raw_input(>..)
        return (self.key, choice)


class Engine(object):
    
    def __init__(self, scene_map):
        pass
    
    def play(self):
        pass


class Death(Scene):
    
    self.enter_description = "Death enter description"
    self.choice_description = "Death choice description"
    self.key = death


class CentralCorridor(Scene):
    
    self.enter_description = "CentralCorridor enter description"
    self.choice_description = "CentralCorridor choice description"
    self.key = central_corridor


class LaserWeaponArmory(Scene):
    
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
        self.current_scene = start_scene
        self.scene_structure = { 'death' :  [Death(), CentralCorridor()], 
        'central_corridor' :  [CentralCorridor(), Death(), LaserWeaponArmory()]
        , 'laser_weapon_armory' : [LaserWeaponArmory(), Death(), TheBridge()]
    
    
    def next_scene(self, scene_name):
        if self.current_scene != None:
            self.opening_scene()
        pass
    
    def opening_scene(self):
        scene_list = self.scene_structure[scene_name]
        scene = scene_list[0]
        


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
