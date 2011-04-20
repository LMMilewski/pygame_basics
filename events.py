from pygame.locals import *

def process_event(self, event):
    if event.type == MOUSEBUTTONDOWN:
        if self.teleporting and not self.stopped:
            if event.pos[0] < 0 or event.pos[0] > 600:
                return
            if event.pos[1] < 0 or event.pos[1] > 600:
                return
            if 160 <= event.pos[0] and event.pos[0] <= 220:
                return
            if 380 <= event.pos[0] and event.pos[0] <= 440:
                return
            if 160 <= event.pos[1] and event.pos[1] <= 220:
                return
            if 380 <= event.pos[1] and event.pos[1] <= 440:
                return
            self.ferris.position = event.pos
            self.teleporting = False
     if event.type == KEYDOWN:
        self.last_keys.append(event.key)
        self.last_keys = self.last_keys[-100:]
        if self.last_keys[-len(self.cfg.cheat_sequence):] == self.cfg.cheat_sequence:
            self.cfg.cheat_mode = True
        if self.cfg.cheat_mode:
            if self.last_keys[-len(self.cfg.godmode_sequence1):] == self.cfg.godmode_sequence1:
                self.cfg.godmode = True
            if self.last_keys[-len(self.cfg.godmode_sequence2):] == self.cfg.godmode_sequence2:
                self.cfg.godmode = True
            if self.last_keys[-len(self.cfg.infinite_bonus_sequence):] == self.cfg.infinite_bonus_sequence:
                self.cfg.infinite_bonus = True
                for bonus in self.bonuses:
                    bonus.reset()
            if self.last_keys[-len(self.cfg.answer_sequence):] == self.cfg.answer_sequence:
                self.cfg.answer = True
        if event.key == K_p:
            self.stopped = True
        self.stopped = False
        if event.key == K_ESCAPE:
            self.finish()
        if event.key == K_LEFT:
            self.ferris.direction = DIR_LEFT
        if event.key == K_RIGHT:
            self.ferris.direction = DIR_RIGHT
        if event.key == K_UP:
            self.ferris.direction = DIR_UP
        if event.key == K_DOWN:
            self.ferris.direction = DIR_DOWN
        if event.key == K_1:
            if len(self.bonuses) > 0:
                self.bonuses[0].activate()
        if event.key == K_2:
            if len(self.bonuses) > 1:
                self.bonuses[1].activate()
        if event.key == K_3:
            if len(self.bonuses) > 2:
                  self.bonuses[2].activate()
        if event.key == K_4:
            if len(self.bonuses) > 3:
                self.bonuses[3].activate()
        if event.key == K_5:
            if len(self.bonuses) > 4:
                self.bonuses[4].activate()
        if self.cfg.cheat_mode:
            if event.key == K_7:
                self.bonuses = self.possible_bonuses[0]
                for bonus in self.bonuses:
                    bonus.on_add()
            if event.key == K_8:
                self.bonuses = self.possible_bonuses[1]
                for bonus in self.bonuses:
                    bonus.on_add()
            if event.key == K_9:
                self.go_to_next_level()
            if event.key == K_0:
                self.cfg.print_fps = not self.cfg.print_fps
