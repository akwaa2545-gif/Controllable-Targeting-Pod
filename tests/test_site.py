import hashlib, pathlib, unittest
from html.parser import HTMLParser
ROOT=pathlib.Path(__file__).resolve().parents[1]
class Site(HTMLParser):
 def __init__(self): super().__init__(); self.links=[]; self.images=[]; self.ids=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a: self.ids.append(a['id'])
  if tag=='a': self.links.append(a.get('href',''))
  if tag=='img': self.images.append(a)
class Tests(unittest.TestCase):
 def test_site_exists_and_local_links_resolve(self):
  p=ROOT/'docs/index.html'; self.assertTrue(p.exists(),'Website not implemented')
  s=Site(); s.feed(p.read_text())
  self.assertEqual(len(s.ids),len(set(s.ids)))
  for h in s.links:
   if h.startswith('#'): self.assertIn(h[1:],s.ids,h)
   elif not h.startswith(('https:','mailto:')): self.assertTrue((p.parent/h.split('#')[0]).is_file(),h)
  self.assertEqual(len(s.images),4)
  for i in s.images: self.assertTrue(i.get('alt')); self.assertTrue((p.parent/i['src']).is_file())
 def test_versions_limits_and_defaults_are_visible(self):
  p=ROOT/'docs/index.html'; self.assertTrue(p.exists(),'Website not implemented')
  t=p.read_text()
  for phrase in ['0.1.17','0.5.7','0.34.6','5.4.23.5','5.4.23.6','experimental','not live-game','None','Layout preview','HUD illustration','Enabled','false']:
   self.assertIn(phrase,t)
 def test_release_hashes(self):
  for file,sha in {'Observer-0.5.7_TGP-0.1.17-runtime.zip':'979d4cc7f1fa604d5cb91f5d783244bbb1d8908ac5c3acebecc858e8476a6c88','Observer.dll':'88a3499bc65cefebf119c60c9a2f5b42cc7829bb46718de896850bb1d0791d2d','TargetingPodDisplay.dll':'5e8ca78f9a11c90539eef3193a637d4e864ca1b62f39a0012fe193be0403f7b5'}.items():
   p=ROOT/'docs/downloads'/file; self.assertTrue(p.is_file(),file); self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),sha)
if __name__=='__main__': unittest.main()
