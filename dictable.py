class Dictable:
    def dict(self):
        members = [attr for attr in list(set(dir(self))-set(dir(self.__class__)))
                   if not callable(attr) and not attr.startswith("_")]
        members.sort()
        d = {}
        for m in members:
            v = getattr(self, m)
            if isinstance(v, Dictable):
                d[m] = v.dict()
            elif "__dict__" in dir(v):
                d[m] = v.__dict__
            else:
                d[m] = v
        return d
