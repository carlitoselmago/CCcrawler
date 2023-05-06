from CCcrawler import CCcrawler

# prepare files




CCc=CCcrawler()

#modes 
# sentence: grabs the whole sentence in the timing
# word: guesses the timing on sentence level (adding padding might help)
# exact (with word level srt)

CCc.compose("E:/TRABAJO/videos irena/footage", [" dit"],mode="sentence",padding=3200)

#print (CCc.getSource("E:/TRABAJO/videos irena/footage"))

"""

lines = CCc.LoadFileIntoStringList("/home/haxoorx/Downloads/Dexter.S03E01.720p.BRRip.XviD.AC3-ViSiON.srt")

#search="DEXTER [love]"

CCc.createMatches(lines,["love"])
"""