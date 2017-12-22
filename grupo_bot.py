from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import randint
from msvcrt import getch
import os

bot_ext = "!"
ball8_answers = ["En mi opinión, sí","Es cierto","Es decididamente así",
                "Probablemente","Buen pronóstico","Todo apunta a que sí",
                "Sin duda","Sí","Sí - definitivamente","Debes confiar en ello",
                "Respuesta vaga, vuelve a intentarlo","Pregunta en otro momento",
                "Será mejor que no te lo diga ahora","No puedo predecirlo ahora",
                "Concéntrate y vuelve a preguntar","No cuentes con ello",
                "Mi respuesta es no","Mis fuentes me dicen que no",
                "Las perspectivas no son buenas","Muy dudoso"]

brw_excpt = ""
lst_cmd = ""
lst_cmd_c = ""
lst_msg = ""
ttl_cmd = 0

print("Cargando las paginas necesarias...")
browser = webdriver.Chrome("C:/Users/ramir/Desktop/WhatsApp-Bot/WhatsApp-Bot/chromedriver.exe")
browser.get("https://web.whatsapp.com/")
search_browser = webdriver.Chrome("C:/Users/ramir/Desktop/WhatsApp-Bot/WhatsApp-Bot/chromedriver.exe")
search_browser_main_window = search_browser.current_window_handle

time.sleep(1)
print("Se han cargado las páginas necesarias...")

def random_img(kw):
    search_browser.get("https://www.google.com.mx/search?tbm=isch&q="+kw)
    webdriver.ActionChains(search_browser).send_keys(Keys.END).perform()
    time.sleep(.5)
    webdriver.ActionChains(search_browser).send_keys(Keys.END).perform()
    time.sleep(.5)
    webdriver.ActionChains(search_browser).send_keys(Keys.END).perform()
    time.sleep(.5)
    webdriver.ActionChains(search_browser).send_keys(Keys.END).perform()
    time.sleep(.5)
    search_browser.execute_script('document.getElementsByClassName("rg_ic rg_i")['+str(randint(0,99))+'].click(); document.getElementsByClassName("irc_fsl i3596")[1].click();')
    search_browser.switch_to_window(search_browser.window_handles[1])
    webdriver.ActionChains(search_browser).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    webdriver.ActionChains(browser).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(2)
    webdriver.ActionChains(browser).send_keys(Keys.RETURN).perform()
    time.sleep(.5)
    search_browser.close()
    search_browser.switch_to_window(search_browser_main_window)
def send_msg(output):
    txt = output.split("\n")
    for t in txt:
        chat = browser.find_element_by_class_name("pluggable-input-body")
        chat.click()
        chat.send_keys("*"+t+"*")
        btn = browser.find_element_by_class_name("compose-btn-send")
        btn.click()

def comando(cmd, cnt):
    if(cmd == bot_ext+"say"):
        send_msg(cnt)
    elif(cmd == bot_ext+"card"):
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
                                    t == "Opiniones" or t == "Sugerir una edición · ¿Eres propietario de esta empresa?" or
                                    t == "Sugerir una edición")):
                                if(not(t == "Más imágenes" or t == "Ver fotos" or t == "Ver por fuera" or t == "Sitio webIndicaciones")):
                                    send_msg(t)
                            else:
                                break
                    else:
                        send_msg("No se encontraron resultados")

    elif(cmd == bot_ext+"dic"):
        send_msg("Buscando...")
        search_browser.get("https://www.google.com.mx/search?q="+cnt.replace(" ","+")+"+definicion")
        res = search_browser.find_elements_by_css_selector(".lr_dct_ent.vmod")
        if(res):
            send_msg( res[0].text)
        else:
            send_msg( "No se encontraron resultados")
    elif(cmd == bot_ext+"search"):
        send_msg("Buscando...")
        search_browser.get("https://www.google.com.mx/search?q="+cnt.replace(" ","+"))

        for i in range(5):
            send_msg(search_browser.execute_script('return document.getElementsByClassName("r")['+str(i)+'].innerText + " en " + document.getElementsByClassName("r")['+str(i)+'].getElementsByTagName("a")[0].getAttribute("href");'))
    elif(cmd == bot_ext+"chiste"):
        send_msg("Pensando...")
        search_browser.get("http://www.losmejoreschistescortos.net/humor-negro/page/"+str(randint(1,15)))

        send_msg(search_browser.execute_script('var txt=""; for(var i = 0 ; i < document.getElementsByClassName("entry-content")['+str(randint(0,19))+'].getElementsByTagName("p").length ; i++){txt += document.getElementsByClassName("entry-content")['+str(randint(0,19))+'].getElementsByTagName("p")[i].innerText;} return txt;'))
    elif(cmd == bot_ext+"conf"):
        send_msg("Buscando...")
        search_browser.get("http://www.nogare.net/?s="+str(randint(0,1000)))

        send_msg(search_browser.execute_script('return document.getElementsByClassName("conftext")['+str(randint(0,9))+'].innerText'))
    elif(cmd == bot_ext+"loli"):
        send_msg("Ahí te va 7u7...")
        send_msg("(Esta cuenta no se responsabiliza de los contenidos audiovisuales enviados por el bot, los contenidos han sido elegidos al azar desde Google Imagenes)")
        random_img("lolis")
        send_msg("Servido papu 7u7")
    elif(cmd == bot_ext+"mywaifu"):
        send_msg("Y tu waifu es...")
        random_img("anime waifu")
    elif(cmd == bot_ext+"dados"):
        send_msg("Lanzando...")
        send_msg(str(randint(1,6)))
    elif(cmd == bot_ext+"8ball"):
        if(cnt == bot_ext+"8ball"):
            send_msg("Por favor pregunta algo a la bola mágica...")
        else:
            send_msg(ball8_answers[randint(0,19)])
    elif(cmd == bot_ext+"cmd"):
        send_msg("• "+bot_ext+"say solicitud -> El bot dirá lo que escribas. (ej. "+bot_ext+"say Soy un bot :v)")
        send_msg("• "+bot_ext+"search solicitud -> El bot te enviará 5 links a páginas sobre lo que escribas. (ej. "+bot_ext+"search 7 razones para no suicidarme)")
        send_msg("• "+bot_ext+"dic solicitud -> El bot buscará la definicion de diccionario sobre lo que escribas. (ej. "+bot_ext+"dic Computadora)")
        send_msg("• "+bot_ext+"card solicitud -> El bot te mandara información de las tarjetas de Google sobre lo que escribas como bandas, lugares, personas, peliculas, repartos, etc. (ej. "+bot_ext+"card Cinemex cartelera)")
        send_msg("• "+bot_ext+"chiste -> El bot contará un chiste.")
        send_msg("• "+bot_ext+"conf -> El bot buscará confesiones.")
        send_msg("• "+bot_ext+"loli -> El bot te mandará una loli 7u7.")
        send_msg("• "+bot_ext+"dados -> El bot dará un número entre 1 y 6.")
        send_msg("• "+bot_ext+"mywaifu -> El bot te eligirá una waifu.")
        send_msg("• "+bot_ext+"8ball pregunta -> El bot te responderá la pregunta (preguntas sí/no) que le mandes.")
    else:
        send_msg( "Para ver los comandos escribe "+bot_ext+"cmd.")

