import imp
from logging import root
from multiprocessing import set_forkserver_preload
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

Builder.load_file('src/screens/mensaje.kv')


class MensajeScreen(Screen, FloatLayout):
    secs = 0
    event = None

    def __init__(self, **kw):
        self.app = App.get_running_app()
        self.image_gif_esp = Image(source=self.app.get_path_resources('español','mensaje.gif'), pos=self.pos, size=self.size, keep_ratio=False, keep_data=True, anim_delay=-1, anim_loop=1)
        self.image_gif_en = Image(source=self.app.get_path_resources('ingles','mensaje.gif'), pos=self.pos, size=self.size, keep_ratio=False, keep_data=True, anim_delay=-1, anim_loop=1)
        super().__init__(**kw)
        

    def update_time(self, sec):
        """
        Contador de tiempo de visualización del mensaje.
        """
        self.secs = self.secs+1
        if self.secs == 5:
            self.image_gif_en.anim_delay = -1
            self.image_gif_esp.anim_delay = -1
            self.event.cancel()
            self.secs = 0
            self.app.sm.current = "inicio"    
 
    def on_enter(self):
        """
        Inicio del contador y la animación.
        """
        self.event = Clock.schedule_interval(self.update_time, 1)
        if self.app.inicio_option == "español":
            self.image_gif_esp.anim_delay = 0.10
        elif self.app.inicio_option == "ingles":
            self.image_gif_en.anim_delay = 0.10

    def update_gif(self, lang):
        """
        Actualizar archivo gif del mensaje.
        """
        if lang =="español":
            self.remove_widget(self.image_gif_en)
            self.add_widget(self.image_gif_esp)
        elif lang == "ingles":
            self.add_widget(self.image_gif_en)
            self.remove_widget(self.image_gif_esp)