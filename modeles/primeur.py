from modeles.article import Article
from interfaces.par_kilogramme import ParKilogramme

# class Primeur(Article, ParKilogramme): # heritage et implementation d'interface
class Primeur(Article): # heritage
    """La classe des primeurs."""

    def __init__(self, nom : str, fournisseur : str, prix : float):
        super().__init__(nom, fournisseur, prix)
        self.__kg_en_stock : float = 0 # polymorphisme
    
    # property kg_en_stock
    @property
    def kg_en_stock(self):
        return self.__kg_en_stock
    
    @kg_en_stock.setter
    def kg_en_stock(self, value : float):
        self.__kg_en_stock = value
    
    # methodes complementaires
    # ## remplir le stock
    # def remplir_stock(self, qtte : float):
    #     self.kg_en_stock += qtte
    
    # ## vendre
    # def vendre(self, kg_vendus: float) -> float:
    #     super().vendre(kg_vendus)
    #     self.kg_en_stock -= kg_vendus
    
    ## description de l'article
    def description(self): # redefinition de methode
        return f"{super().description()}\nStock : {self.kg_en_stock} kg"