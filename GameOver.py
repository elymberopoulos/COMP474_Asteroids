import pygame as pg
import sys

class HighScore:
    def __init__(self,score):
        self.screen = pg.display.set_mode((640,480))
        self.font = pg.font.Font(None, 32)
        self.color = pg.Color('white')
        self.text = ''

        # self.font = pg.font.SysFont("monospace", 32)

        file = open("highscores.txt")
        scores = str(file.readlines())
        score_list = scores.split(',')
        y = 200
        for line in score_list:
            self.scores = self.font.render(line, True, self.color)
            # self.screen.blit(self.scores, (50, y))
            y += 30
        file.close()

        while True:
            self.screen.fill((0, 0, 0))
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        self.writeHighScore(self.text, score)
                        pg.quit()
                        sys.exit(0)
                    elif event.key == pg.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode

            self.readHighScore()
            self.onscreentext = self.font.render("Enter your name! Highscore: " + str(score), True, self.color)
            self.screen.blit(self.onscreentext, (50, 100))
            self.txt_surface = self.font.render(self.text, True, self.color)
            self.screen.blit(self.txt_surface, (400, 100))
            pg.display.flip()

    def writeHighScore(self, name, score):
        file = open("highscores.txt", "a")
        file.write(name + ":" + str(score) + ",")
        file.close()

    def readHighScore(self):
        file = open("highscores.txt")
        scores = str(file.readlines())
        score_list = scores.split(',')
        y = 200
        for line in score_list:
            self.scores = self.font.render(line, True, self.color)
            self.screen.blit(self.scores, (50, y))
            y += 30
        file.close()