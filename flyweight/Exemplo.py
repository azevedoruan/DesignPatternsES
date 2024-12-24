class ProjetilFlyweight:
    def __init__(self, sprite, color):
        self.sprite = sprite
        self.color = color
    
    def draw(canvas, coords):
        canvas.draw(sprite, color, coords)

class ProjetilFactory:
    _flyweights = {}

    def get_projetil(sprite, color):
        obj = _flyweights.find(sprite, color)
        if obj == null:
            obj = ProjetilFlyweght(repeatingState)
            _flyweights.add(obj)
        
        return obj

class Projetil:
    _projetilFlyweght

    def __init__(self, coords, vector, speed, projetilFlyweight):
        self.coords = coords
        self.vector = vector
        self.speed = speed
        _projetilFlyweght = projetilFlyweight

    def move_and_draw(canvas):
        # algoritmo de movimento extremamente básico
        coords += vector * speed

        _projetilFlyweght.draw(canvas, coords)

class Game:
    _projetils = {}
    _projetilFactory

    def shot_projetil(sprite, color, coords, vector, speed):
        projetilFlyweight = _projetilFactory.get_projetil(sprite, color)
        projetil = Projetil(coords, vector, speed, projetilFlyweight)
        _projetils.add(projetil)
    
    def draw(canvas):
        for projetil in _projetils:
            projetil.move_and_draw(canvas)