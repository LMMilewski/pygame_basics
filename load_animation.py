def load_animation_file(self, name):
    if os.path.isfile(self.cfg.gfx_path(name) + ".png"): # there is only one static image
        img = self.__load_image(self.cfg.gfx_path(name) + ".png")
        self.animation[name] = []
        self.animation[name].append(img)
        return self.animation
    else: # there is a sequence of images - an animation
        count = 0
        animation = []
        while True:
            fname = self.cfg.gfx_path(name) + "-" + str(count) + ".png"
            if not os.path.isfile(fname):
                break
            animation.append(self.__load_image(fname))
            count += 1
        self.animation[name] = animation
        return animation
