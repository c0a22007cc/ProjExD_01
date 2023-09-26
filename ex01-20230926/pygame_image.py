import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/ex01-20230926/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("ex01/ex01-20230926/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img_rzoom = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_imgs = [kk_img, kk_img_rzoom]

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr % 1600
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img, [1600 - x, 0])
        screen.blit(kk_imgs[tmr%2], [300, 200])#tmrの値が奇数または偶数
        pg.display.update()
        tmr += 1        
        clock.tick(150)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()