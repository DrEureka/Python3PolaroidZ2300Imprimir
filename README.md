 # Python3 Polaroid Z2300 Imprimir 2024
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)

Convertir imágenes para que sean compatibles con Polaroid Z2300

 ![polaroidz2300Dr](https://github.com/DrEureka/Python3PolaroidZ2300Imprimir/assets/44514691/8244c239-18d9-46d7-9c67-dbd8c94868ad)


**[https://www.dpreview.com/articles/3208135372/poloroid-creates-z2300-instant-digital-camera](https://www.dpreview.com/articles/3208135372/poloroid-creates-z2300-instant-digital-camera)**

**[http://www.amazon.com/Polaroid-Z2300-Digital-Instant-Camera/dp/B008GVXL1A](http://www.amazon.com/Polaroid-Z2300-Digital-Instant-Camera/dp/B008GVXL1A)**

**# Propósito:**

La impresora de la Z2300 puede utilizarse para imprimir imágenes desde otros dispositivos, pero si se intenta imprimir imágenes que han sido recortadas en el PC, la Z2300 las rechazará con un "Error de archivo". Este proyecto resuelve este problema redimensionando las imágenes a un tamaño compatible con la impresora, ademas esta version permite copiar los EXIF escenciales para el funcionamiento correcto y lectura de las imágenes.

**# Requisitos:**

- Python 3.x
- Biblioteca de imágenes Python (PIL)
  
```
pip install Pillow
o
pip install --upgrade Pillow
```

**# Uso:**

1. Toma una tarjeta SD y coloca todas las imágenes que deseas imprimir en la tarjeta.
2. Copia el proyecto Py `Polaroid Z2300-FotosAImprimir.py` a la tarjeta SD + el archivo "PICT0001.JPG".
3. Abre una sesión de shell en la tarjeta SD y ejecuta el siguiente comando:

```
python "Polaroid Z2300-FotosAImprimir.py"
```

**# Importante:**

- NUNCA ejecutes este script en las imágenes originales. SIEMPRE haz una copia o crear una carpeta y opera sobre la copia.
