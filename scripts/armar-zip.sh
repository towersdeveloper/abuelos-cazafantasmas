#!/usr/bin/env bash
# Arma dist/abuelos-cazafantasmas-vX.Y.Z.zip con la app, el código, los assets y el prompt.
# Antes: compilar (dist/*.aab y dist/*.apk) y exportar assets:
#   python scripts/exportar_assets.py www/index.html "dist/abuelos-cazafantasmas-vX.Y.Z/assets"
set -euo pipefail
cd "$(dirname "$0")/.."
V=$(node -p "require('./package.json').version")
N="abuelos-cazafantasmas-v$V"
D="dist/$N"
mkdir -p "$D/app" "$D/assets/app" "$D/assets/tienda" "$D/assets/fuentes"
for f in dist/*.aab dist/*.apk; do [ -f "$f" ] && cp "$f" "$D/app/"; done
rm -rf "$D/codigo" && git archive --format=tar --prefix=codigo/ HEAD | tar -x -C "$D"
cp assets/icon-only.png "$D/assets/app/icono-1024.png"
cp assets/splash.png "$D/assets/app/pantalla-de-carga-2732.png"
cp store/icon-512.png "$D/assets/tienda/icono-512.png"
cp store/feature-graphic-1024x500.png "$D/assets/tienda/grafico-destacado-1024x500.png"
cp www/fonts/*.woff2 "$D/assets/fuentes/"
cp node_modules/@fontsource/creepster/LICENSE "$D/assets/fuentes/LICENCIA-creepster.txt"
cp node_modules/@fontsource/nunito/LICENSE "$D/assets/fuentes/LICENCIA-nunito.txt"
cp docs/PROMPT_PARA_CLAUDE.md "$D/"
sed "s/{{VERSION}}/$V/g" docs/LEEME-zip.md > "$D/LEEME.md"
rm -f "dist/$N.zip"
(cd dist && zip -qr "$N.zip" "$N")
echo "Listo: dist/$N.zip"
