# Hybrid Inheritance

class GrandParent:
    def gearnsmoney(self):
        print("Grand Parent gives property to Child")


class Father(GrandParent):
    def fearnsmoney(self):
        print("Father earns property")


class Mother:
    def mearnsmoney(self):
        print("Mother earns property")


class GrandChild(Father, Mother):
    def gcearnsmoney(self):
        print("Grand Child earns property")


G = GrandChild()

G.gearnsmoney()       # From GrandParent
G.fearnsmoney()       # From Father
G.mearnsmoney()       # From Mother
G.gcearnsmoney()      # From GrandChild