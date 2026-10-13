import statistics as st

corrArray1 = [1,2,3,4,5,6,7,8,9,10]
corrArray2 = [1,3,3,4,4,6,5,8,7,11]

# define the class object
class PearsonCorrelation:
    def __init__(self, corrArray1, corrArray2):
        self.corrArray1 = corrArray1
        self.corrArray2 = corrArray2

    def fxPearson(self):
        return st.correlation(self.corrArray1, self.corrArray2)

# return function from class object
clPearson = PearsonCorrelation(corrArray1, corrArray2)
print(clPearson.fxPearson())

# define the class object
class SpearmanCorrelation:
    def __init__(self, correlationArray1, correlationArray2):
        self.correlationArray1 = correlationArray1
        self.correlationArray2 = correlationArray2

    def fxSpearman(self):
        return st.correlation(self.correlationArray1, self.correlationArray2, method="ranked")

# return function from class object
clSpearman = SpearmanCorrelation(corrArray1, corrArray2)
print(clSpearman.fxSpearman())



