#i.e. the program starts here
import subprocess as sp
import os
import os.path
from pathlib import Path

def generateList():
    #get the names to all the files in the current directory
    cmd = 'ls'
    path  = 'music-test'
    result = sp.run([cmd, path], stdout = sp.PIPE)
    bash_str = result.stdout.decode('utf-8')
    music_list = bash_str.splitlines()

    #make a new directory for the final files
    cmd = 'mkdir final-lib'
    sp.run(cmd, shell = True)
    pre_process(music_list)

def pre_process(music_list):
    #swap out all the () or （）in the name of the song, so the name of the song can be 
    #passed into bash without too much hassle
    for i in range(len(music_list)):
        old_name = 'music-test/' + music_list[i]
        music_list[i] = music_list[i].replace("(", "<")
        music_list[i] = music_list[i].replace(")", ">")
        music_list[i] = music_list[i].replace("（", "<")
        music_list[i] = music_list[i].replace("）", "<")
        dst = 'music-test/' + music_list[i]
        #rename the original file with the new name
        os.rename(old_name, dst)
    getType(music_list)

#final process of the list
def getType(music_list):
    print("Your folder contains ", len(music_list), " songs")
    #find the file type of the file in the list
    mp3 = 0
    flac = 0
    for i in range(len(music_list)):
        #U can uncomment the next line if u prefer more output :)
        #print(music_list[i])
        
        #acquire the filetype
        temp = music_list[i].split(".")
        file_type = temp[len(temp) - 1]
        old_name = "".join(temp[0 : len(temp) - 1])
        #print(old_name)

        #manipulate the file name since NetEase local file name is of the form:
        #Artist - SongName.filetype
        index = 0
        fileName = ''
        info = []

        #remove all " - "s inside the name of the song
        while index < len(temp):
            if temp[index].find(' - ') != -1:
                info = temp[index].split(" - ")
                if len(info) > 1:
                    for j in range(len(info)):
                        if j > 0:
                            fileName += info[j]
                else:
                    fileName = info[1]
                index += 1
            else:
                index += 1

        #temporary str for the final output path
        file_path = 'music-test/' + music_list[i]
        
        if file_type == 'mp3':
            cmd = 'mv'
            #temp str to check if there's an existing song with the same name but possibly differ in detail
            #i.e. a cover sang by another artist
            #if existing, append a (2) to the end of the filename
            tmp = 'final-lib/' + fileName + '.mp3'
            if Path(tmp).is_file():
                fileName += '(2)'
            #generate the parameter to pass to bash
            fileName = 'final-lib/' + fileName + '.mp3'
            result = sp.run([cmd, file_path, fileName])
            #counter add
            mp3 += 1
        elif file_type == 'flac':
            #test of destination directiory
            tmp = 'final-lib/' + fileName + '.flac'
            if Path(tmp).is_file():
                fileName += '(2)'
            #generate command
            cmd = 'mv'
            fileName = 'final-lib/' + fileName + '.flac'
            result = sp.run([cmd, file_path, fileName])
            #counter add
            flac += 1
        elif file_type == 'ncm':
            #test of destination directory
            tmp_mp3 = 'final-lib/' + fileName + '.mp3' 
            tmp_flac = 'final-lib/' + fileName + '.flac'
            if Path(tmp_mp3).is_file() or Path(tmp_flac).is_file() :
                fileName += '-NCM'
            #generate command to perform format conversion
            cmd = 'ncmdump' 
            sp.run([cmd, file_path])
            #finish up on the ncmdump leftovers
            scrapup(old_name, fileName)
        else:
            #TODO: possible add support of other files
            pass
        #line separator
        print('****')
        
    #statistical usage    
    print("processed ", mp3, "files")
    print("processed ", flac, "files")

#scrap up for ncm files
def scrapup(src, dst):
    #move the output file to final-lib from ncmdump
    cmd = 'mv'
    path = ''
    out_name = ''
    print(os.path.join(os.getcwd(), src + '.ncm'))
    #determine the type of output file
    if os.path.exists(os.path.join(os.getcwd(), src + '.mp3')):
        out_name = src + '.mp3'
        path = 'final-lib/' + dst + '.mp3'
    elif os.path.exists(os.path.join(os.getcwd(), src + '.flac')):
        out_name = src + '.flac'
        path = 'final-lib/' + dst + '.flac'
    else:
        print("???")
        #TODO: if NetEase will convert types other than .flac and .mp3 to .ncm, 
        #Add accordingly or switch case if converting everying to ncm for MEMBERSHIP!
        
    result = sp.run([cmd, out_name, path])

    #delete the original .ncm file
    cmd = 'rm'
    path = 'music-test/' + src + '.ncm'
    sp.run([cmd, path])
    
#debug usage - output current full directory
def currentDir():
    cmd = 'echo $PWD'
    result = sp.run(cmd, shell = True)
generateList()
