
class ModuladorBPSK:
    
    def __init__(self):
        pass

    def modula(self, bloco):
        out = []
        for bit in bloco:
            if bit==0:
                out.append(-1)
            else:
                out.append(1)
        return out[:]