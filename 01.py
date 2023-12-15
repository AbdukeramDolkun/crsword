file = open("requirements.txt", "r")  # 以只读模式读取文件

lines = []

for i in file:
    lines.append(i)  # 逐行将文本存入列表lines中

file.close()

new = []

for line in lines:  # 逐行遍历

    p = 0  # 定义计数指针

    for bit in line:  # 对每行进行逐个字遍历

        if bit == " ":  # 遇到空格时进行处理

            new.append(line[0:p])  # 将line中的0：p字段存入新列表new中，用于写入新的.txt中

            break  # 处理完一行后跳出当前循环

        else:

            p = p + 1  # 如果bit不是空格，指针加一

# 以写的方式打开文件，如果文件不存在，就会自动创建，如果存在就会覆盖原文件

file_write_obj = open("requirements.txt", 'w')

for var in new:
    file_write_obj.writelines(var)

    file_write_obj.writelines('\n')

file_write_obj.close()