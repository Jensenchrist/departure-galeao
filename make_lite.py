# Gera lite.html a partir de index.html (versão leve). Rode de novo após mudar o index.
import re,sys
from PIL import Image
D='/home/claude/site2/'
s=open(D+'index.html').read()
def R(a,b,n=1):
    global s
    assert s.count(a)>=1,(a[:60]); s=s.replace(a,b)
# imagens menores (60%) e sem "fim de tarde" separado
for src,dst in [('map.jpg','lite_map.jpg'),('map_noite.jpg','lite_map_noite.jpg'),('maph_dia.jpg','lite_maph.jpg'),('maph_noite.jpg','lite_maph_noite.jpg')]:
    im=Image.open(D+src).convert('RGB');im.resize((round(im.width*.6),round(im.height*.6)),Image.LANCZOS).save(D+dst,quality=72)
R("url(map.jpg)","url(lite_map.jpg)");R("url(maph_dia.jpg)","url(lite_maph.jpg)")
R("url(maph_tarde.jpg)","url(lite_maph.jpg)");R("url(maph_noite.jpg)","url(lite_maph_noite.jpg)")
R("url(map_tarde.jpg)","url(lite_map.jpg)");R("url(map_noite.jpg)","url(lite_map_noite.jpg)")
R("<title>Departure · Galeão</title>","<title>Departure Lite · Galeão</title>")
R("<h1>DEPARTURE <span class=\"apt\">","<h1>DEPARTURE <span class=\"apt\">LITE · ")
# sem sombras/filtros pesados nos aviões
R("el.style.filter=`drop-shadow(${-4-34*p.al}px ${5+46*p.al}px ${3+9*p.al}px rgba(0,0,0,${.45-.25*p.al})) brightness(${PB})`;","")
# desenha aviões a ~30 fps
R("  drawPlanes();\n","  if((liteF=(liteF+1)%2)===0)drawPlanes();\n")
R("var PICK={};","var liteF=0;var PICK={};")
# mapa de voos sem retina
R("dpr=Math.min(2,window.devicePixelRatio||1)","dpr=1")
# sons: ambiente e chuva desligados por padrão (economiza memória)
R("var PICK={};SLOTS.forEach(x=>PICK[x.k]=x.o[0][0]);","var PICK={};SLOTS.forEach(x=>PICK[x.k]=x.o[0][0]);PICK.ambiente='off';PICK.chuva='off';")
# sem animações contínuas
R("</style>","""/* LITE */
.lt.w,.lt.reil{animation:none!important;opacity:.7}
#storm{animation:none!important;background:rgba(12,18,34,.45)!important}
.tg.emerg .tg-h,.sign.ok .plate,.sign.ready .plate,.tg-now{animation:none!important}
.sign.ready .plate{box-shadow:0 0 0 3px #5dff8f!important}
.pl img{filter:none!important}
.fl{background:#1d1d1d!important}
.lite-tag{position:fixed;left:8px;bottom:6px;z-index:5;font:700 10px sans-serif;color:#FDE934;background:#000;padding:2px 6px;border-radius:4px;opacity:.7;pointer-events:none}
</style>""")
R("<div class=\"app\">","<div class=\"lite-tag\">LITE</div>\n<div class=\"app\">")
open(D+'lite.html','w').write(s)
print('ok')
