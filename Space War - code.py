import pygame
from tkinter import *
from PIL import ImageTk, Image
import random
import time
import threading

#ventana principal
board = Tk()
# Tamaño de la ventana y nombre
board.geometry("700x750")
board.resizable(height=False, width=False)
board.title("SPACE WAR")
#tamaño de la pantalla
height = 750
width = 700
#transitores
pasar2=False
Pasar3=False
verificar_disparo1=False
verificar_disparo2=False
verificar_disparo3=False
transicion=True
transicion2=True
transicion3=True
transicion3_1=True
pausa=True
pausa2=True
pausa3=True
pase_n=True
pase_n2=True
pase_n3=True
pase_n3_1=True
#marcadores
Score = 0
Time = 0
Life = 50
Hostile =30
# "x" to move the airplane for "right and left"
x=10
# "y" to move the airplane for "UP and DOWN"
y=10

#Parametros de puntuaciones
Score_final=0
Bonos=0
#sonidos
pygame.mixer.init()
sonido_nave= pygame.mixer.Sound("Laser shot.mp3")
Press_botton=pygame.mixer.Sound("Boton.mp3")
sound_enem2=pygame.mixer.Sound("Bola de Fuego.mp3")
sound_enem3=pygame.mixer.Sound("Apagando sistema.mp3")
sound_enem1=pygame.mixer.Sound("Alien Apagado.mp3")
sound_enem3_disparo=pygame.mixer.Sound("PISTOLA LASER.mp3")

"Pantalla about"
def pasar_about_inicio():
    global about
    Press_botton.play()
    about.destroy()
    pantalla_inicio()

def pantalla_about():
    global fondo,about
    Press_botton.play()
    fondo.destroy()
    img_about = ImageTk.PhotoImage(Image.open("PlanetsGalaxyUniverse2.jpg")) 
    about = Canvas(board,height = height, width = width)
    about.pack()
    about_fondo= about.create_image(0,0,anchor=NW, image=img_about)
    información= Label(about,borderwidth=10,relief="sunken",bg="black",anchor=N, 
    text="About ?\n\n""Producido en Costa Rica \n\n Instituto Tecnológico de Costa Rica \n\n Área Académica de Ingeniería"
    " en Computadores \n\n Curso \n Introducción a la Programación"
    "\n\n Docente a cargo: Leonardo Araya Martínez \n\n Estudiante Creador: Ludwin José Ramos Briceño"
    "\n\n Grupo 03 \n\n Curso I-2021",height=19,width=50,fg="white",font=("Courier",13))
    información.place(x=100,y=100)
    regresar=Button(about,padx=12,pady=5,bd=5,bg="darkgrey", text = "Volver", font=("Franklin Gothic Medium",15 ), command=pasar_about_inicio)
    regresar.place(x=width /2-50, y=550)
    about.mainloop()

"NIVEL 3"

# pantalla donde termina el juego

def pantalla3_final_inicio():
    global salir3
    Press_botton.play()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Interstellar Main Theme.mp3") 
    pygame.mixer.music.play(100)
    salir3=False
    final.destroy()
    pantalla_inicio()

def pantalla_final():
    global final,Nivel_3,img_final3,Score_final,Bonos
    Press_botton.play()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Epic Space Emotional Music.mp3")
    pygame.mixer.music.play(10)
    Nivel_3.destroy()
    puntaje_final=Score_final + Bonos
    img_final = ImageTk.PhotoImage(Image.open("Pantalla de ganador.jpg")) 
    final = Canvas(board,height = height, width = width)
    final.pack()
    img_final3= final.create_image(0,0,anchor=NW, image=img_final)
    tabla= Label(final,borderwidth=10,relief="sunken",bg="black",anchor=N, 
    text= "¡Enhorabuena Soldado! \n\n Scores: {} \n\n Bono: {} \n\n Total Score: {}".format(Score_final,Bonos,puntaje_final),height=18,width=50,fg="white",font=("Courier",13))
    tabla.place(x=100,y=100)
    boton_volver=Button(final,padx=12,pady=5,bd=5,bg="darkgrey", text = "Volver", font=("Franklin Gothic Medium",15 ), command=pantalla3_final_inicio)
    boton_volver.place(x=width /2-50, y=550)

    final.mainloop()

def cambiara_derrota3():
    global transicion3
    if not transicion3:
        return derrota3()
    else:
        board.after(10,cambiara_derrota3)

def cambiara_nivel_final():
    global pase_n3
    if not pase_n3:
        return transiciona_nivel_final()
        #pase_n2=True
    else:
        board.after(10,cambiara_nivel_final)

def transiciona_nivel_final():
    continuar_final= Label(Nivel_3,borderwidth=10,relief="sunken",bg="black",anchor=N, text= "Ha sido un honor soldado, has salvado el Universo",height=4,width=50,fg="white",font=("Courier",13))
    continuar_final.place(x=100,y=300)
    continuara_final=Button(continuar_final,padx=10,pady=4,bd=5,bg="darkgrey", text = "Continuar", font=("Franklin Gothic Medium",10 ), command=pantalla_final)
    continuara_final.place(x=200 /2+120, y=200 /2-70)

#Transición de pantalla de juego a pantalla de inicio al presionar el boton "salir"
def pantalla3_inicio():
    global Score, Life3, Hostile, Time,Marcadores3,salir3
    Press_botton.play()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Interstellar Main Theme.mp3") 
    pygame.mixer.music.play(100)
    Score=0
    Time=0
    Life3=50
    Hostile=30
    Marcadores3.config(text="Score: {}   Time: {} seg  Life:{}    Hostile: {}   {}".format(Score, Time,Life3,Hostile,Player))
    Nivel_3.unbind_all("<Key>")
    salir3=False
    thread_3.isDaemon
    proyectiles3_1.isDaemon
    proyectiles3_2.isDaemon
    proyectiles3_3.isDaemon
    Villano3.isDaemon()
    Nivel_3.destroy()
    pantalla_inicio()

#Transición de pantalla de derrota a pantalla de inicio
def pantalla_derrota3_inicio():
    global Score, Life3, Hostile, Time
    Press_botton.play()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Interstellar Main Theme.mp3") 
    pygame.mixer.music.play(100)
    derrota_canv3.destroy()
    pantalla_inicio()

