# vim: set fileencoding=utf-8 :

# #SPCTHVRIAEOcsthpr*ieao
KEYS = (
    '#',
    'S-', 'P-', 'C-', 'T-', 'H-', 'V-', 'R-',
    'I-', 'A-',
    '-E', '-O',
    '-c', '-s', '-t', '-h', '-p', '-r',
    '*',
    '-i', '-e', '-a', '-o',
)

IMPLICIT_HYPHEN_KEYS = KEYS

SUFFIX_KEYS = ()

NUMBER_KEY = '#'

NUMBERS = {
    'S-': '1-',
    'P-': '2-',
    'T-': '3-',
    'V-': '4-',
    'I-': '5-',
    '-O': '0-',
    '-c': '-6',
    '-t': '-7',
    '-p': '-8',
    '-i': '-9',
}

UNDO_STROKE_STENO = '*'

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Gemini PR': {
        '#'         : ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C'),
        'S-'        : ('S1-', 'S2-'),
        'P-'        : 'T-',
        'C-'        : 'K-',
        'T-'        : 'P-',
        'H-'        : 'W-',
        'V-'        : 'H-',
        'R-'        : 'R-',
        'I-'        : 'A-',
        'A-'        : 'O-',
        '*'         : ('*1', '*2', '*3', '*4'),
        '-E'        : '-E',
        '-O'        : '-U',
        '-c'        : '-F',
        '-s'        : '-R',
        '-t'        : '-P',
        '-h'        : '-B',
        '-p'        : '-L',
        '-r'        : '-G',
        '-i'        : '-T',
        '-e'        : '-S',
        '-a'        : '-D',
        '-o'        : '-Z',
        'no-op'     : ('Fn', 'pwr', 'res1', 'res2'),
    },
    'Keyboard': {
        '#'         : ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        'S-'        : ('a', 'q'),
        'P-'        : 'w',
        'C-'        : 's',
        'T-'        : 'e',
        'H-'        : 'd',
        'V-'        : 'r',
        'R-'        : 'f',
        'I-'        : 'c',
        'A-'        : 'v',
        '*'         : ('t', 'g', 'y', 'h'),
        '-E'        : 'n',
        '-O'        : 'm',
        '-c'        : 'u',
        '-s'        : 'j',
        '-t'        : 'i',
        '-h'        : 'k',
        '-p'        : 'o',
        '-r'        : 'l',
        '-i'        : 'p',
        '-e'        : ';',
        '-a'        : '[',
        '-o'        : '\'',
        'arpeggiate': 'space',
        # Suppress adjacent keys to prevent miss-strokes.
        'no-op'     : ('z', 'x', 'b', ',', '.', '/', ']', '\\'),
    },
    'Passport': {
        '#'    : '#',
        'S-'   : ('S', 'C'),
        'P-'   : 'T',
        'C-'   : 'K',
        'T-'   : 'P',
        'H-'   : 'W',
        'V-'   : 'H',
        'R-'   : 'R',
        'I-'   : 'A',
        'A-'   : 'O',
        '*'    : ('~', '*'),
        '-E'   : 'E',
        '-O'   : 'U',
        '-c'   : 'F',
        '-s'   : 'Q',
        '-t'   : 'N',
        '-h'   : 'B',
        '-p'   : 'L',
        '-r'   : 'G',
        '-i'   : 'Y',
        '-e'   : 'X',
        '-a'   : 'D',
        '-o'   : 'Z',
        'no-op': ('!', '^', '+'),
    },
    'Stentura': {
        '#'    : '#',
        'S-'   : 'S-',
        'P-'   : 'T-',
        'C-'   : 'K-',
        'T-'   : 'P-',
        'H-'   : 'W-',
        'V-'   : 'H-',
        'R-'   : 'R-',
        'I-'   : 'A-',
        'A-'   : 'O-',
        '*'    : '*',
        '-E'   : '-E',
        '-O'   : '-U',
        '-c'   : '-F',
        '-s'   : '-R',
        '-t'   : '-P',
        '-h'   : '-B',
        '-p'   : '-L',
        '-r'   : '-G',
        '-i'   : '-T',
        '-e'   : '-S',
        '-a'   : '-D',
        '-o'   : '-Z',
        'no-op': '^',
    },
    'TX Bolt': {
        '#'    : '#',
        'S-'   : 'S-',
        'P-'   : 'T-',
        'C-'   : 'K-',
        'T-'   : 'P-',
        'H-'   : 'W-',
        'V-'   : 'H-',
        'R-'   : 'R-',
        'I-'   : 'A-',
        'A-'   : 'O-',
        '*'    : '*',
        '-E'   : '-E',
        '-O'   : '-U',
        '-c'   : '-F',
        '-s'   : '-R',
        '-t'   : '-P',
        '-h'   : '-B',
        '-p'   : '-L',
        '-r'   : '-G',
        '-i'   : '-T',
        '-e'   : '-S',
        '-a'   : '-D',
        '-o'   : '-Z',
    },
    'Treal': {
        '#'    : ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B'),
        'S-'   : ('S1-', 'S2-'),
        'P-'   : 'T-',
        'C-'   : 'K-',
        'T-'   : 'P-',
        'H-'   : 'W-',
        'V-'   : 'H-',
        'R-'   : 'R-',
        'I-'   : 'A-',
        'A-'   : 'O-',
        '*'    : ('*1', '*2'),
        '-E'   : '-E',
        '-O'   : '-U',
        '-c'   : '-F',
        '-s'   : '-R',
        '-t'   : '-P',
        '-h'   : '-B',
        '-p'   : '-L',
        '-r'   : '-G',
        '-i'   : '-T',
        '-e'   : '-S',
        '-a'   : '-D',
        '-o'   : '-Z',
        'no-op': ('X1-', 'X2-', 'X3'),
    },
}
