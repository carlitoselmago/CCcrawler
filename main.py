from CCcrawler.CCcrawler import CCcrawler

# prepare files




CCc=CCcrawler()

CCc.compose('@SERIES/BLACKMIRROR "laugh"')

#print CCc.getSource("SERIES/BLACKMIRROR")

"""

lines = CCc.LoadFileIntoStringList("/home/haxoorx/Downloads/Dexter.S03E01.720p.BRRip.XviD.AC3-ViSiON.srt")

#search="DEXTER [love]"

CCc.createMatches(lines,["love"])
"""