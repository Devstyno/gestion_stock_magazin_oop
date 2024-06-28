class Article:
    """Classe générale des Articles."""

    __nombre_instance = 0

    def __init__(self, nom : str, fournisseur : str, achat : float, vente : float):
        self.__nom : str = nom # le nom du produit
        self.__fournisseur : str = fournisseur # le nom du fournisseur du produit
        self.__prix_achat : float = achat # le prix pour lequel le supermarché achète le produit
        self.__prix_vente : float = vente # le prix pour lequel le supermarché vend le produit

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
    def fournisseur(self, value : str):
        self.__fournisseur = value

    # property prix_achat
    @property
    def prix_achat(self):
        return self.__prix_achat
    
    @prix_achat.setter
    def prix_achat(self, value : float):
        self.__prix_achat = value

    # property prix_vente
    @property
    def prix_vente(self):
        return self.__prix_vente
    
    @prix_vente.setter
    def prix_vente(self, value : float):
        self.__prix_vente = value

    # methodes complementaires
    ## calculateur du taux du rendement
    def taux_rendement(self):
        """Calculateur du taux du rendement."""
        gain = (self.prix_vente - self.prix_achat)
        rendement = 100 * gain / self.prix_achat
        return rendement
    
    ## description article
    def description(self):
        """Description des caractéristiques du produit sur l'écran (les prix, le nom, le fournisseur; rendement)."""
        return f"Nom : {self.nom}\nFournisseur : {self.fournisseur}\nPrix d'achat : {self.prix_achat} XOF\nPrix de vente : {self.prix_vente} XOF\nRendement : {self.taux_rendement()} %"