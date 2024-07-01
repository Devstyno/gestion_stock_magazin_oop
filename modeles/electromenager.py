from modeles.fournisseur import Fournisseur
from modeles.article import Article
from interfaces.par_piece import ParPiece

# class Electromenager(Article, ParPiece): # heritage et implementation d'interface
class Electromenager(Article): # heritage
    """La classe des articles élécroménagers."""

    def __init__(self, nom : str, fournisseur : Fournisseur, prix : float):
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
    # ## remplir le stock
    # def remplir_stock(self, qtte : int):
    #     self.pieces_en_stock += qtte
    
    # ## vendre
    # def vendre(self, pieces_vendues: int) -> float:
    #     super().vendre(pieces_vendues)
    #     self.pieces_en_stock -= pieces_vendues
    
    ## description de l'article
    def description(self): # redefinition de methode
        return f"{super().description()}\nStock : {self.pieces_en_stock} pieces"