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
    
    self.enter_description = "Death enter_description"
    self.choice_description = "Death choice_description"



class CentralCorridor(Scene):
    
    def enter(self):
        pass


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
        pass
    
    def next_scene(self, scene_name):
        pass
    
    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
