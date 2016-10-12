#!/bin/bash

# Herramientas básicas necesarias
PANDOC=$(which pandoc 2>/dev/null)

# Abandonar si no se encuentra alguna de las herramientas necesarias
if [ "$PANDOC" == "" ]; then
  echo "No se encontró el comando 'pandoc'... Abortando." > /dev/stderr
  exit 1
fi

cat Preambulo.md ParteEstadisticoOrdenK.md ParteCaminoMinimoGrafos.md |
  $PANDOC -N --template=plantilla.tex -o Informe.pdf

echo "Informe generado!"
