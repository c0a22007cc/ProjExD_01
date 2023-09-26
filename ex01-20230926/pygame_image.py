import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/ex01-20230926/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01/ex01-20230926/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img_rz1 = pg.transform.rotozoom(kk_img, 1, 1.0)
    kk_img_rz2 = pg.transform.rotozoom(kk_img, 2, 1.0)
    kk_img_rz3 = pg.transform.rotozoom(kk_img, 3, 1.0)
    kk_img_rz4 = pg.transform.rotozoom(kk_img, 4, 1.0)
    kk_img_rz5 = pg.transform.rotozoom(kk_img, 5, 1.0)
    kk_img_rz6 = pg.transform.rotozoom(kk_img, 6, 1.0)
    kk_img_rz7 = pg.transform.rotozoom(kk_img, 7, 1.0)
    kk_img_rz8 = pg.transform.rotozoom(kk_img, 8, 1.0)
    kk_img_rz9 = pg.transform.rotozoom(kk_img, 9, 1.0)
    kk_img_rz10 = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_imgs = [kk_img, kk_img_rz1, kk_img_rz2, kk_img_rz3, kk_img_rz4, kk_img_rz5, kk_img_rz6, kk_img_rz7, kk_img_rz8, kk_img_rz9, kk_img_rz10]

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr % 1600
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img, [1600 - x, 0])
        screen.blit(kk_imgs[tmr%10], [300, 200])#tmrの値が奇数または偶数
        pg.display.update()
        tmr += 1        
        clock.tick(30)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()