def derrota3():
    global derrota_canv3,Score
    pygame.mixer.music.stop()
    pygame.mixer.music.load("INFINITY Epic Futuristic Music.mp3")
    pygame.mixer.music.play()
    img_derrota3= ImageTk.PhotoImage(Image.open("Pantalla perdedor.jpg"))
    img_Lastima3= ImageTk.PhotoImage(Image.open("Derrota.png").resize((500,150)))
    img_titulo_derrota3= ImageTk.PhotoImage(Image.open("titulo derrota.png").resize((600,300)))  
    derrota_canv3= Canvas(board, width=width, height=height)
    derrota_canv3.pack()
    derrota_canv3.create_image(0,0,anchor=NW, image=img_derrota3)
    derrota_canv3.create_image(100,350,anchor=NW, image=img_Lastima3)
    derrota_canv3.create_image(60,50,anchor=NW, image=img_titulo_derrota3)
    score_nivel3= Label(derrota_canv3,borderwidth=10,relief="sunken",bg="black",anchor=N, text= "Score: {}".format(Score),height=1,width=15,fg="white",font=("Courier",13))
    score_nivel3.place(x=width/2-80,y=350)
    derrota_boton3=Button(derrota_canv3,bd=5,bg="darkgrey", text = "   ¡salir!   ", font=("Franklin Gothic Medium",15 ), command=pantalla_derrota3_inicio)
    derrota_boton3.place(x= width/2- 50, y= height/2+100)
    derrota_canv3.mainloop()

#Pausar tres
def detener3():
    Press_botton.play()
    global pausa3
    pausa3= not pausa3
    if pausa3==False:
        pygame.mixer.music.pause()
    if pausa3==True:
        pygame.mixer.music.unpause()

#colisión entre la nave y el enemigo nivel 3
def colision3():
    global punto_choque3_1,Life3, Marcadores3, esperar3,Hostile, transicion3,pase_n3,Bonos,Time
    choque_enem3_1=Nivel_3.bbox(enemigo3)
    choque_Nave3_1= Nivel_3.bbox(Nave3)
    #Colisiones para el nivel 3
    if choque_enem3_1[0] < choque_Nave3_1[2] < choque_enem3_1[2] and choque_enem3_1[1] <choque_Nave3_1[1] < choque_enem3_1[3] and punto_choque3_1: 
        #Nivel_1.move(Nave)
        Life3-=10
        Marcadores3.config(text="Score: {}   Time: {} seg  Life:{}    Hostile: {}   {}".format(Score, Time,Life3,Hostile,Player))
        punto_choque3_1=False #Punto_choque3_1 hace referecia al choque entre la nave y el enemigo
        esperar3=0
        print(Life3)
    if Life3<=0:
        Life3=0
        transicion3=False
    if Hostile<=0:
        if Life3==50:
            Bonos+=20
        if Time<=180:
            Bonos+=10
        pase_n3=False

#colisiones entre los disparos del enemigo y la nave del usuario

def ataque3(x_enemigo3,y_enemigo3,daño_enem3):
    global verificar_disparo3,Life3,Marcadores3,Hostile,Score,Nave3,transicion3,pase_n3,Bonos,Time
    sound_enem3_disparo.play()
    punto_choque3=True #Punto_choque3 hace referecia al choque entre la nave y los disparos del enemigo
    x2=0
    y2=7
    lazers_enem3= ImageTk.PhotoImage(Image.open("Disparos4.png").resize((50,60)))
    disparos_enem3= Nivel_3.create_image(x_enemigo3+50,y_enemigo3+50,anchor=NW, image=lazers_enem3,tags="disparos_enem3")
    x3, y3= Nivel_3.coords(disparos_enem3)
    choque_disparo3=Nivel_3.bbox(disparos_enem3)
    choque_Nave3=Nivel_3.bbox(Nave3)
    while y3<(height-150) and transicion3 and pase_n3:
        choque_disparo3=Nivel_3.bbox(disparos_enem3)
        choque_Nave3=Nivel_3.bbox(Nave3)
        x3, y3= Nivel_3.coords(disparos_enem3)
        Nivel_3.move(disparos_enem3,x2,y2)
        if choque_Nave3[0] < choque_disparo3[2] < choque_Nave3[2] and choque_Nave3[1] < choque_disparo3[1] < choque_Nave3[3] and punto_choque3:
            Life3 -=daño_enem3
            Marcadores3.config(text="Score: {}   Time: {} seg  Life:{}    Hostile: {}   {}".format(Score, Time,Life3,Hostile,Player))
            y3=(height+1)
            punto_choque3=False
        board.update()
        time.sleep(0.01)
    if y3>(height-150):
        Nivel_3.delete(disparos_enem3)
        board.update()
        time.sleep(0.01)
    punto_choque3=False
    if Life3<=0:
        transicion3=False
    elif Hostile<=0:
        if Life3==50:
            Bonos+=20
        if Time<=180:
            Bonos+=10
        pase_n3=False

#teletransporte del enmigo 3
def posicion_enem3():
    global posicion3
    lista=[100,550,250,50,300,400]
    posicion3=random.choice(lista)

# Llamada de los proyectiles del enemigo del nivel 3
def ataque3_aux():
    global proyectiles3_1,proyectiles3_2,proyectiles3_3
    proyectiles3_1 = threading.Thread(target=ataque3,args=(x_enemigo3,y_enemigo3,3))
    proyectiles3_1.start()
    time.sleep(0.33)
    proyectiles3_2 = threading.Thread(target=ataque3,args=(x_enemigo3,y_enemigo3,1))
    proyectiles3_2.start()
    time.sleep(0.33)
    proyectiles3_3 = threading.Thread(target=ataque3,args=(x_enemigo3,y_enemigo3,1))
    proyectiles3_3.start()

