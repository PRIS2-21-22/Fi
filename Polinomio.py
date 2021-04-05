class Polinomio(list):

    def __add__(self, other):
        '''Overloaded Method Sum. Return the sum of itself and other polynomial'''
        if len(self) > len(other):
            PolinomioSolucion = self[:]
            for x in range(len(other)): PolinomioSolucion[x] += other[x]
        else:
            PolinomioSolucion = other[:]
            for x in range(len(self)): PolinomioSolucion[x] += self[x]
        return PolinomioSolucion

    def __sub__(self, other):
        '''Overloaded Method Rest. Return the sum of itself and other polynomial'''
        if len(self) > len(other):
            PolinomioSolucion = self[:]
            for x in range(len(other)): PolinomioSolucion[x] += other[x]
        else:
            PolinomioSolucion = other[:]
            for x in range(len(self)): PolinomioSolucion[x] += self[x]
        return PolinomioSolucion

    def __mul__(self, other):
        ''''Overloaded Method Product. Return the product of itself and other polynomial'''
        PolinomioSolucion = [0]*(len(self)+len(other)-1)
        for pos1, val1 in enumerate(self):
            for pos2, val2 in enumerate(other):
                PolinomioSolucion[pos1+pos2] += val1*val2
        return PolinomioSolucion
