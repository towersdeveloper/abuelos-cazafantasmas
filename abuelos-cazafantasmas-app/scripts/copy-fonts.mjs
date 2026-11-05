// Copia las fuentes de node_modules a www/fonts para que el juego ande sin internet.
import { mkdirSync, copyFileSync } from 'node:fs';
const out = 'www/fonts';
mkdirSync(out, { recursive: true });
const files = [
  ['@fontsource/creepster/files/creepster-latin-400-normal.woff2', 'creepster-400.woff2'],
  ['@fontsource/nunito/files/nunito-latin-700-normal.woff2', 'nunito-700.woff2'],
  ['@fontsource/nunito/files/nunito-latin-800-normal.woff2', 'nunito-800.woff2'],
  ['@fontsource/nunito/files/nunito-latin-900-normal.woff2', 'nunito-900.woff2'],
];
for (const [src, dst] of files) copyFileSync(`node_modules/${src}`, `${out}/${dst}`);
console.log('Fuentes copiadas en', out);
