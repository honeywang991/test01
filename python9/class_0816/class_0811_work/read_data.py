
def read_data(file):
    file = open(r'D:\wf\python9\class_0816\class_0811_work\test_data','r',encoding='utf-8')
    test_data = file.readlines()
    #print("第一行数据："，test_data[0])
    list_data=[]
    for line_data in test_data:
        split_data=line_data.split('@')
        # split_data=test_data[0].split('@')#列表类型的数据
        #print("第一行数据切割后的结果"，split_data)
        dict_data={}
        for item in split_data:
            #print("遍历切割后的结果"，item)
            #print(item.split(':',1))返回的也是列表类型的数据
            dict_data[item.split(':',1)[0]]=item.split(':',1)[1].strip('\n')

        list_data.append(dict_data)
    return list_data

if __name__ == '__main__':
    result=read_data(r'D:\wf\python9\class_0816\class_0811_work\test_data')
    print(result)