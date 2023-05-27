# Author: Charles Terrell <tachyon@pobox.com>
# Character set conversion tools for use with autokey cipher

class Latin:
    # Table to convert language-specific letters into basic Latin
    # forms. Esperanto X-sistemo included due to author interest.
    # (H-sistemo is more official, but X works better for computers.)
    # A few from other languages included as examples. Please tell me
    # if these conflict with official respelling standards.
    #
    # If using lots of diacritics and ligatures, a more sophisticted
    # solution might be needed.
    latin_map = {
        "ĉ": "cx", "Ĉ": "CX", "ĝ": "gx", "Ĝ": "GX",
        "ĵ": "jx", "Ĵ": "JX", "ĥ": "hx", "Ĥ": "HX",
        "ŝ": "sx", "Ŝ": "SX", "ŭ": "ux", "Ŭ": "UX",
        "œ": "oe", "Œ": "OE", "þ": "th", "Þ": "TH",
        "ñ": "ny", "Ñ": "NY", "ç": "c", "Ç": "C",
        "ß": "ss", "ü": "ue"
    }

    @staticmethod
    def latinize(src):
        for letter in Latin.latin_map.keys():
            src = src.replace(letter, Latin.latin_map[letter])
        return src

