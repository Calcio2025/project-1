from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class JanelaGerenciadora(ScreenManager):
    pass

class JanelaPrincipal(Screen):
    pass

class Janela1(Screen):
    def limpar(self):
        self.ids.resposta.text = ''
        self.ids.caixa_texto.text = ''
        
    def calcular(self):
        self.dialog = MDDialog(title = 'ERROR', text = 'Algo Errado, Repita!',
                                buttons=[MDFlatButton(text='ok',
                                on_release = self.liberar)])
        try:
            v1 = float(self.ids.caixa_texto.text)
            v2 = v1 / 3.6
            self.ids.resposta.text = '{:0.2f}'.format(v2) + 'm/s'
        except ValueError:
            self.dialog.open()
            
    def liberar (self, obj):
            self.dialog.dismiss()

class Janela2(Screen):
    def limpar(self):
        self.ids.resposta.text = ''
        self.ids.caixa_texto.text = ''
        
    def calcular(self):
        self.dialog = MDDialog(title = 'ERROR', text = 'Algo Errado, Repita!',
                                buttons=[MDFlatButton(text='ok',
                                on_release = self.liberar)])
        try:
            v1 = float(self.ids.caixa_texto.text)
            v2 = v1 * 3.6
            self.ids.resposta.text = '{:0.2f}'.format(v2) + 'm/s'
        except ValueError:
            self.dialog.open()
            
    def liberar (self, obj):
            self.dialog.dismiss()



class Meuapp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="Teal"
        self.title='Conversor de Velocidade'
        return Builder.load_file('main.kv')
    
    def fechar(self):
        self.stop()
    
Meuapp().run()



   
    

 