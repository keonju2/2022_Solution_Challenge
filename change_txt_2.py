
import json
import os
from pathlib import Path

def make_txt(file):
    names = []
    file = Path(file)

    with open(file,encoding='utf-8') as f:  # load json
        json_data = json.load(f)

    for data in json_data:
        if data == 'ObjectInfo':
            lxtl, lytl, lxbr, lybr = json_data[data]['BoundingBox']['Leye']['Position']
            rxtl, rytl, rxbr, rybr = json_data[data]['BoundingBox']['Reye']['Position']
            # xtl, ytl, xbr, ybr : x상, y상, x하, y하

            if json_data[data]['BoundingBox']['Leye']['Opened'] == True:
                l_label = 0
            elif json_data[data]['BoundingBox']['Leye']['Opened'] == False:
                l_label = 1
            if json_data[data]['BoundingBox']['Reye']['Opened'] == True:
                R_label = 0
            elif json_data[data]['BoundingBox']['Reye']['Opened'] == False:
                R_label = 1

        if data == 'FileInfo':
            file_width = json_data[data]['Width']
            file_height = json_data[data]['Height']

    lxtl = float(lxtl)
    lytl = float(lytl)
    lxbr = float(lxbr)
    lybr = float(lybr)
    rxtl = float(rxtl)
    rytl = float(rytl)
    rxbr = float(rxbr)
    rybr = float(rybr)
    file_width = float(file_width)
    file_height = float(file_height)

        # 좌표 구하기
    l_width = lxbr - lxtl
    l_height = lybr - lytl
    l_center_x = (lxbr + lxtl) / 2
    l_center_y = (lybr + lytl) / 2

    r_width = rxbr - rxtl
    r_height = rybr - rytl
    r_center_x = (rxbr + rxtl) / 2
    r_center_y = (rybr + rytl) / 2

    f_dw = 1. / file_width
    f_dh = 1. / file_height

    l_x = l_center_x * f_dw
    l_y = l_center_y * f_dh
    l_w = l_width * f_dw
    l_h = l_height * f_dh

    r_x = r_center_x * f_dw
    r_y = r_center_y * f_dh
    r_w = r_width * f_dw
    r_h = r_height * f_dh


    l_box = [str(l_label), str(l_x), str(l_y), str(l_w), str(l_h)]
    r_box = [str(R_label), str(r_x), str(r_y), str(r_w), str(r_h)]

    return l_box, r_box


path_dir = 'C:/Users/keonj/PycharmProjects/pythonProject2/custom_dataset'
file_list = os.listdir(path_dir) #train, test


for i in file_list:#test train
    path_dir_2 = path_dir + '/' + i  #C:\Users\keonj\PycharmProjects\pythonProject2\custom_dataset\test
    file_list_2 = os.listdir(path_dir_2) # 버스, 승용, 택시..

    for j in file_list_2: # labels
        path_dir_3 = path_dir_2 + '/' + j #C:\Users\keonj\PycharmProjects\pythonProject2\custom_dataset\test\labels
        file_list_3 = os.listdir(path_dir_3)

        for l in file_list_3: # 버스. 001
            path_dir_4 = path_dir_3 + '/' + l #C:\Users\keonj\PycharmProjects\pythonProject2\custom_dataset\test\labels\1.버스
                                             #C:\Users\keonj\PycharmProjects\pythonProject2\custom_dataset\train\labels\001_G1


            if '버스' in path_dir_4 or '승용' in path_dir_4 or '택시' in path_dir_4 or '트럭' in path_dir_4:

                file_list_4 = os.listdir(path_dir_4) #폴더들



                for m in file_list_4:
                    path_dir_5 = path_dir_4 + '/' + m # C:\Users\keonj\PycharmProjects\pythonProject2\custom_dataset\train\labels\1.버스\R_001_60_M
                    file_list_5 = os.listdir(path_dir_5)

                    for n in file_list_5:
                        path_dir_6 = path_dir_5 + '/' + n #C:\Users\keonj\PycharmProjects\pythonProject2\custom_dataset\test\labels\1.버스\R_216_60_M\R_216_60_M_01_M0_G1_C0_01.json

                        if os.path.splitext(path_dir_6)[1] == '.json':
                            try:
                                l_b, r_b = make_txt(path_dir_6)
                                new_file = path_dir_6.replace('.json', '')
                                f = open(new_file + '.txt', 'w')
                                f.write(' '.join(l_b))
                                f.write('\n')
                                f.write(' '.join(r_b))
                                f.close()

                                os.remove(path_dir_6)
                                print('ok2')
                            except:
                                print(path_dir_6)
                                new_file = path_dir_6.replace('.json', '')
                                f = open(new_file + '.txt', 'w')
                                f.close()
                                os.remove(path_dir_6)



            else:
                file_list_7 = os.listdir(path_dir_4)  # json 파일들

                for o in file_list_7:
                     path_dir_7 = path_dir_4 + '/' + o #C:\Users\keonj\PycharmProjects\pythonProject2\custom_dataset\train\labels\001_G1\001_G1_01_무광원_계기판_정상주시_20200917_182234_02144.json

                     if os.path.splitext(path_dir_7)[1] == '.json':
                         try:
                             l_b, r_b = make_txt(path_dir_7)
                             new_file = path_dir_7.replace('.json', '')
                             f = open(new_file + '.txt', 'w')
                             f.write(' '.join(l_b))
                             f.write('\n')
                             f.write(' '.join(r_b))
                             f.close()
                             os.remove(path_dir_7)
                             print('ok')
                         except:
                             print(path_dir_7)
                             new_file = path_dir_7.replace('.json', '')
                             f = open(new_file + '.txt', 'w')
                             f.close()
                             os.remove(path_dir_7)


# C:/Users/keonj/PycharmProjects/pythonProject2/custom_dataset/test/labels/Q_105_40_M_02_M0_G0_C0/Q_105_40_M_02_M0_G0_C0_23.json
# C:/Users/keonj/PycharmProjects/pythonProject2/custom_dataset/test/labels/Q_108_20_F_10_M0_G1_C0/Q_108_20_F_10_M0_G1_C0_16.json
# C:/Users/keonj/PycharmProjects/pythonProject2/custom_dataset/train/labels/Q_084_70_M_05_M0_G0_C0/Q_084_70_M_05_M0_G0_C0_21.json