from modele.article import Article
from modele.electromenager import Electromenager
from modele.primeur import Primeur

class Magasin:
    """Classe générale des Articles."""

    __nombre_instance = 0

    def __init__(self):
        self.__produits : dict = {"electromenagers" : [], "primeurs" : [], "autres" : []} # deux tableaux de deux articles (éléctroménagers et primeurs)
        self.__depenses : float = 0 # le coût d'achat des produits
        self.__revenus : float = 0 # les revenus après la vente des produits

        Magasin.__nombre_instance += 1

    # property produits
    @property
    def produits(self):
        return self.__produits
    
    @produits.setter
    def produits(self, value : dict):
        self.__produits = value

    # property depenses
    @property
    def depenses(self):
        depenses = 0
        for electromenager in self.produits["electromenagers"]:
            depenses += electromenager.prix_achat
        for primeurs in self.produits["primeurs"]:
            depenses += primeurs.prix_achat
        self.__depenses = depenses
        return self.__depenses
    
    @depenses.setter
    def depenses(self, value : float):
        self.__depenses = value

    # property revenus
    @property
    def revenus(self):
        revenus = 0
        for electromenager in self.produits["electromenagers"]:
            revenus += electromenager.prix_vente
        for primeurs in self.produits["primeurs"]:
            revenus += primeurs.prix_vente
        self.__revenus = revenus
        return self.__revenus
    
    @revenus.setter
    def revenus(self, value : float):
        self.__revenus = value

    # methodes complementaires
    ## calculateur du taux du rendement
    def taux_rendement(self):
        """Calculateur du taux de rendement du magasin."""
        gains = self.revenus - self.depenses
        rendement = 100 * gains / self.depenses
        return rendement
    
    ## description article
    def description(self):
        """Description de l'état du magasin."""
        return f"Depenses : {self.depenses} XOF\nRevenus : {self.revenus} XOF\nRendement : {self.taux_rendement()} %"
    
    ## ajouter un article
    def ajout_electromenager(self, article):
        if isinstance(article, Article):
            if isinstance(article, Electromenager):
                self.produits["electromenagers"].append(article)
            elif isinstance(article, Primeur):
                self.produits["primeurs"].append(article)
            else:
                self.produits["autres"].append(article)
        raise ValueError("Vous essayez d'ajouter tout sauf un article !")
    
    ## nombre de magasin
    @classmethod
    def nombre_magasins(cls):
        return cls.__nombre_instance