# Hostile moving level 3
def mover_enemigo3():
    global x_enemigo3, y_enemigo3,punto_choque3_1,esperar3,Time,transicion3,pausa3,pase_n3,pase_n3_1,posicion3,salir3,proyectiles3_1,proyectiles3_2,proyectiles3_3,Life3,thread_3
    punto_choque3_1=True # punto de colisión
    x2=3
    y2=0
    n1=0
    pausa3=True
    esperar3=0
    cont1=0
    envestir3_1=False # variable que detona la envestida
    x_enemigo3=500
    y_enemigo3=0
    segundos=0
    transicion3=True
    #transicion3_1=True
    pase_n3_1=True
    pase_n3=True
    salir3=True
    while transicion3 and pase_n3 and salir3:
        if pausa3:
            Nivel_3.move(enemigo3,x2,y2)
            x_enemigo3, y_enemigo3 = Nivel_3.coords(enemigo3)
            if segundos==600:
                n1=0
                envestir3_1=True
            if cont1>=200:
                cont1=0
                esperar3=0
            if segundos%100==0 and not envestir3_1:
                #ataque3_aux()
                thread_3=threading.Thread(target=ataque3_aux)
                thread_3.start()

            if envestir3_1:
                sound_enem3.play()
                #print("si pasa")
                #print(y_enemigo3)
                #print(n1)
                if y_enemigo3==0 and n1==0:
                    x2=0
                    y2=7
                    print(y2)
                    n1+=1
                elif y_enemigo3>(height-230):
                    x2=0
                    y2=-7
                    print(y2)
                    #Nivel_3.move(enemigo3,x2,y2)
                    
                elif y_enemigo3<=0:
                    decision=[1,2] #es lo que hará el enemigo al terminar la envestida 50% porciento para escoger
                    A_lazar =random.choice(decision)
                    if A_lazar==1:
                        velocidades=[-3,3]
                        x2=random.choice(velocidades)
                        y2=0
                        #Nivel_3.move(enemigo3,x2,y2)
                    elif A_lazar==2:
                        posicion_enem3()
                        velocidades=[-3,3]
                        x2=random.choice(velocidades)
                        x_enemigo3 = posicion3
                        y_enemigo3 = 0
                        y2=0
                        #Nivel_3.move(enemigo3,x2,y2)
                    #Nivel_1.move(enemigo1,x2,y2)
                    segundos=0
                    envestir3_1=False
                colision3()
            else:
                if esperar3 >= 60 and punto_choque3_1==True:
                    colision3() 
                if x_enemigo3>(width-150):
                    x2=-3
                    y2=0
                    Nivel_3.move(enemigo3,x2,y2)
                elif x_enemigo3<0:
                    x2=3
                    y2=0
                    Nivel_3.move(enemigo3,x2,y2)
            board.update()
            time.sleep(0.01)
            if not envestir3_1:
                esperar3+=1
                cont1+=1
                punto_choque3_1=True
            #if segundos==600:
            #    segundos=0
            segundos+=1
            if segundos%100==0:
                Time+=1
                Marcadores3.config(text="Score: {}   Time: {} seg  Life:{}    Hostile: {}   {}".format(Score, Time,Life3,Hostile,Player))
            if Time>300:
                Life3=0
                transicion3=False
        else:
            time.sleep(0.01)

    if Hostile<=0:
        Nivel_3.unbind_all("<Key>")
        thread_3.isDaemon
        proyectiles3_1.isDaemon
        proyectiles3_2.isDaemon
        proyectiles3_3.isDaemon
        Life3=10
    elif Life3<=0:
        Nivel_3.unbind_all("<Key>")
        Nivel_3.destroy()
        thread_3.isDaemon
        proyectiles3_1.isDaemon
        proyectiles3_2.isDaemon
        proyectiles3_3.isDaemon
        

def pantalla_3():
    global Nivel_3, Nave3, enemigo3, disparo3, Marcadores3,Score,Time,Life3,Hostile,Pasar3,Bonos,Villano3
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Zathura Soundtrack 11.mp3")
    pygame.mixer.music.play(loops=100)
    if Pasar3:
        Bonos=0
        fondo.destroy()
        Pasar3=False
    else:
        Press_botton.play()
        Nivel_2.destroy()
    Score = 0
    Time = 0
    Life3= 50
    Hostile =5
    imagen3 = ImageTk.PhotoImage(Image.open("Nivel 3L.png"))
    overlay3 = ImageTk.PhotoImage(Image.open("overlay2.png").resize((695,100)))
    Nivel_3= Canvas(board, width=width, height=height)
    Nivel_3.pack()
    Nivel_3.create_image(0,0,anchor=NW, image=imagen3)
    Nivel_3.create_image(2,650,anchor=NW, image=overlay3)
    #Marcadores del nivel 2
    Marcadores3= Label(Nivel_3,bg="black",fg="White", text="Score: {}   Time: {} seg  Life:{}    Hostile: {}   {}".format(Score, Time,Life3,Hostile,Player),font=("Courier",13))
    Marcadores3.place(x=50,y=670)
    #Boton salir y detener
    regreso_boton3=Button(Nivel_3,bd=5,bg="lightGoldenrod2", text = "   ¡salir!   ", font=("Franklin Gothic Medium",8 ), command=pantalla3_inicio)
    regreso_boton3.place(x= 250, y= height-50)
    detener_boton3=Button(Nivel_3,bd=5,bg="lightGoldenrod2", text = "   ¡Pausa!   ", font=("Franklin Gothic Medium",8 ),command=detener3)
    detener_boton3.place(x= 350, y= height-50)
    #nave del usuario
    Naveimg3 = ImageTk.PhotoImage(Image.open("Nave1.png").resize((100,100)))
    Nave3= Nivel_3.create_image(400,450,anchor=NW, image=Naveimg3)
    #nave del enemigo
    nave_enemiga3= ImageTk.PhotoImage(Image.open("Enemigo3.png").resize((150,150)))
    enemigo3= Nivel_3.create_image(200,0,anchor=NW, image=nave_enemiga3)
    #mover nave y Disparos
    Nivel_3.bind_all("<Key>",mover3)

    #mover enemigo
    Villano3= threading.Thread(target=mover_enemigo3)
    Villano3.start()

    #cambiar de pantallas al terminar el nivel
    cambiara_derrota3()
    cambiara_nivel_final()

    Nivel_3.mainloop()

# disparos de la nave del usuario nivel 2
def disparo3(x1,y1):
    global verificar_disparo3,Life3,Marcadores3,Hostile,Score,Score_final
    x2=0
    y2=-7
    cohete3= ImageTk.PhotoImage(Image.open("Disparo.png").resize((50,50)))
    disparo_3= Nivel_3.create_image(x1+25,y1,anchor=NW, image=cohete3,tags="disparo_3")
    x3, y3= Nivel_3.coords(disparo_3)
    choque_disparo3=Nivel_3.bbox(disparo_3)
    choque_enem3=Nivel_3.bbox(enemigo3)
    while y3>0:
        choque_disparo3=Nivel_3.bbox(disparo_3)
        choque_enem3=Nivel_3.bbox(enemigo3)
        x3, y3= Nivel_3.coords(disparo_3)
        Nivel_3.move(disparo_3,x2,y2)
                    
        if choque_enem3[0] < choque_disparo3[2] < choque_enem3[2] and choque_enem3[1] <choque_disparo3[1] < choque_enem3[3] and verificar_disparo3==True:
            Hostile -=1
            Score+=1
            Score_final+=1
            Marcadores3.config(text="Score: {}   Time: {} seg  Life:{}    Hostile: {}   {}".format(Score, Time,Life3,Hostile,Player))
            print(Hostile)
            verificar_disparo3=False
            y3=-1
        board.update()
        time.sleep(0.01)
    if y3<0:
        Nivel_3.delete("disparo_3")
        board.update()
        time.sleep(0.01)
    verificar_disparo3=False

