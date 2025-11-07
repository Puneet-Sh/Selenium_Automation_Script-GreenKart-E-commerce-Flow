from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.implicitly_wait(2)

expectedLst=['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")

time.sleep(2)


prods = driver.find_elements(By.XPATH,"//div[@class='products']/div") # implicitwait fails here because if we won't wait for 2 seconds list is empty and selenium will take it to next code

prods_names = driver.find_elements(By.XPATH,"//h4[@class='product-name']")

count = len(prods)
assert count>0

names_lst=[]
for prod_name in prods_names :
    names_lst.append(prod_name.text.strip())

# print(names_lst)
assert names_lst == expectedLst

for prod in prods :
    prod.find_element(By.XPATH,"div/button").click()

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()

driver.find_element(By.XPATH,"//div[@class='action-block']/button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

# explicit wait 
e_wait = WebDriverWait(driver,10)
e_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))

promo_succ = driver.find_element(By.CLASS_NAME,"promoInfo").text

print(promo_succ)

time.sleep(2)
amts = driver.find_elements(By.XPATH,"//td[5]/p[@class='amount']")

# print(len(amts))

sum=0
for amt in amts:
    sum+=int(amt.text.strip())


t_amt = int(driver.find_element(By.CSS_SELECTOR,'.totAmt').text)

# print(sum, t_amt)

assert sum == t_amt

disct_amt = float(driver.find_element(By.CLASS_NAME,"discountAmt").text)

# print(t_amt, disct_amt)

assert t_amt>disct_amt



