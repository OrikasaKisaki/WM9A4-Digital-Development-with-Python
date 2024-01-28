"""
Date Scheduler Function

Objective:
Write a function named 'date_passed' to determine the relationship between two dates.

Function Parameters:
1. todays_date (string): The current date in the format 'day Month'.
2. scheduled_date (string): The scheduled date to compare, in the same format.

Instructions:
- The function should compare todays_date and scheduled_date and print whether the scheduled date has passed, is yet to pass, or is today.
- Assume the dates are in the same year.
- The dates are in a format like '26th March'. Consider how to convert these for comparison.
- https://www.w3schools.com/python/python_datetime.asp

Example Test Cases:
1. date_passed('26th March', '25th March') should indicate that the scheduled date has passed.
2. date_passed('26th March', '26th March') should indicate that the scheduled date is today.
3. date_passed('26th March', '27th March') should indicate that the scheduled date is yet to pass.
"""


#导入 datetime 模块
from datetime import datetime
#定义了一个函数 date_passed，它接受两个参数：todays_date（当前日期）和 scheduled_date（预定日期）
def date_passed(todays_date, scheduled_date):
    # Your code goes here
    # Implement the logic to compare the dates and print the appropriate message


    # Function to convert date string into a format suitable for datetime
    #convert_date 负责将日期字符串转换成 datetime 
    def convert_date(date_str):


        # Split the string into day and month
        #date_str.split()：将日期字符串分割成两部分，分别是日期和月份
        day, month = date_str.split()


        # Remove ordinal suffix from day (like 'th', 'rd', 'nd', 'st')
        #''.join(filter(str.isdigit, day))：从日期部分移除任何非数字字符（比如 "th", "rd", "nd", "st"），只保留数字。
        day = ''.join(filter(str.isdigit, day))


        # Return the formatted date string
        #return f"{day} {month}"：返回格式化后的字符串，仅包含日期和月份。
        return f"{day} {month}"

    # Converting the strings to datetime objects for comparison
    #datetime.strptime() 方法将字符串转换为 datetime 对象。

    #convert_date(todays_date) 和 convert_date(scheduled_date) 分别处理两个日期字符串，将它们转换成适合 strptime 方法的格式。
    #"%d %B" 是日期格式，其中 %d 表示日，%B 表示月份的全名
    todays_date = datetime.strptime(convert_date(todays_date), "%d %B")
    scheduled_date = datetime.strptime(convert_date(scheduled_date), "%d %B")


    #这部分代码比较 todays_date 和 scheduled_date。
    # Comparing the dates and printing the result
    if todays_date > scheduled_date:
        print("The scheduled date has passed.")
    elif todays_date < scheduled_date:
        print("The scheduled date is yet to pass.")
    else:
        print("The scheduled date is today.")






# Test cases
date_passed("26th March", "25th March")  # Expected: Scheduled date has passed
date_passed("26th March", "26th March")  # Expected: Scheduled date is today
date_passed("26th March", "27th March")  # Expected: Scheduled date is yet to pass

