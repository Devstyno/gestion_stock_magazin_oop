from modeles.article import Article

class Electromenager(Article): # heritage
    """La classe des articles élécroménagers."""

    def __init__(self, nom : str, fournisseur, prix : float):
        super().__init__(nom, fournisseur, prix)
        self.__pieces_en_stock : int = 0 # polymorphisme
    
    # property pieces_en_stock
    @property
    def pieces_en_stock(self):
        return self.__pieces_en_stock
    
    @pieces_en_stock.setter
    def pieces_en_stock(self, value : int):
        self.__pieces_en_stock = value
    
    # methodes complementaires    
    ## description de l'article
    def description(self): # redefinition de methode
        return f"{super().description()}\nStock : {self.pieces_en_stock} pieces"