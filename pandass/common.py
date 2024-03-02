from typing import Dict
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
        return df.merge(df, left_on=left_on, right_on=right_on, how=how)

    @staticmethod
    def parent_child_relation_dict(df: pd.DataFrame, parent_col, child_col):
        """階層構造の親子関係を辞書型で返す"""
        def hierarchy_dict(parent_child_dict, node):
            if not parent_child_dict[node]:
                return node
            return {node: [hierarchy_dict(parent_child_dict, child) for child in parent_child_dict[node]]}
        
        parent_child_dict = defaultdict(list)
        for _, row in df.iterrows():
            parent_child_dict[row[parent_col]].append(row[child_col])
        parent_nodes = list(parent_child_dict.keys())
        dic_h = {parent: hierarchy_dict(parent_child_dict, parent) for parent in parent_nodes}
        return dic_h

    @staticmethod
    def print_all(df, max_rows=999, max_colwidth=200):
        with pd.option_context('display.max_rows', max_rows, 'display.max_colwidth', max_colwidth):
            print(df)

    @staticmethod
    def datetime_to_str(df, date_col):
        df[date_col] = df[date_col].dt.strftime('%Y-%m-%d')
        return df
    
    @staticmethod
    def str_to_datetime(df, date_col):
        df[date_col] = pd.to_datetime(df[date_col])
        return df
    
