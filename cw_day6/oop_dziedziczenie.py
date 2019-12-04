class Auto: # klasa modelu - struktura danych
    def __init__(self, model, engine_type):
        self.model = model
        self.engine_type = engine_type
    def __str__(self):
        return "model:  %15s \nengine: %15s" % (self.model, self.engine_type)


class Hybrid(Auto):
    def __init__(self, model, engine_type, acu_cap):
        super().__init__(model, engine_type) # wywołanie konstruktora Auto
        self.acu_cap = acu_cap # Hybrid widzi 3 pola tekstowe
    def __str__(self):
        return super().__str__() + "\naku: %18s" % (self.acu_cap)

class AutoComparator:
    def compareAutos(self, a1, a2):
        print("%15s | %15s"  % (a1.model, a2.model))
        print("%15s | %15s"  % (a1.engine_type, a2.engine_type))
        if(a1.__class__.__name__ == "Hybrid" and a2.__class__.__name__ == "Hybrid"):
            print("%15s | %15s" % (a1.acu_cap, a2.acu_cap))
        elif(a1.__class__.__name__ == "Hybrid"):
            print("%15s | %15s" % (a1.acu_cap, "b/d"))
        elif (a2.__class__.__name__ == "Hybrid"):
            print("%15s | %15s" % ("b/d", a2.acu_cap))



### obiekt klasy aUTO
a = Auto("VW PASSAT","TDI 2.0")
print(a)
#obiekt klasy Hybrid
h = Hybrid("Toyota Prius", "H 2.5", "1200Ah")
#dostep do składowych klas
h.model = "Toyota Avensis"
print(h)
ac = AutoComparator()
ac.compareAutos(a,a)
ac.compareAutos(h,h)
ac.compareAutos(a,h)
ac.compareAutos(h,a)
print(a.__class__.__name__)
print(h.__class__.__name__)
