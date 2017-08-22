# Fix glyph uni042b. The components need swapping
python fix_uni042b.py

# Update font version number
FONTS=$(ls *.ttf)
fontbakery update-version $FONTS 1.002 1.003



rm $FONTS
FONTS_VERSION_BUMPED=$(ls *.fix)
# replace .fix with .ttf
for font in $FONTS_VERSION_BUMPED
do
    mv $font "${font%.*}"
done