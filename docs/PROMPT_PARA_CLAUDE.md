# Prompt: Abuelos Cazafantasmas

Copiá todo lo que está abajo de la línea y pegalo al principio de una conversación nueva con Claude. Si podés, adjuntá también `codigo/www/index.html` (el juego completo) y `assets/hoja-de-sprites.png` (cómo se ve). El repo es `towersdeveloper/abuelos-cazafantasmas` en GitHub.

---

Estoy desarrollando un juego para celular llamado **Abuelos Cazafantasmas** y quiero que me ayudes a seguir haciéndolo. Hablame en español rioplatense, directo y sin vueltas. Te paso todo el contexto.

## La idea

Tres jubilados argentinos trabajan de cazafantasmas. Cada partida es una casa embrujada distinta: hay que **atrapar a todos los fantasmas**, **juntar las pruebas** y **escapar por la puerta de entrada** antes de que la casa se venga abajo.

Es un juego **cooperativo**: cada abuelo tiene una herramienta distinta y ninguno puede hacer todo solo. La gracia está en coordinarse en medio del caos, cuando todos se están riendo.

## Tono y humor

- Humor absurdo y bien argentino (el PAMI, la merienda, Norma la del club, el conventillo de la Boca).
- La risa tiene que salir de las situaciones y de la física (un abuelo arrastrado por la aspiradora llevándose muebles puestos, otro corriendo sin control con los pelos parados), no de llenar la pantalla de carteles.
- Gráficos absurdos y exagerados, pero sin saturar.
- **Nada de emojis**, ni en el juego ni en los textos: se nota que es hecho con IA. Todo se dibuja a mano en código.

## Los abuelos

| Nombre | Herramienta | Qué hace | Movimiento |
|---|---|---|---|
| **Don Tito** | Aspiradora de fantasmas (mochila con manguera) | Mantiene apretado ASPIRAR: un rayo naranja debilita al fantasma. Mientras forcejea, el fantasma lo tironea y lo arrastra por la casa. Cuando el fantasma queda "cansado", el rayo lo va acercando. | Rápido |
| **Doña Pocha** | Andador con la trampa encima | Toca TRAMPA para dejarla en el piso o levantarla. Un fantasma cansado que pasa cerca de la trampa abierta es absorbido ("¡CLAC!"). Si se asusta, se le cae la trampa. | Lenta |
| **Cacho** | Linterna UV y cámara | Mantiene apretado LUZ UV: es el **único que hace ver a los fantasmas** (todos son invisibles) y las huellas ocultas. Si se queda quieto alumbrando una huella, le saca la foto. | Rápido |

**Atrapar un fantasma, paso a paso:** 1) Cacho lo alumbra con la UV; 2) mientras lo alumbra, Tito lo aspira hasta cansarlo y lo arrastra con el rayo; 3) Pocha tiene la trampa en el piso y el fantasma cansado cae adentro.

Juegan de 1 a 3 personas, cada una con su celu y su abuelo (ver Multijugador). Los abuelos sin jugador los maneja el que creó la sala: cambia de abuelo tocando las caras de la derecha, y los otros lo siguen o esperan si toca "ESPEREN". **Cacho sin jugador alumbra solo al fantasma más cercano**, para que el modo solo siga siendo jugable.

## Los fantasmas

| Tipo | Cómo es | Qué hace | Aguante |
|---|---|---|---|
| **De sábana** | Sábana blanca con medias rayadas que asoman abajo | Persigue a los abuelos para asustarlos | Bajo |
| **Gordo** | Bola verde de ectoplasma, alitas, muslo de pollo en la mano | Lento, deja charcos de baba donde todo resbala | Alto |
| **Poltergeist** | Violeta, un solo ojo, pantalla de lámpara como sombrero | Tira sillas y floreros a los abuelos | Medio |

Para atrapar a un fantasma: Tito lo aspira hasta cansarlo, Pocha tiene la trampa abierta cerca y el fantasma cansado cae adentro. Si nadie lo sigue aspirando, a los 2 segundos se recupera ("¡Ya descansé! ¡Buuu!").

**Regla UV (importante):** **todos los fantasmas** y las huellas son invisibles. **No se ven en absoluto** sin la luz UV: ni borrosos, ni transparentes, ni sus frases, ni su brillo. Aparecen solo mientras Cacho los alumbra y desaparecen en cuanto deja de hacerlo, así que Tito solo puede aspirar mientras Cacho alumbra. La excepción: un fantasma **cansado** (con estrellitas) o que está cayendo en la trampa se ve sin UV, así Tito lo puede llevar a la trampa aunque Cacho se vaya. Lo que sí delata a un fantasma invisible: la baba del gordo, los muebles que vuelan y los sustos.

## Las pruebas (se sortean 4 por casa)

- **Huella fantasmal:** solo con UV, quedarse quieto alumbrándola para sacarle la foto.
- **Muñeca que parpadea:** acercarse a juntarla.
- **Muestra de ectoplasma:** quedarse al lado un rato llenando el frasco.
- **Voz en la radio:** necesita **dos abuelos al lado a la vez** para sintonizarla. La voz dice: «Devuélvanme la pava eléctrica».

