'''main_menu_text = [['SPACE KID', 'Play', 'Settings', 'Credits', 'Exit'],
                  [(530, 20, 380, 100), (648, 250, 100, 55), (606, 320, 185, 55), (619, 390, 160, 55),
                   (653, 460, 90, 55)], [100, 55, 55, 55, 55], [1, 5]]'''

# 0
main_menu_text = [['Exit', 'Play', 'Settings', 'Credits', 'SPACE KID'], [(80, 500, 130, 60), (80, 290, 140, 60),
                                                                         (80, 360, 255, 60), (80, 430, 220, 60),
                                                                         (750, 40, 380, 100)], [55, 55, 55, 55, 130],
                  [0, 4]]
# 1
settings_text = [['Back', 'Controls', 'Graphics', 'Audio', 'Settings'],  [(80, 500, 130, 60), (80, 290, 140, 60),
                                                                         (80, 360, 255, 60), (80, 430, 220, 60),
                                                                         (750, 40, 380, 100)], [55, 55, 55, 55, 130],
                  [0, 4]]

play = [['Back', 'Graphics', 'Controls', 'Audio', 'Settings'],
                 [(20, 30, 100, 60), (620, 290, 180, 55), (623, 360, 175, 55), (647, 430, 120, 55),
                  (573, 170, 260, 80)], [50, 50, 50, 50, 80], [0, 4]]
# 1
credits_text = [['Back', 'Author: Mansur Ischanov', 'Mail: mansur.ischanov@gmail.com', 'Github: mischano',
                 'Big thanks to pygame creators!', 'Credits'],
                [(20, 30, 100, 60), (530, 330, 420, 40), (440, 380, 554, 45), (580, 430, 280, 40),
                 (535, 520, 400, 35), (605, 180, 250, 80)], [50, 40, 40, 40, 30, 80], [0, 1]]

# 2
settings_graphics_text = [['Back', 'Screen Size', 'FPS', 'Settings'],
                          [(20, 30, 100, 60), (610, 290, 230, 55), (684, 380, 70, 55), (590, 170, 250, 80)],
                          [50, 50, 50, 80], [0, 3]]
# 2
settings_controls_text = [['Back', 'W', 'S', 'Control'], [(20, 30, 100, 60), (620, 290, 190, 55),
                                                          (585, 360, 255, 55), (573, 170, 260, 80)], [50, 50, 50, 80],
                          [0, 3]]
# 2
settings_audio_text = [['Back', 'On', 'Off', 'Music'],
                          [(20, 30, 100, 60), (610, 290, 230, 55), (684, 380, 70, 55), (590, 170, 250, 80)],
                          [50, 50, 50, 80], [0, 3]]
# 3
settings_graphics_window_size = [['Back', 'Full Screen', 'Window', 'Window Size'],
               [(20, 30, 100, 60), (615, 290, 220, 55), (644, 380, 165, 55), (540, 170, 380, 80)],
               [50, 50, 50, 80], [0, 3]]
# 3
fps_text = [['Back', '60', '90', '120', 'Frames Per Second'],
            [(20, 30, 100, 60), (654, 290, 60, 55), (654, 355, 60, 55), (650, 420, 60, 55), (410, 170, 600, 80)],
            [50, 50, 50, 50, 50, 80], [0, 4]]


def get_properties(index):
    surface_prop = {0: main_menu_text, 1: [0, play, settings_text, credits_text],
                    2: [0, settings_controls_text, settings_graphics_text, settings_audio_text],
                    3: [0, settings_graphics_window_size, fps_text]}

    return surface_prop[index]
