class DataFrame:
    def __init__(self, data):
        self.data = data
        self.loc = LocIndexer(self)
        self.iloc = iLocIndexer(self)

class LocIndexer:
    def __init__(self, df):
        self.df = df
    def __getitem__(self, key):
        # label-based logic here
        pass

class iLocIndexer:
    def __init__(self, df):
        self.df = df
    def __getitem__(self, key):
        # position-based logic here
        pass