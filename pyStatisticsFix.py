# This code holds all 19 statistics functions with the criteria instrcuted that claude low could not do by me.
import statistics as st

varList = [1,2,3,4,4,4,5,6,7,8,9,4]
varList2 = [1,2,3,4,4,4,5,7,7,8,8,4]
varInteger = 2

class cl_Stats:
    def __init__(self, varList, varList2, varInteger):
        self.varList = varList
        self.varList2 = varList2
        self.varInteger = varInteger

    def fn_correlation(self):
        return st.correlation(varList, varList2)

    def fn_covariance(self):
        return st.covariance(varList, varList2)

    def fn_fast_mean(self):
        return st.fmean(varList)

    def fn_geometric_mean(self):
        return st.geometric_mean(varList)

    def fn_harmonic_mean(self):
        return st.harmonic_mean(varList, varList2)

    def fn_kde(self):
        varkde = st.kde(varList, varInteger)
        return varkde(varInteger)

    def fn_linear_regression(self):
        return st.linear_regression(varList, varList2)

    def fn_mean(self):
        return st.mean(varList)

    def fn_median(self):
        return st.median(varList)

    def fn_median_grouped(self):
        return st.median_grouped(varList, varInteger)

    def fn_median_high(self):
        return st.median_high(varList)

    def fn_median_low(self):
        return st.median_low(varList)

    def fn_mode(self):
        return st.mode(varList)

    def fn_multi_mode(self):
        return st.multimode(varList)

    def fn_pstdev(self):
        return st.pstdev(varList)

    def fn_pvariance(self):
        return st.pvariance(varList)

    def fn_quantiles(self):
        return st.quantiles(varList)

    def fn_stdev(self):
        return st.stdev(varList)

    def fn_variance(self):
        return st.variance(varList)

cl_functions = cl_Stats(varList, varList2, varList)

print(cl_functions.fn_correlation())
print(cl_functions.fn_covariance())
print(cl_functions.fn_fast_mean())
print(cl_functions.fn_geometric_mean())
print(cl_functions.fn_harmonic_mean())
print(cl_functions.fn_kde())
print(cl_functions.fn_linear_regression())
print(cl_functions.fn_mean())
print(cl_functions.fn_median())
print(cl_functions.fn_median_high())
print(cl_functions.fn_median_low())
print(cl_functions.fn_median_grouped())
print(cl_functions.fn_mode())
print(cl_functions.fn_multi_mode())
print(cl_functions.fn_pstdev())
print(cl_functions.fn_pvariance())
print(cl_functions.fn_quantiles())
print(cl_functions.fn_stdev())
print(cl_functions.fn_variance())
