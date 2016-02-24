class ListMatchException (Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self, value):
        return repr(self.value)



class ProgParam:
    _types = []
    _values = []
    
    def __init__(self, types = [], vallist = [], valstring = ""):
        if types == []:
            self._types = []
            self._values = []
        else:
            self._types = types
            if len(vallist) == 0:
                if len(valstring) == 0:
                    self._values = []
                else:
                    self._values = self.getTypedValues(valstring)
            elif len(vallist) != len(self._types):
                raise ListMatchException("The vallist size must match type list size!") 

    def getTypedValues(self, valstring, delim = ';'):
        if len(self._types) == 0:
            return []

        vlist = valstring.split(delim)
        if (valstring[-1] == delim):
            vlist = vlist[:-1]
        if len(vlist) != len(self._types):
            raise ListMatchException("The vallist size must match type list size!")

        for idx, typ in self._types:
            vlist[idx] = conv_to_type(vlist[idx], typ)
        return vlist
