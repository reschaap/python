from ex43_book import *

#a_map = Map('laser_weapon_armory')
#a_game = Engine(a_map)
#a_game.play()

a_combat = CombatRound('central_corridor')
end_result = a_combat.play()
print "result of the CombatRound is: ", end_result

exit(1)