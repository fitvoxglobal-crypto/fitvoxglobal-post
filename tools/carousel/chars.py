# Original flat-vector character cast for Fitvox carousels (origin = base of neck, y up is negative)
def _g(x, y, s, inner, flip=False):
    sx = -s if flip else s
    return '<g transform="translate(%s,%s) scale(%s,%s)">%s</g>' % (x, y, sx, s, inner)

SHOULDERS = "M-175,340 L-175,76 Q-175,22 -120,8 L-40,-4 L40,-4 L120,8 Q175,22 175,76 L175,340 Z"

def _face(skin, eye="#231812", blush="#E58C7A", smile="#7A3E2E", ry=64, lashes=False):
    f = '<ellipse cx="0" cy="-92" rx="54" ry="%d" fill="%s"/>' % (ry, skin)
    f += '<ellipse cx="-24" cy="-92" rx="5.5" ry="7.5" fill="%s"/><ellipse cx="24" cy="-92" rx="5.5" ry="7.5" fill="%s"/>' % (eye, eye)
    f += '<path d="M-37,-111 Q-24,-119 -11,-111" stroke="#2B1D14" stroke-width="5" fill="none" stroke-linecap="round"/>'
    f += '<path d="M11,-111 Q24,-119 37,-111" stroke="#2B1D14" stroke-width="5" fill="none" stroke-linecap="round"/>'
    f += '<path d="M0,-90 Q-7,-70 3,-67" stroke="rgba(120,70,40,0.55)" stroke-width="3.5" fill="none" stroke-linecap="round"/>'
    f += '<ellipse cx="-38" cy="-70" rx="10" ry="7" fill="%s" opacity="0.35"/><ellipse cx="38" cy="-70" rx="10" ry="7" fill="%s" opacity="0.35"/>' % (blush, blush)
    f += '<path d="M-17,-52 Q0,-37 17,-52" stroke="%s" stroke-width="4.5" fill="none" stroke-linecap="round"/>' % smile
    if lashes:
        f += '<path d="M-31,-100 Q-36,-104 -38,-101 M31,-100 Q36,-104 38,-101" stroke="#231812" stroke-width="3" fill="none" stroke-linecap="round"/>'
    return f

def emirati_man():
    s = '<path d="%s" fill="#F7F5EF"/>' % SHOULDERS
    s += '<path d="M62,-4 L120,8 Q175,22 175,76 L175,340 L80,340 Z" fill="#E4E0D4" opacity="0.75"/>'
    s += '<path d="M-26,-4 L0,44 L26,-4 Z" fill="#E6E2D6"/><path d="M0,44 L0,340" stroke="#D9D4C6" stroke-width="3"/>'
    s += '<circle cx="0" cy="78" r="3.5" fill="#CFC9B8"/><circle cx="0" cy="118" r="3.5" fill="#CFC9B8"/>'
    s += '<path d="M-31,-30 L31,-30 L31,8 Q0,28 -31,8 Z" fill="#C48E66"/>'
    s += '<path d="M-96,-108 Q-100,-196 0,-202 Q100,-196 96,-108 L134,24 Q62,50 0,48 Q-62,50 -134,24 Z" fill="#FDFDFB" stroke="#E2DFD5" stroke-width="3"/>'
    s += '<ellipse cx="0" cy="-90" rx="57" ry="67" fill="#D5A07A"/>'
    s += '<path d="M-58,-82 Q-62,-28 0,-18 Q62,-28 58,-82 Q54,-62 38,-46 Q0,-34 -38,-46 Q-54,-62 -58,-82 Z" fill="#2A211B"/>'
    s += _face("none", smile="#6B3A2C")
    s += '<path d="M-70,-122 Q-66,-196 0,-198 Q66,-196 70,-122 Q40,-148 0,-148 Q-40,-148 -70,-122 Z" fill="#FDFDFB"/>'
    s += '<path d="M-80,-140 Q0,-182 80,-140" stroke="#16130F" stroke-width="12" fill="none" stroke-linecap="round"/>'
    s += '<path d="M-84,-158 Q0,-202 84,-158" stroke="#16130F" stroke-width="7" fill="none" stroke-linecap="round"/>'
    return s

def consultant_woman():
    s = '<path d="%s" fill="#23463D"/>' % SHOULDERS
    s += '<path d="M62,-4 L120,8 Q175,22 175,76 L175,340 L80,340 Z" fill="#1B3A32" opacity="0.8"/>'
    s += '<path d="M0,20 L0,340" stroke="#86D6AB" stroke-width="5"/>'
    s += '<path d="M-104,-96 Q-104,-198 0,-204 Q104,-198 104,-96 Q108,-30 138,16 Q0,76 -138,16 Q-108,-30 -104,-96 Z" fill="#E9EDE8" stroke="#D2D9D2" stroke-width="3"/>'
    s += '<path d="M-112,12 Q0,64 112,12 Q124,42 114,82 Q0,120 -114,82 Q-124,42 -112,12 Z" fill="#E9EDE8" stroke="#D2D9D2" stroke-width="3"/>'
    s += '<path d="M-28,-30 L28,-30 L28,10 Q0,30 -28,10 Z" fill="#CD9A74"/>'
    s += '<ellipse cx="0" cy="-90" rx="55" ry="66" fill="#E3B28B"/>'
    s += _face("none", smile="#A9444F", lashes=True)
    s += '<path d="M-62,-98 Q-60,-168 0,-172 Q60,-168 62,-98 Q54,-134 0,-138 Q-54,-134 -62,-98 Z" fill="#E9EDE8"/>'
    s += '<path d="M-62,-98 Q-60,-168 0,-172 Q60,-168 62,-98" stroke="#D2D9D2" stroke-width="3" fill="none"/>'
    s += '<circle cx="0" cy="38" r="9" fill="#86D6AB"/>'
    return s

def suit_man():
    s = '<path d="%s" fill="#1E3350"/>' % SHOULDERS
    s += '<path d="M-44,-4 L0,118 L44,-4 Z" fill="#F4F4F1"/>'
    s += '<path d="M-44,-4 L-104,44 L-64,168 L0,118 Z" fill="#152840"/><path d="M44,-4 L104,44 L64,168 L0,118 Z" fill="#152840"/>'
    s += '<path d="M-13,14 L13,14 L8,34 L-8,34 Z" fill="#86D6AB"/><path d="M-8,34 L8,34 L20,128 L0,150 L-20,128 Z" fill="#6FC59A"/>'
    s += '<path d="M-31,-30 L31,-30 L31,8 Q0,26 -31,8 Z" fill="#A87850"/>'
    s += '<ellipse cx="-56" cy="-88" rx="9" ry="14" fill="#B98A62"/><ellipse cx="56" cy="-88" rx="9" ry="14" fill="#B98A62"/>'
    s += '<ellipse cx="0" cy="-92" rx="54" ry="66" fill="#BE8D66"/>'
    s += _face("none", smile="#6E3425")
    s += '<path d="M-58,-104 Q-62,-172 0,-174 Q62,-172 58,-104 Q44,-138 0,-136 Q-44,-138 -58,-104 Z" fill="#17120F"/>'
    s += '<path d="M-52,-62 Q0,-36 52,-62 Q40,-24 0,-22 Q-40,-24 -52,-62 Z" fill="#2B211B" opacity="0.28"/>'
    return s

CAST = {"emirati": emirati_man, "consultant": consultant_woman, "suit": suit_man}

def char(name, x, y, s=1.0, flip=False):
    return _g(x, y, s, CAST[name](), flip)
