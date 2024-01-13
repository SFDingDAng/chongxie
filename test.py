# 要删除的行
line_to_delete = "^http[s]?:\/\/magev6\.if\.qidian\.com\/argus\/api\/v1\/bookshelf\/refresh url reject-200"

# 要处理的文件名
filename = "chongxie.txt"

# 读取文件内容，并存储除了要删除的行之外的所有行
with open(filename, 'r') as file:
    lines = file.readlines()
new_lines = [line for line in lines if line.strip("\n") != line_to_delete]

# 将新内容写回文件
with open(filename, 'w') as file:
    file.writelines(new_lines)
