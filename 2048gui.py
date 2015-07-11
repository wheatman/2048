from 2048 import *







class game(BoxLayout):
    def __init__(self, **kwargs):
        super(start_screen, self).__init__(**kwargs)
        btn_layout = BoxLayout()
        restart = Button(text = 'Restart')
        restart.bind(on_release = restartGame)
        random = Button(text = 'random')
        random.bind(on_release = runRandom)
        DRLU = Button(text = "style 1")
        DRLU.bind(on_release = runDRLU)
        DRDR = Button(text = "style 2")
        DRDR.bind(on_release = runDRDR)
        
        btn_layout.add_widget(restart)
        btn_layout.add_widget(random)
        btn_layout.add_widget(DRLU)
        btn_layout.add_widget(DRDR)
        self.add(btn_layout)
        gameboard = GridLayout(
















########################################################################
class Sim(App):
    
    #----------------------------------------------------------------------
    def build(self): # when its built load the start screen
        return game()

#----------------------------------------------------------------------
app = Sim()
app.run() # run the app
