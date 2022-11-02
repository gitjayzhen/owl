# -*- coding: utf-8 -*- 

import zipfile
import os


# 解压zip文件
def unzip():
    source_zip = "c:\\update\\SW_Servers_20120815.zip"
    target_dir = "c:\\update\\"
    myzip = zipfile.ZipFile(source_zip)
    myfilelist = myzip.namelist()
    for name in myfilelist:
        f_handle = open(target_dir + name, "wb")
        f_handle.write(myzip.read(name))
        f_handle.close()
    myzip.close()


# 添加文件到已有的zip包中
def addzip(currentfolder, ready2compression):
    zipfname = "AutoTesting-Reports.zip"
    absZIPpath = os.path.join(currentfolder, zipfname)
    absfpath = os.path.join(currentfolder, ready2compression)
    f = zipfile.ZipFile(absZIPpath, 'w', zipfile.ZIP_DEFLATED)
    f.write(absfpath)
    f.close()

    return absZIPpath, zipfname


# 把整个文件夹内的文件打包
def adddirfile():
    f = zipfile.ZipFile('archive.zip', 'w', zipfile.ZIP_DEFLATED)
    startdir = "c:\\mydirectory"
    for dirpath, dirnames, filenames in os.walk(startdir):
        for filename in filenames:
            f.write(os.path.join(dirpath, filename))
    f.close()
# latestfpath, fname,currentfolder= FileChecK().get_LatestFile()
# absZIPpath, zipfname = addzip(currentfolder,fname)
