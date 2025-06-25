import os
import json
import shutil

def merge_dicts(ejemplo, actual):
    """
    Fusiona recursivamente dos diccionarios:
    - agrega claves que falten en 'actual'
    - si la clave existe y es un dict, hace merge recursivo
    """
    actualizado = False
    for key, value in ejemplo.items():
        if key not in actual:
            actual[key] = value
            actualizado = True
        elif isinstance(value, dict) and isinstance(actual[key], dict):
            if merge_dicts(value, actual[key]):
                actualizado = True
    return actualizado


def inicializar_config(path_config="config.json", path_ejemplo="config.example.json"):
    """
    Verifica si config.json existe. Si no existe, lo crea a partir del ejemplo.
    Si existe, agrega las claves que falten del ejemplo sin borrar las existentes.
    """
    if not os.path.exists(path_config):
        if os.path.exists(path_ejemplo):
            shutil.copy(path_ejemplo, path_config)
            print(f"[INFO] '{path_config}' creado a partir de '{path_ejemplo}'.")
        else:
            raise FileNotFoundError(f"No se encontró '{path_config}' ni '{path_ejemplo}'.")

    with open(path_config, "r") as f:
        config = json.load(f)

    with open(path_ejemplo, "r") as f:
        ejemplo = json.load(f)

    se_actualizo = merge_dicts(ejemplo, config)

# Si hubo cambios, los guardamos
    if se_actualizo:
        with open(path_config, "w") as f:
            json.dump(config, f, indent=4)
        print("[INFO] Se actualizaron claves faltantes en 'config.json'.")