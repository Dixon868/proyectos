# 📁 Organizador de Archivos

Un script en Python que ordena automáticamente los archivos de una carpeta desordenada, agrupándolos en subcarpetas según su tipo (imágenes, documentos, videos, audio, comprimidos, código y más).

¿Tu carpeta de Descargas es un caos de fotos, PDFs, videos y archivos random mezclados? Este script lo arregla en segundos.

---

## ✨ Funcionalidades

- **Organización automática por tipo de archivo** — reconoce imágenes, documentos, videos, audio, comprimidos y código, y agrupa el resto en `Otros/`.
- **Modo vista previa (`--vista-previa`)** — te muestra exactamente qué se movería, sin tocar nada todavía. Ideal para probar sin miedo antes de aplicar los cambios de verdad.
- **Protección contra sobrescritura** — si ya existe un archivo con el mismo nombre en el destino, el script no lo reemplaza: lo guarda como `archivo(1).jpg`, `archivo(2).jpg`, etc.
- **Manejo de errores robusto** — si un archivo específico no se puede mover (por permisos u otro problema), el script no se detiene: lo reporta y sigue con el resto.
- **Resumen final** — al terminar, te dice cuántos archivos se movieron y cuántos fallaron.
- **Idempotente** — puedes correrlo varias veces sobre la misma carpeta sin que duplique trabajo ni rompa nada; si ya está todo organizado, simplemente no encuentra nada más que mover.
- **Ayuda integrada** — corre `--help` en cualquier momento para ver cómo usarlo.

---

## 📋 Requisitos

- Python 3.6 o superior (no necesitas instalar nada más — solo usa librerías incluidas en Python)

Para verificar que tienes Python instalado, abre una terminal y escribe:
```bash
python3 --version
```
Si no lo tienes, descárgalo gratis desde [python.org](https://www.python.org/downloads/).

---

## 🚀 Instalación

1. Descarga el archivo `organizador.py`
2. Guárdalo en cualquier carpeta de tu computadora
3. Ya está — no requiere instalar librerías adicionales

---

## 🖥️ Cómo usarlo

Abre una terminal en la carpeta donde guardaste `organizador.py` y usa alguno de estos comandos:

### Ver la ayuda
```bash
python3 organizador.py --help
```

### Simular antes de organizar (recomendado la primera vez)
Esto te muestra qué haría el script, **sin mover nada todavía**:
```bash
python3 organizador.py "C:\Users\TuNombre\Downloads" --vista-previa
```

### Organizar de verdad
Cuando ya revisaste la vista previa y quieres aplicar los cambios:
```bash
python3 organizador.py "C:\Users\TuNombre\Downloads"
```

> 💡 En Mac/Linux la ruta se ve distinto, por ejemplo: `/Users/TuNombre/Downloads`

---

## 📂 Categorías de archivos

| Carpeta destino | Extensiones incluidas |
|---|---|
| Imagenes | `.jpg` `.jpeg` `.png` `.gif` `.webp` |
| Documentos | `.pdf` `.docx` `.txt` `.xlsx` `.pptx` |
| Videos | `.mp4` `.mov` `.avi` |
| Audio | `.mp3` `.wav` |
| Comprimidos | `.zip` `.rar` `.7z` |
| Codigo | `.py` `.js` `.html` `.css` |
| Otros | Cualquier otra extensión no listada arriba |

¿Necesitas agregar más tipos de archivo? Es fácil: abre `organizador.py`, busca el diccionario `TIPOS_DE_ARCHIVO` al inicio del archivo, y agrega la extensión que quieras a la categoría correspondiente (o crea una categoría nueva).

---

## 🧪 Ejemplo de uso

Supongamos que tu carpeta `Descargas` se ve así:

```
Descargas/
├── vacaciones.jpg
├── factura.pdf
├── cancion.mp3
├── pelicula.mp4
```

Después de correr `python3 organizador.py Descargas`, quedará así:

```
Descargas/
├── Imagenes/
│   └── vacaciones.jpg
├── Documentos/
│   └── factura.pdf
├── Audio/
│   └── cancion.mp3
├── Videos/
│   └── pelicula.mp4
```

---

## ❓ Preguntas frecuentes

**¿Puedo deshacer los cambios si algo sale mal?**
El script no incluye una función de "deshacer" automática, pero como agrupa por tipo en subcarpetas claras, siempre puedes mover los archivos de vuelta manualmente. Por eso se recomienda usar siempre `--vista-previa` primero.

**¿Sobrescribe archivos si hay nombres repetidos?**
No. Si detecta un archivo con el mismo nombre en el destino, guarda el nuevo con un sufijo como `(1)`, sin borrar ni reemplazar nada.

**¿Qué pasa con las subcarpetas que ya existen dentro de la carpeta que organizo?**
El script las ignora — solo mueve archivos sueltos, no reorganiza carpetas existentes.

**¿Funciona en Windows, Mac y Linux?**
Sí, es compatible con los tres siempre que tengas Python instalado.

---

## 🔮 Posibles mejoras futuras

- Función para deshacer la última organización
- Archivo de configuración externo para personalizar categorías sin editar el código
- Interfaz gráfica simple para quienes no usan la terminal

---

## 📝 Licencia

Uso libre para fines personales y comerciales.
