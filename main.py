# Nickname Atlas
from pyscript import display, document


def reveal_nickname (e):
    document.getElementById('display1').innerHTML = " " # ="" to avoid stacking displays
    nickname = document.getElementById('select_country').value # Getting nickname from the selected country

    display(nickname, target='display1') # display selected nickname in display1