from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
name = raw_input("Enter the name you want to send msg")
msg = raw_input("Enter the message you want to send")
count = int(input("Enter the number of count"))

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
msg_box = driver.find_element_by_class_name("_3u328")

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name("_3M-N-")
    button.click()
