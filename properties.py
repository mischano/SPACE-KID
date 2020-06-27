# 0
main_menu_text = [['Exit', 'Play', 'Settings', 'Credits', 'SPACE KID'], [(80, 500, 105, 60), (80, 290, 120, 60),
                                                                         (80, 360, 210, 60), (80, 430, 185, 60),
                                                                         (750, 40, 630, 135)], [45, 45, 45, 45, 130],
                  [0, 4]]
# 1
settings_text = [['Back', 'Controls', 'Graphics', 'Audio', 'Character'],  [(80, 500, 115, 60), (80, 290, 233, 60),
                                                                         (80, 360, 215, 60), (80, 430, 135, 60),
                                                                         (80, 220, 260, 60)], [45, 45, 45, 45, 45],
                  [0, 5]]

# 1
credits_text = [['Back', 'Author: Mansur Ischanov', 'Github: mischano',
                 'Python 3.8.2', 'Pygame 1.9.6', 'Credits'],
                [(20, 30, 115, 60), (451, 330, 537, 45), (541, 380, 358, 45),
                 (630, 520, 180, 35), (627.5, 565, 185, 35), (565, 180, 310, 85)], [50, 40, 40, 30, 30, 80], [0, 1]]

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
    surface_prop = {0: main_menu_text, 1: [0, 0, settings_text, credits_text],
                    2: [0, settings_controls_text, settings_graphics_text, settings_audio_text],
                    3: [0, settings_graphics_window_size, fps_text]}

    return surface_prop[index]
