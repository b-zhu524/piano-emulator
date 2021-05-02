import pygame

pygame.init()

#Intro stuff for display
win = pygame.display.set_mode((1300, 700))
pygame.mixer.set_num_channels(88)
piano = pygame.image.load("Piano1.jpg")
piano = pygame.transform.scale(piano,(1300,200))

piano_x = 0
piano_y = 500
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
pygame.display.set_caption("Piano Emulator")

win.fill((255,255,255))
win.blit(piano, (piano_x, piano_y))
grey = (128, 128, 128)
pygame.display.update()

Big_Font = pygame.font.SysFont("Times New Roman, Arial", 60)
Big_Text = Big_Font.render("How to Play Happy Birthday!", True, black)
Small_Font = pygame.font.SysFont("Times New Roman, Arial", 30)
Small_First_text = Small_Font.render("a a d a h g a a d a k h ", True, black)
Small_Second_text = Small_Font.render("a a ; h g g d ' ' ; h k h ", True, black)
Introductory_text = Small_Font.render("Press these keys on your keyboard", True, black)


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
        pygame.draw.circle(win,red,(self.x_coordinate,self.y_coordinate),3)
    def dot_removal(self):
        if "sharp" in self.file_name:
            pygame.draw.circle(win,black,(self.x_coordinate,self.y_coordinate),3)
        else:
            pygame.draw.circle(win,white,(self.x_coordinate,self.y_coordinate),3)

keys = []


def find_piano_key(piano_key):
    global keys
    for character in keys:
        if character.key == piano_key:
            return character







#2nd octave
keys.append(Piano_Key("`","converted_wav_notes/_c2.wav",25,255))
keys.append(Piano_Key("1","converted_wav_notes/_c2sharp.wav",33,268))
keys.append(Piano_Key("2","converted_wav_notes/_d2.wav",40, 282))
keys.append(Piano_Key("3","converted_wav_notes/_d2sharp.wav",47,299))
keys.append(Piano_Key("4","converted_wav_notes/_e2.wav",54,312))
keys.append(Piano_Key("5","converted_wav_notes/_f2.wav",61,326))
keys.append(Piano_Key("6","converted_wav_notes/_f2sharp.wav",68,339))
keys.append(Piano_Key("7","converted_wav_notes/_g2.wav",75,352))
keys.append(Piano_Key("8","converted_wav_notes/_g2sharp.wav",82,367))
keys.append(Piano_Key("9","converted_wav_notes/_a2.wav",2,379))
keys.append(Piano_Key("0","converted_wav_notes/_a2sharp.wav",10,395))
keys.append(Piano_Key("-","converted_wav_notes/_b2.wav",18,406))

#3rd octave
keys.append(Piano_Key("q","converted_wav_notes/_c3.wav",26,422))
keys.append(Piano_Key("w", "converted_wav_notes/_c3sharp.wav",34,435))
keys.append(Piano_Key("e","converted_wav_notes/_d3.wav",41,448))
keys.append(Piano_Key("r", "converted_wav_notes/_d3sharp.wav",48,464))
keys.append(Piano_Key("t","converted_wav_notes/_e3.wav",55,475))
keys.append(Piano_Key("y","converted_wav_notes/_f3.wav",62,492))
keys.append(Piano_Key("u", "converted_wav_notes/_f3sharp.wav",69,506))
keys.append(Piano_Key("i","converted_wav_notes/_g3.wav",76,517))
keys.append(Piano_Key("o", "converted_wav_notes/_g3sharp.wav",83,532))
keys.append(Piano_Key("p", "converted_wav_notes/_a3.wav",3,544))
keys.append(Piano_Key("[", "converted_wav_notes/_a3sharp.wav",11,559))
keys.append(Piano_Key("]", "converted_wav_notes/_b3.wav",19,572))

#4th octave
keys.append(Piano_Key("a", "converted_wav_notes/_c4.wav",27,586))
keys.append(Piano_Key("s","converted_wav_notes/_c4sharp.wav",35,600))
keys.append(Piano_Key("d", "converted_wav_notes/_d4.wav",42,613))
keys.append(Piano_Key("f","converted_wav_notes/_d4sharp.wav",49,628))
keys.append(Piano_Key("g", "converted_wav_notes/_e4.wav",56,640))
keys.append(Piano_Key("h", "converted_wav_notes/_f4.wav",63,656))
keys.append(Piano_Key("j","converted_wav_notes/_f4sharp.wav",70,670))
keys.append(Piano_Key("k", "converted_wav_notes/_g4.wav",77,682))
keys.append(Piano_Key("l","converted_wav_notes/_g4sharp.wav",84,696))
keys.append(Piano_Key(";","converted_wav_notes/_a4.wav",4,708))
keys.append(Piano_Key("'","converted_wav_notes/_a4sharp.wav",12,722))
keys.append(Piano_Key("return","converted_wav_notes/_b4.wav",20,734))

#5th octave
keys.append(Piano_Key("c","converted_wav_notes/_c5.wav",28,750))
keys.append(Piano_Key("v","converted_wav_notes/_c5sharp.wav",36,765))
keys.append(Piano_Key("b","converted_wav_notes/_d5.wav",43,776))
keys.append(Piano_Key("n","converted_wav_notes/_d5sharp.wav",50,794))
keys.append(Piano_Key("m","converted_wav_notes/_e5.wav",57,804))
keys.append(Piano_Key(",","converted_wav_notes/_f5.wav",64,821))
keys.append(Piano_Key(".","converted_wav_notes/_f5sharp.wav",71,835))
keys.append(Piano_Key("/","converted_wav_notes/_g5.wav" , 78,847))
keys.append(Piano_Key("right shift","converted_wav_notes/_g5sharp.wav",85,861))
keys.append(Piano_Key("left shift","converted_wav_notes/_a5.wav",5,875))
keys.append(Piano_Key("z","converted_wav_notes/_a5sharp.wav",13,888))
keys.append(Piano_Key("x","converted_wav_notes/_b5.wav",21,900))
win.blit(Big_Text, (250, 50))
win.blit(Introductory_text, (400, 150))
win.blit(Small_First_text, (450, 250))
win.blit(Small_Second_text, (450, 300))
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
                released_key.dot_removal()
                pygame.display.update()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    except KeyError:
        print("Not binded key")



