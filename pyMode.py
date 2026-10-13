import statistics as st

modeArray = [1,2,3,2,3,2,5,2,6,2]

def fnMode(modeArray):
    return st.mode(modeArray)

print(fnMode(modeArray))

