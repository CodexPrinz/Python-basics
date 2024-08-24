import pandas as pd
print("\n------------> Reading csv Pandas <----------------")
content = pd.read_csv('output.csv')

print(content)

print("\n------------> Writing csv Pandas <----------------")
data = pd.DataFrame([['Pele', 'Brazil'], ['Diego', 'Argentina'], ['Baggio', 'Italy']], columns=['player', 'team'])
data.to_csv('output_pandas.csv', index=False)