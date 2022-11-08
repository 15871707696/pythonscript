# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 11:55:31 2022

@author: Lenovo
"""

class Format_processing(object):
    def __init__(self, read_path, write_path,list_save):
        self.read_path=read_path
        self.write_path=write_path
        self.list_save=list_save
        
        
    def read(self):
        with open(self.read_path,'r') as file:
            list_temp=[]
            while True:
                line = file.readline()
                if not line:
                    break
                else:
                    lists = line.split()
                    if lists[0] == "ATOM":
                        number=len(lists[4])
                        if number >1:
                            dot_count=lists[7].count(".")
                            if dot_count >1:
                                list_temp.append(lists[2])
                                list_temp.append(lists[1]) 
                                list_temp.append(lists[5])
                                list_temp.append(lists[6])
                                list_temp.append(lists[7][:-3])
                                self.list_save.append(list_temp)
                                list_temp=[]
                            else:
                                list_temp.append(lists[2])
                                list_temp.append(lists[1]) 
                                list_temp.append(lists[5])
                                list_temp.append(lists[6])
                                list_temp.append(lists[7])
                                self.list_save.append(list_temp)
                                list_temp=[]
                        else:
                            dot_count=lists[8].count(".")
                            if dot_count >1:
                                list_temp.append(lists[2])
                                list_temp.append(lists[1]) 
                                list_temp.append(lists[6])
                                list_temp.append(lists[7])
                                list_temp.append(lists[8][:-3])
                                self.list_save.append(list_temp)
                                list_temp=[]
                            else:
                                list_temp.append(lists[2])
                                list_temp.append(lists[1]) 
                                list_temp.append(lists[6])
                                list_temp.append(lists[7])
                                list_temp.append(lists[8])
                                self.list_save.append(list_temp)
                                list_temp=[]
                                
                                
    def write(self):
        with open(self.write_path,'a+') as wfile:
            for i in range(len(self.list_save)):
                wfile.write(self.list_save[i][0] + "            " + self.list_save[i][1]+"\n")
                wfile.write("    " + self.list_save[i][2] + "   " + self.list_save[i][3] + "   "+ self.list_save[i][4]+"\n")
        
                    
if  __name__=="__main__":
    read_path = "D:\\python_script\\mix.pdb"
    write_path = "D:\\python_script\\config"
    list_save=[]
    test1=Format_processing(read_path, write_path,list_save)
    test1.read()
    test1.write()