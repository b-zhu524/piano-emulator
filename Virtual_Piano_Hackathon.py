import pygame

pygame.init()

#Intro stuff for display
win = pygame.display.set_mode((1300, 700))
pygame.mixer.set_num_channels(88)
piano = pygame.image.load("piano 1.jpg")
piano = pygame.transform.scale(piano,(1300,200))
piano_x = 0
piano_y = 500
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
win = pygame.display.set_mode((1300, 700))

win.fill((255,255,255))
c3coordinates = (590,630)
win.blit(piano, (piano_x, piano_y))
grey = (128, 128, 128)
win = pygame.display.set_mode((1300, 700))
pygame.mixer.set_num_channels(88)
pygame.display.update()
#pygame.draw.circle(win,red,c3coordinates,3)


class Piano_Key:
    def __init__(self, key, file_name, Channel_ID, x_coordinate):
        self.key = key
        self.file_name = file_name
        self.Channel_ID = Channel_ID
        self.x_coordinate = x_coordinate
        self.y_coordinate = 630

    def play(self):
        file_play = pygame.mixer.Sound(self.file_name)
        pygame.mixer.Channel(self.Channel_ID).set_volume(1.05)
        pygame.mixer.Channel(self.Channel_ID).play(file_play)

    def stop(self):
        pygame.mixer.Channel(self.Channel_ID).fadeout(300)
    def dot_placement(self):
        pygame.draw.circle(win,red,(self.x_piano_coordinate,  y_piano_coordinate),3)
        

keys = []


def find_piano_key(piano_key):
    global keys
    for character in keys:
        if character.key == piano_key:
            return character
    return c




# home-row c maj scale
keys.append(Piano_Key("caps lock", "converted_wav_notes/_b2.wav", 81))
# we will use this note later
c = Piano_Key("a", "converted_wav_notes/_c3.wav", 26)
keys.append(c)

keys.append(Piano_Key("s", "converted_wav_notes/_d3.wav", 27))
keys.append(Piano_Key("d", "converted_wav_notes/_e3.wav", 28))
keys.append(Piano_Key("f", "converted_wav_notes/_f3.wav", 29))
keys.append(Piano_Key("g", "converted_wav_notes/_g3.wav", 30))
keys.append(Piano_Key("h", "converted_wav_notes/_a3.wav", 31))
keys.append(Piano_Key("j", "converted_wav_notes/_b3.wav", 32))
keys.append(Piano_Key("k", "converted_wav_notes/_c4.wav", 33))
keys.append(Piano_Key("l", "converted_wav_notes/_d4.wav", 34))
keys.append(Piano_Key(";", "converted_wav_notes/_e4.wav", 35))
keys.append(Piano_Key("'", "converted_wav_notes/_f4.wav", 36))
keys.append(Piano_Key("enter", "converted_wav_notes/_g4.wav", 56))

# QWERTY row (sharps)
keys.append(Piano_Key("q", "converted_wav_notes/_b2.wav", 15))
keys.append(Piano_Key("w", "converted_wav_notes/_c3sharp.wav", 16))
keys.append(Piano_Key("e", "converted_wav_notes/_d3sharp.wav", 17))
keys.append(Piano_Key("r", "converted_wav_notes/_f3.wav", 18))
keys.append(Piano_Key("t", "converted_wav_notes/_f3sharp.wav", 19))
keys.append(Piano_Key("y", "converted_wav_notes/_g3sharp.wav", 20))
keys.append(Piano_Key("u", "converted_wav_notes/_a3sharp.wav", 21))
# keys.append(Piano_Key("i","converted_wav_notes/_b3.wav",22))
keys.append(Piano_Key("o", "converted_wav_notes/_c3sharp.wav", 23))
keys.append(Piano_Key("p", "converted_wav_notes/_d3sharp.wav", 49))

# Bass notes (number row)
keys.append(Piano_Key("[1]", "converted_wav_notes/_c2.wav", 63))
keys.append(Piano_Key("[2]", "converted_wav_notes/_d2.wav", 64))
keys.append(Piano_Key("[3]", "converted_wav_notes/_e2.wav", 65))
keys.append(Piano_Key("[4]","converted_wav_notes/_f2.wav",66))
keys.append(Piano_Key("[5]","converted_wav_notes/_g2.wav",67))
keys.append(Piano_Key("[6]","converted_wav_notes/_a2.wav",68))
keys.append(Piano_Key("[7]","converted_wav_notes/_b2.wav",61))
keys.append(Piano_Key("[8]","converted_wav_notes/_c3.wav",70))
keys.append(Piano_Key("[9]","converted_wav_notes/_d3.wav",71))
keys.append(Piano_Key("[0]","converted_wav_notes/_e3.wav",72))
keys.append(Piano_Key("[-]","converted_wav_notes/_f3.wav",75))
keys.append(Piano_Key("[+]", "converted_wav_notes/_g3.wav",77))

keys.append(Piano_Key("1","converted_wav_notes/_c2.wav",1))
keys.append(Piano_Key("2","converted_wav_notes/_d2.wav",2))
keys.append(Piano_Key("3", "converted_wav_notes/_e2.wav",3))
keys.append(Piano_Key("4","converted_wav_notes/_f2.wav",4))
keys.append(Piano_Key("5","converted_wav_notes/_g2.wav",5))
keys.append(Piano_Key("6","converted_wav_notes/_a2.wav",6))
keys.append(Piano_Key("7","converted_wav_notes/_b2.wav",7))
keys.append(Piano_Key("8", "converted_wav_notes/_c3.wav",8))
keys.append(Piano_Key("9","converted_wav_notes/_d3.wav",9))
keys.append(Piano_Key("0","converted_wav_notes/_e3.wav",10))
keys.append(Piano_Key("-", "converted_wav_notes/_f3.wav",11))
keys.append(Piano_Key("=","converted_wav_notes/_g3.wav",12))
keys.append(Piano_Key("backspace", "converted_wav_notes/_a3.wav",13))

# Bottom row (extended c major scale)
keys.append(Piano_Key("left shift","converted_wav_notes/b3.wav",38))
keys.append(Piano_Key("z", "converted_wav_notes/_c4.wav",39))
keys.append(Piano_Key("x","converted_wav_notes/_d4.wav",40))
keys.append(Piano_Key("c","converted_wav_notes/_e4.wav",41))
keys.append(Piano_Key("v", "converted_wav_notes/_f4.wav", 42))
keys.append(Piano_Key("b", "converted_wav_notes/_g4.wav", 43))
keys.append(Piano_Key("n", "converted_wav_notes/_a4.wav", 44))
keys.append(Piano_Key("m", "converted_wav_notes/_b4.wav", 45))
keys.append(Piano_Key(",", "converted_wav_notes/_c5.wav", 46))
keys.append(Piano_Key(".", "converted_wav_notes/_d5.wav", 47))
keys.append(Piano_Key("/", "converted_wav_notes/_e5.wav", 48))
keys.append(Piano_Key("right shift","converted_wav_notes/_f5.wav",51))
piano = pygame.image.load("piano 1.jpg")
pygame.display.set_caption("Piano Emulator")


pygame.display.update()
while True:
    try:
        pygame.event.pump()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keyname = pygame.key.name(event.key)
                pressed_key = find_piano_key(keyname)
                pressed_key.play()
                pressed_key.dot_placement()
                pygame.display.update()
            if event.type == pygame.KEYUP:
                keyupname = pygame.key.name(event.key)
                released_key = find_piano_key(keyupname)
                released_key.stop()
                pygame.display.update()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    except KeyError:
        print("There is a key error")
