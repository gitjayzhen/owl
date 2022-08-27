# -*- coding:UTF-8 -*-

'''
Created on 2016年4月28日

@author: jayzhen
'''
import time
import datetime
import calendar


def get_current_date_time():
    """
    * 获取系统当前日期和时间并格式化为yyyyMMddHHmmss即类似20110810155638格式
    * @param 无
    * @return 系统当前日期和时间并格式化为yyyyMMddHHmmss即类似20110810155638格式
    """
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")


def get_date_time():
    """
     * 获取系统当前日期和时间并格式化为yyyyMMddHHmmssSSS即类似20130526002728796格式
     * @param 无
     * @return 系统当前日期和时间并格式化为yyyyMMddHHmmssSSS即类似20130526002728796格式
    """
    return datetime.datetime.now()


def get_current_date():
    """
     * 获取系统当前日期并格式化为yyyyMMdd即类似20110810格式
     * @param 无
     * @return 系统当前日期并格式化为yyyyMMdd即类似20110810格式
     """
    return datetime.datetime.now().strftime("%Y%m%d")


def get_current_time():
    """
     * 获取系统当前时间并格式化为HHmmss即类似155638格式
     * @param 无
     * @return 系统当前时间并格式化为HHmmss即类似155638格式
     """
    return datetime.datetime.now().strftime("%H%M%S")


def get_time():
    """
     * 获取系统当前时间并格式化为HHmmssSSS即类似155039527格式
     * @param 无
     * @return 系统当前时间并格式化为HHmmssSSS即类似155039527格式
    """
    return datetime.datetime.now().strftime("%H%M%S%f")


def get_formate_time(format_scheme):
    """
    * 根据自定义格式化获取系统当前时间
    * @param format: 时间格式化如yyyy-MM-dd HH:mm:ss:SSS  "%Y%m%d%H%M%S%f"
    * @return 根据自定义格式化返回系统当前时间
    """
    return datetime.datetime.now().strftime(format_scheme)


def add_days_by_formatter(adddays,dateFormat):
    """
     * get specified time string in specified date format.
     * @param days
     *            days after or before current date, use + and - to add.
     * @param dateFormat
     *            the formatter of date, such as:yyyy-MM-dd HH:mm:ss:SSS.
     """
    afteraddtime = datetime.datetime.now() + datetime.timedelta(days=adddays)     
    return time.strftime(afteraddtime,dateFormat)


def add_months_by_formatter(months, date_format):
    """
     * get specified time string in specified date format.
     * @param months： months after or before current date, use + and - to add.
     * @param dateFormat：the formatter of date, such as:yyyy-MM-dd HH:mm:ss:SSS.
     """
    d = datetime.datetime.now()
    c = calendar.Calendar()
    year = d.year
    month = d.month
    today = d.day
    if month+months > 12:
        month = months
        year += 1
    else :
        month += months
    days = calendar.monthrange(year, month)[1]  
    
    if today > days:
        afteraddday = days
    else:
        afteraddday = today
    return datetime.datetime(year,month,afteraddday).strftime(date_format)


def add_years_by_formatter(years, dateFormat):
    """
     * get specified time string in specified date format.
     * @param years：years after or before current date, use + and - to add.
     * @param dateFormat：the formatter of date, such as:yyyy-MM-dd HH:mm:ss:SSS.
     """
    d = datetime.datetime.now()
    c = calendar.Calendar()
    year = d.year + years
    month = d.month
    today = d.day
    
    days = calendar.monthrange(year, month)[1]  
    
    if today > days:
        afterday = days
    else:
        afterday = today
    return datetime.datetime(year,month,afterday).strftime(dateFormat)


def first_day_of_next_month(dateFormat):
    """
    * get first day of next month in specified date format.
    * @param dateFormat： the formatter of date, such as:yyyy-MM-dd HH:mm:ss:SSS.
    """
    d = datetime.datetime.now()
    year = d.year
    month = d.month
    if month+1 > 12 :
        month = 1
        year += 1
    else :
        month += 1
    
    return datetime.datetime(year,month,1).strftime(dateFormat)


def first_day_of_month(year, month, dateFormat):
    """
     * get first day of specified month and specified year in specified date
     * format.
     * @param year: the year of the date.
     * @param month:the month of the date.
     * @param dateFormat:the formatter of date, such as:yyyy-MM-dd HH:mm:ss:SSS.
    """
    return datetime.datetime(year, month, 1).strftime(dateFormat)


def first_day_of_month_this_year(month, dateFormat):
    """
      get first day of specified month of current year in specified dateformat.
      @param month:the month of the date.
      @param dateFormat:the formatter of date, such as:yyyy-MM-dd HH:mm:ss:SSS.
        """
    d = datetime.datetime.now()
    year = d.year
    return datetime.datetime(year, month, 1).strftime(dateFormat)


def getMilSecNow():
    """
    get the system current milliseconds.
    """
    return time.time()


