from config.path import image_location
from config.save_img import path_img_save
from config.size import max_size
from PIL import Image

def resize_image_with_aspect(image_path, new_width, path_save):
  # Abrir la imagen
  img = Image.open(image_path)

  # Obtener dimensiones originales
  original_width, original_height = img.size

  # Calcular nueva altura manteniendo la proporción
  aspect_ratio = original_height / original_width
  new_height = int(new_width * aspect_ratio)

  # Redimensionar la imagen
  resized_img = img.resize((new_width, new_height), Image.LANCZOS)

  # Guardar imagen
  resized_img.save(path_save)

  # Previsualizar imagen
  resized_img.show()


resize_image_with_aspect(image_location(), max_size(), path_img_save())