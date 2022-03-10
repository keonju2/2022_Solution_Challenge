import json
import json
import os
from pathlib import Path
import zipfile

def unzip(source_file, dest_path):
    with zipfile.ZipFile(source_file, 'r') as zf:
        zipInfo = zf.infolist()
        for member in zipInfo:
            try:
                print(member.filename.encode('cp437').decode('euc-kr', 'ignore'))
                member.filename = member.filename.encode('cp437').decode('euc-kr', 'ignore')
                zf.extract(member, dest_path)
            except:
                print(source_file)
                raise Exception('what?!')



path_dir = 'C:/Users/keonj/Desktop/졸음운전 예방을 위한 운전자 상태 정보 영상' #첫 폴더
file_list = os.listdir(path_dir) #train, valid

for i in file_list:
    path_dir_2 = path_dir + '/' + i # train, valid 폴더
    file_list_2 = os.listdir(path_dir_2)

    for j in file_list_2:
        if '라벨' in j and i == 'Training':
            unzip(path_dir_2+'/'+j,'C:/Users/keonj/PycharmProjects/pythonProject2/custom_dataset/train/labels')

        elif '라벨' in j and i == 'Validation':
            unzip(path_dir_2+'/'+j,'C:/Users/keonj/PycharmProjects/pythonProject2/custom_dataset/test/labels')


    print(j+' finish')

