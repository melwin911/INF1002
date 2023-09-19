import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Read the CSV file
df = pd.read_csv("data.csv")

# View the first 5 rows
# print(df.head())

# Horizontal bar graph showing count of 'town'
# sns.countplot(y='town', data = df)
# plt.show()