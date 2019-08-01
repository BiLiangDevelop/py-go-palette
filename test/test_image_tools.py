# coding:utf-8
__author__ = 'rk.feng'

import logging
import os
import time
import unittest

from PIL import Image

from pypalette import ImageThemeTools


class TestColorTools(unittest.TestCase):
    def setUp(self) -> None:
        self.logger = logging.getLogger("TestColorTools")
        self.tools = ImageThemeTools(logger=self.logger)

    @staticmethod
    def _get_image() -> Image.Image:
        return Image.open(os.path.join(os.path.dirname(__file__), "t.jpg"))

    def testDemo(self):
        """ demo """
        print(self.tools.get_theme_color(image=self._get_image()))

    def testMemory(self):
        """ OOM Test """
        image = self._get_image()
        for _ in range(10):
            print(self.tools.get_theme_color(image=image))
            time.sleep(1)
