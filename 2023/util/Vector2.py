class Vector2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector2(self.x + other.x,self.y + other.y)
    
    def __sub__(self, other):
        return Vector2(self.x - other.x,self.y - other.y)
    
    def __eq__(self, other) -> bool:
        if other == None:
            return False
        return self.x == other.x and self.y == other.y

    def __neg__(self):
        return Vector2(-self.x, -self.y)
    
    def __str__(self) -> str:
        return f"{self.x}:{self.y}"
    
    def __repr__(self) -> str:
        return str(self)
        