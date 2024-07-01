class Article:
    """Classe générale des Articles."""

    __nombre_instance = 0

    def __init__(self, nom : str, fournisseur, prix : float):
        self.__nom : str = nom # le nom du produit
        self.__fournisseur = fournisseur # le fournisseur du produit
        self.__prix : float = prix # le prix pour lequel le fournisseur vend le produit
    
        Article.__nombre_instance += 1
        self.__id = Article.__nombre_instance

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

    # property fournisseur
    @property
    def fournisseur(self):
        return self.__fournisseur
    
    @fournisseur.setter
    def fournisseur(self, value):
        self.__fournisseur = value

    # property prix
    @property
    def prix(self):
        return self.__prix
    
    @prix.setter
    def prix(self, value : float):
        self.__prix = value

    # methodes complementaires
    ## description article
    def description(self):
        """Description des caractéristiques du produit sur l'écran (les prix, le nom, le fournisseur; rendement)."""
        return f"Nom : {self.nom}\nFournisseur : {self.fournisseur.nom}\nPrix : {self.prix} XOF"
    
    ## nombre d'articles
    @classmethod
    def nombre_articles(cls):
        return cls.__nombre_instance