#controles de movimiento y disparo de la nave del usuario del nivel 3
def mover3(event):
    global verificar_disparo3
    x1, y1= Nivel_3.coords(Nave3)
    if event.keysym=='Left' and pausa3:
        if x1<0:
            x1=0
            Nivel_3.coords(Nave3, x1,y1)
        Nivel_3.coords(Nave3, x1-x,y1)
    elif event.keysym=="Right" and pausa3:
        if x1>(width-100):
            x1=width-100
            Nivel_3.coords(Nave3, x1,y1)
        Nivel_3.coords(Nave3, x1+x,y1)
    elif event.keysym=="Up" and pausa3:
        if y1<0:
            y1=0
            Nivel_3.coords(Nave3, x1,y1)
        Nivel_3.coords(Nave3, x1,y1-y)
    elif event.keysym=="Down" and pausa3:
        if y1>height-200:
            y1=height-200
            Nivel_3.coords(Nave3, x1,y1)
        Nivel_3.coords(Nave3, x1,y1+y)
    elif event.keysym=="space" and pausa3:
        if not verificar_disparo3:
            sonido_nave.play()
            verificar_disparo3=True
            disparo_var3 = threading.Thread(target=disparo3,args=(x1,y1))
            disparo_var3.start()

"NIVEL 2"

#Transición de pantalla de juego a pantalla de derrota
def cambiara_derrota2():
    global transicion2,Villano2
    if not transicion2:
        Villano2.isDaemon
        proyectiles2_1.isDaemon
        proyectiles2_2.isDaemon
        proyectiles2_3.isDaemon
        transicion2=True
        return derrota2()
    else:
        board.after(10,cambiara_derrota2)

def cambiara_nivel3():
    global pase_n2
    if not pase_n2:
        return transiciona_nivel3()
        #pase_n2=True
    else:
        board.after(10,cambiara_nivel3)

# transición a nivel 3
def transiciona_nivel3():
    continuar_nivel2= Label(Nivel_2,borderwidth=10,relief="sunken",bg="black",anchor=N, text= "¡FELICIDADES! Continua al siguiente nivel soldado",height=4,width=50,fg="white",font=("Courier",13))
    continuar_nivel2.place(x=100,y=300)
    continuara_nivel2=Button(continuar_nivel2,padx=10,pady=4,bd=5,bg="darkgrey", text = "Continuar", font=("Franklin Gothic Medium",10 ), command=pantalla_3)
    continuara_nivel2.place(x=200 /2+120, y=200 /2-70)

# Transición de pantalla del nivel 2 a pantalla de inicio al presionar el boton "salir"
def pantalla2_inicio():
    global Score, Life, Hostile, Time,Marcadores2,salir2
    Press_botton.play()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Interstellar Main Theme.mp3") 
    pygame.mixer.music.play(100)
    Score=0
    Time=0
    Life=50
    Hostile=30
    Marcadores2.config(text="Score: {}   Time: {} seg  Life:{}    Hostile: {}   {}".format(Score, Time,Life2,Hostile,Player))
    Nivel_2.unbind_all("<Key>")
    salir2=False
    thread_1.isDaemon
    proyectiles2_1.isDaemon
    proyectiles2_2.isDaemon
    proyectiles2_3.isDaemon
    Nivel_2.destroy()
    pantalla_inicio()

#Transición de pantalla de derrota a pantalla de inicio
def pantalla_derrota2_inicio():
    global Score, Life2, Hostile, Time,Marcadores2
    Press_botton.play()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Interstellar Main Theme.mp3") 
    pygame.mixer.music.play(100)
    Score=0
    Time=0
    Life2=50
    Hostile=30
    derrota_canv2.destroy()
    pantalla_inicio()

#pantalla de derrota del nivel 2
def derrota2():
    global derrota_canv2,Score
    pygame.mixer.music.stop()
    pygame.mixer.music.load("INFINITY Epic Futuristic Music.mp3")
    pygame.mixer.music.play()
    img_derrota2= ImageTk.PhotoImage(Image.open("Pantalla perdedor.jpg"))
    img_Lastima2= ImageTk.PhotoImage(Image.open("Derrota.png").resize((500,150)))
    img_titulo_derrota2= ImageTk.PhotoImage(Image.open("titulo derrota.png").resize((600,300)))  
    derrota_canv2= Canvas(board, width=width, height=height)
    derrota_canv2.pack()
    derrota_canv2.create_image(0,0,anchor=NW, image=img_derrota2)
    derrota_canv2.create_image(100,350,anchor=NW, image=img_Lastima2)
    derrota_canv2.create_image(60,50,anchor=NW, image=img_titulo_derrota2)
    score_nivel2= Label(derrota_canv2,borderwidth=10,relief="sunken",bg="black",anchor=N, text= "Score: {}".format(Score),height=1,width=15,fg="white",font=("Courier",13))
    score_nivel2.place(x=width/2-80,y=350)
    derrota_boton2=Button(derrota_canv2,bd=5,bg="darkgrey", text = "   ¡salir!   ", font=("Franklin Gothic Medium",15 ), command=pantalla_derrota2_inicio)
    derrota_boton2.place(x= width/2- 50, y= height/2+100)
    derrota_canv2.mainloop()

# Pausar nivel 2
def detener2():
    Press_botton.play()
    global pausa2
    pausa2= not pausa2
    if pausa2==False:
        pygame.mixer.music.pause()
    if pausa2==True:
        pygame.mixer.music.unpause()

