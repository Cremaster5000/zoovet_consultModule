#!/bin/bash

# Ruta del entorno virtual
VENV_PATH="/home/lalo/Documentos/consult_module"

cd $VENV_PATH

# Ruta del script de Python
PYTHON_SCRIPT="/home/lalo/Documentos/consult_module/main.py"

# Activar el entorno virtual
source "venv/bin/activate"

# Ejecutar el script de Python
python3 "main.py"

# Desactivar el entorno virtual
deactivate
