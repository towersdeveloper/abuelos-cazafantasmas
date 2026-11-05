# Abuelos Cazafantasmas

Juego para Android hecho en un solo HTML (`www/index.html`) y empaquetado con Capacitor 8.
Tres jubilados (Don Tito con la aspiradora, Doña Pocha con la trampa en el andador y Cacho con la linterna UV) atrapan fantasmas, juntan pruebas y escapan de una casa embrujada.

- **ID de la app:** `com.abuelos.cazafantasmas` (cambialo **antes** de la primera subida: después no se puede).
- **Target SDK:** 36 · **Min SDK:** 24 · Orientación vertical.
- Anda sin internet: las fuentes están adentro de `www/fonts`.

## Estructura

```
www/index.html          el juego completo (lo único que editás para cambiar el juego)
www/fonts/              fuentes locales (las copia `npm run fonts`)
android/                proyecto Android generado por Capacitor (se sube a git)
assets/                 ícono y splash de origen (1024 y 2732 px)
store/                  imágenes para la ficha de Play Store (ícono 512 y gráfico 1024x500)
capacitor.config.json   nombre, ID y configuración de la app
PRIVACIDAD.md           plantilla de política de privacidad
```

## Requisitos

- Node.js 20 o más nuevo
- Android Studio (trae el SDK y Java)

## Primera vez

```bash
npm install
npm run sync      # copia las fuentes y sincroniza www/ con android/
npm run open      # abre el proyecto en Android Studio
```

En Android Studio, con el celu conectado por USB (depuración USB activada), tocá **Run**.

## Cambiar el juego

1. Editá `www/index.html`.
2. `npm run sync`
3. Run en Android Studio.

Si cambiás el ícono o el splash: reemplazá los archivos en `assets/` y corré `npm run assets`.

## Subir a Play Store

### 1. Crear la llave de firma (una sola vez)

```bash
keytool -genkey -v -keystore abuelos-release.jks -keyalg RSA -keysize 2048 -validity 10000 -alias abuelos
```

Guardá el `.jks` y las claves en un lugar seguro (y con copia). **Si los perdés, no vas a poder actualizar la app.**
Git ya ignora `*.jks` y `keystore.properties`.

### 2. Configurar la firma

Copiá `android/keystore.properties.example` como `android/keystore.properties` y completá tus datos.

### 3. Subir la versión y generar el paquete

En `android/app/build.gradle`, aumentá `versionCode` en cada subida (1, 2, 3…) y ajustá `versionName` ("1.0", "1.1"…).

```bash
npm run sync
cd android
./gradlew bundleRelease
```

El archivo queda en `android/app/build/outputs/bundle/release/app-release.aab`.
También podés hacerlo desde Android Studio: **Build → Generate Signed App Bundle**.

### 4. En Play Console

- **Crear app:** nombre "Abuelos Cazafantasmas", juego, gratis.
- **Ficha de la tienda:** ícono `store/icon-512.png`, gráfico destacado `store/feature-graphic-1024x500.png` y al menos 2 capturas de pantalla del juego (sacalas desde el celu).
- **Política de privacidad:** publicá `PRIVACIDAD.md` en una URL pública (por ejemplo GitHub Pages o Google Sites) y pegá el link.
- **Seguridad de los datos:** el juego no recolecta ni comparte datos y no usa internet.
- **Clasificación de contenido:** completá el cuestionario (hay sustos de dibujo animado, sin violencia real).
- **Público objetivo:** si marcás menores de 13, Google aplica reglas extra de la política de Familias. Decidilo antes de completar.
- **Pruebas:** las cuentas personales de desarrollador nuevas tienen que hacer una prueba cerrada con al menos 12 testers durante 14 días antes de poder publicar en producción. Si tu cuenta es más vieja, puede que no te lo pida.

Después subís el `.aab` en la pista que corresponda y mandás a revisión.
