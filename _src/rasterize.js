// Rendert alle SVGs aus _src/svg/ mit Chromium (Playwright) zu PNG in _src/png/.
// Danach erzeugt _src/optimize.py die WebP/JPG-Dateien in assets/img/.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const svgDir = path.join(__dirname, 'svg');
const pngDir = path.join(__dirname, 'png');
const fontDir = path.join(__dirname, '..', 'assets', 'fonts');
fs.mkdirSync(pngDir, { recursive: true });
(async () => {
  const browser = await chromium.launch();
  for (const f of fs.readdirSync(svgDir).filter(f => f.endsWith('.svg'))) {
    const svg = fs.readFileSync(path.join(svgDir, f), 'utf8');
    const [, w, h] = svg.match(/viewBox="0 0 (\d+) (\d+)"/);
    const page = await browser.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 1 });
    const html = `<!doctype html><style>
      @font-face{font-family:"Cormorant Garamond";font-weight:600;src:url("file://${fontDir}/cormorant-garamond-latin-600-normal.woff2")}
      @font-face{font-family:"Cormorant Garamond";font-style:italic;font-weight:500;src:url("file://${fontDir}/cormorant-garamond-latin-500-italic.woff2")}
      html,body{margin:0}svg{display:block}</style>${svg}`;
    const tmp = path.join(pngDir, f + '.html');
    fs.writeFileSync(tmp, html);
    await page.goto('file://' + tmp);
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(pngDir, f.replace('.svg', '.png')) });
    fs.unlinkSync(tmp);
    await page.close();
    console.log('ok', f);
  }
  await browser.close();
})();
