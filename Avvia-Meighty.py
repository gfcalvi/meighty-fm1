#!/usr/bin/env python3
"""Serve this bundle locally; no upload, LAN exposure or directory listing."""
from pathlib import Path
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
from urllib.parse import urlsplit
import argparse,mimetypes,webbrowser,socket
base=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--no-browser',action='store_true');p.add_argument('--lan',action='store_true');p.add_argument('--port',type=int,default=8799);a=p.parse_args()
names=['Meighty.html','Installazione.html','Backup.html','Slot-e-Convertitore.html','LEGGIMI.html','Manuale-Meighty.pdf','Meighty-1.01-RC7.fwsc','Sorgenti.zip','MANIFEST.json','SHA256SUMS','LICENSE-Meighty.md','LICENSE-LZFSE.txt']
allowed={n:base/n for n in names}
for f in (base/'RemoteFM1').glob('*.rfm1'):allowed['RemoteFM1/'+f.name]=f
class Handler(BaseHTTPRequestHandler):
 def do_GET(self):self.reply(True)
 def do_HEAD(self):self.reply(False)
 def reply(self,body):
  name=urlsplit(self.path).path.lstrip('/') or 'Meighty.html'
  if name not in allowed or not allowed[name].is_file():self.send_error(404);return
  raw=allowed[name].read_bytes();self.send_response(200);self.send_header('Content-Type',mimetypes.guess_type(name)[0] or 'application/octet-stream');self.send_header('Content-Length',str(len(raw)));self.send_header('Cache-Control','no-store');self.send_header('X-Content-Type-Options','nosniff');self.end_headers()
  if body:self.wfile.write(raw)
 def log_message(self,*args):pass
url='http://127.0.0.1:'+str(a.port)+'/Meighty.html'
try:server=ThreadingHTTPServer(('0.0.0.0' if a.lan else '127.0.0.1',a.port),Handler)
except OSError as e:raise SystemExit('Porta locale occupata o non disponibile: '+str(e))
print('Meighty 1.01 RC7 / caricamento brani: '+url+'\nCTRL+C chiude il server.',flush=True)
if a.lan:
 try:
  with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
   s.connect(('192.0.2.1',80));ip=s.getsockname()[0]
  print('iPhone sulla stessa Wi-Fi: http://'+ip+':'+str(a.port)+'/Meighty.html',flush=True)
 except OSError:print('Usa l’indirizzo IP del Mac mostrato in Impostazioni → Rete.',flush=True)
 print('In MIDIWeb scegli Make Available Offline. Poi arresta il server: il Mac non serve durante l’uso offline. Solo i file pubblici del pacchetto sono esposti sulla rete locale, senza login.',flush=True)
if not a.no_browser and not a.lan:
 try:webbrowser.get('chrome').open(url)
 except webbrowser.Error:webbrowser.open(url)
try:server.serve_forever()
except KeyboardInterrupt:pass
finally:server.server_close()
