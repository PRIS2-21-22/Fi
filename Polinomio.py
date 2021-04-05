class Polinomio(list):

    def __add__(self, other):
        """Overloaded Method Sum. Return the sum of itself and other polynomial."""
        if len(self) > len(other):
            polinomio_solucion = self[:]
            for x in enumerate(other): polinomio_solucion[x] += other[x]
        else:
            polinomio_solucion = other[:]
            for x in enumerate(self): polinomio_solucion[x] += self[x]
        return polinomio_solucion

    def __sub__(self, other):
        """Overloaded Method Rest. Return the sum of itself and other polynomial."""
        if len(self) > len(other):
            polinomio_solucion = self[:]
            for x in enumerate(other): polinomio_solucion[x] -= other[x]
        else:
            polinomio_solucion = other[:]
            for x in enumerate(self): polinomio_solucion[x] -= self[x]
        return polinomio_solucion

    def __mul__(self, other):
        """Overloaded Method Product. Return the product of itself and other polynomial."""
        polinomio_solucion = [0]*(len(self)+len(other)-1)
        for pos1, val1 in enumerate(self):
            for pos2, val2 in enumerate(other):
                polinomio_solucion[pos1+pos2] += val1*val2
        return polinomio_solucion
