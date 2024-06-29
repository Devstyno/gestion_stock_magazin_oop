class ParPiece:
    """L'interface pour les produits qui se comptent par pièce."""

    def vendre(self, pieces_vendues : int) -> float:
        pass

    def remplir_stock(self, qtte_pieces : int) -> None:
        pass