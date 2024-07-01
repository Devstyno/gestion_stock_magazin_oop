from modeles.article import Article
from modeles.stock import Stock
from modeles.electromenager import Electromenager
from modeles.primeur import Primeur

class Magazin:
    """Classe pour les magasins."""

    __nombre_instance = 0

    def __init__(self, nom : str):
        self.__nom : str = nom # nom du magazin
        self.__produits : dict = {"electromenagers" : [], "primeurs" : [], "autres" : []} # deux tableaux de deux articles (éléctroménagers et primeurs)
        self.__depenses : float = 0 # le coût d'achat des produits
        self.__revenus : float = 0 # les revenus après la vente des produits

        Magazin.__nombre_instance += 1
        self.__id : int = Magazin.__nombre_instance

    # property id
    @property
    def id(self):
        return self.__id

    # property nom
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, value : str):
        self.__nom = value

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
        return self.__depenses
    
    @depenses.setter
    def depenses(self, value : float):
        self.__depenses = value

    # property revenus
    @property
    def revenus(self):
        return self.__revenus
    
    @revenus.setter
    def revenus(self, value : float):
        self.__revenus = value

    # methodes complementaires
    def __is_article_in_store(self, article : Article):
        for stock in self.produits["electromenagers"]:
            if article == stock.article:
                return True, stock
        for stock in self.produits["primeurs"]:
            if article == stock.article:
                return True, stock
        for stock in self.produits["autres"]:
            if article == stock.article:
                return True, stock
        return False, None

    def __in_store_article(self, stock : Stock, qtte : float):
        stock.quantite += qtte

    def __ask_for_selling_price(self):
        while True:
            prix_vente = input("A combien comptez vous vendre cet article ? ")
            if prix_vente.isdecimal():
                prix_vente = float(prix_vente)
                return prix_vente
            else:
                print("Saisissez une valeur decimale !")

    def __not_in_store_article(self, article : Article, qtte : float):
        prix_vente = self.__ask_for_selling_price()
        stock = Stock(self, article, prix_vente)
        stock.quantite = qtte
        if isinstance(article, Electromenager):
            self.produits["electromenagers"].append(stock)
        elif isinstance(article, Primeur):
            self.produits["primeurs"].append(stock)
        else:
            self.produits["autres"].append(stock)

    ## remplir le stock
    def remplir_stock(self, article : Article, qtte : float):
        if isinstance(article, Article):
            is_article_in_store, stock = self.__is_article_in_store(article)
            if is_article_in_store:
                self.__in_store_article(stock, qtte)
            else:
                self.__not_in_store_article(article, qtte)
            self.depenses += article.prix * qtte
        else:
            raise ValueError("Ceci n'est pas un article !")

    ## vendre un article
    def vendre(self, article : Article, qtte : float):
        in_store, stock = self.__is_article_in_store(article)
        if in_store:
            if stock.quantite > 0:
                if qtte <= stock.quantite:
                    stock.quantite -= qtte
                    self.revenus += stock.prix_vente * qtte
                else:
                    print("Quantite en stock insuffisante !")
            else:
                print("Rupture de stock !")
        else:
            print("Vous ne pouvez vendre un article que vous ne possedez pas !")

    ## calculateur du taux du rendement
    def taux_rendement(self):
        """Calculateur du taux de rendement du magazin."""
        gains = self.revenus - self.depenses
        rendement = 100 * gains / self.depenses
        return rendement
    
    ## description article
    def description(self):
        """Description de l'état du magazin."""
        return f"Nom : {self.nom}\nDepenses : {self.depenses} XOF\nRevenus : {self.revenus} XOF\nRendement : {self.taux_rendement()} %"
    
    ## nombre de magazin
    @classmethod
    def nombre_magasins(cls):
        return cls.__nombre_instance