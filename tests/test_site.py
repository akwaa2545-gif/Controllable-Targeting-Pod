import hashlib, pathlib, unittest, json, re
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
  for file,sha in {'TargetingPodDisplay.dll':'5e8ca78f9a11c90539eef3193a637d4e864ca1b62f39a0012fe193be0403f7b5'}.items():
   p=ROOT/'docs/downloads'/file; self.assertTrue(p.is_file(),file); self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),sha)
 def test_only_tgp_binary_is_distributed(self):
  files={p.name for p in (ROOT/'docs/downloads').iterdir() if p.suffix in ['.dll','.zip']}
  self.assertEqual(files,{'TargetingPodDisplay.dll'})
  readme=(ROOT/'README.md').read_text()
  self.assertIn('docs/assets/tgp-in-game.jpg',readme)
  self.assertIn('TGP-only',readme)
  self.assertNotIn('downloads/Observer.dll',readme)
  self.assertNotIn('runtime.zip',readme)
  html=(ROOT/'docs/index.html').read_text()
  self.assertNotIn('href="downloads/Observer.dll"',html)
  self.assertNotIn('runtime.zip',html)
  self.assertIn('Standalone setup',html)
 def test_readme_links_and_release_metadata_agree(self):
  p=ROOT/'README.md';s=p.read_text()
  for link in re.findall(r'\]\(([^)]+)\)',s)+re.findall(r'src="([^"]+)"',s):
   if not link.startswith(('https://','#')): self.assertTrue((ROOT/link).is_file(),link)
  info=json.loads((ROOT/'docs/downloads/BUILD_INFO.json').read_text())
  dll=ROOT/'docs/downloads/TargetingPodDisplay.dll'
  self.assertEqual(info['sha256'],hashlib.sha256(dll.read_bytes()).hexdigest())
  self.assertEqual(info['size_bytes'],dll.stat().st_size)
  self.assertEqual((ROOT/'docs/downloads/SHA256SUMS.txt').read_text().strip(),info['sha256']+'  TargetingPodDisplay.dll')
  self.assertIn(info['sha256'],s)
  self.assertEqual(info['distribution'],'TGP-only')
  self.assertFalse(info['runtime_validated'])
if __name__=='__main__': unittest.main()
