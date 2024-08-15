import pandas as pd

def solution(arr1, arr2):
    df1 = pd.DataFrame(arr1)
    df2 = pd.DataFrame(arr2)
    
    result = df1.dot(df2)
    
    return result.values.tolist()