import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Read the CSV file
df = pd.read_csv("sorted_output.csv")

# View the first 5 rows
# print(df.head())

# Bar graph showing count of 'town'
# sns.countplot(x='town', data = df)
# plt.xticks(rotation=90)
# plt.show()

# Bar graph showing count of 'flat_type'
# sns.countplot(x='flat_type', data = df)
# plt.xticks(rotation=90)
# plt.show()

# Bar graph showing count of 'flat_model'
# sns.countplot(x='flat_model', data = df)
# plt.xticks(rotation=90)
# plt.show()