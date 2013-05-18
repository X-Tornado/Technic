'''
Created on 18/05/2013

@author: marc
'''

import os

class Mod(object):
    def __init__(self,filename):
        self.name=filename.split("-")[0]
        try:
            self.version=filename.split("-",1)[1].rsplit(".",1)[0]
        except:
            print "Ha petat:"+filename
class ModList(object):
    def __init__(self):
        self.mods= {}
        
    def add(self,mod):
        try:
            self.mods[mod.name]+=[mod.version]
        except KeyError:
            self.mods[mod.name]=[mod.version]
class FolderReaderMods(object):
    def __init__(self,directory,modlist):
        self.directory=directory
        self.modlist=modlist
    def search(self):
        l=[]
        for dirname, dirnames, filenames in os.walk(os.path.join('.',self.directory)):
            l+= [x for x in filenames]
        for x in l:
            self.modlist.add(Mod(x))
class ModLibrary(object):
    def __init__(self,modlist):
        self.modlist=modlist
    def generate(self):
        f=open("modlibrary.yml","w")
        towrite="\tmods:\n"
        for x in sorted(self.modlist.mods.keys()):
            towrite+="\t\t"+x+":\n\t\t\tname: \"\"\n\t\t\tdescription: \"\"\n\t\t\tinstalltype: \"zip\"\n\t\t\tmodtype: \"content\"\n\t\t\tlink: \"\"\n\t\t\tversions:\n"
            for z in self.modlist.mods[x]:
                towrite +="\t\t\t\t"+z+":\n"
            towrite+="\n"
        f.write(towrite)
        f.close()

if __name__ == '__main__':
    Ml=ModList()
    FolderReader=FolderReaderMods("mods",Ml)
    FolderReader.search()
    M=ModLibrary(Ml)
    M.generate()