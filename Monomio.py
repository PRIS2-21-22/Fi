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
        return igualLiteral && terminosCompatiblesLiteral(self, other)

    @staticmethod
    def sumar(self, other):
        '''Return the sum of itself and other Monomial'''
        if(! terminosCompatiblesLiteralyExponente(self, other)) raise TypeError("Error: Diferente Exponentes o Literal")
        monomioSumado = Monomio(self.numero + other.numero, self.literal, self.exponente)
        return monomioSumado

    @staticmethod
    def restar(self, other):
        '''Return the rest of itself and other Monomial'''
        if(! terminosCompatiblesLiteralyExponente(self, other)) raise TypeError("Error: Diferente Exponentes o Literal")
        monomioSumado = Monomio(self.numero - other.numero, self.literal, self.exponente)
        return monomioSumado

    @staticmethod
    def producto(self, other):
        '''Return the product of itself and other Monomial'''
        if(! terminosCompatiblesLiteral(self, other)) raise TypeError("Error: Diferente Literal")
        monomioProducto = Monomio(self.numero * other.numero, self.literal, self.exponente + other.exponente)
        return monomioProducto
