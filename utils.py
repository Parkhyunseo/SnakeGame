from random import randint

class Utils():
    @classmethod
    def get_rand_position(cls, size:int) -> int:
        return (randint(-size//2, size//2), randint(-size//2, size//2))

    @classmethod
    def get_distance(cls, pos_a:tuple, pos_b:tuple) -> float:
        return ( (pos_a[0]-pos_b[0])**2 + (pos_a[1]-pos_b[1])**2 ) ** 0.5