## Sustos, desmayos y escape

- Si un fantasma toca a un abuelo, o le pega un mueble tirado, el abuelo se asusta: grita y corre sin control un par de segundos con los pelos parados.
- **Al tercer susto se desmaya** (ojos de espiral, lengua afuera). Otro abuelo tiene que pararse al lado unos 2 segundos para despertarlo.
- Si se desmayan los tres, se pierde.
- Con todos los fantasmas atrapados y todas las pruebas juntas, empieza el **escape**: la casa tiembla, se abre la puerta, cae yeso del techo (asusta si te pega) y hay **50 segundos** para salir. Gana el que llega afuera; los que quedan adentro "los rescatan los bomberos".

**Estrellas:**
1. Escapar con las pruebas.
2. Que salgan los tres.
3. Cuatro sustos o menos en total.

## Las casas

Cada partida genera una casa nueva al azar: cuartos con piso de madera, baldosa o alfombra, puertas, muebles con física (silla, sillón, mesa, lámpara, cajón, piano) que se empujan y chocan, y fantasmas y pruebas repartidos.

- **Nombres:** la Casona de los Pérez Gutiérrez, el ex Hotel Bristol de Mar del Plata, la Mansión de la Tía Clotilde, el Caserón de Adrogué, la Quinta Abandonada de Escobar, el Conventillo de la Boca, la Estancia La Llorona, el Palacete del Doctor Bustamante.
- **Motivos del trabajo:** "La dueña dice que los fantasmas le comen las medialunas", "Pagan en efectivo y con merienda incluida", "El nieto de Norma juró que vio algo en el placard", "Es eso o volver al taller de cerámica", "Un fantasma le debe plata a Cacho desde 1974", "La inmobiliaria no la puede vender ni regalada".

## Todos los textos actuales

**Abuelos asustados (al azar):** ¡MAMITA! · ¡MI MARCAPASOS! · ¡AUXILIO, NORMA! · ¡QUE ALGUIEN LLAME AL PAMI! · ¡ME SALTÓ LA DENTADURA! · ¡SOCORRO!

**Al despertar:** ¿Qué pasó? ¿Ya es la hora del té? · Estoy bien, estoy bien. · ¿Quién apagó la luz?

**Doña Pocha:** «¡SE ME CAYÓ LA TRAMPA!» (si se asusta) · «La trampa quedó allá, querido.» (si toca el botón lejos de la trampa)

**Radio con uno solo:** «Con uno solo no se sintoniza. ¡Vengan!»

**Fantasma de sábana:** ¡Buuu! · ¡Fuera de mi casa! · ¡Buuu! Digo, buenas tardes. · ¡Esta es mi sábana!

**Fantasma gordo:** ¿Hay más torta? · Ñam ñam ñam · ¡Mi heladera! · ¿Ese sánguche es suyo?

**Poltergeist:** ¡Volá, silla! · ¡Ja ja ja! · ¿Quién se tomó mi té? · ¡Tomá, un florero!

**Cuando la UV los descubre:** sábana «¡Uy, me vieron!» / «¡Ey, no me alumbre!» · gordo «¡No me mire, estoy comiendo!» / «¡Apague eso!» · poltergeist «¡Uy, me vieron!» / «¡Me encandiló!»

**Cartel la primera vez que manejás a cada abuelo:** Tito «Sos Tito. Cuando Cacho alumbra un fantasma, mantené ASPIRAR. Cuando se cansa, arrastralo hasta la trampa de Pocha.» · Pocha «Sos Pocha. Dejá la trampa en el piso (TRAMPA) por donde Tito va a traer al fantasma cansado.» · Cacho «Sos Cacho. Sin tu luz nadie ve a los fantasmas: alumbralos para que Tito los pueda aspirar.»

**Fantasma aspirado:** ¡Soltame! · ¡Nooo! · ¡Aaah, cosquillas! · ¡Me despeina! · «Uf... estoy fundido...» (cuando se cansa)

**Fantasma atrapado:** ¡Noooooo! · ¡Me voy por el caño! · ¡Volveré!

**Carteles:** «¡CANSADO!» · «¡CLAC! ¡ATRAPADO!» · «¡FOTO!» · «¡La muñeca me guiñó un ojo!» · «Frasco lleno» · «[Nombre] se desmayó»

## Estilo visual

