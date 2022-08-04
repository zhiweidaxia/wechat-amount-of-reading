import os
import datetime

from pip import main
fenge = '$'
def get_data(data_file):
    nums = 0
    title = ''
    dates = ''
    reads = ''
    with open('%s'%data_file,'r',encoding='utf-8') as f:
        for line in f.readlines():
            #
            if line == '\n':
                continue
            if nums == 0:
                line = line.strip('\n')
                title = line

            if nums == 1:
              
                dat = line.split(' ')
                s = 0
                for i in dat:
                    s += 1
                    try:    
                        datetime.datetime.fromisoformat(i)
                        dates = i.strip('\n')
                        dates = dates +fenge+ dat[s].strip('\n')
                    except:
                        #print('日期格式错误')
                        pass
            if line.find('Reads') > -1:
                line = line.strip('\n')
                line = line.split(' ')
                reads = line[-1]
                if reads.find('k') > -1:
                    reads = str(int(float(reads[:reads.find('k')])*1000))
            #print(nums,line)
            nums += 1
    f.close()
    return dates,title,reads
def get_file(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(file)
    lens = len(file_list)
    file_dir = []
    for file in range(0,lens):
        file_dir.append(os.path.join(root, str(file)+'.txt'))
    print(file_dir)
    return file_dir
if __name__ == '__main__':
    path = '11'
    a = get_file(path)
    test = 0
    for i in a:
        get_data(i)
        with open('%s.txt'%path,'a+',encoding='utf-8') as f:
            f.write(path+fenge+get_data(i)[0]+fenge+get_data(i)[1]+fenge+get_data(i)[2])
            print(test,'----',path+"**"+get_data(i)[0]+' ** '+get_data(i)[1]+' ** '+get_data(i)[2])
            f.write('\n')
            f.close()
            test += 1
    #print('\n')