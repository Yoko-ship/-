import google.generativeai as genai
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import tkinter as tk
import time

api_key = "AIzaSyCrj3saz9DtSmuesXjHKLR7HIAxRJD3RrY"
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
user_input = ""
def get_present():
    global user_input
    user_input = entry.get()
    if len(user_input) >= 3:
        root.destroy()
        error_label.forget()
    elif len(user_input) < 3:
        warning_label.pack(pady=5)
        user_input = None
        error_label.forget()

    else:
        error_label.pack()
        user_input = None

root = tk.Tk()
root.geometry("400x400")
root.title("Presentation")
root.configure(bg="#f0f0f0")  


label = tk.Label(root, text="Тема презентации", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
label.pack(pady=20) 

entry = tk.Entry(root, font=("Helvetica", 14), width=30, bd=2, relief="solid")
entry.pack(pady=10)  
error_label = tk.Label(root, text="Пожалуйста, напишите тему", fg="red", bg="#f0f0f0", font=("Helvetica", 10))
error_label.pack(pady=5)
warning_label = tk.Label(root,text="Ваш текст должен содержать как минимум 3 символов",fg="yellow",bg="black",font=("Helvetica",10))

button = tk.Button(root, text="Подтвердить", fg="white", bg="#28a745", font=("Helvetica", 12), command=get_present)
button.pack(pady=15)
button.config(cursor="hand2")

root.mainloop()

if user_input:
    driver = webdriver.ChromiumEdge()
    driver.get("https://slidesgo.com/")
    elem = driver.find_element(By.ID,"ai-animated")
    elem.click()
    input_element = driver.find_element(By.NAME,"topic")
    select_tone = driver.find_element(By.CSS_SELECTOR,"select")
    select_opt = Select(select_tone)
    select_opt.select_by_value("Formal")
    select_language = driver.find_element(By.CSS_SELECTOR,".flex-1 select")
    select = Select(select_language)
    select.select_by_value("ru")
    input_number = driver.find_element(By.NAME,"slides")
    input_number.clear()
    input_number.send_keys(14)
    input_element.send_keys(user_input)
    input_element.send_keys(Keys.RETURN)
    signing_up = driver.find_element(By.CSS_SELECTOR,".have-account a")
    signing_up.click()
    google_continue = driver.find_element(By.CSS_SELECTOR,".continue-with button:nth-of-type(2)")
    google_continue.click()
    input_auth = driver.find_element(By.CSS_SELECTOR,".label input")
    input_auth.send_keys(f"oxbdtin885@gmail.com")
    password_auth = driver.find_element(By.NAME,"password")
    password_auth.send_keys("23132asdagaasfk")
    time.sleep(2)
    password_auth.send_keys(Keys.RETURN)

    

