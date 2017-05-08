import os
os.chdir('D:\Python实验')
def main():
    f1=open('Book1.txt','rb')
    f2=open('Book2.txt','rb')
    f1.readline()
    f2.readline()
    line1=f1.readlines()
    line2=f2.readlines()
    dict1={}
    dict2={}
    for line in line1:
        elements = line.split()
        dict1[elements[0]] = str(elements[1].decode('gbk'))
    for line in line2:
        elements = line.split()
        dict2[elements[0]] = str(elements[1].decode('gbk'))
    lines=[]
    lines.append('书名\t原价格\t现价格\n')
    for key in dict1:
        s= ''
        if key in dict2.keys():
            s = '\t'.join([str(key.decode('gbk')), dict1[key], dict2[key]])
            s += '\n'
        else:
            s = '\t'.join([str(key.decode('gbk')), dict1[key], str('-----')])
            s += '\n'
        lines.append(s)
    for key in dict2:
            s= ''
            if key not in dict1.keys():
                s = '\t'.join([str(key.decode('gbk')), str('-----'), dict2[key]])
                s += '\n'
            lines.append(s)

    f3=open('Book3.txt','w')
    f3.writelines(lines)

    f3.close()
    f2.close()
    f1.close()


