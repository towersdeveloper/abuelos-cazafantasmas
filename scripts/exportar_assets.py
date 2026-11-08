#!/usr/bin/env python3
"""Exporta los sprites (PNG transparentes) y los sonidos (WAV) del juego.

El juego dibuja todo y genera los sonidos por código, así que se abren con un
navegador sin ventana y se graban tal cual. Uso:

    python scripts/exportar_assets.py www/index.html carpeta-de-salida

Necesita: pip install playwright pillow  y  python -m playwright install chromium
(o la variable CHROME_PATH apuntando a un Chrome/Chromium ya instalado).
"""
import asyncio, base64, os, sys, wave
from playwright.async_api import async_playwright

JS_SPR=r"""
async()=>{
 window.requestAnimationFrame=()=>0; await new Promise(r=>setTimeout(r,60));
 await document.fonts.load('40px Creepster');await document.fonts.load('900 16px Nunito');
 G=buildHouse();G.trap.carried=true;BOIL=0;
 const out={};
 function shot(name,w,h,fn){cv.width=w*2;cv.height=h*2;ctx.setTransform(2,0,0,2,0,0);ctx.clearRect(0,0,w,h);ctx.save();fn(w,h);ctx.restore();out[name]=cv.toDataURL('image/png')}
 function pose(p,set){p.x=110;p.y=150;p.vx=p.vy=0;p.panic=0;p.fainted=false;p.beam=null;p.uv=false;p.escaped=true;p.scares=0;p.dist=0;p.face=1;p.aim=0;
   for(const k of['head','hl','hr']){p[k].x=p.x;p[k].y=p.y;p[k].vx=p[k].vy=0}set&&set(p);
   const others=G.players.filter(q=>q!==p);const keep=G.players;G.players=[p];for(let i=0;i<150;i++){cosmetic(1/60);BOIL=0;if(set)set(p)}G.players=keep;}
 const slug={0:'don-tito',1:'dona-pocha',2:'cacho'};
 for(const p of G.players){
   const n=slug[p.id];
   const P=[['parado',null],['caminando',q=>{q.vx=180;q.dist=(q.dist||0)+3}],['susto',q=>{q.panic=1;q.vx=120}],['desmayado',q=>{q.fainted=true}]];
   if(p.tool==='vac')P.push(['aspirando',q=>{q.beam='miss';q.aim=0}]);
   if(p.tool==='uv')P.push(['luz-uv',q=>{q.uv=true;q.aim=0}]);
   for(const [k,f] of P){if(p.tool==='trap')G.trap.carried=true;pose(p,f);
     shot(`personajes/${n}_${k}.png`,220,240,()=>{if(k==='aspirando'){drawPerson(p);drawBeam(p,'miss')}else drawPerson(p)});}
   if(p.tool==='trap'){G.trap.carried=false;pose(p,null);shot(`personajes/${n}_sin-trampa.png`,220,240,()=>drawPerson(p));G.trap.carried=true}
 }
 G.players.forEach((p,i)=>{p.x=-999;p.y=-999});
 const mk=(type,o)=>Object.assign({type,x:100,y:100,vx:0,vy:0,r:type==='jefe'?50:type==='gordo'?40:28,ph:0,hp:1,max:1,weak:false,beamT:0,rev:0,sucked:0,seed:42+type.length,alive:true,say:null},o||{});
 for(const t of['sabana','gordo','polter','jefe']){const z=t==='jefe'?280:200,m=mk(t,{rev:1,x:z/2,y:z/2+(t==='jefe'?20:0)});
   shot(`fantasmas/${t}.png`,z,z,()=>drawGhost(m));
   shot(`fantasmas/${t}_cansado.png`,z,z,()=>drawGhost(Object.assign({},m,{weak:true})));
 }
 shot('fantasmas/sabana_sin-uv.png',200,200,()=>drawGhost(mk('sabana',{rev:0})));
 for(const it of Object.keys(ITEMS))shot(`objetos/robado_${it}.png`,90,80,()=>drawItem({k:'item',it,x:45,y:42,done:false,car:-1,seed:17}));
 shot('objetos/tablero-de-luz.png',110,100,()=>drawFuse({k:'fuse',x:55,y:56,done:false,prog:0,seed:19}));
 shot('objetos/tablero-de-luz_arreglado.png',110,100,()=>drawFuse({k:'fuse',x:55,y:56,done:true,prog:0,seed:19}));
 const F=['silla','sillon','mesa','lampara','cajon','piano'];const R={silla:16,sillon:27,mesa:32,lampara:12,cajon:22,piano:40};
 for(const k of F)shot(`objetos/mueble_${k}.png`,120,110,()=>drawFurn({kind:k,x:58,y:52,r:R[k],ang:0,seed:7,hue:330}));
 for(const k of['doll','ecto','radio']){const names={doll:'prueba_muneca',ecto:'prueba_ectoplasma',radio:'prueba_radio'};
   shot(`objetos/${names[k]}.png`,140,130,()=>drawEvidence({k,x:70,y:80,done:false,prog:0,rev:0,seed:11}))}
 shot('objetos/prueba_huella-uv.png',120,110,()=>drawMark({k:'mark',x:60,y:62,done:false,prog:0,rev:1,seed:13}));
 G.trap.carried=false;G.trap.x=70;G.trap.y=70;G.trap.clack=0;shot('objetos/trampa_abierta.png',140,110,()=>drawTrap());
 G.trap.clack=1;shot('objetos/trampa_cerrada.png',140,110,()=>drawTrap());
 const room=(fl)=>({x:0,y:0,w:240,h:240,name:'',floor:fl,tint:0});
 for(const fl of['wood','tile','carpet']){const nm={wood:'madera',tile:'baldosa',carpet:'alfombra'}[fl];shot(`escenario/piso_${nm}.png`,240,240,()=>drawFloor(room(fl),-10,999,-10,999))}
 shot('escenario/pared.png',240,40,()=>drawWall({x:5,y:5,w:230,h:30},31));
 shot('escenario/baba.png',140,100,()=>{well(70,50,55,34,0,5,4,14);fs('rgba(120,220,90,.55)',3,'rgba(30,90,30,.8)')});
 shot('escenario/yeso-que-cae.png',80,70,()=>{wrect(20,18,40,30,40,3);fs('#d9cdb8',3)});
 shot('escenario/puerta-de-entrada.png',200,40,()=>{wrect(10,5,180,30,999);fs('#6b4226',3);ctx.fillStyle='#ffd23f';ctx.beginPath();ctx.arc(176,20,4,0,TAU);ctx.fill()});
 const fake={hr:{x:20,y:60},aim:0};shot('escenario/rayo-aspiradora.png',240,120,()=>drawBeam(fake,'miss'));
 shot('escenario/estrella-mareo.png',40,40,()=>{ctx.fillStyle='#ffd23f';drawStar(20,20,14)});
 return out;}
"""
JS_SND=r"""
async()=>{
 const enc=(buf)=>{const d=buf.getChannelData(0);let end=d.length;while(end>2000&&Math.abs(d[end-1])<.0008)end--;end=Math.min(d.length,end+2205);
  const ab=new ArrayBuffer(44+end*2),v=new DataView(ab);const w=(o,s)=>{for(let i=0;i<s.length;i++)v.setUint8(o+i,s.charCodeAt(i))};
  w(0,'RIFF');v.setUint32(4,36+end*2,true);w(8,'WAVE');w(12,'fmt ');v.setUint32(16,16,true);v.setUint16(20,1,true);v.setUint16(22,1,true);v.setUint32(24,44100,true);v.setUint32(28,88200,true);v.setUint16(32,2,true);v.setUint16(34,16,true);w(36,'data');v.setUint32(40,end*2,true);
  for(let i=0;i<end;i++)v.setInt16(44+i*2,Math.max(-1,Math.min(1,d[i]))*32767,true);
  let s='';const u=new Uint8Array(ab);for(let i=0;i<u.length;i+=32768)s+=String.fromCharCode.apply(null,u.subarray(i,i+32768));return btoa(s)};
 const list=[['fantasma-buu',()=>SFX.boo(1)],['fantasma-gordo-buu',()=>SFX.boo(.7)],['grito-don-tito',()=>SFX.scream(1)],['grito-dona-pocha',()=>SFX.scream(1.25)],['grito-cacho',()=>SFX.scream(.85)],
  ['desmayo',()=>SFX.faint()],['despertar',()=>SFX.revive()],['trampa-clac',()=>SFX.trap()],['fantasma-absorbido',()=>SFX.suck()],['trueno',()=>SFX.thunder()],['flash-foto',()=>SFX.flash()],
  ['mueble-choque',()=>SFX.crash()],['baba-resbalon',()=>SFX.squish()],['prueba-conseguida',()=>SFX.pick()],['progreso-tic',()=>SFX.tick()],['paso',()=>SFX.step()],['crujido',()=>SFX.creak()],
  ['puerta',()=>SFX.door()],['derrumbe',()=>SFX.rumble()],['victoria',()=>SFX.win()],['derrota',()=>SFX.lose()],['radio-estatica',()=>SFX.radio()],['risa-fantasma',()=>SFX.ghostLaugh()],
  ['aspiradora-loop',()=>{beamSound(true)}],
  ...[['don-tito',0],['dona-pocha',1],['cacho',2]].flatMap(([n,i])=>['scream','faint','grunt','effort','bonk','hup','happy','revive','wow','mumble'].map(k=>[`voz-${n}-${k}`,()=>vox(i,k)]))];
 const out={};
 for(const [n,f] of list){ac=new OfflineAudioContext(1,44100*(n==='aspiradora-loop'?2:3),44100);nb=null;beamNode=null;for(const k in lastS)delete lastS[k];f();const buf=await ac.startRendering();out[n]=enc(buf)}
 ac=null;nb=null;beamNode=null;return out}
"""

