if __name__ == "__main__":
    fichier = open('input.txt', 'r')
    content = fichier.read()
    tab1 = [ int(i) for i in content.split('\n')]
    for e in tab1:
        for j in tab1:
            if e + j == 2020:
                print(e*j, e, j)
    for e in tab1:
        for j in tab1:
            for f in tab1:
                if e + j + f == 2020:
                    print(e * j * f)

