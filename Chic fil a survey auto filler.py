from selenium import webdriver
import tkinter as tk
import time

#window = tk.Tk()
#label = tk.Label(text="enter the first 7 numbers of code")
#code1 = tk.Entry()
code1 = input("enter the first 7 numbers of code ")
code2 = input("enter the next 5 numbers of code ")
code3 = input("enter the next 4 numbers of code ")
code4 = input("enter the next 4 numbers of code ")
code5 = input("enter the last 2 numbers of code ")


web = webdriver.Chrome()
web.get('https://www.mycfavisit.com/')

time.sleep(2)

#lastName = input("")
firstName = "Justin"
lastName = "Tornetta"



#code1 = 1234567
#code2 = 12345
#code3 = 1234
#code4 = 1234
#code5 = 12

firstEl = web.find_element_by_class_name('coupon-length-7')
secondEl = web.find_element_by_class_name('coupon-length-5')
thirdEl = web.find_element_by_class_name('coupon-length-4')
fourthEl = web.find_element_by_class_name('coupon-length-4')
fifthEl = web.find_element_by_class_name('coupon-length-2')

firstEl.send_keys(code1)
secondEl.send_keys(code2)
thirdEl.send_keys(code3)
fourthEl.send_keys(code4)
fifthEl.send_keys(code5)

enter = web.find_element('submit')
enter.click()
enter.click()