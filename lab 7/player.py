import pygame
import os

# Инициализация Pygame
pygame.init()

# Загрузка музыки
playlist = []
music_dir = "C:\\Users\\yernu\\Music"
for file in os.listdir(music_dir):
    if file.endswith(".mp3"):
        playlist.append(os.path.join(music_dir, file))

# Настройка экрана Pygame
size = width, height = 300, 200
screen = pygame.display.set_mode(size)

# Настройка шрифта Pygame
font = pygame.font.SysFont("Arial", 20)

# Начальные значения переменных
playing = False
paused = False
track_index = 0

# Функция для воспроизведения трека
def play_music(track):
    pygame.mixer.music.load(track)
    pygame.mixer.music.play()

# Начальная загрузка первого трека
play_music(playlist[track_index])

# Основной цикл программы
while True:
    # Обработка событий Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Воспроизведение/пауза
                if playing:
                    if paused:
                        pygame.mixer.music.unpause()
                        paused = False
                    else:
                        pygame.mixer.music.pause()
                        paused = True
                else:
                    play_music(playlist[track_index])
                    playing = True
            elif event.key == pygame.K_RIGHT:
                # Следующий трек
                track_index = (track_index + 1) % len(playlist)
                play_music(playlist[track_index])
            elif event.key == pygame.K_LEFT:
                # Предыдущий трек
                track_index = (track_index - 1) % len(playlist)
                play_music(playlist[track_index])

    # Отображение текущего трека и состояния плеера
    screen.fill((255, 255, 255))
    if playing:
        if paused:
            text = font.render("Paused: " + os.path.basename(playlist[track_index]), True, (0, 0, 0))
        else:
            text = font.render("Playing: " + os.path.basename(playlist[track_index]), True, (0, 0, 0))
    else:
        text = font.render("Press SPACE to play", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Обновление экрана Pygame
    pygame.display.update()
