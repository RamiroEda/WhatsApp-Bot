from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import randint
bot_ext = "!"

print("Cargando las paginas necesarias...")
browser = webdriver.Chrome("C:/Users/ramir/Desktop/WhatsApp-Bot/WhatsApp-Bot/chromedriver.exe")
browser.get("https://web.whatsapp.com/")
search_browser = webdriver.Chrome("C:/Users/ramir/Desktop/WhatsApp-Bot/WhatsApp-Bot/chromedriver.exe")
time.sleep(1)
print("Se han cargado las páginas necesarias...")
def send_msg(output):
    chat = browser.find_element_by_class_name("pluggable-input-body")
    chat.click()
    chat.send_keys(output)
    btn = browser.find_element_by_class_name("compose-btn-send")
    btn.click()

def comando(cmd, cnt):
    if(cmd == bot_ext+"say"):
        return cnt
    elif(cmd==bot_ext+"card"):
        send_msg("Buscando...")
        search_browser.get("https://www.google.com.mx/search?q="+cnt.replace(" ","+"))

        if(search_browser.find_element_by_id("extabar").text != ""):
            res = search_browser.find_element_by_id("botabar")
            if(res.is_displayed()):
                try:
                    search_browser.execute_script('document.getElementById("botabar").getElementsByClassName("_tho")[0].innerText = ">";')
                except Exception as e:
                    print(e)
                search_browser.execute_script('for(var i = 0 ; i < document.getElementsByClassName("klzc").length; ++i){document.getElementsByClassName("klzc")[i].innerText = "~";} for(var i = 0 ; i < document.getElementsByClassName("_bgi").length; ++i){document.getElementsByClassName("_bgi")[i].innerText = "~";}')
                send_msg(res.text)
            else:
                try:
                    search_browser.execute_script('document.getElementsByClassName("kp-hc")[0].getElementsByClassName("_IWg _HWg _eXg mod")[0].innerText')
                    res = search_browser.find_element_by_class_name("kp-hc")
                    send_msg(res.text)
                except Exception as e:
                    res = search_browser.find_element_by_id("rhs_block")
                    if(res.text != ""):
                        txt = res.text.split("\n")
                        for t in txt:
                            if(not(t == "Otras personas también buscan" or
                                    t == "Canciones" or t == "También se buscó" or
                                    t == "Comentarios" or t == "Preguntas y respuestas" or
                                    t == "Opiniones")):
                                if(not(t == "Más imágenes")):
                                    send_msg(t)
                            else:
                                break
                    else:
                        return "No se encontraron resultados"

    elif(cmd==bot_ext+"dic"):
        send_msg("Buscando...")
        search_browser.get("https://www.google.com.mx/search?q="+cnt.replace(" ","+")+"+definicion")
        res = search_browser.find_elements_by_css_selector(".lr_dct_ent.vmod")
        if(res):
            return res[0].text
        else:
            return "No se encontraron resultados"
    elif(cmd==bot_ext+"search"):
        send_msg("Buscando...")
        search_browser.get("https://www.google.com.mx/search?q="+cnt.replace(" ","+"))
        for i in range(5):
            send_msg(search_browser.execute_script('return document.getElementsByClassName("r")['+str(i)+'].innerText + " en " + document.getElementsByClassName("r")['+str(i)+'].getElementsByTagName("a")[0].getAttribute("href");'))
    elif(cmd == bot_ext+"chiste"):
        send_msg("Pensando...")
        search_browser.get("http://www.chistescortos.eu/top?page="+str(randint(1,100)))
        send_msg(search_browser.execute_script('return document.getElementsByClassName("post")['+str(randint(3,12))+'].getElementsByTagName("p")[0].innerText'))
    elif(cmd==bot_ext+"cmd"):
        send_msg("• "+bot_ext+"say solicitud -> El bot dirá lo que escribas. (ej. "+bot_ext+"say Soy un bot :v)")
        send_msg("• "+bot_ext+"search solicitud -> El bot te enviará 5 links a páginas sobre lo que escribas. (ej. "+bot_ext+"search 7 razones para no suicidarme)")
        send_msg("• "+bot_ext+"dic solicitud -> El bot buscará la definicion de diccionario sobre lo que escribas. (ej. "+bot_ext+"dic Computadora)")
        send_msg("• "+bot_ext+"card solicitud -> El bot te mandara información de las tarjetas de Google sobre lo que escribas como bandas, lugares, personas, peliculas, repartos, etc. (ej. "+bot_ext+"card Cinemex cartelera)")
        send_msg("• "+bot_ext+"chiste -> El bot contará un chiste.")
    else:
        return "Para ver los comandos escribe "+bot_ext+"cmd."

try:
    browser.find_element_by_class_name("chat-title")
except Exception as e:
    input("[input]     Esperando iniciar sesión en whatsapp... Enter para continuar")

indice = browser.execute_script('chat = document.getElementsByClassName("chat-title");'+
                                'for(var i = 0 ; i < chat.length ; ++i){if(chat[i].innerText == "Ingeniería en Sistemas")return i}')

grupo = browser.find_elements_by_css_selector("._2wP_Y")
grupo[indice].click()
send_msg("---- *Bot iniciado* ----")
send_msg("Envía "+bot_ext+"cmd para ver los comandos.")
while (1):
    try:
        msg_content = browser.execute_script('var el = document.getElementsByClassName("msg"); return el[el.length-1].getElementsByClassName("selectable-text")[0].innerText')
        print("[ultimo_mensaje]     "+msg_content)
        msg = browser.find_elements_by_css_selector(".msg")
        if(msg[browser.execute_script('return document.getElementsByClassName("msg").length-1;')].get_attribute("id") != "1" and msg_content[0]==bot_ext):
            browser.execute_script('var el = document.getElementsByClassName("msg"); el[el.length-1].id = 1')
            split = msg_content.split(" ")
            output = comando(split[0], msg_content.replace(split[0], "", 1))
            send_msg(output)
        time.sleep(.25)
    except Exception as e:
        print("[browser_exception]     "+str(e))
