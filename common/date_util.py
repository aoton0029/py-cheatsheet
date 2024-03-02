from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
import numpy as np
import pandas as pd
from enum import Enum

class DateTimeFormat(Enum):
    DATE = '%Y-%m-%d'
    TIME = '%H:%M:%S'
    DATE_TIME = '%Y-%m-%d %H:%M:%S'
    SLASH_DATE = '%Y/%m/%d'
    NUMBER_FORMAT = '%Y%m%d'

class DateUtil:
    @staticmethod
    def get_current_date():
        return datetime.now().strftime('%Y-%m-%d')

    @staticmethod
    def get_current_time():
        return datetime.now().strftime('%H:%M:%S')

    @staticmethod
    def get_current_date_time():
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    @staticmethod
    def get_date_time_str(dt:datetime, format):
        """日付を指定フォーマットの文字列に変換する"""
        if isinstance(format, DateTimeFormat):
            format = format.value
        return dt.strftime(format)

    @staticmethod
    def today():
        now =  datetime.now()
        return datetime(now.year, now.month, now.day)
    
    @staticmethod
    def business_day_diff(start_date:datetime, end_date:datetime, holidays=[]):
        """営業日数を計算する"""
        business_days = np.busday_count(start_date, end_date, holidays=holidays)
        return business_days
    
    @staticmethod
    def business_day_add(start_date:datetime, days:int, holidays=[]):
        """営業日を加算する"""
        end_date = start_date + np.busday_offset(days, roll='forward', holidays=holidays)
        return end_date
    
    @staticmethod
    def business_day_sub(start_date:datetime, days:int, holidays=[]):
        """営業日を減算する"""
        end_date = start_date - np.busday_offset(days, roll='backward', holidays=holidays)
        return end_date
    
    @staticmethod
    def holiday_list(start_date:date, end_date:date, holidays=[]):
        """指定期間の祝日のリストを返す"""
        return np.busdaycalendar(start_date, end_date, holidays=holidays).holidays
    
    @staticmethod
    def add_to_date(d: datetime, years=0, months=0, days=0, hours=0, minutes=0, seconds=0, microseconds=0):
        return d + relativedelta(years=years, months=months, days=days, hours=hours, minutes=minutes, seconds=seconds, microseconds=microseconds)