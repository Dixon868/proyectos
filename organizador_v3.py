import os
import shutil
import argparse

TIPOS_DE_ARCHIVO = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Comprimidos": [".zip", ".rar", ".7z"],
    "Codigo": [".py", ".js", ".html", ".css"],
}


def obtener_nombre_disponible(destino, nombre_archivo):
    """
    Si ya existe un archivo con ese nombre en destino, genera un nombre
    alternativo tipo 'foto(1).jpg', 'foto(2).jpg', etc, para no sobrescribir nada.
    """
    ruta_destino = os.path.join(destino, nombre_archivo)
    if not os.path.exists(ruta_destino):
        return nombre_archivo

    base, extension = os.path.splitext(nombre_archivo)
    contador = 1
    while True:
        nuevo_nombre = f"{base}({contador}){extension}"
        if not os.path.exists(os.path.join(destino, nuevo_nombre)):
            return nuevo_nombre
        contador += 1


def mover_archivo(ruta_base, ruta_completa, carpeta_destino, nombre_archivo, vista_previa):
    """
    Mueve un archivo a su carpeta destino. Devuelve True si tuvo éxito
    (o simulación en vista previa), False si falló.
    """
    destino = os.path.join(ruta_base, carpeta_destino)
    nombre_final = obtener_nombre_disponible(destino, nombre_archivo)

    etiqueta = "[VISTA PREVIA] " if vista_previa else ""
    if nombre_final != nombre_archivo:
        print(f"{etiqueta}⚠️  '{nombre_archivo}' ya existe en {carpeta_destino}/, se guardará como '{nombre_final}'")

    if vista_previa:
        print(f"{etiqueta}Movería: {nombre_archivo} -> {carpeta_destino}/{nombre_final}")
        return True

    try:
        os.makedirs(destino, exist_ok=True)
        shutil.move(ruta_completa, os.path.join(destino, nombre_final))
        print(f"✅ Movido: {nombre_archivo} -> {carpeta_destino}/{nombre_final}")
        return True
    except PermissionError:
        print(f"❌ Sin permisos para mover '{nombre_archivo}'. Sáltandolo.")
        return False
    except OSError as error:
        # Cubre casos como disco lleno, archivo en uso, ruta demasiado larga, etc.
        print(f"❌ No se pudo mover '{nombre_archivo}': {error}. Sáltandolo.")
        return False


def organizar_carpeta(ruta, vista_previa=False):
    if not os.path.isdir(ruta):
        print(f"❌ La carpeta '{ruta}' no existe.")
        return

    try:
        archivos = os.listdir(ruta)
    except PermissionError:
        print(f"❌ No tienes permisos para leer la carpeta '{ruta}'.")
        return

    movidos = 0
    fallidos = 0

    for nombre_archivo in archivos:
        ruta_completa = os.path.join(ruta, nombre_archivo)

        if not os.path.isfile(ruta_completa):
            continue  # ignoramos subcarpetas ya existentes

        _, extension = os.path.splitext(nombre_archivo)
        extension = extension.lower()

        carpeta_destino = "Otros"
        for nombre_categoria, extensiones in TIPOS_DE_ARCHIVO.items():
            if extension in extensiones:
                carpeta_destino = nombre_categoria
                break

        exito = mover_archivo(ruta, ruta_completa, carpeta_destino, nombre_archivo, vista_previa)
        if exito:
            movidos += 1
        else:
            fallidos += 1

    print(f"\n📊 Resumen: {movidos} archivo(s) {'a mover' if vista_previa else 'movidos'}, {fallidos} fallido(s).")
    if vista_previa:
        print("Esto fue solo una simulación. Corre sin --vista-previa para aplicar los cambios de verdad.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Organiza los archivos de una carpeta en subcarpetas según su tipo."
    )
    parser.add_argument("carpeta", help="Ruta de la carpeta a organizar")
    parser.add_argument(
        "-v", "--vista-previa",
        action="store_true",
        help="Muestra qué se movería, sin mover nada realmente"
    )

    args = parser.parse_args()
    organizar_carpeta(args.carpeta, vista_previa=args.vista_previa)
