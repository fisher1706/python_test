from dataclasses import dataclass, field, InitVar


class Vector3D:
    def __init__(self, x: int, y: int, z: int, calc_len: bool = True):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x * x + y * y + z * z) ** 0.5 if calc_len else 0


@dataclass
class V3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    calc_len: InitVar[bool] = True
    length: float = field(init=False, compare=False, default=0)

    def __post_init__(self, calc_len):
        if calc_len:
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


if __name__ == '__main__':
    v1 = V3D(1, 2, 3)
    print(v1)
    print(v1.__dict__)

    v2 = V3D(1, 2, 5)

    print(v1 == v2)

    v3 = V3D(1, 2, 3, False)
    print(v3)
