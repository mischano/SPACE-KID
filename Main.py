from menu import Menu
from character import Character
import audio

audio.setUpAudio()
audio.playAudio()
menu_obj = Menu(False, 120)
mm = menu_obj.main_menu()
character = Character(menu_obj).main_menu()
