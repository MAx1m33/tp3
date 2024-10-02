import random as rd



class jeu:

    def __init__(self, m, n):
        self.k = rd.randint(0, m)
        print(self.k)
        self.n = n
        print(self.k)


    # q14: 2eme methode pour n:
    # def __init__(self,m):
    #     self.k = rd.randint(0,m)
    #     self.n = int(input("entrez le nombre maximal d'essais:"))
    #     print(self.k)


    def test(self, i):
        self.n = self.n - 1
        if i == self.k:
            print("Bravo, tu as gagné!")
            return True
        elif i > self.k:
            print("Trop grand!")
            return False
        else:
            print("Trop petit!")
            return False

    def jouer(self,):
        while self.n > 0:
            try:
                print("attention, il vous reste ", self.n, " essais")
                partie = int(input("Entrez un nombre entier : "))
                if self.test(partie):
                    break
                if self.n == 0:
                    print("Tu as perdu!")
            except ValueError:
                print("Ceci n'est pas un entier, entrez un nouveau nombre")
        return

if __name__ == "__main__":
    import doctest
    doctest.testmod()
j = jeu(100, 6)
k = jeu.jouer(j)

