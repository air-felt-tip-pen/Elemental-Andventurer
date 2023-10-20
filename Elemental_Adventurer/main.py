from mycode.funk import *

if "__main__" == __name__:
    pygame.init()

    running = True
    while running:

        key = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if running and event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                running = False

        game.update()
        if player.health <= 0:
            running = False

        pygame.display.flip()
        clock.tick(50)
    pygame.quit()