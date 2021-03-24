class Monomio():
    numero = ""
    literal = ""
    exponente = ""

    def __init__(self,numero, literal, exponente):
        self.numero = numero
        self.literal = literal
        self.exponente = exponente

    def terminosCompatiblesLiteral(self, other):
        return self.exponente == other.exponente

    def terminosCompatiblesLiteralyExponente(self, other):
        igualLiteral = self.exponente == other.exponente
        return igualLiteral and terminosCompatiblesLiteral(self, other)

    def __add__(self, other):
        '''Overloaded Method Sum. Return the sum of itself and other Monomial'''
        if(! terminosCompatiblesLiteralyExponente(self, other)) raise TypeError("Error: Diferente Exponentes o Literal")
        return Monomio(self.numero + other.numero, self.literal, self.exponente)

    def __sub__(self, other):
        '''Overloaded Method Rest. Return the rest of itself and other Monomial'''
        if(! terminosCompatiblesLiteralyExponente(self, other)) raise TypeError("Error: Diferente Exponentes o Literal")
        return Monomio(self.numero - other.numero, self.literal, self.exponente)

    def __mul__(self, other):
        '''Overloaded Method Mul. Return the product of itself and other Monomial'''
        if(! terminosCompatiblesLiteral(self, other)) raise TypeError("Error: Diferente Literal")
        return Monomio(self.numero * other.numero, self.literal, self.exponente + other.exponente)
