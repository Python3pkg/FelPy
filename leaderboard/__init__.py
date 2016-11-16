def write(number, name, *filename):
    if filename:
        filename = ', '.join(str(x) for x in filename)
    else:
        filename = "leaderboard.txt"
    try:
        f = open(filename, 'r+')
    except TypeError:
        raise TypeError("That file doesn't exist")
    for i in range(9):
        l = f.readline()
        v = l[:2]
        v = v.strip()
        if int(number) >= int(v):
            break
    f.seek(15*(i))
    r = f.read(150-(15*i)-30)
    f.seek(15*(i+1)-1)
    f.write(r)
    f.seek(15*i)
    f.write("{0:2s} {1:10s}".format(str(number), name))
    f.close()

def read(*filename):
    if filename:
        filename = ', '.join(str(x) for x in filename)
    else:
        filename = "leaderboard.txt"
    f = open(filename, 'r')
    return (f.read())

def make(*filename):
    if filename:
        filename = ', '.join(str(x) for x in filename)
    else:
        filename = "leaderboard.txt"
    f = open(filename, 'w+')
    for i in range(0,10):
        f.write("0            \n")
