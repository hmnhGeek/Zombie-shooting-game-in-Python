import pygame, random
from Tkinter import*
import os, pickle
import tkMessageBox
from PIL import ImageTk, Image
from uuid import getnode as get_mac
mac = get_mac()
given_time = 60
game_sound = 'on'
def game():
    def start():
        root.destroy()
        pygame.init()

        display_width=1200
        display_height=600
        AppleThickness = 20
        block_size=15
        x=pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('Shoot the Zombie!!')
        icon = pygame.image.load('zombie.png')
        pygame.display.set_icon(icon)

        img = pygame.image.load('zombie.png')
        #appleimg=pygame.image.load('Apple.png')

        clock=pygame.time.Clock()

        smallfont=pygame.font.SysFont('comicsansms', 25)
        medfont=pygame.font.SysFont('comicsansms', 50)
        largefont=pygame.font.SysFont('comicsansms', 80)



        def pause():
            paused=True
            msg_2_scr('Paused', (0,0,0), -100, 'large')
            msg_2_scr('Press C to continue or Q to quit.', (0,0,0), 25)
            pygame.display.update()
            while paused:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            paused = False
                        elif event.key == pygame.K_q:
                            pygame.quit()
                            quit()
                clock.tick(5)
                    

        def score(score):
            text = smallfont.render('Score: '+str(score), True, (200,100,77))
            x.blit(text, [0,0])

        def timer(seconds):
            text = smallfont.render('Time Left: '+str(seconds), True, (200,100,77))
            x.blit(text, [1030,0])

        def randAppleGen():
            applX = round(random.randrange(0, display_width-AppleThickness))
            applY = round(random.randrange(0, display_height-AppleThickness))
            return applX, applY

        def game_intro():
            intro=True
            while intro:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            intro = False

                        elif event.key == pygame.K_q:
                            pygame.quit()
                            quit()
                            
                        
                x.fill((255, 255, 255))
                msg_2_scr('Welcome to "Shoot the Zombie"!', (0, 255, 0), -100, 'large')
                msg_2_scr('The objective of the game is to shoot and kill as many',
                          (0, 0, 0), -30)
                msg_2_scr('zombies as possible that pop up and that too in a limited time.',
                          (0, 0, 0), 10)
                msg_2_scr('The more zombies you kill, the more you score.',
                          (0, 0, 0), 50)
                msg_2_scr('Press C to play, P to pause or Q to quit.',
                          (0, 0, 0), 180)
                pygame.display.update()
                clock.tick(15)

        def text_objects(text, color, size):
            if size == 'small':
                textSurface = smallfont.render(text, True, color)
            elif size == 'medium':
                textSurface = medfont.render(text, True, color)
            elif size == 'large':
                textSurface = largefont.render(text, True, color)
                
            return textSurface, textSurface.get_rect()

        def msg_2_scr(msg, clr, y_displace=0, size='small'):
            textSurf, textRect = text_objects(msg, clr, size)
            textRect.center = (display_width/2), (display_height/2) + y_displace
            x.blit(textSurf, textRect)

        pygame.mixer.music.load('zombieSound.mp3')
        def gameLoop():
            
            gameExit=False
            gameOver=False
            X, Y = randAppleGen()
            FPS=2
            scr = 0
            start_ticks=pygame.time.get_ticks() #starter tick
            
            while not gameExit:
                #print pygame.mouse.get_focused()
                if gameOver == True:
                    x.fill((255, 255, 255))
                    msg_2_scr('Time over', (255, 0,0), -100, size='large')
                    msg_2_scr('Press C to play again or Q to quit', (0, 0, 0), 0, size='medium')
                    msg_2_scr('Your Score: '+str(scr), (0, 0, 255), 100, size = 'medium')
                    pygame.display.update()
                while gameOver==True:

                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            gameExit=True
                            gameOver=False
                        if event.type==pygame.KEYDOWN:
                            if event.key==pygame.K_q:
                                gameExit=True
                                gameOver=False
                            elif event.key==pygame.K_c:
                                gameLoop()
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        gameExit=True
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_ESCAPE:
                            gameExit=True
                        elif event.key==pygame.K_p:
                            pause()
                cur = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                #pygame.time.delay(1000)
                if ((X + 100 > cur[0] > X) and (Y + 100 > cur[1] > Y)):
                    x.blit(img, (X, Y))
                    pygame.display.update()
                    if click[0] == 1:
                        pygame.display.update()
                        x.fill((255, 255, 255))
                        pygame.display.update()
                        scr+=1
                        if game_sound == 'on':
                            pygame.mixer.music.play()
                        else:
                            pass
                X, Y = randAppleGen()
                seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
                if seconds+1>given_time: # if more than 10 seconds close the game
                    gameOver = True
                leftTime = given_time - seconds
                x.fill((255, 255, 255))
                score(scr)
                timer(leftTime)
                x.blit(img, (X, Y))
                pygame.display.update()
                clock.tick(FPS)
                
            pygame.quit()
            quit()

        game_intro()
        gameLoop()
    root = Tk()
    root.title('Shoot the Zombie!! Menu')
    img = ImageTk.PhotoImage(Image.open('stz.png'))
    panel = Label(root, image = img)
    panel.pack(side = 'bottom', fill = 'both', expand = 'yes')
    rvar = IntVar()
    CVAR1 = IntVar()
    def first():
        global given_time
        given_time = 10
    def second():
        global given_time
        given_time = 20
    def third():
        global given_time
        given_time = 30
    def fourth():
        global given_time
        given_time = 40
    def fifth():
        global given_time
        given_time = 50
    def sixth():
        global given_time
        given_time = 60
    def sounds_off():
        global game_sound
        if CVAR1.get():
            game_sound = 'off'
        else:
            game_sound = 'on'
    def Help():
        f = open('Help.txt', 'r')
        s = f.read()
        f.close()
        helpWin = Tk()
        helpWin.title('Help Window')
        helpL = Label(helpWin, text = s).pack()
        helpWin.resizable(height = FALSE, width = FALSE)
        helpWin.mainloop()
    def about():
        f = open('aboutGame.txt', 'r')
        s = f.read()
        f.close()
        aboutWin = Tk()
        aboutWin.title('About Window')
        aboutL = Label(aboutWin, text = s).pack()
        aboutWin.resizable(height = FALSE, width = FALSE)
        aboutWin.mainloop()
    l = Label(root, text = 'Choose your time limit').pack()
    c1 = Radiobutton(root, text = '10 sec', variable = rvar, value = 1, command = first)
    c1.pack()
    c2 = Radiobutton(root, text = '20 sec', variable = rvar, value = 2, command = second)
    c2.pack()
    c3 = Radiobutton(root, text = '30 sec', variable = rvar, value = 3, command = third)
    c3.pack()
    c4 = Radiobutton(root, text = '40 sec', variable = rvar, value = 4, command = fourth)
    c4.pack()
    c5 = Radiobutton(root, text = '50 sec', variable = rvar, value = 5, command = fifth)
    c5.pack()
    c6 = Radiobutton(root, text = '60 sec', variable = rvar, value = 6, command = sixth)
    c6.pack()
    box = Checkbutton(root, text = 'Turn sound off', variable = CVAR1, onvalue = 1, offvalue = 0, height = 5, width = 20, command = sounds_off)
    box.pack()
    conf = Button(root, text = 'Play!!', command = start, width = 20, height = 2, bg = 'Green', fg = 'Red', activebackground = 'Red', activeforeground = 'White')
    conf.pack(pady = 5)
    hlp = Button(root, text = 'Help', command = Help, width = 20, height = 2, bg = 'Green', fg = 'Red', activebackground = 'Red', activeforeground = 'White')
    hlp.pack(pady = 5)
    abt = Button(root, text = 'About "Shoot the Zombie"', command = about, width = 20, height = 2, bg = 'Green', fg = 'Red', activebackground = 'Red', activeforeground = 'White')
    abt.pack(pady = 5)
    root.resizable(height = FALSE, width = FALSE)
    root.mainloop()
    
#------------------------------------------------------------
#Authentication check
f = open('MACFILE.dat', 'rb')
fw = open('temp.dat', 'wb')
try:
    while True:
        d = {}
        d = pickle.load(f)
        if d == {}:
            print 'Master permission required!!!'
            msterKey = raw_input('Enter master key: ')
            if msterKey == hex(mac).split('x')[1]:
                d.update({mac:'Registered'})
                pickle.dump(d, fw)
                tkMessageBox.showinfo('Alert', 'You are now registered, open game again, you will now be able to play it.')
            else:
                pickle.dump(d, fw)
        else:
            pickle.dump(d, fw)
            game()
except:
    f.close()
fw.close()
os.remove('MACFILE.dat')
os.rename('temp.dat', 'MACFILE.dat')
