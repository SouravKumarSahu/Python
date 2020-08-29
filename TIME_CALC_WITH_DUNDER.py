#Example of magic methods / dunder with custom time class#

class Time():
    def __init__(self,HH,MM,SS):
        self.HH, self.MM, self.SS = 00, 00, 00
        try:
            self.HH, self.MM, self.SS = abs(HH), abs(MM), abs(SS)
            if 0 <= HH < 24 and 0 <= MM < 60 and 0 <= SS < 60 \
            and isinstance(HH,int) and isinstance(MM,int) and isinstance(SS,int):
                pass
            else:
                raise TypeError()
        except:
            print("Format error", HH, MM, SS)
            
    def __str__(self):
        return "%02d"%self.HH + ":" + "%02d"%self.MM + ":" + "%02d"%self.SS
        
    def time2secs(self):
        secs = self.SS + (self.MM + (self.HH * 60) ) * 60
        return secs
    
    def secs2time(self, secs):
        ss = secs % (24 * 3600) #excess days eliminated
        hh = ss // 3600         #hours calculated on remaining seconds
        ss %= 3600              #excess minutes eliminated
        mm = ss // 60           #minutes calculated on remaining seconds
        ss %= 60                #excess seconds eliminated
        return Time(hh,mm,ss)
    
    def __add__(self,other):
        if isinstance(other,Time):
            return self.secs2time( self.time2secs() + other.time2secs() )
        elif isinstance(other,int):
            return self.secs2time( self.time2secs() + other )
        else:
            raise ValueError()
    
    def __sub__(self,other):
        if isinstance(other,Time):
            return self.secs2time( self.time2secs() - other.time2secs() )
        elif isinstance(other,int):
            return self.secs2time( self.time2secs() - other )
        else:
            raise ValueError()
    
    def __mul__(self,num):
        return self.secs2time(self.time2secs() * 2)

try:
    fti = Time(21,58,50)
    sti = Time(1,45,22)
    assert fti.__str__() == "21:58:50"
    assert sti.__str__() == "01:45:22"
    assert (fti + sti).__str__() == "23:44:12"
    assert (fti - sti).__str__() == "20:13:28"
    assert (fti * 2).__str__() == "19:57:40"
    
    tti = Time(21,58,50)
    assert tti.__str__() == "21:58:50"
    assert (tti + 62).__str__() == "21:59:52"
    assert (tti - 62).__str__() == "21:57:48"
    
except:
    print("test failed")
else:
    print("test passed \n")
    print(fti)
    print(sti)
    print(fti + sti)
    print(fti - sti)
    print(fti * 2)
    print()
    print(tti)
    print(tti + 62)
    print(tti - 62)