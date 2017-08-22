"""
Fixes issue: https://github.com/google/fonts/issues/7
"""

import os
from fontTools.ttLib import TTFont


BAD_GLYPH = 'uni042B'

NEW_COORDS = {
    'PlayfairDisplay-Black.ttf': {'uni042C': 0, 'I': 1393},
    'PlayfairDisplay-Bold.ttf': {'uni042C': 0, 'I': 1311},
    'PlayfairDisplay-Regular.ttf': {'uni042C': 0, 'I': 1188},

}

def main():
    fonts_paths = [p for p in os.listdir('.')
                   if p.endswith('.ttf') and not
                   'Italic' in p]
    for font_path in fonts_paths:
        font = TTFont(font_path)

        for i, component in enumerate(font['glyf'][BAD_GLYPH].components):
            c_name = component.glyphName
            if c_name in NEW_COORDS[font_path]:
                font['glyf'][BAD_GLYPH].components[i].x = NEW_COORDS[font_path][c_name]

        os.remove(font_path)
        print('Rewriting ttf %s' % font_path)
        font.save(font_path)
    print 'Done!'

if __name__ == '__main__':
    main()
