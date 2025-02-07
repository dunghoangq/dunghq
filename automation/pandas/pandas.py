import pandas as pd
import numpy as np

numbers = np.random.randint(1_000_000_000, 9_999_999_999, size=100)
numbers.tofile('phone_numbers.txt', sep='\n')

df = pd.DataFrame(numbers, columns=['phone_number'])

df = df
print(df)