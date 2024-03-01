import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

def create_dataframe(size, schema):
    data = {}
    for column, dtype in schema.items():
        if dtype == 'int':
            data[column] = np.random.randint(0, 100, size=size)
        elif dtype == 'float':
            data[column] = np.random.random(size=size)
        elif dtype == 'str':
            data[column] = np.random.choice(['a', 'b', 'c', 'd', 'e'], size=size)
        elif dtype == 'datetime':
            data[column] = pd.date_range('2020-01-01', periods=size)
        elif dtype == 'bool':
            data[column] = np.random.choice([True, False], size=size)
    return pd.DataFrame(data)

sizes = [10000*i for i in range(1, 10)]
times = []

def take_time_dataframe(df):
    # 時間がかかる処理
    df['waste'] = df['int'] + df['float']

for size in sizes:
    df = create_dataframe(size, {'int': 'int', 'float': 'float', 'str': 'str', 'datetime': 'datetime', 'bool': 'bool'})
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