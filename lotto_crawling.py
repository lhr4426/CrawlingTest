import numpy as np
import pandas as pd
import math
import random
import matplotlib.pyplot as plt
from collections import Counter

df = pd.read_csv('lotto_numbers.csv',index_col=0)

col_names = [i for i in df.columns]

lotto_all_number =  [i for i in range(1, 46)]
counting_numbers = [0 for i in range(45)]

for i in col_names :
    for j in range(1,46) :
        counting_numbers[j-1] += Counter(df[i])[j]

lotto_data = np.column_stack((lotto_all_number, counting_numbers))

counting_mean = math.floor(np.mean(counting_numbers))

lotto_data = sorted(lotto_data, key=lambda x:-x[1])

print("평균 : ", counting_mean)
print("가장 많이 나온 숫자 : ", lotto_data[0][0])
print("가장 적게 나온 숫자 : ", lotto_data[44][0])

upper_percent = math.floor(np.percentile(counting_numbers, 80))

for i in range(7) :
    print(lotto_data[i][0], end=' ')

plt.plot([i for i in range(1, 46)],counting_numbers)
plt.axis([1,45,100,200])
plt.show()

print("\n추천 리스트 : ")

reco_list = []

for i in range(len(lotto_data)) :
    if lotto_data[i][1] >=  upper_percent:
        reco_list.append(lotto_data[i][0])

reco_list.sort()

print(reco_list)






