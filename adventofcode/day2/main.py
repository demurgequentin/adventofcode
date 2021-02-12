if __name__ == "__main__":
    fichier = open('input.txt', 'r')
    content = fichier.read()
    tab1 = [ i for i in content.split('\n')]
    x = 0
    y = 0
    for e in tab1:
        decoupe = e.split(' ')
        nombre = [int(z) for z in decoupe[0].split('-')]
        lettre1 = decoupe[1].split(':')
        min = nombre[0]
        max = nombre[1]
        lettre = lettre1[0]
        mdp = decoupe[2]
        #nb = decoupe[2].count(tacle[0])
        print(decoupe)
        #print(nombre)
        print(lettre)
        print(min)
        print(max)
        print(mdp)
        #print(nb)
        #if nombre[0] <= nb <= nombre[1]:
           # x = x + 1
        #print('x = ', x)

        if (lettre == mdp[min-1]) ^ (lettre == mdp[max-1]):
            print('true')
            x = x + 1
            print('x = ', x)
        else:
            print('false')
            print('x = ', x)
        #if lettre == mdp[max-1]:
         #   print('true')
        #else:
         #   print('false')
