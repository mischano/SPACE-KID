from Menu import GameMenu
import Audio

Audio.setUpAudio()
Audio.playAudio()
window = GameMenu(1440, 820)
play = window.main_menu()

