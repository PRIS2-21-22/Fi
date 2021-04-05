class Polinomio(list):

    def __add__(self, other):
        """Overloaded Method Sum. Return the sum of itself and other polynomial"""
        if len(self) > len(other):
            solucion = self[:]
            for x in range(len(other)): solucion[x] += other[x]
        else:
            solucion = other[:]
            for x in range(len(self)): solucion[x] += self[x]
        return solucion

    def __sub__(self, other):
        """Overloaded Method Rest. Return the sum of itself and other polynomial"""
        if len(self) > len(other):
            solucion = self[:]
            for x in range(len(other)): solucion[x] += other[x]
        else:
            solucion = other[:]
            for x in range(len(self)): solucion[x] += self[x]
        return solucion

    def __mul__(self, other):
        """Overloaded Method Product. Return the product of itself and other polynomial"""
        solucion = [0]*(len(self)+len(other)-1)
        for pos1, val1 in enumerate(self):
            for pos2, val2 in enumerate(other):
                solucion[pos1+pos2] += val1*val2
        return solucion
