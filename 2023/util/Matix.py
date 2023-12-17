class Matrix:

    def __init__(self) -> None:
        self.row = []

    def fill(self, content: str):
        self.row = [list(line) for line in content.splitlines()]

    def __str__(self) -> str:
        return "\n".join([str(row) for row in self.row])

    def __iter__(self):
        return iter(self.row)

    @staticmethod
    def invert(matrix):
        inv_matrix = Matrix()
        inv_matrix.row = [list(x) for x in zip(*matrix.row)]
        return inv_matrix
