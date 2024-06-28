# Gestion de stock d'un magasin

_On écrira un programme qui gère le stock d'un magasin._

On suppose qu'on a déjà conçu la description du problème en termes des classes et des interfaces.
Vous devez d'abord comprendre la hiérarchie des classes et des interfaces comme suit.
Cela est nécessaire pour voir clairement les paramètres de retour des méthodes ainsi que la liste de leurs paramètres formels.

Voici une spécification du programme en termes de classes et des interfaces:

## I. On aura deux interfaces

1. Vendable par kilogramme : l'interface pour les produits qui se vendent par kilogramme
    Méthodes:
        - vendre: cette méthode reçoit la quantité vendue du produit, retourne le revenu du magasin et modifie le stock

2. Vendable par pièce: l'interface pour les produits qui se vendent par pièces
    Méthodes:
        - vendre: cette méthode reçoit la quantité vendue du produit, retourne le revenu du magasin et modifie le stock

## II. On aura une classe générale des Articles

### Propriétés

- prix d'achat: le prix pour lequel le supermarché achète le produit
- prix de vente: le prix pour lequel le supermarché vend le produit
- nom: le nom du produit
- fournisseur: le nom du fournisseur du produit

### Méthodes (autre que le constructeur)

- calculateur du taux du rendement
- description des caractéristiques du produit sur l'écran (les prix, le nom, le fournisseur; rendement)

_Cette classe n'implémente aucune interface._

## III. On a deux classes dérivées des Articles

Chaque classe dérivée des articles respecte la règle suivante : ***au moment de la construction de l'objet, le stock est vide.***

1. La classe des articles élécroménagers
    Propriétés supplémentaires:
        - nombre de pièces en stock :

    Méthodes supplémentaires (autre que le constructeur):
        - remplir le stock
        - description des caractéristiques du produit sur l'écran (les prix, le nom, le fournisseur; rendement; stock)

    _Il faut implémenter les interfaces correspondantes à cette classe._

2. La classe des primeurs
    Propriété supplémentaires:
        - quantité en stock
    Méthodes supplémentaires:
        - remplir le stock
        - description des caractéristiques du produit sur l'écran (les prix, le nom, le fournisseur; rendement; stock)

    _Il faut implémenter les interfaces correspondantes à cette classe._

## IV. On a une classe pour les magasins

### Propriétés

- Dépenses: le coût d'achat des produits
- Revenus: les revenus après la vente des produits
- Produits: deux tableaux de deux articles (éléctroménagers et primeurs)

### Méthodes (autre que le constructeur)

- description de l'état du magasin
- calculateur du taux de rendement

## Travail à faire

A. Coder les interfaces et les classes.
B. Créer un fichier de testes qui crée un magasin, définit les articles à vendre, effectue le remplissage du stock et simule les ventes.
