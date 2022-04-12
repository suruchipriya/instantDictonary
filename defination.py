import pandas

class Definition:

    def __init__(self, tern):
      self.tern = tern
    
    def get(self):
        df = pandas.read_csv("data.csv")
        return tuple(df.loc[df['word']==self.tern]['definition'])

d = Definition(tern= "sum")
print(d.get())
