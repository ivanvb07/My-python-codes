import pygame
from pygame.locals import *

pygame.init()

def lobby():
    menu = pygame.display.set_mode((1400,1300))
    run_menu  =True
    color_play = (0,50,255)
    color_quit = (255,0,0)
    color_credits = (0,255,0)

    while run_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_menu = False
            #affichage du titre
            police_titre = pygame.font.SysFont("Polya", 60)
            image_titre = police_titre.render ("Chess and Cards",10,(255,255,255))
            menu.blit(image_titre, (450, 200))
            #affiche du texte de lancement du jeu
            pygame.draw.rect(menu, color_play, pygame.Rect(250, 380,240, 80))
            police_play = pygame.font.SysFont("Polya" ,55)
            image_play = police_play.render ( "PLAY", 5 , (255,255,255) )
            menu.blit(image_play, (300,400))
            #affiche des crédits
            pygame.draw.rect(menu, color_credits, pygame.Rect(500, 580,240, 80))
            police_credits = pygame.font.SysFont("Polya" ,55)
            image_credits = police_credits.render ("CREDITS", 5 , (255,255,255))
            menu.blit(image_credits, (530,600))
            #affichage du texte pour fermer le jeu
            pygame.draw.rect(menu, color_quit, pygame.Rect(750, 380,240, 80))
            police_quit = pygame.font.SysFont("Polya" ,55)
            image_quit = police_quit.render ( "QUIT", 5 , (255,255,255) )
            menu.blit(image_quit, (800,400))
            pygame.display.flip()
            #récupération des coordonnées de la souris
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            #print(pygame.mouse.get_pos())

            if pygame.mouse.get_pressed()[0] == 1:
                if (252) < x < (489) and (380) < y < (455):
                    game_luncher()
                    #ouvrir la fenêtre du jeu

                elif (500) < x < (738) and (580) < y < (658):
                    credits()
                    #ouvrir les crédits

                elif (750) < x < (988) and (380) < y < (460):
                    run_menu = False
                #fermer la fenêtre

    pygame.quit()
    quit()

def credits():
    creds = pygame.display.set_mode((1400,1300))
    pygame.display.set_caption("Chess and Cards")
    color_crédits = (0,255,0)

    crédits_lancés = True
    while crédits_lancés:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crédits_lancés = False
            #affichage des crédits
            police_crédits = pygame.font.SysFont("Polya", 60)
            image_crédits = police_crédits.render ("Created by Ivan, Jonah and Ilian",10,(255,255,255))
            creds.blit(image_crédits, (350, 200))
            #affichage du bouton retour au menu
            police_retour = pygame.font.SysFont("Polya", 60)
            pygame.draw.rect(creds, color_crédits, pygame.Rect(500, 400,300, 80))
            image_retour = police_retour.render ("Back to menu",10,(255,255,255))
            creds.blit(image_retour, (520, 420))
            pygame.display.flip()
            #récupération des coordonnées de la souris
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            if  (500) < x < (797) and (400) < y < (478)  and pygame.mouse.get_pressed()[0] == 1:
                lobby()
                #retour au menu

def game_luncher():
    screen = pygame.display.set_mode((1920,1600))
    pygame.display.set_caption("Chess and Cards")
    background = pygame.image.load("interface2.png").convert()
    pion_blanc= pygame.image.load("plateau.png").convert()
    x, y = 40, 40

    jeu_lancé = True
    while jeu_lancé:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jeu_lancé = False
            if (x-50,y-50) < pygame.mouse.get_pos() < (x+100,y+100) and pygame.mouse.get_pressed()[0] == 1 :
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
            screen.fill((0, 0, 0))
            screen.blit(background, (0,0))
            screen.blit(pion_blanc, (x, y))
            pygame.display.update()
    pygame.quit()
    quit()

