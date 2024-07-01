from datetime import datetime
from modeles.article import Article
# from modeles.magasin import Magazin

class Stock:
    """Classe générale des Stocks."""

    __nombre_instance = 0

    def __init__(self, magazin, article : Article, prix_vente : float):
        self.__magazin = magazin # le magazin
        self.__article : Article = article # l'article
        self.__prix_vente : float = prix_vente # le prix pour lequel le magazin vend le produit
        self.__quantite : float = 0

        self.__date_created : datetime = datetime.now() # date de creation du stock
        self.__date_updated : datetime = datetime.now() # date de mise a jour du stock

        Stock.__nombre_instance += 1
        self.__id = Stock.__nombre_instance

    # property id
    @property
    def id(self):
        return self.__id

    # property magazin
    @property
    def magazin(self):
        return self.__magazin
    
    @magazin.setter
    def magazin(self, value):
        self.__magazin = value

    # property article
    @property
    def article(self):
        return self.__article

    @article.setter
    def article(self, value : Article):
        self.__article = value

    # property date_created
    @property
    def date_created(self):
        return self.__date_created

    # property date_updated
    @property
    def date_updated(self):
        return self.__date_updated

    @date_updated.setter
    def date_updated(self, value : datetime):
        self.__date_updated = value

    # property prix_vente
    @property
    def prix_vente(self):
        return self.__prix_vente
    
    @prix_vente.setter
    def prix_vente(self, value : float):
        self.__prix_vente = value

    # property quantite
    @property
    def quantite(self):
        return self.__quantite
    
    @quantite.setter
    def quantite(self, value : float):
        self.__quantite = value

    # methodes complementaires
    ## mettre a jour la quantite
    def update_quantite(self, qtte : float):
        self.quantite += qtte
        self.date_updated = datetime.now()

    ## calculateur du taux du rendement
    def taux_rendement(self):
        """Calculateur du taux du rendement."""
        gain = (self.prix_vente - self.article.prix)
        rendement = 100 * gain / self.article.prix
        return rendement
    
    ## description stock
    def description(self):
        """Description des caractéristiques du produit sur l'écran (les prix_vente, le magazin, le article; rendement)."""
        return f"Magazin : {self.magazin.nom}\nArticle : {self.article.nom}\nprix d'achat : {self.article.prix} XOF\nprix de vente : {self.prix_vente} XOF\nRendement : {self.taux_rendement()} %"
    
    ## nombre d'stocks
    @classmethod
    def nombre_stocks(cls):
        return cls.__nombre_instance