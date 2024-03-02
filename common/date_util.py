from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
import numpy as np
import pandas as pd

# DateUtil class
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
    def get_date_time(format):
        return datetime.now().strftime(format)
    
    @staticmethod
    def business_day_diff(start_date, end_date, holidays=[]):
        """営業日数を計算する"""
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        business_days = np.busday_count(start_date, end_date, holidays=holidays)
        return business_days
    
    @staticmethod
    def business_day_add(start_date, days, holidays=[]):
        start_date = pd.to_datetime(start_date)
        end_date = start_date + np.busday_offset(days, roll='forward', holidays=holidays)
        return end_date
