class MagicMethods:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Salom, men {self.name}!"

    def __repr__(self):
        return f"MagicMethods(name='{self.name}')"

    def __eq__(self, other):
        if isinstance(other, MagicMethods):
            return self.name == other.name
        return False

    def __lt__(self, other):
        if isinstance(other, MagicMethods):
            return self.name < other.name
        return False

    def __gt__(self, other):
        if isinstance(other, MagicMethods):
            return self.name > other.name
        return False

    def __add__(self, other):
        if isinstance(other, MagicMethods):
            return f"{self.name} + {other.name}"
        return f"{self.name} + {other}"

    def __sub__(self, other):
        if isinstance(other, MagicMethods):
            return f"{self.name} - {other.name}"
        return f"{self.name} - {other}"

    def __mul__(self, other):
        if isinstance(other, MagicMethods):
            return f"{self.name} * {other.name}"
        return f"{self.name} * {other}"

    def __truediv__(self, other):
        if isinstance(other, MagicMethods):
            return f"{self.name} / {other.name}"
        return f"{self.name} / {other}"

    def __floordiv__(self, other):
        if isinstance(other, MagicMethods):
            return f"{self.name} // {other.name}"
        return f"{self.name} // {other}"

    def __mod__(self, other):
        if isinstance(other, MagicMethods):
            return f"{self.name} % {other.name}"
        return f"{self.name} % {other}"

    def __pow__(self, other):
        if isinstance(other, MagicMethods):
            return f"{self.name} ** {other.name}"
        return f"{self.name} ** {other}"

    def __len__(self):
        return len(self.name)

    def __getitem__(self, index):
        return self.name[index]

    def __setitem__(self, index, value):
        self.name = self.name[:index] + value + self.name[index+1:]

    def __delitem__(self, index):
        self.name = self.name[:index] + self.name[index+1:]

    def __contains__(self, item):
        return item in self.name

    def __iter__(self):
        return iter(self.name)

    def __reversed__(self):
        return reversed(self.name)

    def __hash__(self):
        return hash(self.name)

    def __call__(self, *args, **kwargs):
        return f"Men {self.name} deb atam!"

obj1 = MagicMethods("Ali")
obj2 = MagicMethods("Vali")

print(obj1)  # Salom, men Ali!
print(obj2)  # Salom, men Vali!

print(obj1 == obj2)  # False
print(obj1 < obj2)   # False
print(obj1 > obj2)   # True

print(obj1 + obj2)  # Ali + Vali
print(obj1 - obj2)  # Ali - Vali
print(obj1 * obj2)  # Ali * Vali
print(obj1 / obj2)  # Ali / Vali
print(obj1 // obj2) # Ali // Vali
print(obj1 % obj2)  # Ali % Vali
print(obj1 ** obj2) # Ali ** Vali

print(len(obj1))  # 3
print(obj1[0])    # A
obj1[0] = 'X'
print(obj1[0])    # X
del obj1[0]
print(obj1[0])    # (bo'sh)

print('A' in obj1)  # True
print('X' in obj1)  # True

for i in obj1:
    print(i)

for i in reversed(obj1):
    print(i)

print(hash(obj1))  # hash qiymat

print(obj1())  # Men Ali deb atam!
