import sys
import os
from PIL import Image

class ImageProcess(object):

    def __init__(self, argv):
        self._dir = '/'.join(argv.split('/')[0:-1])
        self.im = Image.open(argv)
        (self.width, self.height) = self.im.size

    def crop(self):
        w_intrvl = self.width / 3
        h_intrvl = self.height / 2
        self.right = self.im.crop(box=(0, 0, w_intrvl, h_intrvl))
        self.back = self.im.crop(box=(w_intrvl, 0, w_intrvl * 2, h_intrvl))
        self.left = self.im.crop(box=(w_intrvl * 2, 0, self.width, h_intrvl))
        self.down = self.im.crop(box=(0, h_intrvl, w_intrvl, self.height))
        self.up = self.im.crop(box=(w_intrvl, h_intrvl, w_intrvl * 2, self.height))
        self.front = self.im.crop(box=(w_intrvl * 2, h_intrvl, self.width, self.height))

    def save(self):
        dwnld_dir = self._dir + '/skybox6-imgsplit'
        if not os.path.exists(dwnld_dir):
            os.makedirs(dwnld_dir)
        images = ['right', 'back', 'left', 'down', 'up', 'front']
        for i in images:
            print 'Downloading ' + i + ': ' + dwnld_dir + '/skybox6-imgsplit/' + i
            getattr(self, i).save(self._dir + '/skybox6-imgsplit/' + i + '.png', 'PNG')

if __name__ == "__main__":
    ip = ImageProcess(sys.argv[1])
    ip.crop()
    ip.save()
