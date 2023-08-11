import PySimpleGUI as sg
import math

def calculator():
  sg.theme('Dark Blue 2')
  layout = [
    [
      sg.Input(key='input',
               size=(20, 2),
               do_not_clear=True,
               font=('Arial', 16)),
      sg.Button('X', size=(4, 2), button_color=('white', 'red'))
    ],
    [
      sg.Button('1', size=(4, 2), button_color=('white', 'green')),
      sg.Button('2', size=(4, 2), button_color=('white', 'blue')),
      sg.Button('3', size=(4, 2), button_color=('white', 'blue')),
      sg.Button('+', size=(4, 2), button_color=('white', 'green')),
      sg.Button('sqrt', size=(4, 2), button_color=('white', 'blue')),
     
    ],
    [
      sg.Button('4', size=(4, 2), button_color=('white', 'yellow')),
      sg.Button('5', size=(4, 2), button_color=('white', 'blue')),
      sg.Button('6', size=(4, 2), button_color=('white', 'blue')),
      sg.Button('-', size=(4, 2), button_color=('white', 'green')),
       sg.Button('pow', size=(4, 2), button_color=('white', 'blue')),
     
    ],
    [
      sg.Button('7', size=(4, 2), button_color=('white', 'blue')),
      sg.Button('8', size=(4, 2), button_color=('white', 'blue')),
      sg.Button('9', size=(4, 2), button_color=('white', 'blue')),
      sg.Button('*', size=(4, 2), button_color=('white', 'green')),
       sg.Button('sin', size=(4, 2), button_color=('white', 'blue')),
     
    ],
    [
      sg.Button('.', size=(4, 2), button_color=('white', 'blue')),
      sg.Button('0', size=(4, 2), button_color=('white', 'blue')),
      sg.Button('C', size=(4, 2), button_color=('white', 'red')),
      sg.Button('/', size=(4, 2), button_color=('white', 'green')),
       sg.Button('cos', size=(4, 2), button_color=('white', 'blue')),
     
    ],
    [
      sg.Button('=', size=(6, 2), button_color=('white', 'purple')),
      sg.Button('Cancel', size=(8, 2), button_color=('white', 'red')),
      sg.Button('History', size=(6, 2), button_color=('white', 'blue')),
       sg.Button('tan', size=(4, 2), button_color=('white', 'blue')),
    ],
  ]

  