def ataque2(x_enemigo2,y_enemigo2,daño_enem2):
    global verificar_disparo2,Life2,Marcadores2,Hostile,Score,Nave2,transicion2,pase_n2,Bonos,Time
    sound_enem2.play()
    punto_choque2=True
    x2=0
    y2=7
    lazers_enem2= ImageTk.PhotoImage(Image.open("Disparos3.png").resize((50,60)))
    disparos_enem2= Nivel_2.create_image(x_enemigo2+50,y_enemigo2+20,anchor=NW, image=lazers_enem2,tags="disparos_enem2")
    x3, y3= Nivel_2.coords(disparos_enem2)
    choque_disparo2=Nivel_2.bbox(disparos_enem2)
    choque_Nave2=Nivel_2.bbox(Nave2)
    while y3<(height-150) and transicion2 and pase_n2:
        choque_disparo2=Nivel_2.bbox(disparos_enem2)
        choque_Nave2=Nivel_2.bbox(Nave2)
        x3, y3= Nivel_2.coords(disparos_enem2)
        Nivel_2.move(disparos_enem2,x2,y2)
        if choque_Nave2[0] < choque_disparo2[2] < choque_Nave2[2] and choque_Nave2[1] < choque_disparo2[1] < choque_Nave2[3] and punto_choque2:
            Life2 -=daño_enem2
            Marcadores2.config(text="Score: {}   Time: {} seg  Life:{}    Hostile: {}   {}".format(Score, Time,Life2,Hostile,Player))
            y3=(height+1)
            punto_choque2=False
        board.update()
        time.sleep(0.01)
    if y3>(height-150):
        Nivel_2.delete(disparos_enem2)
        board.update()
        time.sleep(0.01)
    punto_choque2=False
    if Life2<=0:
        Life2=0
        Marcadores2.config(text="Score: {}   Time: {} seg  Life:{}    Hostile: {}   {}".format(Score, Time,Life2,Hostile,Player))
        transicion2=False
    elif Hostile<=0:
        if Life2==50:
            Bonos+=20
        if Time<=180:
            Bonos+=10
        pase_n2=False

#Random positions of hostile 2
def posicion_enem2():
    global posicion
    lista=[100,550,250,50,300,400]
    posicion=random.choice(lista)

# Transitory function when the hostile fire
def ataque2_aux():
    global proyectiles2_1,proyectiles2_2,proyectiles2_3
    proyectiles2_1 = threading.Thread(target=ataque2,args=(x_enemigo2,y_enemigo2,3))
    proyectiles2_2 = threading.Thread(target=ataque2,args=(x_enemigo2,y_enemigo2,1))
    proyectiles2_3 = threading.Thread(target=ataque2,args=(x_enemigo2,y_enemigo2,1))
    time.sleep(0.33)
    proyectiles2_1.start()
    time.sleep(0.33)
    proyectiles2_2.start()
    time.sleep(0.33)
    proyectiles2_3.start()

# Hostile moving level 2
def mover_enemigo2():
    global x_enemigo2, y_enemigo2,Life2,esperar2,Time,transicion2,pausa2,pase_n2,posicion,salir2,proyectiles2_1,proyectiles2_2,proyectiles2_3,thread_1
    cont1=0
    x_enemigo2=500
    y_enemigo2=0
    n1=0
    segundos=0
    transicion2=True
    pase_n2=True
    salir2=True
    while transicion2 and pase_n2 and salir2:
        if pausa2:
            x_enemigo2, y_enemigo2 =Nivel_2.coords(enemigo2)
            if cont1>=200:
                cont1=1
                posicion_enem2()
                x_enemigo2 = posicion
                Nivel_2.coords(enemigo2,x_enemigo2,y_enemigo2)
            
            if segundos%200==0:
                
                thread_1=threading.Thread(target=ataque2_aux)
                thread_1.start()

            board.update()
            time.sleep(0.01)
            cont1+=1
            segundos+=1
            if segundos==1000:
                segundos=0
            if segundos%100==0:
                Time+=1
                Marcadores2.config(text="Score: {}   Time: {} seg  Life:{}    Hostile: {}   {}".format(Score, Time,Life2,Hostile,Player))
            if Time>300:
                Life2=0
                transicion2=False
        else:
            time.sleep(0.01)
    if Hostile<=0:
        Nivel_2.unbind_all("<Key>")
        thread_1.isDaemon
        proyectiles2_1.isDaemon
        proyectiles2_2.isDaemon
        proyectiles2_3.isDaemon
    elif Life2<=0:
        Nivel_2.unbind_all("<Key>")
        Nivel_2.destroy()
        thread_1.isDaemon
        proyectiles2_1.isDaemon
        proyectiles2_2.isDaemon
        proyectiles2_3.isDaemon

        
# Level 2 Screen
def pantalla_2():
    global Nivel_2, Nave2, enemigo2, disparo2, Marcadores2,Score,Time,Life2,Hostile,Villano2,pasar2,Bonos
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Zathura Soundtrack 8.mp3")
    pygame.mixer.music.play()
    if pasar2:
        Bonos=0
        fondo.destroy()
        pasar2=False
    else:
        Press_botton.play()
        Nivel_1.destroy()
    Score = 0
    Time = 0
    Life2= 50
    Hostile =5
    imagen2 = ImageTk.PhotoImage(Image.open("Nivel 2L.jpg"))
    overlay2 = ImageTk.PhotoImage(Image.open("overlay2.png").resize((695,100)))
    Nivel_2= Canvas(board, width=width, height=height)
    Nivel_2.pack()
    Nivel_2.create_image(0,0,anchor=NW, image=imagen2)
    Nivel_2.create_image(2,650,anchor=NW, image=overlay2)
    #Marcadores del nivel 2
    Marcadores2= Label(Nivel_2,bg="black",fg="White", text="Score: {}   Time: {} seg  Life:{}    Hostile: {}   {}".format(Score, Time,Life2,Hostile,Player),font=("Courier",13))
    Marcadores2.place(x=50,y=670)
    #Boton salir y detener
    regreso_boton2=Button(Nivel_2,bd=5,bg="lightGoldenrod2", text = "   ¡salir!   ", font=("Franklin Gothic Medium",8 ), command=pantalla2_inicio)
    regreso_boton2.place(x= 250, y= height-50)
    detener_boton2=Button(Nivel_2,bd=5,bg="lightGoldenrod2", text = "   ¡Pausa!   ", font=("Franklin Gothic Medium",8 ),command=detener2)
    detener_boton2.place(x= 350, y= height-50)
    #nave del usuario
    Naveimg2 = ImageTk.PhotoImage(Image.open("Nave1.png").resize((100,100)))
    Nave2= Nivel_2.create_image(400,450,anchor=NW, image=Naveimg2)
    #nave del enemigo
    nave_enemiga2= ImageTk.PhotoImage(Image.open("Enemigo2.png").resize((150,150)))
    enemigo2= Nivel_2.create_image(200,0,anchor=NW, image=nave_enemiga2)
    #mover nave y Disparos
    
    Nivel_2.bind_all("<Key>",mover2)

    #mover enemigo
    
    Villano2= threading.Thread(target=mover_enemigo2)
    Villano2.start()
    #cambiar de pantallas al terminar el nivel
    cambiara_derrota2()
    cambiara_nivel3()

    Nivel_2.mainloop()

