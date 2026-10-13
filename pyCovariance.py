import statistics as st

varArray1 = [1,2,3,4,5,6,7,8,9,10]
varArray2 = [10,9,8,7,6,5,4,3,2,1]

class clCovariance:
    def __init__(self, varArray1, varArray2):
        self.varArray1 = varArray1
        self.varArray2 = varArray2

    def fnCovariance(self):
        return st.covariance(varArray1, varArray2)

varCovariance = clCovariance(varArray1, varArray2)

print(varCovariance.fnCovariance())