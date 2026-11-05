// Copia fuentes y PeerJS de node_modules a www/ para que la app no dependa de CDNs.
import { mkdirSync, copyFileSync } from 'node:fs';
const files = [
  ['@fontsource/creepster/files/creepster-latin-400-normal.woff2', 'www/fonts/creepster-400.woff2'],
  ['@fontsource/nunito/files/nunito-latin-700-normal.woff2', 'www/fonts/nunito-700.woff2'],
  ['@fontsource/nunito/files/nunito-latin-800-normal.woff2', 'www/fonts/nunito-800.woff2'],
  ['@fontsource/nunito/files/nunito-latin-900-normal.woff2', 'www/fonts/nunito-900.woff2'],
  ['peerjs/dist/peerjs.min.js', 'www/vendor/peerjs.min.js'],
];
mkdirSync('www/fonts', { recursive: true });
mkdirSync('www/vendor', { recursive: true });
for (const [src, dst] of files) copyFileSync(`node_modules/${src}`, dst);
console.log('Fuentes y PeerJS copiados en www/');
