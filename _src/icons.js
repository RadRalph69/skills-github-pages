// Erzeugt App-/Touch-Icons aus favicon.svg (quadratisch, ohne Transparenz).
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
const root = path.join(__dirname, '..');
const svg = fs.readFileSync(path.join(root, 'favicon.svg'), 'utf8').replace('rx="14"', 'rx="0"');
(async () => {
  const b = await chromium.launch();
  for (const [name, size] of [['apple-touch-icon', 180], ['icon-192', 192], ['icon-512', 512]]) {
    const p = await b.newPage({ viewport: { width: size, height: size } });
    await p.setContent(`<style>html,body{margin:0}svg{width:${size}px;height:${size}px;display:block}</style>${svg}`);
    await p.screenshot({ path: path.join(root, 'assets/img', name + '.png') });
    await p.close();
  }
  await b.close(); console.log('icons ok');
})();
