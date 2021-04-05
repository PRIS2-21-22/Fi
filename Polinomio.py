class Polinomio(list):

    def __add__(self, other):
        '''Overloaded Method Sum. Return the sum of itself and other polynomial'''
        if len(self) > len(other):
            polinomioSolucion = self[:]
            for x in range(len(other)): polinomioSolucion[x] += other[x]
        else:
            polinomioSolucion = other[:]
            for x in range(len(self)): polinomioSolucion[x] += self[x]
        return polinomioSolucion

    def __sub__(self, other):
        '''Overloaded Method Rest. Return the sum of itself and other polynomial'''
        if len(self) > len(other):
            polinomioSolucion = self[:]
            for x in range(len(other)): polinomioSolucion[x] += other[x]
        else:
            polinomioSolucion = other[:]
            for x in range(len(self)): polinomioSolucion[x] += self[x]
        return polinomioSolucion

    def __mul__(self, other):
        ''''Overloaded Method Product. Return the product of itself and other polynomial'''
        polinomioSolucion = [0]*(len(self)+len(other)-1)
        for pos1, val1 in enumerate(self):
            for pos2, val2 in enumerate(other):
                polinomioSolucion[pos1+pos2] += val1*val2
        return polinomioSolucion
