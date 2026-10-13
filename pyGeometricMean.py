import statistics as st

varlawOfAveragesWinnings = [1000, 2000, 3000, 1000]

class clMean:
    def __init__(self, varLawOfAveragesWinnings):
        self.varLawOfAveragesWinnings = varLawOfAveragesWinnings
    def fnFMean(self):
        return st.fmean(varlawOfAveragesWinnings)
    def fnGeometricMean(self):
        return st.geometric_mean(varlawOfAveragesWinnings)

clMethodMean = clMean(varlawOfAveragesWinnings)

print("Floating Mean")
print(clMethodMean.fnFMean())
print("Geometric Mean")
print(clMethodMean.fnGeometricMean())