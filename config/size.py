import os

def max_size():
  width = 0
  while True:
    try:
      os.system('cls' if os.name == 'nt' else 'clear')
      width = int(input("Nuevo Ancho: \n> "))
      break
    except TypeError:
      print("Error inesperado, Vuelve a intentarlo")
    except Exception:
      print("Error desconocido")

  return width