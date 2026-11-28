import sys

PROJ = '/home/claude/fitvox/project/'
TOTAL = 4
LOGO_W = '/_blob/f043bd966aa8244868feba590904b4f6'
LOGO_D = '/_blob/3cb9a901f7c326e8ea2d3c40d5afad39'

HEAD = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>%(title)s</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<style>
body{margin:0}
</style>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800&amp;family=Montserrat:ital,wght@1,800&amp;display=swap">
</helmet>
'''
TAIL = '''</x-dc>
<script type="text/x-dc" data-dc-script data-props='%(props)s'>
class Component extends DCLogic {
renderVals() {
return { accent: this.props.accent ?? '%(default)s' };
}
}
</script>
</body>
</html>
'''
FONT = "font-family: 'Plus Jakarta Sans', system-ui, sans-serif"
ROOT = {
 'dark': ("position: relative; overflow: hidden; width: 1080px; height: 1350px; box-sizing: border-box; padding: 88px; display: flex; flex-direction: column; justify-content: space-between; " + FONT + "; color: #ffffff; "
          "background: radial-gradient(820px 640px at 88% 8%, rgba(134,214,171,0.20), rgba(134,214,171,0) 65%), linear-gradient(165deg, #10251F 0%, #1D3F37 52%, #2A5749 100%)"),
 'cream': ("position: relative; overflow: hidden; width: 1080px; height: 1350px; box-sizing: border-box; padding: 88px; display: flex; flex-direction: column; justify-content: space-between; " + FONT + "; color: #10251F; "
           "background: radial-gradient(780px 620px at 92% 4%, rgba(134,214,171,0.42), rgba(134,214,171,0) 66%), linear-gradient(170deg, #F8F5EE 0%, #F1EDE3 100%)"),
 'mint': ("position: relative; overflow: hidden; width: 1080px; height: 1350px; box-sizing: border-box; padding: 88px; display: flex; flex-direction: column; justify-content: space-between; " + FONT + "; color: #0F2A22; "
          "background: radial-gradient(760px 600px at 92% 4%, rgba(255,255,255,0.38), rgba(255,255,255,0) 66%), linear-gradient(165deg, #9DE3C0 0%, #86D6AB 55%, #74C99B 100%)"),
}
PROPS = {
 'dark': ('{"accent":{"editor":"color","default":"#86D6AB","options":["#86D6AB","#6FCF97","#B7F0CE"]},"$preview":{"width":1080,"height":1350}}', '#86D6AB'),
 'cream': ('{"accent":{"editor":"color","default":"#1B6B4B","options":["#1B6B4B","#2A7F5B","#0F5A3C"]},"$preview":{"width":1080,"height":1350}}', '#1B6B4B'),
 'mint': ('{"accent":{"editor":"color","default":"#14573C","options":["#14573C","#0F4A33","#1E6B4B"]},"$preview":{"width":1080,"height":1350}}', '#14573C'),
}
INK = {'dark': '255,255,255', 'cream': '16,37,31', 'mint': '15,42,34'}
HEADC = {'dark': '#ffffff', 'cream': '#10251F', 'mint': '#0F2A22'}

def logo(theme):
    if theme == 'dark':
        return '<div style="position: relative; display: flex; align-items: center"><img src="%s" alt="Fitvox Global" style="width: 300px; height: auto; display: block"></div>\n' % LOGO_W
    return '<div style="position: relative; display: flex; align-items: center"><img data-logo="dark" src="%s" alt="Fitvox Global" style="width: 300px; height: auto; display: block"></div>\n' % LOGO_D

def headline(theme, eyebrow, lines, accent_line, size=108):
    h = '<br>'.join(lines[:-1] + ['<span style="color: {{accent}}">%s</span>' % lines[-1]]) if accent_line else '<br>'.join(lines)
    return ('<div style="position: relative; display: flex; flex-direction: column; gap: 30px">'
            '<div style="font-size: 26px; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: {{accent}}">%s</div>'
            '<h1 style="margin: 0; font-weight: 800; font-size: %dpx; line-height: 1.1; letter-spacing: -0.025em; color: %s">%s</h1></div>\n') % (eyebrow, size, HEADC[theme], h)

def topblock(theme, eyebrow, lines, size=108, gap=64):
    return ('<div style="position: relative; display: flex; flex-direction: column; gap: %dpx">\n' % gap) + logo(theme) + headline(theme, eyebrow, lines, True, size) + '</div>\n'

def dashes(theme, cur):
    off = 'rgba(%s,0.26)' % INK[theme]
    d = ''.join('<div style="width: 56px; height: 6px; border-radius: 6px; background: %s"></div>' % ('{{accent}}' if i == cur else off) for i in range(1, TOTAL + 1))
    return '<div style="display: flex; gap: 10px; align-items: center">%s</div>' % d

ARROW = '<svg width="26" height="24" viewBox="0 0 26 24" fill="none" stroke="%s" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12 H21 M14 5 L21 12 L14 19"/></svg>'

def bottom(theme, cur, right=''):
    return '<div style="position: relative; display: flex; justify-content: space-between; align-items: center; height: 56px">' + dashes(theme, cur) + right + '</div>\n'

def swipe(theme):
    col = '#ffffff' if theme == 'dark' else '#10251F'
    return ('<div style="display: flex; align-items: center; gap: 16px"><div style="font-size: 24px; font-weight: 700; letter-spacing: 0.04em; color: %s">Swipe</div>'
            '<div style="width: 56px; height: 56px; border-radius: 56px; background: {{accent}}; display: flex; align-items: center; justify-content: center">%s</div></div>') % (col, ARROW % ('#10251F' if theme == 'dark' else '#ffffff'))

def sitetag(theme):
    return '<div style="font-size: 26px; font-weight: 800; color: {{accent}}">fitvoxglobal.com</div>'

def medallion(who, bg, ring='{{accent}}', s=0.58, hy=118):
    # 280px circle with a character bust; placed top-right
    origin = hy + 92 * s
    return ('<svg aria-hidden="true" width="280" height="280" viewBox="0 0 280 280" style="position: absolute; right: 88px; top: 150px">'
            '<defs><clipPath id="m"><circle cx="140" cy="140" r="138"/></clipPath></defs>'
            '<circle cx="140" cy="140" r="138" fill="%s"/><g clip-path="url(#m)">%s</g>'
            '<circle cx="140" cy="140" r="138" fill="none" stroke="%s" stroke-width="5"/></svg>\n') % (bg, char(who, 140, origin, s), ring)

def page(theme, title, body, fname):
    props, default = PROPS[theme]
    html = (HEAD % {'title': title}) + '<div style="%s">\n' % ROOT[theme] + body + '</div>\n' + (TAIL % {'props': props, 'default': default})
    open(PROJ + fname, 'w', encoding='utf-8').write(html)

# ---------------- photo version ----------------
PH = {
 'team': ('df423bf8d1f6a0106043d7562dbe02f6', 'photos/cast-team-cover.jpg'),
 'pair': ('0e5a85c6245063686d3229f2d3f7ce32', 'photos/cast-desk-pair.jpg'),
 'woman': ('a8457f56fa9762809a223c0980e46ce8', 'photos/cast-woman-portrait.jpg'),
 'man': ('5c95c681e6af30bed5c12ef0e9eb4dc4', 'photos/cast-man-portrait.jpg'),
}
ROOT['photo'] = ROOT['dark'].split('background:')[0] + 'background: linear-gradient(90deg, #0A3C34 0%, #052D28 100%)'
PROPS['photo'] = PROPS['dark']

def photo(key, style, alt):
    b, l = PH[key]
    return '<img src="/_blob/%s" data-local="%s" alt="%s" style="%s">' % (b, l, alt, style)

def photo_medallion(key, ring, zoom, fx, fy, alt):
    W = int(280 * zoom)
    left = int(140 - fx * W)
    top = min(0, int(135 - fy * W))
    img = photo(key, 'position: absolute; left: %dpx; top: %dpx; width: %dpx; height: %dpx; display: block' % (left, top, W, W), alt)
    return ('<div style="position: absolute; right: 88px; top: 150px; width: 280px; height: 280px; border-radius: 280px; overflow: hidden; background: #dfe9e4">' + img +
            '<div style="position: absolute; left: 0; top: 0; width: 280px; height: 280px; box-sizing: border-box; border-radius: 280px; border: 5px solid %s"></div></div>\n') % ring

def page2(root, theme_props, title, body, fname):
    props, default = PROPS[theme_props]
    html = (HEAD % {'title': title}) + '<div style="%s">\n' % ROOT[root] + body + '</div>\n' + (TAIL % {'props': props, 'default': default})
    open(PROJ + fname, 'w', encoding='utf-8').write(html)

BOTTOM_FADE = ('<div style="position: absolute; left: 0; bottom: 0; width: 1080px; height: 330px; background: linear-gradient(0deg, rgba(6,30,25,0.97) 0%, rgba(6,30,25,0.84) 30%, rgba(6,30,25,0.46) 62%, rgba(6,30,25,0) 100%)"></div>\n')

# ---- Slide 1: cover (photo) ----
cover_img = photo('team', 'position: absolute; left: 0; top: 0; width: 1080px; height: 1350px; object-fit: cover; display: block',
                  'Three Fitvox Global business consultants smiling behind a consultation desk in a Dubai office')
cover_top = '<div style="position: absolute; left: 0; top: 0; width: 1080px; height: 620px; background: linear-gradient(180deg, rgba(5,38,30,0.5) 0%, rgba(5,38,30,0) 100%)"></div>\n'
body = cover_img + '\n' + cover_top + BOTTOM_FADE + topblock('dark', 'Beyond the licence', ['Your licence is', 'only the start.'], size=100, gap=64) + bottom('dark', 1, swipe('dark'))
page2('photo', 'photo', 'Fitvox Global carousel – Beyond the licence (1/4)', body, '2026-11-29-1-beyond-licence-s1.dc.html')

# ---- Slide 2: growth services (cream, woman portrait) ----
def check_row(label, last=False):
    return ('<div style="display: flex; align-items: center; gap: 28px; height: 104px; box-sizing: border-box; %s">'
            '<div style="width: 52px; height: 52px; border-radius: 52px; background: #86D6AB; display: flex; align-items: center; justify-content: center">'
            '<svg width="26" height="20" viewBox="0 0 26 20" fill="none" stroke="#10251F" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10 L10 17 L23 3"/></svg></div>'
            '<div style="font-size: 38px; font-weight: 700; color: #10251F">%s</div></div>\n') % ('' if last else 'border-bottom: 2px dashed rgba(16,37,31,0.2)', label)

rows = ''.join(check_row(l, i == 4) for i, l in enumerate(['Marketing services', 'Social media management', 'E-commerce', 'Software development', 'Document clearing']))
body = photo_medallion('woman', '{{accent}}', 1.3, 0.49, 0.30, 'Fitvox Global consultant smiling') + topblock('cream', 'Growth services', ['Grow with', 'one team.'], gap=64) + \
       '<div style="position: relative; display: flex; flex-direction: column">' + rows + '</div>\n' + bottom('cream', 2, sitetag('cream'))
page('cream', 'Fitvox Global carousel – Beyond the licence (2/4)', body, '2026-11-29-1-beyond-licence-s2.dc.html')

# ---- Slide 3: essentials (mint, man portrait) ----
ICONS = {
 'audit': '<circle cx="18" cy="18" r="11"/><path d="M26 26 L35 35"/><path d="M12 18 L16 22 L24 13"/>',
 'tax': '<path d="M31 9 L9 31"/><circle cx="13" cy="13" r="5"/><circle cx="27" cy="27" r="5"/>',
 'bank': '<path d="M5 15 L20 6 L35 15 Z"/><path d="M10 19 V30 M20 19 V30 M30 19 V30"/><path d="M5 34 H35"/>',
 'tm': '<path d="M20 4 L34 9 V20 C34 28 28 33 20 37 C12 33 6 28 6 20 V9 Z"/><text x="20" y="25" text-anchor="middle" font-size="11" font-weight="800" fill="#86D6AB" stroke="none" font-family="Plus Jakarta Sans, sans-serif">TM</text>',
}
def card(icon, label):
    return ('<div style="flex: 1; box-sizing: border-box; height: 262px; padding: 34px; border-radius: 36px; background: rgba(248,246,240,0.94); display: flex; flex-direction: column; justify-content: space-between">'
            '<div style="width: 76px; height: 76px; border-radius: 76px; background: #0F2A22; display: flex; align-items: center; justify-content: center">'
            '<svg width="40" height="40" viewBox="0 0 40 40" fill="none" stroke="#86D6AB" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">%s</svg></div>'
            '<div style="font-size: 34px; line-height: 1.2; font-weight: 700; color: #0F2A22">%s</div></div>') % (ICONS[icon], label)
grid = ('<div style="position: relative; display: flex; flex-direction: column; gap: 24px">'
        '<div style="display: flex; gap: 24px">' + card('audit', 'Auditing') + card('tax', 'Corporate tax consulting') + '</div>'
        '<div style="display: flex; gap: 24px">' + card('bank', 'Bank account opening') + card('tm', 'Trademark registration') + '</div></div>\n')
body = photo_medallion('man', '#0F2A22', 1.25, 0.51, 0.33, 'Fitvox Global business advisor smiling') + topblock('mint', 'Business essentials', ['The basics,', 'covered.'], gap=64) + grid + bottom('mint', 3, sitetag('mint'))
page('mint', 'Fitvox Global carousel – Beyond the licence (3/4)', body, '2026-11-29-1-beyond-licence-s3.dc.html')

# ---- Slide 4: CTA (photo of the pair at the desk) ----
ICO = {
 'globe': '<circle cx="20" cy="20" r="13"/><path d="M7 20 H33"/><ellipse cx="20" cy="20" rx="6" ry="13"/>',
 'mail': '<rect x="7" y="11" width="26" height="18" rx="3"/><path d="M7 14 L20 24 L33 14"/>',
 'phone': '<path d="M12 8 Q9 8 9.5 12.5 Q11 26 27.5 30.5 Q32 31 32 28 L32 25 L26 23 L24 26 Q18 23 15 17 L17 15 L15 9 Z"/>',
}
def contact(icon, text):
    return ('<div style="display: flex; align-items: center; gap: 20px"><div style="width: 52px; height: 52px; border-radius: 52px; box-sizing: border-box; border: 2px solid rgba(134,214,171,0.6); background: rgba(6,40,33,0.55); display: flex; align-items: center; justify-content: center">'
            '<svg width="28" height="28" viewBox="0 0 40 40" fill="none" stroke="#86D6AB" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">%s</svg></div>'
            '<div style="font-size: 30px; font-weight: 700; color: #ffffff">%s</div></div>') % (ICO[icon], text)
pill = ('<div style="display: flex; align-items: center; justify-content: space-between; width: 610px; height: 88px; box-sizing: border-box; padding: 0 14px 0 38px; border-radius: 88px; background: #F6F5EF">'
        '<div style="font-size: 32px; font-weight: 700; color: #10251F">Message us on WhatsApp</div>'
        '<div style="width: 60px; height: 60px; border-radius: 60px; background: #10251F; display: flex; align-items: center; justify-content: center">' + (ARROW % '#ffffff') + '</div></div>')
contacts = '<div style="display: flex; flex-direction: column; gap: 14px">' + contact('globe', 'fitvoxglobal.com') + contact('mail', 'info@fitvoxglobal.com') + contact('phone', '+971 55 527 8262') + '</div>'
save = ('<div style="display: flex; align-items: center; gap: 14px"><svg width="22" height="28" viewBox="0 0 22 28" fill="none" stroke="#ffffff" stroke-width="3" stroke-linejoin="round"><path d="M3 3 H19 V25 L11 19 L3 25 Z"/></svg>'
        '<div style="font-size: 24px; font-weight: 700; color: #ffffff">Save for later</div></div>')
pair_img = photo('pair', 'position: absolute; left: 0; top: 180px; width: 1080px; height: 1350px; object-fit: cover; display: block',
                 'Two Fitvox Global consultants at a desk with a laptop, ready to help')
pair_top = '<div style="position: absolute; left: 0; top: 0; width: 1080px; height: 560px; background: linear-gradient(180deg, rgba(8,52,45,1) 0%, rgba(8,52,45,1) 34%, rgba(8,52,45,0) 100%)"></div>\n'
head = '<div style="position: relative; display: flex; flex-direction: column; gap: 44px">' + topblock('dark', "Let’s talk", ["Let’s build", 'it together.'], size=100, gap=56) + pill + contacts + '</div>\n'
body = pair_img + '\n' + pair_top + BOTTOM_FADE + head + bottom('dark', 4, save)
page2('photo', 'photo', 'Fitvox Global carousel – Beyond the licence (4/4)', body, '2026-11-29-1-beyond-licence-s4.dc.html')
print('photo slides written')