try:
    browser.find_element_by_class_name("chat-title")
except Exception as e:
    input("[input]     Esperando iniciar sesión en whatsapp... Enter para continuar")

indice = browser.execute_script('chat = document.getElementsByClassName("chat-title");'+
                                'for(var i = 0 ; i < chat.length ; ++i){if(chat[i].innerText == "Ingeniería en Sistemas")return i}') #+52 1 492 171 3244 Ingeniería en Sistemas

try:
    grupo = browser.find_elements_by_css_selector("._2wP_Y")
    grupo[indice].click()
    #send_msg("---- Bot iniciado ----")
    #send_msg("Envía "+bot_ext+"cmd para ver los comandos.")
except Exception as e:
    print(e)
while (1):
    try:
        try:
            msg_content = browser.execute_script('var el = document.getElementsByClassName("msg"); return el[el.length-1].getElementsByClassName("selectable-text")[0].innerText')
            msg_complete = browser.execute_script('var el = document.getElementsByClassName("msg"); return el[el.length-1].innerText')
            msg_complete = msg_complete.replace('\n', " -> ", 2)
            msg_complete = msg_complete.replace('\n', "")
        except Exception as e:
            brw_excpt = "["+time.strftime("%H:%M:%S")+"]   "+str(e).split("(")[0]
            msg_content = "["+time.strftime("%H:%M:%S")+"]   [No se puede leer el mensaje]"
        lst_msg = "["+time.strftime("%H:%M:%S")+"]   "+msg_complete
        msg = browser.find_elements_by_css_selector(".msg")
        if(msg[browser.execute_script('return document.getElementsByClassName("msg").length-1;')].get_attribute("id") != "1" and msg_content[0]==bot_ext):
            ttl_cmd += 1;
            browser.execute_script('var el = document.getElementsByClassName("msg"); el[el.length-1].id = 1')
            split = msg_content.split(" ")
            comando(split[0], msg_content.replace(split[0]+" ", "", 1))
            lst_cmd = "["+time.strftime("%H:%M:%S")+"]   "+split[0]
            lst_cmd_c = "["+time.strftime("%H:%M:%S")+"]   "+msg_complete
    except Exception as e:
        brw_excpt = "["+time.strftime("%H:%M:%S")+"]   "+str(str(e))
    except:
        brw_excpt = "["+time.strftime("%H:%M:%S")+"]   [Error desconocido]"
    os.system('cls')
    try:
        print("[WhatsApp Bot Debug Panel]")
        print("[Total de comandos usados]    "+str(ttl_cmd))
        print("[Ultimo comando]              "+lst_cmd)
        print("[Ultimo comando completo]     "+lst_cmd_c)
        print("[Ultimo mensaje]              "+lst_msg)
        print("[Ultimo error]                "+brw_excpt)
    except Exception as e:
        print("[Ultimo mensaje]              [No se puede leer el mensaje]")
        print("[Ultimo error]                "+str(e))
