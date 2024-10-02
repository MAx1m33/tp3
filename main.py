import random as rd


class jeu:

    def __init__(self, m, n):
        self.k = rd.randint(0, m)
        self.n = n
        print(k)
        if __name__ == "__main__":
            import doctest
            doctest.testmod()

    # q14: 2eme methode pour n:
    # def __init__(self,m):
    #     self.k = rd.randint(0,m)
    #     self.n = int(input("entrez le nombre maximal d'essais:"))
    #     #"""__summary__
    #     print(k)
    #     if __name__== "__main__":
    #         import doctest
    #         doctest.testmod()

    def test(self, i, k):
        self.n = self.n - 1
        if i == k:
            print("Bravo, tu as gagné!")
            return True
        elif i > k:
            print("Trop grand!")
            return False
        else:
            print("Trop petit!")
            return False

    def jouer(self):
        while self.n > 0:
            try:
                print("attention, il vous reste ", self.n, " essais")
                partie = int(input("Entrez un nombre entier : "))
                if self.test(partie):
                    break
            except ValueError:
                print("Ceci n'est pas un entier, entrez un nouveau nombre")
        if self.n == 0:
            print("Tu as perdu!")
        return


j = jeu(100, 6)
k = jeu.jouer()
