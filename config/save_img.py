import os

def path_img_save():
    path = ""
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')

            path = input("Ruta donde desea guardar la imagen (incluyendo la extensión, ej. 'imagen_modificada.jpg'): \n > ")
            
            # Verificar si la ruta proporcionada tiene una extensión válida
            if not any(path.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif']):
                raise ValueError("La extensión de archivo proporcionada no es válida. Usa .jpg, .jpeg, .png, o .gif.")
            
            # Verificar si la ruta proporcionada corresponde a un directorio
            if os.path.isdir(os.path.dirname(path)):
                print(f"La nueva imagen redimensionada ha sido guardada en: {os.path.dirname(path)}")
                return path 
            else:
                raise NotADirectoryError("La ruta proporcionada no es un directorio válido.")
            break            
        except NotADirectoryError as e:
            print(e)
        except Exception as e:
            print(f"Error: {e}")