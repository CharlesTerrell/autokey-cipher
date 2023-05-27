from latin import Latin

def test_latinize_eo():
    result = Latin.latinize("Eĥoŝanĝo Ĉiuĵaŭde")
    assert result == "Ehxosxangxo CXiujxauxde"

def test_latinize_de():
    result = Latin.latinize("Stülerstraße")
    assert result == "Stuelerstrasse"