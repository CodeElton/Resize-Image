import os

def image_location():
    img = ""
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            img = input("Ruta completa de la imagen: \n> ")
            with open(img, "rb"):
                pass
            break
        except FileNotFoundError:
            print("Imagen no encontrada")
        except TypeError:
            print("Error, Porfavor inserta una ruta correcta")
        except Exception:
            print("Error desconocido!!")
            
    return img    