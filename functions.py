chips = 250000                 # Gesamte Chips im Spiel
anz = 27                       # Anzahl Teilnehmer
bbpro = 100                   # Big Blinds pro Teilnehmer zu Beginn
gesbbe = 20                   # Gesamte Big Blinds nach bestimmter Zeit
zeit = 120                    # Zeit, bis gesbbe erreicht wird (in Minuten)
llen = 15                     # Länge der Level (in Minuten)
#############################################################################
start = chips / anz           # Startstack pro Spieler
gesbb = anz * bbpro           # Gesamte BB am Start
lev = zeit / llen             # Anzahl Level
mult = gesbb / gesbbe         # BB - Multiplikator
bbstart = start / bbpro # Start- BB
sbstart = bbstart / 2         # Start- SB

def starts():
    return start

def BBS():
    return gesbb

def BBE():
    return gesbbe

def zeitf():
    return zeit

def level():
    return lev

def bbmult():
    return mult

def BBSA():
    return bbstart

def SBSA():
    return sbstart
