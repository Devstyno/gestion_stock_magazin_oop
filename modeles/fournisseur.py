from modeles.article import Article

class Fournisseur:
    """Classe des Fournisseurs."""

    __nombre_instance = 0

    def __init__(self, nom : str, email : str):
        self.__nom : str = nom # le nom du fournisseur
        self.__email : str = email # l'email du fournisseur
    
        Fournisseur.__nombre_instance += 1
        self.__id : int = Fournisseur.__nombre_instance

    # property id
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value : int):
        self.__id = value

    # property nom
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, value : str):
        self.__nom = value

    # property email
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value : str):
        self.__email = value

    # methodes complementaires
    ## produire un article
    def produire(self, nom : str, prix : float):
        return Article(nom, self, prix)

    ## description article
    def description(self):
        """Description du fournisseur."""
        return f"Nom : {self.nom}\nEmail : {self.email}"
    
    ## nombre de fournisseurs
    @classmethod
    def nombre_fournisseurs(cls):
        return cls.__nombre_instance