def the_end(winner):
    if winner == "black":
        victory = pygame.display.set_mode((1920,1600))
        background_victory = pygame.image.load("interface2.png").convert()
        win_black = True
        color_winner = (0,0,0)
        color_reset = (0,50,255)
        color_back = (255,0,0)

        while win_black:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    win_black = False
                victory.fill((0, 0, 0))
                victory.blit(background_victory, (0,0))
                #affichage du message de victoire
                police_black_win = pygame.font.SysFont("Polya", 90)
                image_black_win = police_black_win.render ("Black Wins",19,(0,0,0))
                victory.blit(image_black_win, (750, 200))
                #affiche du texte de relancement du jeu
                pygame.draw.rect(victory, color_reset, pygame.Rect(250, 380,340, 80))
                police_reset = pygame.font.SysFont("Polya" ,55)
                image_reset = police_reset.render ( "RESTART GAME", 5 , (255,255,255) )
                victory.blit(image_reset, (260,400))
                #affichage du texte pour fermer le jeu
                pygame.draw.rect(victory, color_back, pygame.Rect(850, 380,340, 80))
                police_back = pygame.font.SysFont("Polya" ,55)
                image_back = police_back.render ( "BACK TO MENU", 5 , (255,255,255) )
                victory.blit(image_back, (880,400))
                pygame.display.flip()
                #récupération des coordonnées de la souris
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                #print(x,y)
                pygame.display.flip()

                if pygame.mouse.get_pressed()[0] == 1:
                    if (251) < x < (529) and (380) < y < (459):
                        game_luncher()
                        #ouvrir la fenêtre du jeu

                    elif (849) < x < (1129) and (380) < y < (460):
                        lobby()
                        #retour au menu

    elif winner == "white":
        victory = pygame.display.set_mode((1920,1600))
        background_victory = pygame.image.load("interface2.png").convert()
        win_white = True
        color_winner = (0,0,0)
        color_reset = (0,50,255)
        color_back = (255,0,0)

        while win_white:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    win_white = False
                victory.fill((0, 0, 0))
                victory.blit(background_victory, (0,0))
                #affichage du message de victoire
                police_white_win = pygame.font.SysFont("Polya", 90)
                image_white_win = police_white_win.render ("White Wins",19,(0,0,0))
                victory.blit(image_white_win, (750, 200))
                #affiche du texte de relancement du jeu
                pygame.draw.rect(victory, color_reset, pygame.Rect(250, 380,340, 80))
                police_reset = pygame.font.SysFont("Polya" ,55)
                image_reset = police_reset.render ( "RESTART GAME", 5 , (255,255,255) )
                victory.blit(image_reset, (260,400))
                #affichage du texte pour fermer le jeu
                pygame.draw.rect(victory, color_back, pygame.Rect(850, 380,340, 80))
                police_back = pygame.font.SysFont("Polya" ,55)
                image_back = police_back.render ( "BACK TO MENU", 5 , (255,255,255) )
                victory.blit(image_back, (880,400))
                pygame.display.flip()
                #récupération des coordonnées de la souris
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                #print(x,y)
                pygame.display.flip()

                if pygame.mouse.get_pressed()[0] == 1:
                    if (251) < x < (588) and (380) < y < (460):
                        game_luncher()
                        #ouvrir la fenêtre du jeu

                    elif (849) < x < (1189) and (380) < y < (460):
                        lobby()
                        #retour au menu
    else:
        victory = pygame.display.set_mode((1920,1600))
        background_victory = pygame.image.load("interface2.png").convert()
        win_no = True
        color_winner = (0,0,0)
        color_reset = (0,50,255)
        color_back = (255,0,0)

        while win_no:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    win_no = False
                victory.fill((0, 0, 0))
                victory.blit(background_victory, (0,0))
                #affichage du message de victoire
                police_no_win = pygame.font.SysFont("Polya", 90)
                image_no_win = police_no_win.render ("DRAW",19,(0,0,0))
                victory.blit(image_no_win, (750, 200))
                #affiche du texte de relancement du jeu
                pygame.draw.rect(victory, color_reset, pygame.Rect(250, 380,340, 80))
                police_reset = pygame.font.SysFont("Polya" ,55)
                image_reset = police_reset.render ( "RESTART GAME", 5 , (255,255,255) )
                victory.blit(image_reset, (260,400))
                #affichage du texte pour fermer le jeu
                pygame.draw.rect(victory, color_back, pygame.Rect(850, 380,340, 80))
                police_back = pygame.font.SysFont("Polya" ,55)
                image_back = police_back.render ( "BACK TO MENU", 5 , (255,255,255) )
                victory.blit(image_back, (880,400))
                pygame.display.flip()
                #récupération des coordonnées de la souris
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                #print(x,y)
                pygame.display.flip()

                if pygame.mouse.get_pressed()[0] == 1:
                    if (251) < x < (588) and (380) < y < (460):
                        game_luncher()
                        #ouvrir la fenêtre du jeu

                    elif (849) < x < (1189) and (380) < y < (460):
                        lobby()
                        #retour au menu

    pygame.quit()
    quit()

lobby()
