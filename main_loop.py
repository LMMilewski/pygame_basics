cfg = Config()

clock = pygame.time.Clock()
pygame.mixer.pre_init(11025, -16, 2, 256)
flags = 0
if cfg.fullscreen:
  flags |= pygame.FULLSCREEN
screen = pygame.display.set_mode(cfg.screen_resolutio flags)
pygame.init()

res = Resources()
game = Game()

while not game.is_finished:
  dt = clock.tick(cfg.fps_limit) * 0.001
  for event in pygame.event.get():
    if event.type == QUIT:
       game.finish()
     else:
       game.process_event(event)
  game.update()
  game.display(screen)
  pygame.display.flip()