- Vista **cenital** (desde arriba, con los personajes un poco de frente), a pantalla completa en vertical.
- Todo dibujado en canvas con **contornos negros gruesos que "tiemblan"** como dibujo animado: las formas se redibujan con un pequeño ruido cada ~120 ms.
- **La casa está a oscuras.** Solo se ve lo que alumbran las linternas de los abuelos (un cono de luz cada uno) más un halo alrededor de ellos. Cada tanto hay un relámpago que ilumina todo.
- Los fantasmas brillan con un resplandor suave. La trampa abierta tira un haz de luz amarilla hacia arriba.
- **Paleta:** noche violeta oscuro (#130b1c / #2b1b3d), papel viejo (#f3e6cf), verde ectoplasma (#93f56d), naranja calabaza (#ff8a3d, el rayo), violeta UV (#b892ff), tinta (#1a1020).
- **Fuentes:** Creepster para títulos y carteles, Nunito para el resto. Van incluidas en el juego, que anda sin internet.
- **Colores de los abuelos:** Tito rojo (#c9533f), Pocha verde (#4f9a5a, con rodete gris), Cacho azul (#4a6fc4).

## Sonido

Todo **sintetizado con WebAudio**, sin archivos de audio: zumbido de la aspiradora en loop, "buuu" con vibrato de los fantasmas, gritos con un tono distinto para cada abuelo, clac de la trampa, flash de la cámara, trueno, choques de muebles, chapoteo en la baba, estática de radio, risa de fantasma, derrumbe, y música corta de victoria y derrota.

## Controles

- **Joystick:** tocar y arrastrar en cualquier parte de la pantalla.
- **Botón grande de acción:** cambia según el abuelo (ASPIRAR / DEJAR o AGARRAR TRAMPA / LUZ UV).
- **SÍGANME / ESPEREN.**
- **Caras de la derecha:** cambiar de abuelo.
- **Teclado:** WASD, J acción, 1-3 o Tab para cambiar de abuelo, F síganme.

## Pantallas

Menú (Crear partida / Unirse a partida / Cómo se juega) → Sala (código y elección de abuelo) → Briefing de la casa → Partida → Resultado → Otra casa o volver a la sala. **Cómo se juega** explica el rol de cada abuelo con su dibujo, las pruebas, los sustos y el modo multijugador.

## Multijugador

- De 1 a 3 jugadores, uno por abuelo. Uno toca **Crear partida** y le sale un **código de 4 letras**; los demás tocan **Unirse a partida** y lo escriben.
- Conexión **peer-to-peer con WebRTC** usando **PeerJS 1.5.5** (incluido en `www/vendor`). Internet hace falta solo para encontrarse (servidor de señalización gratuito de PeerJS, con STUN y TURN propios); después los datos van de celu a celu. No hace falta estar en el mismo WiFi: se puede jugar desde distintos países, con más demora para los que no crearon la sala.
- Modelo **host autoritativo**: el celu del que creó la sala corre `step()`. Los demás mandan su joystick unas 30 veces por segundo y reciben el estado unas 20 veces por segundo junto con los eventos (sonidos, carteles), e interpolan.
- Latido cada 2 segundos: si un jugador no responde en 10 segundos, su abuelo pasa al host. Si se va el host, los demás vuelven al menú.
- La web y la app juegan juntas (así se suman amigos con iPhone desde el navegador).
- Sin internet se puede jugar solo.

## Parte técnica

- El juego es **un solo archivo HTML** (`www/index.html`) con CSS y JS adentro. Fuentes en `www/fonts/` y PeerJS en `www/vendor/` (los copia `npm run vendor`).
- Se empaqueta con **Capacitor 8** para Android: ID `com.abuelos.cazafantasmas`, target SDK 36, solo vertical. El botón atrás de Android hace lo que corresponde según la pantalla. El sonido se pausa si salís de la app.
- **Versión:** sale solo de `"version"` en `package.json` (hoy 1.0.0). De ahí salen el `versionName`, el `versionCode` (1.0.0 → 10000) y el nombre de los archivos: `abuelos-cazafantasmas-vX.Y.Z`.
- **GitHub Actions:**
  - *Compilar AAB y APK*: en cada push a `main`, compila el `.aab` (para Play Store) y el `.apk` firmados con la llave de subida (secretos `ANDROID_KEYSTORE_BASE64` y `ANDROID_KEYSTORE_PASSWORD`, alias `abuelos`) y los publica en Releases.
  - *Publicar en GitHub Pages*: publica `www/` en `towersdeveloper.github.io/abuelos-cazafantasmas` para jugar desde el navegador.
- Arquitectura:
  - Toda la partida vive en un objeto `G`.
  - `step(G, dt)` simula a 60 Hz con los inputs de cada jugador y deja eventos en `G.events`.
  - El dibujo (`render`) y el sonido (`handleEvents`) solo leen el estado y los eventos.

## Para dónde vamos

- Probar el multijugador con celus reales y ajustar.
- **Predicción del lado del cliente**, para que el que se une no sienta el retraso cuando juega lejos.
- Aviso de "actualizá el juego" si los celus tienen versiones distintas.
- Más casas, más tipos de fantasmas, más pruebas y más situaciones de coordinación entre abuelos.
- Siempre: humor absurdo pero no forzado, sin emojis, gráficos dibujados a mano.

Cuando te pida cambios, mantené la estructura de un solo HTML y el estilo dibujado a mano, y avisame si algo rompe la parte de Android o el multijugador.
