import PIL.Image
import os
import shutil
import re
import random
import piexif

ok = re.compile(r'^PICT\d\d\d\d$')

def rename(f):
    while True:
        nf = "PICT%04d.JPG" % random.randint(1111, 9999)
        if not os.path.isfile(nf):
            print(f, "->", nf)
            return nf

# Fix image paths
for f in os.listdir('.'):
    if f.upper().endswith('JPG'):
        a, b = os.path.splitext(f)
        if not ok.match(a):
            shutil.move(f, rename(f))

# Find the source image for EXIF data // No eliminar esta foto, Esto permite tomar los
# EXIF/Metadatos para aplicarlos en cada foto
source_image = "PICT0001.JPG"

# Load EXIF data from the source image
exif_dict_source = piexif.load(source_image)

for f in os.listdir('.'):
    if f.upper().endswith('JPG'):
        print("Chequeando", f)
        # Find the image size
        im = PIL.Image.open(f)
        im_size = im.size

        if im_size != (3648, 2736) and im_size != (2736, 3648):
            print("Adaptando la imagen a las dimensiones de una Polaroid")
            im = im.resize((im_size[0] * 4, im_size[1] * 4), resample=PIL.Image.LANCZOS)
            if im_size[0] > im_size[1]:
                into = PIL.Image.new(im.mode, (3648, 2736))
                im.thumbnail((3648, 2736), PIL.Image.LANCZOS)
            else:
                into = PIL.Image.new(im.mode, (2736, 3648))
                im.thumbnail((2736, 3648), PIL.Image.LANCZOS)
            into.paste(im, (int((into.size[0] - im.size[0]) / 2), int((into.size[1] - im.size[1]) / 2)))

            # Copy EXIF data to the new image // Aca sucede la magia, esto permite que la Z2300 lea los archivos.
            try:
                existing_exif = into.info['exif']
                exif_dict_source.update(piexif.load(existing_exif))
            except KeyError:
                pass  # If 'exif' key doesn't exist, proceed without updating // Falta archivo "PICT0001.JPG"

            exif_bytes = piexif.dump(exif_dict_source)
            into.save(f, exif=exif_bytes)
print("Proceso finalizado, No borrar archivo PICT0001.JPG.")