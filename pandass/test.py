import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

from common import PandasUtil


sizes = [1000*i for i in range(1, 10)]
times = []

def take_time_dataframe(df:pd.DataFrame):
    # 時間がかかる処理
    df['dt'] = df['datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')

for size in sizes:
    df = PandasUtil.create_sample_df(size, {'int': 'int', 'float': 'float', 'str': 'str', 'datetime': 'datetime', 'bool': 'bool'})
    print(df.info())
    start_time = time.time()
    take_time_dataframe(df)
    end_time = time.time()
    times.append(end_time - start_time)

plt.plot(sizes, times, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Size of DataFrame')
plt.ylabel('Time to create DataFrame (seconds)')
plt.show()