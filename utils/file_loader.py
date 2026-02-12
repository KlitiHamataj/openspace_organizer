import pandas as pd



def load_colleagues(filepath = 'data/colleagues.xlsx'):
    df = pd.read_excel(filepath)
    names = df['Name'].tolist()
    return names
print(load_colleagues())