def hoja_de_sprites(out):
    from PIL import Image, ImageDraw, ImageFont
    files = []
    for sub in ['personajes', 'fantasmas', 'objetos', 'escenario']:
        for f in sorted(os.listdir(os.path.join(out, sub))):
            files.append(f'{sub}/{f}')
    cell, cols = 220, 6
    rows = (len(files) + cols - 1) // cols
    sheet = Image.new('RGBA', (cols * cell, rows * (cell + 28)), (43, 27, 61, 255))
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 13)
    except Exception:
        font = ImageFont.load_default()
    d = ImageDraw.Draw(sheet)
    for i, f in enumerate(files):
        im = Image.open(os.path.join(out, f)).convert('RGBA')
        im.thumbnail((cell - 16, cell - 16))
        x, y = (i % cols) * cell, (i // cols) * (cell + 28)
        d.rectangle([x + 4, y + 4, x + cell - 4, y + cell - 4], fill=(30, 18, 44, 255))
        sheet.alpha_composite(im, (x + (cell - im.width) // 2, y + (cell - im.height) // 2))
        d.text((x + 8, y + cell - 2), f.split('/')[1][:-4], fill=(243, 230, 207, 255), font=font)
    sheet.convert('RGB').save(os.path.join(out, 'hoja-de-sprites.png'))

async def main(html, out):
    for sub in ['personajes', 'fantasmas', 'objetos', 'escenario', 'sonidos']:
        os.makedirs(os.path.join(out, sub), exist_ok=True)
    async with async_playwright() as p:
        exe = os.environ.get('CHROME_PATH') or None
        b = await p.chromium.launch(executable_path=exe, args=['--no-sandbox', '--autoplay-policy=no-user-gesture-required'])
        pg = await b.new_page()
        errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        await pg.goto('file://' + os.path.abspath(html))
        await pg.wait_for_timeout(400)
        spr = await pg.evaluate(JS_SPR)
        for k, v in spr.items():
            with open(os.path.join(out, k), 'wb') as fh:
                fh.write(base64.b64decode(v.split(',')[1]))
        snd = await pg.evaluate(JS_SND)
        for k, v in snd.items():
            with open(os.path.join(out, 'sonidos', k + '.wav'), 'wb') as fh:
                fh.write(base64.b64decode(v))
        await b.close()
    if errs:
        raise SystemExit('Errores en la página: ' + '; '.join(errs))
    hoja_de_sprites(out)
    print(f'{len(spr)} sprites y {len(snd)} sonidos en {out}')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    asyncio.run(main(sys.argv[1], sys.argv[2]))
