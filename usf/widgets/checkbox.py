################################################################################
# copyright 2010 Lucas Baudin <xapantu@gmail.com>                              #
#                                                                              #
# This file is part of Ultimate Smash Friends.                                 #
#                                                                              #
# Ultimate Smash Friends is free software: you can redistribute it and/or      #
# modify it under the terms of the GNU General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or (at your   #
# option) any later version.                                                   #
#                                                                              #
# Ultimate Smash Friends is distributed in the hope that it will be useful, but#
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or#
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for    #
# more details.                                                                #
#                                                                              #
# You should have received a copy of the GNU General Public License along with #
# Ultimate Smash Friends.  If not, see <http://www.gnu.org/licenses/>.         #
################################################################################

'''
This module provide a simple checkbox widget.

'''

#standards imports
import pygame
from os.path import join

#our modules
from usf.widgets.widget import Widget, optimize_size


from usf import CONFIG


class CheckBox(Widget):
    """
    A checkbox widget.
    """

    def __init__(self):
        super(CheckBox, self).__init__()
        self.properties["size_request"] = (25, 25)
        self.state = False
        self.checked = False
        self.screen = pygame.display.get_surface()

    def set_size(self, (w, h)):
        """
        Set the size of the widget.
        """

        self.height = h
        self.width = w
        self.surface_static = loaders.image(join(CONFIG.system_path,
                                                  'gui',
                                                  CONFIG.general.THEME,
                                                  'checkbox_empty.png'),
                                             scale=(w, h))[0]

        self.surface_checked = loaders.image(join(CONFIG.system_path,
                                                  'gui',
                                                  CONFIG.general.THEME,
                                                  'checkbox_full.png'),
                                             scale=(w, h))[0]
        self.surface = self.surface_static

    def handle_mouse(self, event):
        if self.state:
            event.dict['pos'] = (
                    event.dict['pos'][0] - self.parentpos[0] - self.x,
                    event.dict['pos'][1] - self.parentpos[1] - self.y)

        if (0 < event.dict['pos'][0] < self.width and
            0 < event.dict['pos'][1] < self.height and
            event.type == pygame.MOUSEBUTTONUP):
            if self.checked:
                self.checked = False
                self.surface = self.surface_static
            else:
                self.checked = True
                self.surface = self.surface_checked
            self.state = True
            return self, False
        self.state = False
        return False, False

    def get_value(self):
        """
        Get the value of the checkbox, it returns a boolean.
        (true of checked and false if unchecked)
        """
        return self.checked

    def set_value(self, value):
        """
        Set the value of the checkbox, it must be a boolean.
        """
        self.checked = value

