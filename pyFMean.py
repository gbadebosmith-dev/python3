import statistics as st

varMean = [30, 50, 90]
varWeight = [80, 10, 10]

class Cl_FMean:
    def __init__(self, varMean, varWeight):
        self.varMean = varMean
        self.varWeight = varWeight

    def fn_FMean_None(self):
        return st.fmean(varMean,None)

    def fn_FMean_Weighted(self):
        return st.fmean(varMean, varWeight)

varCL_FMean_With_No_Weights = Cl_FMean(varMean, varWeight)
varCL_FMean_With_Weights = Cl_FMean(varMean, varWeight)

print("Not Weighted Average")
print(varCL_FMean_With_No_Weights.fn_FMean_None())
print("")
print("Weighted Average")
print(varCL_FMean_With_Weights.fn_FMean_Weighted())