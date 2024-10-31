import os
import pygame
import random
import sys

pygame.init()

largeur_fenetre = 800
hauteur_fenetre = 600
screen = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Jeu de Lancer de Dés")

NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)

def charger_images():
    images = []
    for i in range(1, 7):  
        image = pygame.image.load(os.path.join('Images', f'de{i}.png'))
        image = pygame.transform.scale(image, (100, 100))  
        images.append(image)
    return images

def lancer_de():
    return random.randint(1, 6)

def jeu_combinaison():
    images_de = charger_images()  
    des = [lancer_de() for _ in range(3)]
    tours = 1
    font = pygame.font.Font(None, 74)
    petit_font = pygame.font.Font(None, 36)

    while tours <= 3:
        screen.fill(NOIR)
        
        # Affichage des résultats en haut de l'écran
        texte_resultats = f"Résultats des dés : {des[0]}, {des[1]}, {des[2]}"
        text_surface = petit_font.render(texte_resultats, True, BLANC)
        screen.blit(text_surface, (largeur_fenetre//2 - text_surface.get_width()//2, 50))

        # Affichage des images de dés au centre de l'écran
        for i in range(3):
            image_de = images_de[des[i] - 1]
            position_x = largeur_fenetre // 2 - (100 * 1.5) + (i * 150)  # Ajustement de l'espacement
            screen.blit(image_de, (position_x, 200))

        # Affichage du message de victoire ou de perte
        if des[0] == des[1] == des[2]:
            texte_gagne = "Félicitations ! Vous avez gagné !"
            text_surface = font.render(texte_gagne, True, ROUGE)
            screen.blit(text_surface, (largeur_fenetre//2 - text_surface.get_width()//2, 150))
        else:
            # Affichage des instructions de relance ou de fin de partie, en bas de l'écran
            if tours < 3:
                texte_instruction = "Appuyez sur R pour relancer ou Échap pour quitter."
            else:
                texte_instruction = "Fin du jeu. Appuyez sur Échap pour quitter."
            text_surface = petit_font.render(texte_instruction, True, BLANC)
            screen.blit(text_surface, (largeur_fenetre//2 - text_surface.get_width()//2, 450))

        pygame.display.flip()
        
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    des = [lancer_de() for _ in range(3)]
                    tours += 1
                    break

    # Fin du jeu : message de remerciement
    screen.fill(NOIR)
    texte_fin = "Merci d'avoir joué !"
    text_surface = font.render(texte_fin, True, ROUGE)
    screen.blit(text_surface, (largeur_fenetre//2 - text_surface.get_width()//2, hauteur_fenetre//2 - 50))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()

jeu_combinaison()
