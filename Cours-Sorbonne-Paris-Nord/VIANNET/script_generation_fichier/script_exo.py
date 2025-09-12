import sys

n = int(sys.argv[1])
for i in range(n):

    f = open( "f" + str(i), "w" )
    f.write( str(i) + "\n" )
    f.close()