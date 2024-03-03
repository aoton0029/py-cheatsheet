from typing import Dict, List, Union
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
from collections import defaultdict, deque
from pprint import pprint


class PandasUtil:
    @staticmethod
    def create_sample_df(size:int, schema:dict):
        """

        Args:
            size (int): _description_
            schema (dict): _description_
                schema = {'int': 'int', 
                            'float': 'float', 
                            'str': 'str', 
                            'datetime': 'datetime', 
                            'bool': 'bool',
                            'id' : 'int'}
        Returns:
            _type_: _description_
        """
        data = {}
        for column, dtype in schema.items():
            if dtype == 'int':
                data[column] = np.random.randint(0, 100, size=size)
            elif dtype == 'float':
                data[column] = np.random.random(size=size)
            elif dtype == 'str':
                data[column] = np.random.choice(['A', 'B', 'C', 'D', 'E'], size=size)
            elif dtype == 'datetime':
                data[column] = pd.date_range('2020-01-01', periods=size)
            elif dtype == 'bool':
                data[column] = np.random.choice([True, False], size=size)
        return pd.DataFrame(data)

    @staticmethod
    def keep_latest_records(df1, df2, sort_col, subset_key_col):
        """最新のレコードを保持する

        Args:
            df1 (_type_): _description_
            df2 (_type_): _description_
            sort_col (_type_): 最新を残すためのソート列
            subset_col (_type_): キーになる列
        """
        df = pd.concat([df1, df2])
        df = df.sort_values(by=sort_col, ascending=False).drop_duplicates(subset=subset_key_col, keep='first')
        return df
    
    @staticmethod
    def filter_by_list(df:pd.DataFrame, column_name:str, filter_by=[], exclude=False):
        """フィルター

        Args:
            df (_type_): _description_
            column_name (_type_): _description_
            filter_by (list, optional): _description_. Defaults to [].
            exclude (bool, optional): _description_. Defaults to False.

        Returns:
            _type_: _description_
        """
        _filtered = df[column_name].isin(filter_by)
        return df[_filtered] if not exclude else df[~_filtered]
    
    @staticmethod
    def filter_by_range(df:pd.DataFrame, column_name:str, min_value=None, max_value=None, exclude=False):
        """範囲でフィルター"""
        if min_value is None:
            _filtered = (df[column_name] <= max_value)
        elif max_value is None:
            _filtered = (df[column_name] >= min_value)
        else:
            _filtered = (df[column_name] >= min_value) & (df[column_name] <= max_value)
        return df[_filtered] if not exclude else df[~_filtered]
    
    @staticmethod
    def filter_by_query(df:pd.DataFrame, query:str):
        """クエリでフィルター"""
        return df.query(query)

    @staticmethod
    def diff(df1:pd.DataFrame, df2:pd.DataFrame, left_on, right_on, which=None):
        """差集合
        - None : df1またはdf2のいずれか一方にのみ存在する行を返す
        - 'both': df1とdf2の両方に存在する行を返す
        - 'left_only': df1にのみ存在し、df2には存在しない行を返す
        - 'right_only': df2にのみ存在し、df1には存在しない行を返す
        
        Args:
            df1 (pd.DataFrame): _description_
            df2 (pd.DataFrame): _description_
            left_on (_type_): _description_
            right_on (_type_): _description_
            which (): 'both', 'left_only', 'right_only' , deafult is None

        Returns:
            _type_: _description_
        """
        merged = pd.merge(df1, df2, how='outer', left_on=left_on, right_on=right_on, indicator=True)
        if which is None:
            diff = merged[merged['_merge'] != 'both']
        else:
            diff = merged[merged['_merge'] == which]
        diff = diff.drop(columns=['_merge'])
        return diff

    @staticmethod
    def self_join(df: pd.DataFrame, left_on, right_on, how='inner'):
        """自己結合"""
        return df.merge(df, left_on=left_on, right_on=right_on, how=how)
    
    @staticmethod
    def create_id_dict(df:pd.DataFrame, parent_col:str, child_col:str, id_col:str):
        """idで親子関係"""
        parent_child_dict = df.set_index(child_col)[parent_col].to_dict()
        id_hierarchy_dict = {}
        for child, parent in parent_child_dict.items():
            child_id = df.loc[df[child_col] == child, id_col].values[0]
            if parent in df[child_col].values:
                parent_id = df.loc[df[child_col] == parent, id_col].values[0]
                id_hierarchy_dict[child_id] = parent_id
            else:
                id_hierarchy_dict[child_id] = None
        return id_hierarchy_dict
   
    @staticmethod
    def create_child_level_dict(df:pd.DataFrame, parent_col:str, child_col:str):
        """階層ごとに分割したdict"""
        df_copy = df.copy()
        df_copy['depth'] = 0
        # for index, row in df_copy.iterrows():
        #     current_parent = row[parent_col]
        #     depth = 0
        #     while current_parent in df_copy[child_col].values:
        #         current_parent = df_copy.loc[df_copy[child_col] == current_parent, parent_col].values[0]
        #         depth += 1
        #     df_copy.loc[index, 'depth'] = depth
        parent_child_dict = df.set_index(child_col)[parent_col].to_dict()
        df_copy['current_parent'] = df_copy[parent_col]
        while df_copy[df_copy['current_parent'].isin(df_copy[child_col])].shape[0] > 0:
            df_copy.loc[df_copy['current_parent'].isin(df_copy[child_col]), 'depth'] += 1
            df_copy['current_parent'] = df_copy['current_parent'].map(parent_child_dict)
        df_copy.drop(columns=['current_parent'], inplace=True)
        depth_dict = {depth: df for depth, df in df_copy.groupby('depth')}
        return depth_dict

    @staticmethod
    def print_all(df, max_rows=999, max_colwidth=200):
        with pd.option_context('display.max_rows', max_rows, 'display.max_colwidth', max_colwidth):
            print(df)

    @staticmethod
    def datetime_to_str(df, format='%Y-%m-%d', *args):
        for date_col in args:
            if not isinstance(df[date_col], pd.DatetimeIndex):
                df[date_col] = df[date_col].dt.strftime(format)
        return df
    
    @staticmethod
    def str_to_datetime(df, *args):
        for date_col in args:
            if not isinstance(df[date_col], pd.DatetimeIndex):
                df[date_col] = pd.to_datetime(df[date_col])
        return df
    
    @staticmethod
    def append_aggregated_row(df: pd.DataFrame, agg_dict: Dict[str, str]) -> pd.DataFrame:
        """
        Args:
            df (pd.DataFrame):
            agg_dict (Dict[str, str]): 
                'mean': 平均値
                'median': 中央値
                'min': 最小値
                'max': 最大値
                'std': 標準偏差
                'var': 分散
                'count': 非NAの要素数
                'nunique': ユニークな要素数
                'first': 最初の非NA要素
                'last': 最後の非NA要素
                'prod': 積
                'mad': 平均絶対偏差
            
        Example:
        ```
        agg_dict = {'A': 'sum', 'B': 'mean', 'C': 'max'}
        ```
        """
        agg_row = df.agg(agg_dict)
        return df.append(agg_row, ignore_index=True)

    @staticmethod
    def create_calender_table(df:pd.DataFrame, name_col:str, date_col:str, status_col:str, start_date=None, end_date=None):
        """工番ごとに日付ごとのステータスをカレンダー表にして返す

        Args:
            df (pd.DataFrame): _description_
            name_col (str): _description_
            date_col (str): _description_
            status_col (str): _description_
            start_date ([type], optional): _description_. Defaults to None.
            end_date ([type], optional): _description_. Defaults to None.
        
        """
        if not isinstance(df[date_col], pd.DatetimeIndex):
            df[date_col] = pd.to_datetime(df[date_col])
        if start_date is None:
            start_date = df[date_col].min()
        if end_date is None:
            end_date = df[date_col].max()
        all_dates = pd.date_range(start_date, end_date, freq='D')
        all_names = df[name_col].unique()
        df_full = pd.DataFrame(index=pd.MultiIndex.from_product([all_names, all_dates], names=[name_col, date_col]))
        df_full = df_full.merge(df, how='left', left_index=True, right_on=[name_col, date_col])
        df_pivot = df_full.pivot(index=name_col, columns=date_col, values=status_col)
        return df_pivot
    
    @staticmethod
    def add_id_column(df:pd.DataFrame):
        if 'id' not in df.columns:
            df['id'] = pd.RangeIndex(1, len(df) + 1, 1, dtype='int')
        return df

    @staticmethod
    def set_values_based_on_condition(df:pd.DataFrame, column_name:str, condition:Union[pd.Series, np.ndarray, List[bool]], true_val, false_val):
        """条件に基づいて値を設定する

        Args:
            df (pd.DataFrame): 
            column_name (str): 対象の列名
            condition (Union[pd.Series, np.ndarray, List[bool]]): 真偽のリスト
            true_val (_type_): 真の場合の値
            false_val (_type_): 偽の場合の値
        
        Example:
        ```
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
        condition = df['A'] > 3
        df = set_values_based_on_condition(df, 'A', condition, 100, 0)
        ```
        """
        df[column_name] = false_val
        df.loc[condition, column_name] = true_val
        #df[column_name] = np.where(condition, value1, value2)
        return df
    
    @staticmethod
    def group_and_sum(df:pd.DataFrame, group_column:str, sum_column:str):
        return df.groupby(group_column)[sum_column].sum()
  
    @staticmethod
    def get_memory_usage(df:pd.DataFrame):
        mem = df.memory_usage(deep=True).sum()
        return PandasUtil.format_bytes(mem)

    @staticmethod  
    def format_bytes(size):
        # 2**10 = 1024
        power = 2 ** 10
        n = 0
        power_labels = {0: " bytes", 1: "KB", 2: "MB", 3: "GB", 4: "TB"}
        while size >= power:
            size /= power
            n += 1
        return str(round(size, 2)) + power_labels[n]

    @staticmethod
    def run_function_in_parallel(func, t_split):
        from multiprocessing import Pool
        import psutil
        N_CORES = psutil.cpu_count()
        num_cores = np.min([N_CORES, len(t_split)])
        pool = Pool(num_cores)
        df = pd.concat(pool.map(func, t_split), axis=1)
        pool.close()
        pool.join()
        return df

# Create a DataFrame with parent-child relationships
df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6, 7,8],
    'child': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'parent': ['プロダクト', '棚', 'E', 'F', 'A', 'B', 'B', 'G']
})
