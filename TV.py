# Lovisa Colérus
# 2015

class TV(object):
#skapar ett TV-objekt
    def __init__(self, namn, kanal, volym):
        self.namn = namn
        self.kanal = kanal
        self.volym = int(volym)
        
#returnerar infon utskriven på ett snygge sätt
    def __str__(self):
        return ' %s \n %s \n %s \n' % (self.namn, self.kanal, self.volym)
       
#byter kanal till den kanalen användaren valt    
    def byt_kanal(TV, ny_kanal, kanaler):
        if ny_kanal < len(kanaler):
            TV.kanal = kanaler[ny_kanal-1]
            
            return True
        return False
#sänker volymen med 1     
    def sank_volym(TV):
        if TV.volym > 0:
            TV.volym = TV.volym-1

#höjer volymen med 1        
    def hoj_volym(TV):
        if TV.volym < 10:
            TV.volym = TV.volym+1
