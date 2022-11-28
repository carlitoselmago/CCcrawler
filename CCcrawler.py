import re
from moviepy.editor import *
import sys
import os
import configparser
from os.path import join
import glob

class CCcrawler():
    
    clips=[]
    founds=0
    block=False
    
    #sourceVideoFileLocation="/home/haxoorx/Downloads/Dexter.S03.Season.3.1080p.5.1Ch.BluRay.ReEnc-DeeJayAhmed/Dexter.S03E01.1080p.5.1Ch.BluRay.ReEnc-DeeJayAhmed.mkv"
    
    def __init__(self):
        print ("CCcrawler init")
        self.Config = configparser.ConfigParser()
        self.Config.read("config.ini")
        self.folderSettings=self.ConfigSectionMap("folders")
    
    def compose(self,folder,search):
        
        """
        #fragment formula
        SOURCES=formula.split("@")
        
        for SOURCE in SOURCES:
            if len(SOURCE)>0:
                parts=SOURCE.split(" ")
                
                episodes = self.getSource(parts[0])
                
                search=parts[1].replace('"','')
                
                for episode in episodes:

                    if ".srt" in episode:
                        
                        self.processFile(episode,search)
            
        """
        for f in self.getSource(folder):

            self.processFile(f,[search])
        #create video output
        final_clip = concatenate_videoclips(self.clips)
        final_clip.write_videofile('E:/TRABAJO/videos irena/footage/supercuts/'+search+".mp4")#,bitrate='3000k')#,audio=False)


    
    def getSource(self,name):
        return glob.glob(name+"/*.srt")
        #return list of fileURIs
        files=[]
        
        if name[-1:] != "/":
            name+="/"
            
        if name[0] !=  "/":
            name="/"+name
        print(self.folderSettings["sources"]+name)
        dirs=self.getDirs(self.folderSettings["sources"]+name)
        for season in dirs:
            for fileList in self.getFiles(self.folderSettings["sources"]+name+"/"+season):
                for file in fileList:
                    files.append(self.folderSettings["sources"]+name+season+"/"+file)
        
        return files
        
    def getDirs(self,sourceFolder):
        dirs=[]
        for root, dir, files in os.walk(sourceFolder):
            if len(dir)>0:
                dirs.append(dir)
        return dirs[0]
    
    def getFiles(self,sourceFolder):
        files=[]
        for root, dir, file in os.walk(sourceFolder):
            if len(file)>0:
                files.append(file)
        return files
        
    def ConfigSectionMap(self,section):
        dict1 = {}
        options = self.Config.options(section)
        for option in options:
            try:
                dict1[option] = self.Config.get(section, option)
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1
    
    def createClip(self,videoUri,start,end):
        print (videoUri)
        clip = VideoFileClip(videoUri).subclip(start,end)
        self.clips.append(clip)
        
        #clip.write_videofile("/home/haxoorx/Downloads/"+str(filename)+".webm")

    def buildName(self,search):
        name=""
        for word in search:
            name+=word+"-"
        return name
    
    def LoadFileIntoStringList(self,fileURI):
        print("LoadFileIntoStringList",fileURI)
        file = open(fileURI,"r", encoding="utf8")
        string = file.read()
        lines=string.split('\n')
        return lines
        
    def processFile(self,file,search):
        lines = self.LoadFileIntoStringList(file)
        self.createMatches(file,lines,search)
    
    
    def getVideoUriFromSrt(self,SRTUri):
        videoUri=SRTUri.replace(".srt",".mp4")
        #videoUri=SRTUri.replace(".srt",".mkv")
        return videoUri
    
    def createMatches(self,SRTUri, lines, search):
        
        # search is an array of strings to search
        
        text=""
        founds=0
        start=False
        end=False
        
        for line in lines:
            
            if line.strip().isdigit():

                block={"text":text,"start":start,"end":end}

                for word in search:

                    if word.upper() in block["text"].upper():
                        print ("found",block)
                        videoURI=self.getVideoUriFromSrt(SRTUri)
                        self.createClip(videoURI,block["start"],block["end"])
                        founds+=1

                text=""


            if "-->" in line:

                timeCodes=line.split("-->")
                start=timeCodes[0].strip().replace(",",".")
                end=timeCodes[1].strip().replace(",",".")
                
                print (start,":::::::::::::::::")
                
            if line != "" and "-->" not in line and not line.strip().isdigit():
                text+=line.rstrip()

   
