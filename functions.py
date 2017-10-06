chips = 250000                # Gesamte Chips im Spiel
anz = 27                      # Anzahl Teilnehmer
bbpro = 100                   # Big Blinds pro Teilnehmer zu Beginn
gesbbe = 20                   # Gesamte Big Blinds nach bestimmter Zeit
zeit = 120                    # Zeit, bis gesbbe erreicht wird (in Minuten)
llen = 15                     # Länge der Level (in Minuten)
#############################################################################
start = chips / anz           # Startstack pro Spieler
gesbb = anz * bbpro           # Gesamte BB am Start
lev = zeit / llen             # Anzahl Level
mult = gesbb / gesbbe         # BB - Multiplikator
bbstart = start / bbpro       # Start- BB
sbstart = bbstart / 2         # Start- SB

def starts():
    start = chips / anz
    return int(round(start))

def BBS():
    return int(round(gesbb))

def BBE():
    return int(round(gesbbe))

def zeitf():
    return int(round(zeit))

def level():
    return int(round(lev))

def bbmult():
    return int(round(mult))

def BBSA():
    return int(round(bbstart))

def SBSA():
    return int(round(sbstart))