# disparos de la nave del usuario nivel 2
def disparo2(x1,y1):
    global verificar_disparo2,Life2,Marcadores2,Hostile,Score,Score_final
    x2=0
    y2=-7
    cohete2= ImageTk.PhotoImage(Image.open("Disparo.png").resize((50,50)))
    disparo_2= Nivel_2.create_image(x1+25,y1,anchor=NW, image=cohete2,tags="disparo_2")
    x3, y3= Nivel_2.coords(disparo_2)
    choque_disparo2=Nivel_2.bbox(disparo_2)
    choque_enem2=Nivel_2.bbox(enemigo2)
    while y3>0:
        choque_disparo2=Nivel_2.bbox(disparo_2)
        choque_enem2=Nivel_2.bbox(enemigo2)
        x3, y3= Nivel_2.coords(disparo_2)
        Nivel_2.move(disparo_2,x2,y2)
                    
        if choque_enem2[0] < choque_disparo2[2] < choque_enem2[2] and choque_enem2[1] <choque_disparo2[1] < choque_enem2[3] and verificar_disparo2==True:
            Hostile -=1
            Score+=1
            Score_final+=1
            Marcadores2.config(text="Score: {}   Time: {} seg  Life:{}    Hostile: {}   {}".format(Score, Time,Life2,Hostile,Player))
            print(Hostile)
            verificar_disparo2=False
            y3=-1
        board.update()
        time.sleep(0.01)
    if y3<0:
        Nivel_2.delete("disparo_2")
        board.update()
        time.sleep(0.01)
    verificar_disparo2=False

#controles de movimiento y disparo de la nave del usuario del nivel 2
def mover2(event):
    global verificar_disparo2
    x1, y1= Nivel_2.coords(Nave2)
    if event.keysym=='Left' and pausa2:
        if x1<0:
            x1=0
            Nivel_2.coords(Nave2, x1,y1)
        Nivel_2.coords(Nave2, x1-x,y1)
    elif event.keysym=="Right" and pausa2:
        if x1>(width-100):
            x1=width-100
            Nivel_2.coords(Nave2, x1,y1)
        Nivel_2.coords(Nave2, x1+x,y1)
    elif event.keysym=="Up" and pausa2:
        if y1<0:
            y1=0
            Nivel_2.coords(Nave2, x1,y1)
        Nivel_2.coords(Nave, x1,y1-y)
    elif event.keysym=="Down" and pausa2:
        if y1>height-200:
            y1=height-200
            Nivel_2.coords(Nave2, x1,y1)
        Nivel_2.coords(Nave2, x1,y1+y)
    elif event.keysym=="space" and pausa2:
        if not verificar_disparo2:
            sonido_nave.play()
            verificar_disparo2=True
            disparo_var2 = threading.Thread(target=disparo2,args=(x1,y1))
            disparo_var2.start()


"NIVEL 1"

#transiciones necesarias de diferentes pantallas
def cambiara_derrota():
    global transicion
    if not transicion:
        Villano1.isDaemon
        return derrota1()
    else:
        board.after(10,cambiara_derrota)
# transición a nivel 2
def cambiara_nivel2():
    global pase_n
    if not pase_n:
        pase_n=True
        return transiciona_nivel2()
    else:
        board.after(5,cambiara_nivel2)

#Mensaje que salta al ganar en el nivel 1 para pasar al nivel 2
def transiciona_nivel2():
    continuar_nivel= Label(Nivel_1,borderwidth=10,relief="sunken",bg="black",anchor=N, text= "¡FELICIDADES! Continua al siguiente nivel soldado",height=4,width=50,fg="white",font=("Courier",13))
    continuar_nivel.place(x=100,y=300)
    continuara_nivel=Button(continuar_nivel,padx=10,pady=4,bd=5,bg="darkgrey", text = "Continuar", font=("Franklin Gothic Medium",10 ), command=pantalla_2)
    continuara_nivel.place(x=200 /2+120, y=200 /2-70)

#De la pantalla de derrota 1 a pantalla de inicio
def pantalla_derrota1_inicio():
    Press_botton.play()
    global Score, Life, Hostile, Time,Marcadores
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Interstellar Main Theme.mp3") 
    pygame.mixer.music.play(100)
    Score=0
    Time=0
    Life=50
    Hostile=30
    derrota_canv.destroy()
    pantalla_inicio()

#Volver a pantalla de juego a pantalla de inicio al presionar el boton "salir".
def pantalla1_inicio():
    Press_botton.play()
    global Score, Life, Hostile, Time,Marcadores,salir1
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Interstellar Main Theme.mp3") 
    pygame.mixer.music.play(100)
    salir1=False
    Score=0
    Time=0
    Life=50
    Hostile=30
    Marcadores.config(text="Score: {}   Time: {} seg  Life:{}    Hostile: {}   {}".format(Score, Time,Life,Hostile,Player))
    Nivel_1.unbind_all("<Key>")
    Nivel_1.destroy()
    pantalla_inicio()

#Detener el juego
def detener():
    Press_botton.play()
    global pausa
    pausa=not pausa
    if pausa==False:
        pygame.mixer.music.pause()
    if pausa==True:
        pygame.mixer.music.unpause()

"Pantalla de derrota"
def derrota1():
    global derrota_canv,Score
    pygame.mixer.music.stop()
    pygame.mixer.music.load("INFINITY Epic Futuristic Music.mp3")
    pygame.mixer.music.play(100)
    img_derrota= ImageTk.PhotoImage(Image.open("Pantalla perdedor.jpg"))
    img_Lastima1= ImageTk.PhotoImage(Image.open("Derrota.png").resize((500,150)))
    img_titulo_derrota= ImageTk.PhotoImage(Image.open("titulo derrota.png").resize((600,300)))
    derrota_canv= Canvas(board, width=width, height=height)
    derrota_canv.pack()
    derrota_canv.create_image(0,0,anchor=NW, image=img_derrota)
    derrota_canv.create_image(100,350,anchor=NW, image=img_Lastima1)
    derrota_canv.create_image(60,50,anchor=NW, image=img_titulo_derrota)
    score_nivel1= Label(derrota_canv,borderwidth=10,relief="sunken",bg="black",anchor=N, text= "Score: {}".format(Score),height=1,width=15,fg="white",font=("Courier",13))
    score_nivel1.place(x=width/2-80,y=350)
    derrota_boton1=Button(derrota_canv,bd=5,bg="darkgrey", text = "   ¡salir!   ", font=("Franklin Gothic Medium",15 ), command=pantalla_derrota1_inicio)
    derrota_boton1.place(x= width/2- 50, y= height/2+100)
    derrota_canv.mainloop()

