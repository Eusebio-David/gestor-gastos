import os

def buscar_archivos_con_error_de_codificacion(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".py"):
                ruta = os.path.join(root, file)
                try:
                    with open(ruta, encoding="utf-8") as f:
                        f.read()
                except UnicodeDecodeError as e:
                    print(f"❌ Archivo con error de codificación: {ruta}")
                    print(f"   Detalle: {e}")

buscar_archivos_con_error_de_codificacion(".")