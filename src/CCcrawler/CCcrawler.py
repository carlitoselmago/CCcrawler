import re
from moviepy.editor import *
import sys


class CCcrawler():
    
    clips=[]
    founds=0
    block=False
    
    
    sourceVideoFileLocation="/home/haxoorx/Downloads/Dexter.S03.Season.3.1080p.5.1Ch.BluRay.ReEnc-DeeJayAhmed/Dexter.S03E01.1080p.5.1Ch.BluRay.ReEnc-DeeJayAhmed.mkv"
    
    def __init__(self):
        print "CCcrawler init"
        
    def createClip(self,start,end):
        clip = VideoFileClip(self.sourceVideoFileLocation).subclip(start,end)
        self.clips.append(clip)
        
        #clip.write_videofile("/home/haxoorx/Downloads/"+str(filename)+".webm")

    def buildName(self,search):
        name=""
        for word in search:
            name+=word+"-"
        return name
    
    def LoadFileIntoStringList(self,fileURI):
        file = open(fileURI,"r")
        string = file.read()
        lines=string.split('\n')
        return lines
        
    def createMatches(self, lines, search):
        
        # search is an array of strings to search
        
        text=""
        founds=0
        
        for line in lines:

            if line.strip().isdigit():

                block={"text":text,"start":start,"end":end}

                for word in search:

                    if word.upper() in block["text"].upper():
                        print "found",block
                        self.createClip(block["start"],block["end"])
                        founds+=1

                text=""


            if "-->" in line:

                timeCodes=line.split("-->")
                start=timeCodes[0].strip().replace(",",".")
                end=timeCodes[1].strip().replace(",",".")

            if line != "" and "-->" not in line and not line.strip().isdigit():
                text+=line.rstrip()

        final_clip = concatenate_videoclips(self.clips)
        final_clip.write_videofile("/home/haxoorx/Downloads/compilations/"+self.buildName(search)+".mp4",bitrate='3000k')#,audio=False)