"pantalla de juego del nivel 1"
#ataque nivel 1
def ataque1():
    envestir1=random.choice(range(1,11))
    if (envestir1%3)==0:
        return True
    else: 
        return False
 
 #colisión entre la nave y el enemigo
def colision1():
    global punto_choque,Life, Marcadores, esperar,Hostile, transicion,pase_n,Time,Bonos
    choque_enem=Nivel_1.bbox(enemigo1)
    choque_nave= Nivel_1.bbox(Nave)
    #Colisiones para el nivel 1
    if choque_enem[0] < choque_nave[2] < choque_enem[2] and choque_enem[1] <choque_nave[1] < choque_enem[3] and punto_choque==True: 
        Life-=10
        Hostile-=1
        Marcadores.config(text="Score: {}   Time: {} seg  Life:{}    Hostile: {}   {}".format(Score, Time,Life,Hostile,Player))
        punto_choque=False
        esperar=0
        print(Life)

    if Life<=0:
        Life=0
        Marcadores.config(text="Score: {}   Time: {} seg  Life:{}    Hostile: {}   {}".format(Score, Time,Life,Hostile,Player))
        transicion=False
    elif Hostile<=0:
        if Life==50:
            Bonos+=20
        if Time<=120:
            Bonos+=10
        pase_n=False
    
#movimiento enemigo nivel 1
def mover_enemigo1():
    global x_enemigo1, y_enemigo1,punto_choque,esperar,Time,transicion,Life,pausa,pase_n,salir1
    x2=3
    y2=0
    cont1=0
    n1=0
    ataque2=False
    punto_choque=False
    esperar=0
    segundos=0
    transicion=True
    pase_n=True
    pausa=True
    salir1=True
    while transicion and pase_n and salir1:
        if pausa:
            #print(f"ataque {ataque2},cont1{cont1}")
            Nivel_1.move(enemigo1,x2,y2)
            x_enemigo1, y_enemigo1 =Nivel_1.coords(enemigo1)
            if cont1>=200 and not ataque2:
                cont1=0
                ataque2= ataque1()
                print(ataque2)
                n1=0
                y_enemigo1=0
                esperar=0
                #print(f"ataque {ataque2},cont1 {cont1}")
            if ataque2:
                sound_enem1.play()
                if y_enemigo1==0 and n1==0:
                    x2=0
                    y2=6
                    n1+=1
                if y_enemigo1>(height-200):
                    x2=0
                    y2=-6
                    #Nivel_1.move(enemigo1,x2,y2)
                    
                elif y_enemigo1<0:
                    velocidades=[-3,3]
                    x2=random.choice(velocidades)
                    y2=0
                    #Nivel_1.move(enemigo1,x2,y2)
                    
                    ataque2=False
                colision1()   
            else:
                if esperar >= 60 and punto_choque==True:
                    colision1() 
                if x_enemigo1>(width-150):
                    x2=-3
                    y2=0
                    Nivel_1.move(enemigo1,x2,y2)
                elif x_enemigo1<0:
                    x2=3
                    y2=0
                    Nivel_1.move(enemigo1,x2,y2)
            board.update()
            time.sleep(0.01)
            if not ataque2:
                esperar+=1
                cont1+=1
                punto_choque=True
            segundos+=1
            if segundos==1000:
                segundos=100
            if segundos%100==0:
                Time+=1
                Marcadores.config(text="Score: {}   Time: {} seg  Life:{}    Hostile: {}   {}".format(Score, Time,Life,Hostile,Player))
            if Time>30:
                Life=0
                transicion=False
        else:
            time.sleep(0.01)
    if Hostile<=0:
        pase_n=False
        Villano1.isDaemon
        Nivel_1.unbind_all("<Key>")
    elif Life<=0:
        Nivel_1.destroy()
        transicion=False
        Nivel_1.unbind_all("<Key>")
        
    "pantalla de juego del nivel 1"        
def pantalla_1():
    global Nivel_1, Nave, enemigo1, disparo, Marcadores,Life,Time,Score,Hostile,Villano1,Bonos
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Zathura Soundtrack 1.mp3")
    pygame.mixer.music.play(100)
    fondo.destroy()
    Bonos=0
    Score = 0
    Time = 0
    Life = 30
    Hostile =5
    imagen1 = ImageTk.PhotoImage(Image.open("Nivel 1L.jpg"))
    Overlay = ImageTk.PhotoImage(Image.open("overlay2.png").resize((695,100)))
    Nivel_1= Canvas(board, width=width, height=height)
    Nivel_1.pack()
    Nivel_1.create_image(0,0,anchor=NW, image=imagen1)
    Nivel_1.create_image(2,650,anchor=NW, image=Overlay)
    #Marcadores del nivel 1
    Marcadores= Label(Nivel_1,bg="black",fg="White", text="Score: {}   Time: {} seg  Life:{}    Hostile: {}   {}".format(Score, Time,Life,Hostile,Player),font=("Courier",13))
    Marcadores.place(x=50,y=670)
    #Boton salir y detener
    regreso_boton1=Button(Nivel_1,bd=5,bg="lightGoldenrod3", text = "   ¡salir!   ", font=("Franklin Gothic Medium",8 ), command=pantalla1_inicio)
    regreso_boton1.place(x= 250, y= height-50)
    detener_boton1=Button(Nivel_1,bd=5,bg="lightGoldenrod3", text = "   ¡Pausa!   ", font=("Franklin Gothic Medium",8 ), command=detener)
    detener_boton1.place(x= 350, y= height-50)
    #nave del usuario

    Naveimg = ImageTk.PhotoImage(Image.open("Nave1.png").resize((100,100)))
    Nave= Nivel_1.create_image(400,450,anchor=NW, image=Naveimg)
    #nave del enemigo
    nave_enemiga1= ImageTk.PhotoImage(Image.open("Enemigo1.png").resize((150,125)))
    enemigo1= Nivel_1.create_image(200,0,anchor=NW, image=nave_enemiga1)
    
    #mover nave y Disparos
    Nivel_1.bind_all("<Key>",mover)
    
    #mover enemigo
    Villano1= threading.Thread(target=mover_enemigo1)
    Villano1.start()
    #cambiar de pantallas al terminar el nivel
    cambiara_derrota()
    cambiara_nivel2()
    Nivel_1.mainloop()
    
#Control de disparo

