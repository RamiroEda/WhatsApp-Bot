from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import kivy
import threading
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from random import randint
import time
import os

class ConfigPanel(GridLayout):
    stop = threading.Event()
    bot_ext = "!"
    ball8_answers = ["En mi opinión, sí","Es cierto","Es decididamente así",
                    "Probablemente","Buen pronóstico","Todo apunta a que sí",
                    "Sin duda","Sí","Sí - definitivamente","Debes confiar en ello",
                    "Respuesta vaga, vuelve a intentarlo","Pregunta en otro momento",
                    "Será mejor que no te lo diga ahora","No puedo predecirlo ahora",
                    "Concéntrate y vuelve a preguntar","No cuentes con ello",
                    "Mi respuesta es no","Mis fuentes me dicen que no",
                    "Las perspectivas no son buenas","Muy dudoso"]

    search_browser = webdriver.Chrome(os.getcwd()+"/chromedriver.exe")
    search_browser_main_window = search_browser.current_window_handle

    browser = webdriver.Chrome(os.getcwd()+"/chromedriver.exe")

    def __init__(self, **kwargs):
        super(ConfigPanel, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Button(background_color=[0.2,0.2,0.2,1],text=''))
        self.add_widget(Button(background_color=[0.2,0.2,0.2,1],text='Activar/Desactivar Comandos'))
        self.add_widget(Button(background_color=[0.2,0.2,0.2,1],text=self.bot_ext+'say'))
        self.cmd1 = CheckBox(active=True)
        self.add_widget(self.cmd1)
        self.add_widget(Button(background_color=[0.2,0.2,0.2,1],text=self.bot_ext+'card'))
        self.cmd2 = CheckBox(active=True)
        self.add_widget(self.cmd2)
        self.add_widget(Button(background_color=[0.2,0.2,0.2,1],text=self.bot_ext+'dic'))
        self.cmd3 = CheckBox(active=True)
        self.add_widget(self.cmd3)
        self.add_widget(Button(background_color=[0.2,0.2,0.2,1],text=self.bot_ext+'search'))
        self.cmd4 = CheckBox(active=True)
        self.add_widget(self.cmd4)
        self.add_widget(Button(background_color=[0.2,0.2,0.2,1],text=self.bot_ext+'chiste'))
        self.cmd5 = CheckBox(active=True)
        self.add_widget(self.cmd5)
        self.add_widget(Button(background_color=[0.2,0.2,0.2,1],text=self.bot_ext+'conf'))
        self.cmd6 = CheckBox(active=True)
        self.add_widget(self.cmd6)
        self.add_widget(Button(background_color=[0.2,0.2,0.2,1],text=self.bot_ext+'loli'))
        self.cmd7 = CheckBox(active=True)
        self.add_widget(self.cmd7)
        self.add_widget(Button(background_color=[0.2,0.2,0.2,1],text=self.bot_ext+'mywaifu'))
        self.cmd8 = CheckBox(active=True)
        self.add_widget(self.cmd8)
        self.add_widget(Button(background_color=[0.2,0.2,0.2,1],text=self.bot_ext+'dados'))
        self.cmd9 = CheckBox(active=True)
        self.add_widget(self.cmd9)
        self.add_widget(Button(background_color=[0.2,0.2,0.2,1],text=self.bot_ext+'8ball'))
        self.cmd10 = CheckBox(active=True)
        self.add_widget(self.cmd10)
        self.add_widget(Button(background_color=[0.2,0.2,0.2,1],text=self.bot_ext+'cat'))
        self.cmd11 = CheckBox(active=True)
        self.add_widget(self.cmd11)
        self.add_widget(Button(background_color=[0.2,0.2,0.2,1],text=self.bot_ext+'monachina3d'))
        self.cmd12 = CheckBox(active=True)
        self.add_widget(self.cmd12)
        self.add_widget(Button(background_color=[0,0,0,1],text=''))
        self.add_widget(Button(background_color=[0,0,0,1],text=''))
        self.add_widget(Button(background_color=[0.2,0.2,0.2,1],text='Bot activado'))
        self.active_bot = Button(background_color=[1,0.2,0.2,1],text='No')
        self.add_widget(self.active_bot)
        self.add_widget(Button(background_color=[0.2,0.2,0.2,1],text='Chat activo'))
        self.active_chat = Button(background_color=[0.2,0.2,0.2,1],text='')
        self.add_widget(self.active_chat)
        self.add_widget(Button(background_color=[0.2,0.2,0.2,1],text='Total de comandos ejecutados'))
        self.ttl_cmd = Button(background_color=[0.2,0.2,0.2,1],text='0')
        self.add_widget(self.ttl_cmd)
        self.add_widget(Button(background_color=[0.2,0.2,0.2,1],text='Ultimo comando'))
        self.lst_cmd = Button(background_color=[0.2,0.2,0.2,1],text='')
        self.add_widget(self.lst_cmd)
        self.add_widget(Button(background_color=[0.2,0.2,0.2,1],text='Ultimo mensaje'))
        self.lst_msg = Button(background_color=[0.2,0.2,0.2,1],text='')
        self.add_widget(self.lst_msg)
        self.add_widget(Button(background_color=[0.2,0.2,0.2,1],text='Ultimo error'))
        self.brw_excpt = Button(background_color=[0.2,0.2,0.2,1],text='')
        self.add_widget(self.brw_excpt)
        self.add_widget(Button(background_color=[0,0,0,1],text=''))
        self.add_widget(Button(background_color=[0,0,0,1],text=''))
        print("juju")

        self.browser.get("https://web.whatsapp.com/")
        self.search_browser_main_window = self.search_browser.current_window_handle
        self.start_second_thread()

    def start_second_thread(self):
        threading.Thread(target=self.main_program).start()

    def to_debug_text(self, s):
        return "["+time.strftime("%H:%M:%S")+"]   "+s

    def re_msg(self, el):
        time.sleep(.25)
        webdriver.ActionChains(self.browser).move_to_element(el).click(self.browser.find_element_by_css_selector("._2DNgV._1i1U7")).perform()
        time.sleep(.25)
        self.browser.execute_script('document.getElementsByClassName("_2DNgV _1i1U7")[0].firstElementChild.click()')
        re_menu = self.browser.find_element_by_css_selector("._3lSL5._2dGjP._1vu-E")
        webdriver.ActionChains(self.browser).move_to_element(re_menu).click(re_menu).perform()

    def send_msg(self, output):
        txt = output.split("\n")
        for t in txt:
            chat = self.browser.find_element_by_class_name("pluggable-input-body")
            chat.click()
            chat.send_keys("*"+t+"*")
            btn = self.browser.find_element_by_class_name("compose-btn-send")
            btn.click()

    def random_img(self, kw, msg_error):
        self.search_browser.get("https://www.google.com.mx/search?tbm=isch&q="+kw)
        for i in range(5):
            webdriver.ActionChains(self.search_browser).send_keys(Keys.END).perform()
            time.sleep(.5)
        try:
            self.search_browser.execute_script('document.getElementsByClassName("rg_ic rg_i")['+str(randint(0,399))+'].click(); document.getElementsByClassName("irc_fsl i3596")[1].click();')
        except:
            self.search_browser.switch_to_window(self.search_browser_main_window)
            self.send_msg(msg_error)
            self.random_img(kw, msg_error)
            return
        self.search_browser.switch_to_window(self.search_browser.window_handles[1])
        try:
            tag = self.search_browser.execute_script('return document.body.firstElementChild.tagName')
        except:
            tag = "undefined"
        if(tag != "IMG"):
            self.search_browser.close()
            self.search_browser.switch_to_window(self.search_browser_main_window)
            self.send_msg(msg_error)
            self.random_img(kw, msg_error)
            return
        webdriver.ActionChains(self.search_browser).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
        webdriver.ActionChains(self.browser).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        time.sleep(2)
        webdriver.ActionChains(self.browser).send_keys(Keys.RETURN).perform()
        time.sleep(.5)
        self.search_browser.close()
        self.search_browser.switch_to_window(self.search_browser_main_window)


    def comando(self, cmd, cnt):
        if(cmd == self.bot_ext+"say" and self.cmd1.active):
            self.send_msg(cnt)
        elif(cmd == self.bot_ext+"card" and self.cmd2.active):
            if(cnt == cmd):
                self.send_msg("Por favor escriba algo para buscar...")
                return;
            self.send_msg("Buscando...")
            self.search_browser.get("https://www.google.com.mx/search?q="+cnt.replace(" ","+"))

            if(self.search_browser.find_element_by_id("extabar").text != ""):
                res = self.search_browser.find_element_by_id("botabar")
                if(res.is_displayed()):
                    try:
                        self.search_browser.execute_script('document.getElementById("botabar").getElementsByClassName("_tho")[0].innerText = ">";')
                    except Exception as e:
                        print(e)
                    self.search_browser.execute_script('for(var i = 0 ; i < document.getElementsByClassName("klzc").length; ++i){document.getElementsByClassName("klzc")[i].innerText = "~";} for(var i = 0 ; i < document.getElementsByClassName("_bgi").length; ++i){document.getElementsByClassName("_bgi")[i].innerText = "~";}')
                    self.send_msg(res.text)
                else:
                    try:
                        self.search_browser.execute_script('document.getElementsByClassName("kp-hc")[0].getElementsByClassName("_IWg _HWg _eXg mod")[0].innerText')
                        res = self.search_browser.find_element_by_class_name("kp-hc")
                        self.send_msg(res.text)
                    except Exception as e:
                        res = self.search_browser.find_element_by_id("rhs_block")
                        if(res.text != ""):
                            txt = res.text.split("\n")
                            for t in txt:
                                if(not(t == "Otras personas también buscan" or
                                        t == "Canciones" or t == "También se buscó" or
                                        t == "Comentarios" or t == "Preguntas y respuestas" or
                                        t == "Opiniones" or t == "Sugerir una edición · ¿Eres propietario de esta empresa?" or
                                        t == "Sugerir una edición")):
                                    if(not(t == "Más imágenes" or t == "Ver fotos" or t == "Ver por fuera" or t == "Sitio webIndicaciones")):
                                        self.send_msg(t)
                                else:
                                    break
                        else:
                            self.send_msg("No se encontraron resultados")

        elif(cmd == self.bot_ext+"dic" and self.cmd3.active):
            if(cnt == cmd):
                self.send_msg("Por favor escriba algo para buscar...")
                return;

            self.send_msg("Buscando...")
            self.search_browser.get("https://www.google.com.mx/search?q=define%3A"+cnt.replace(" ","+"))
            res = self.search_browser.find_elements_by_css_selector(".lr_dct_ent.vmod")
            if(res):
                self.send_msg( res[0].text)
            else:
                self.send_msg( "No se encontraron resultados")
        elif(cmd == self.bot_ext+"search" and self.cmd4.active):
            if(cnt == cmd):
                self.send_msg("Por favor escriba algo para buscar...")
                return;
            self.send_msg("Buscando...")
            self.search_browser.get("https://www.google.com.mx/search?q="+cnt.replace(" ","+"))

            for i in range(5):
                self.send_msg(self.search_browser.execute_script('return document.getElementsByClassName("r")['+str(i)+'].innerText + " en " + document.getElementsByClassName("r")['+str(i)+'].getElementsByTagName("a")[0].getAttribute("href");'))
        elif(cmd == self.bot_ext+"chiste" and self.cmd5.active):
            self.send_msg("Pensando...")
            self.search_browser.get("http://www.losmejoreschistescortos.net/humor-negro/page/"+str(randint(1,15)))

            self.send_msg(self.search_browser.execute_script('var txt=""; for(var i = 0 ; i < document.getElementsByClassName("entry-content")['+str(randint(0,19))+'].getElementsByTagName("p").length ; i++){txt += document.getElementsByClassName("entry-content")['+str(randint(0,19))+'].getElementsByTagName("p")[i].innerText;} return txt;'))
        elif(cmd == self.bot_ext+"conf" and self.cmd6.active):
            self.send_msg("Buscando...")
            self.search_browser.get("http://www.nogare.net/?s="+str(randint(0,1000)))

            self.send_msg(self.search_browser.execute_script('return document.getElementsByClassName("conftext")['+str(randint(0,9))+'].innerText'))
        elif(cmd == self.bot_ext+"loli" and self.cmd7.active):
            self.send_msg("Ahí te va 7u7...")
            self.random_img("lolis", "Uy!... Se nos escapó tu loli.\nTe buscaremos otra.")
            self.send_msg("Servido papu 7u7")
        elif(cmd == self.bot_ext+"mywaifu" and self.cmd8.active):
            self.send_msg("Y tu waifu es...")
            self.random_img("anime waifu", "No puede ser! Uno de tus compañeros te robó a tu waifu.\nTe estoy buscando otra que sea fiel.")
        elif(cmd == self.bot_ext+"dados" and self.cmd9.active):
            self.send_msg("Lanzando...")
            self.send_msg(str(randint(1,6)))
        elif(cmd == self.bot_ext+"8ball" and self.cmd10.active):
            if(cnt == cmd):
                self.send_msg("Por favor pregunta algo a la bola mágica...")
                return;
            self.send_msg(self.ball8_answers[randint(0,19)])
        elif(cmd == self.bot_ext+"cat" and self.cmd11.active):
            self.send_msg("Buscando...")
            self.random_img("cute cats", "Este gato es demasiado para tí.\nBuscando más gatos")
        elif(cmd == self.bot_ext+"monachina3d" and self.cmd12.active):
            self.send_msg("Buscando monas chinas 3d...")
            self.send_msg("(Sujeto a errores con monos chinos 3d :v)")
            self.random_img('"ggspics" cute site:twitter.com', "Resulta que esa mona china 3d era hombre.\nBuscando otra mona china 3d.")
        elif(cmd == self.bot_ext+"cmd"):
            if(self.cmd1.active):
                self.send_msg("• "+self.bot_ext+"say solicitud -> Diré lo que escribas. (ej. "+self.bot_ext+"say Soy un bot :v)")
            if(self.cmd4.active):
                self.send_msg("• "+self.bot_ext+"search solicitud -> Enviaré 5 links a páginas sobre lo que escribas. (ej. "+self.bot_ext+"search 7 razones para no suicidarme)")
            if(self.cmd3.active):
                self.send_msg("• "+self.bot_ext+"dic solicitud -> Buscaré la definicion de diccionario sobre lo que escribas. (ej. "+self.bot_ext+"dic Computadora)")
            if(self.cmd2.active):
                self.send_msg("• "+self.bot_ext+"card solicitud -> Mandaré información de las tarjetas de Google sobre lo que escribas como bandas, lugares, personas, peliculas, repartos, etc. (ej. "+self.bot_ext+"card Cinemex cartelera)")
            if(self.cmd5.active):
                self.send_msg("• "+self.bot_ext+"chiste -> Contaré un chiste.")
            if(self.cmd6.active):
                self.send_msg("• "+self.bot_ext+"conf -> Buscaré confesiones anónimas de internet.")
            if(self.cmd7.active):
                self.send_msg("• "+self.bot_ext+"loli -> Te daré una loli en adopción 7u7.")
            if(self.cmd11.active):
                self.send_msg("• "+self.bot_ext+"cat -> Te mandaré un gato bien prron.")
            if(self.cmd9.active):
                self.send_msg("• "+self.bot_ext+"dados -> Te daré un número entre 1 y 6.")
            if(self.cmd8.active):
                self.send_msg("• "+self.bot_ext+"mywaifu -> Buscaré a tu verdadera waifu 2d.")
            if(self.cmd12.active):
                self.send_msg("• "+self.bot_ext+"monachina3d -> Buscaré a una mona china 3d.")
            if(self.cmd10.active):
                self.send_msg("• "+self.bot_ext+"8ball pregunta -> Te responderé una pregunta (preguntas sí/no) que mandes.")
        else:
            self.send_msg( "Para ver los comandos escribe "+self.bot_ext+"cmd.")

    def main_program(self):
        #try:
            #self.browser.find_element_by_class_name("chat-title")
        #except Exception as e:
            #input("[input]     Esperando iniciar sesión en whatsapp... Enter para continuar")

        #indice = self.browser.execute_script('chat = document.getElementsByClassName("chat-title");'+
                                            #'for(var i = 0 ; i < chat.length ; ++i){if(chat[i].innerText == "+52 1 492 171 3244")return i}') #+52 1 492 171 3244 Ingeniería en Sistemas

        #try:
            #grupo = self.browser.find_elements_by_css_selector("._2wP_Y")
            #grupo[indice].click()
            #self.send_msg("---- Bot iniciado ----")
            #self.send_msg("(Esta cuenta no se responsabiliza de los contenidos audiovisuales enviados por el bot, los contenidos han sido elegidos al azar desde Google Imagenes)")
            #self.send_msg("Envía "+self.bot_ext+"cmd para ver los comandos.")
        #except Exception as e:
            #print(e)
        print("hola1")

        while True:
            if self.stop.is_set():
                print("hola3")
                return
            while True:
                try:
                    self.browser.find_element_by_id("pane-side")
                    self.active_bot.background_color = [0.2,1,0.2,1]
                    self.active_bot.text = "Sí"
                    if(self.active_chat.text == ""):
                        self.active_chat.text = "Por favor entre en un chat..."
                    break;
                except Exception as e:
                    self.active_bot.background_color = [1,0.2,0.2,1]
                    self.active_bot.text = "No"
                    time.sleep(1)
            try:
                try:
                    self.active_chat.text = self.browser.execute_script('return document.getElementsByClassName("_1wjpf")[document.getElementsByClassName("_1wjpf").length-1].innerText')
                    msg_content = self.browser.execute_script('var el = document.getElementsByClassName("selectable-text invisible-space copyable-text"); return el[el.length-1].innerText')
                    msg_complete = self.browser.execute_script('var el = document.getElementsByClassName("selectable-text invisible-space copyable-text"); return el[el.length-1].innerText')
                    msg_complete = msg_complete.replace('\n', "    ")
                except Exception as e:
                    self.brw_excpt.text = self.to_debug_text("[No se puede leer el mensaje]")
                    msg_content  = "[No se puede leer el mensaje]"
                self.lst_msg.text = self.to_debug_text(msg_complete)
                msg = self.browser.find_elements_by_css_selector(".vW7d1")
                msg = msg[self.browser.execute_script('return document.getElementsByClassName("vW7d1").length-1;')]
                if(msg.get_attribute("id") != "1" and msg_content[0]==self.bot_ext):
                    try:
                        self.re_msg(msg)
                    except Exception as e:
                        self.brw_excpt.text = self.to_debug_text("[No se pudo responder el mensaje]")
                    self.ttl_cmd.text = str(int(self.ttl_cmd.text)+1);
                    self.browser.execute_script('var el = document.getElementsByClassName("vW7d1"); el[el.length-1].id = 1')
                    split = msg_content.split(" ")
                    self.comando(split[0], msg_content.replace(split[0]+" ", "", 1))
                    self.lst_cmd.text = self.to_debug_text(msg_complete)
                    time.sleep(2)
                time.sleep(0.1)
            except Exception as e:
                self.brw_excpt.text = self.to_debug_text("[Error al ejecutar el comando]")
            except:
                self.brw_excpt.text = self.to_debug_text("[Error desconocido]")


class MyApp(App):
    title = 'WhatsApp Bot Dashboard'
    def build(self):
        return ConfigPanel()

    def on_stop(self):
        self.root.stop.set()
        self.root.browser.quit()
        self.root.search_browser.quit()

if __name__ == '__main__':
    MyApp().run()
