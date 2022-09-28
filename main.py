import PySimpleGUI as sg
## Persuasion Game
##
##

##  wheel objects are length 4 list
##      Top-Left-Right-Bottom order
##      wedge: size of wedge
##      pref: 1 hate - 4 love
##      play: 1 indicates used option

# modifiers for pref 1-4
mods = [ -1.5, -1, 1, 1.5 ]

def prefToStr(n):
    if n == 1: return 'Hate'
    if n == 2: return 'Dislike'
    if n == 3: return 'Like'
    if n == 4: return 'Love'

class PersGame:
    wedge = [ 0, 0, 0, 0 ]
    pref = [ 0, 0, 0, 0 ]
    used = [ 0, 0, 0, 0 ]
    
    def __init__(self, wedge, pref):
        self.wedge = wedge
        self.pref = pref
    
    def play(self, pick):
        if self.used[pick-1] == 0:
            self.used[pick-1] = 1
            return int(self.wedge[pick-1] * mods[self.pref[pick-1]-1])
        else: return 0

##    def printGame(self):
##        print(prefToStr(self.pref[0]))
##        print(prefToStr(self.pref[1]))
##        print(prefToStr(self.pref[2]))
##        print(prefToStr(self.pref[3]))




game = PersGame([1, 3, 2, 4], [1, 3, 2, 4])
##game.printGame()
##print(game.play(1))
##print(game.play(2))
##print(game.play(3))
##print(game.play(4))

sg.theme('DarkAmber')
layout = [ [sg.Text('Persuasion Game')],
           [sg.Text('Admire', size=(8,1)), sg.ProgressBar(90, orientation='h', size=(20, 20), key='admirebar')],
           [sg.Text('Boast', size=(8,1)), sg.ProgressBar(90, orientation='h', size=(20, 20), key='boastbar')],
           [sg.Text('Joke', size=(8,1)), sg.ProgressBar(90, orientation='h', size=(20, 20), key='jokebar')],
           [sg.Text('Coerce', size=(8,1)), sg.ProgressBar(90, orientation='h', size=(20, 20), key='coercebar')],
           [sg.Combo(['Admire', 'Boast', 'Joke', 'Coerce'])],
           [sg.Button('Select'), sg.Button('Cancel')] ]
window = sg.Window('Persuasion Game Simulator', layout)
admire_bar = window['admirebar']
boast_bar = window['boastbar']
joke_bar = window['jokebar']
coerce_bar = window['coercebar']



active = True
while active:
    active = False
    event, values = window.read()
    admire_bar.UpdateBar(game.wedge[0]*25 -15)
    boast_bar.UpdateBar(game.wedge[1]*25 -15)
    joke_bar.UpdateBar(game.wedge[2]*25 -15)
    coerce_bar.UpdateBar(game.wedge[3]*25 -15)
    window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print(values[0])

window.close()
