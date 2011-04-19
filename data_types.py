x = 102 % 10 + 0.25 * 3
print x # 2.75


fullscreen = x < 3 and x > 1 # True, False

print ("FULLSCREEN" if fullscreen else "WINDOW"), "MODE"


color_by_name = {
    "black"   : (0,0,0,255),
    "red"     : (255,0,0,255),
    "green"   : (0,255,0,255),
    "blue"    : (0,0,255,255),
    "yellow"  : (255,255,0,255),
    "magenta" : (255,0,255,255),
    "teal"    : (0,255,255,255),
    "orange"  : (255,200,70,255),
    "pink"    : (255,222,255,255),
    "white"   : (255,255,255,255)
}
magenta = color_by_name["magenta"]
if "black" in color_by_name:
    print "mamy kolor 'black'"
else:
    print "nie mamy koloru 'black'"


aabb1 = (10, 11, 22, 25)
aabb2 = (34, 55, 88, 202)
opponent_list = [aabb1, aabb2]
for opponent in opponent_list:
    print opponent, ", ",
print ""

print "\nprint = ", color_by_name, "\n"
import pprint
print "pprint = ", pprint.pprint(color_by_name), "\n"
