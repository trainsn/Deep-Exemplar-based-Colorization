import sys

style_id = sys.argv[1]
zSize = 256

fo = open("pairs.txt")
for i in range(zSize):
	fo.write("clip_%d.png %d 1" % (i, style_id) )
fo.close()

