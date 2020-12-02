class Cards:
    def __init__(self, value, suit, volume):
        self.value = value
        self.suit = suit
        self.volume = volume

    def __repr__(self):
        return f"{self.value} {self.suit}"

    def __str__(self):
        return f"{self.value} {self.suit}"

    def __gt__(self, other):    #מלחמה
        in1 = self.volume
        in2 = other.volume
        if in1 > in2:
            return True
        else:
            return False

    def __eq__(self, other):
        eq1 = self.volume
        eq2 = self.volume
        if eq1 == eq2:
            return True
        else:
            return False