def disparo1(x1,y1):
    global verificar_disparo1,Life,Marcadores,Hostile,Score,pase_n,Score_final
    x2=0
    y2=-5
    cohete= ImageTk.PhotoImage(Image.open("Disparo.png").resize((50,50)))
    disparo= Nivel_1.create_image(x1+25,y1,anchor=NW, image=cohete,tags="disparo")
    x3, y3= Nivel_1.coords(disparo)
    choque_disparo=Nivel_1.bbox(disparo)
    choque_enem=Nivel_1.bbox(enemigo1)
    
    while y3>0:
        choque_disparo=Nivel_1.bbox(disparo)
        choque_enem=Nivel_1.bbox(enemigo1)
        x3, y3= Nivel_1.coords(disparo)
        Nivel_1.move(disparo,x2,y2)
                    
        if choque_enem[0] < choque_disparo[2] < choque_enem[2] and choque_enem[1] <choque_disparo[1] < choque_enem[3] and verificar_disparo1==True:
            Hostile -=1
            Score+=1
            Score_final+=1
            Marcadores.config(text="Score: {}   Time: {} seg  Life:{}    Hostile: {}   {}".format(Score, Time,Life,Hostile,Player))
            print(Hostile)
            verificar_disparo1=False
            y3=-1
        board.update()
        time.sleep(0.01)
    if y3<0:
        Nivel_1.delete("disparo")
        board.update()
        time.sleep(0.01)
    if Hostile<=0:
        pase_n=False
    verificar_disparo1=False

"CONTROLES DE JUEGO"
#controles de movimiento de la nave
#<>
def mover(event):
    global verificar_disparo1
    x1, y1= Nivel_1.coords(Nave)
    if event.keysym=='Left' and pausa:
        if x1<0:
            x1=0
            Nivel_1.coords(Nave, x1,y1)
        Nivel_1.coords(Nave, x1-x,y1)
    elif event.keysym=="Right" and pausa:
        if x1>(width-100):
            x1=width-100
            Nivel_1.coords(Nave, x1,y1)
        Nivel_1.coords(Nave, x1+x,y1)
    elif event.keysym=="Up" and pausa:
        if y1<0:
            y1=0
            Nivel_1.coords(Nave, x1,y1)
        Nivel_1.coords(Nave, x1,y1-y)
    elif event.keysym=="Down" and pausa:
        if y1>height-200:
            y1=height-200
            Nivel_1.coords(Nave, x1,y1)
        Nivel_1.coords(Nave, x1,y1+y)
    elif event.keysym=="space" and pausa:
        if not verificar_disparo1:
            sonido_nave.play()
            verificar_disparo1=True
            disparo_var1 = threading.Thread(target=disparo1,args=(x1,y1))
            disparo_var1.start()

"PANTALLA DE INICIO"

def nombre_vacío(Nombre):
    Press_botton.play()
    global Player
    Player=Nombre
    if Nombre=="" or len(Nombre)>=11:
        return ""
    elif Nombre[0]==" ":
        return nombre_vacío(Nombre[1:])   
    pantalla_1()

def nombre_vacío2(Nombre):
    Press_botton.play()
    global Player,fondo,pasar2
    Player=Nombre
    if Nombre=="" or len(Nombre)>=11:
        return ""
    elif Nombre[0]==" ":
        return nombre_vacío2(Nombre[1:])
    pasar2=True   
    pantalla_2()

def nombre_vacío3(Nombre):
    Press_botton.play()
    global Player,Pasar3
    Player=Nombre
    if Nombre=="" or len(Nombre)>=11:
        return ""
    elif Nombre[0]==" ":
        return nombre_vacío2(Nombre[1:])
    Pasar3=True   
    pantalla_3()

def pantalla_inicio():
    global fondo,Bonos
    Bonos=0
    img_titulo=ImageTk.PhotoImage(Image.open("titulo inicio.png"))
    imagenmenu = ImageTk.PhotoImage(Image.open("PlanetsGalaxyUniverse2.jpg")) 
    caracteres = ImageTk.PhotoImage(Image.open("Nombre max.png").resize((250,150)))
    adorno = ImageTk.PhotoImage(Image.open("Logo naves.png").resize((250,150)))
    fondo = Canvas(board,height = height, width = width)
    fondo.pack()
    img_fondo= fondo.create_image(0,0,anchor=NW, image=imagenmenu)
    titulo= fondo.create_image(100,250,anchor=NW, image=img_titulo)
    max_nombre= fondo.create_image(200,50,anchor=NW, image=caracteres)
    Logo= fondo.create_image(200,450,anchor=NW, image=adorno)

    Jugador = Entry(fondo,bd=8, width=26,font=("Franklin Gothic Medium",17 ))
    Jugador.place(x= width/2 - Jugador.winfo_reqwidth()/2/1.5, y= height/2-300,width=240, height=50)
    imagenBoton1 = ImageTk.PhotoImage(Image.open("Boton1.jpg"))
    Boton_luchar = Button(fondo,bg="dark khaki",image=imagenBoton1,bd=8, text = "¡A la guerra!", font=("Franklin Gothic Medium",14 ), padx=25,pady=15, command= lambda: nombre_vacío(Jugador.get()))
    Boton_luchar.place(x= width/2 - Jugador.winfo_reqwidth()/2/2.2, y= height/2-200)
    Boton_about = Button(fondo,bd=6,bg="darkgrey", text = "About ?", font=("Franklin Gothic Medium",9 ), padx=8,pady=2, command= pantalla_about)
    Boton_about.place(x= 30, y= 50)
    Boton_nivel2 = Button(fondo,borderwidth=8,relief="groove",bg="dark khaki", text = "Nivel 2", font=("Franklin Gothic Medium",10 ), padx=25,pady=3, command= lambda: nombre_vacío2(Jugador.get()))
    Boton_nivel2.place(x=width/2-120, y= height-100)
    Boton_nivel3 = Button(fondo,borderwidth=8,relief="groove",bg="dark khaki", text = "Nivel 3", font=("Franklin Gothic Medium",10 ), padx=25,pady=3, command= lambda: nombre_vacío3(Jugador.get()))
    Boton_nivel3.place(x=width/2, y= height-100)
    Boton_about = Button(fondo,bd=6,bg="darkgrey", text = " Salir ", font=("Franklin Gothic Medium",8 ), padx=12,pady=2, command= quit)
    Boton_about.place(x= 30, y= 100)

    Jugador.focus()
    fondo.mainloop()

pygame.mixer.music.load("Interstellar Main Theme.mp3") 
pygame.mixer.music.play(100)   
pantalla_inicio()
board.mainloop()
