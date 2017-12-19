from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("C:/Users/ramir/Desktop/chromedriver.exe")
browser.get("https://web.whatsapp.com/")
time.sleep(5)

def comando(cmd, full):
    if(cmd == "!say"):
        return full.replace(cmd, "", 1)

    return ""

try:
    browser.find_element_by_class_name("chat-title")
except Exception as e:
    input("Esperando iniciar sesión en whatsapp... Enter para continuar")

indice = browser.execute_script('chat = document.getElementsByClassName("chat-title");'+
                                'for(var i = 0 ; i < chat.length ; ++i){if(chat[i].innerText == "Ingeniería en Sistemas")return i}')

grupo = browser.find_elements_by_css_selector("._2wP_Y")

grupo[indice].click()

while (1):
    try:
        msg_content = browser.execute_script('var el = document.getElementsByClassName("msg"); return el[el.length-1].getElementsByClassName("selectable-text")[0].innerText')
        print("Ultimo mensaje: "+msg_content)
        msg = browser.find_elements_by_css_selector(".msg")
        if(msg[browser.execute_script('return document.getElementsByClassName("msg").length-1;')].get_attribute("id") != "1" and msg_content[0]=="!"):
            browser.execute_script('var el = document.getElementsByClassName("msg"); el[el.length-1].id = 1')
            split = msg_content.split(" ")
            output = comando(split[0], msg_content)
            chat = browser.find_element_by_class_name("pluggable-input-body")
            chat.click()
            chat.send_keys(output)
            btn = browser.find_element_by_class_name("compose-btn-send")
            btn.click()
        time.sleep(1)
    except Exception as e:
        print(e)
