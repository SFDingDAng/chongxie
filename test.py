import re

# 要删除的行
line_to_delete = "^http[s]?:\/\/magev6\.if\.qidian\.com\/argus\/api\/v1\/bookshelf\/refresh url reject-200"

# 要替换的字符串
string_to_replace = "https://raw.githubusercontent.com/Yu9191/Rewrite/main/Qidian_my.js"

# 替换后的字符串
replacement_string = "https://raw.githubusercontent.com/SFDingDAng/chongxie/main/Qidian_my.js"

# 要处理的文件名
filename = "chongxie.txt"

# 读取文件内容，并存储除了要删除的行之外的所有行
with open(filename, 'r') as file:
    lines = file.readlines()

# 使用正则表达式替换指定字符串
new_lines = [re.sub(string_to_replace, replacement_string, line) if line.strip("\n") != line_to_delete else line for line in lines]

# 将新内容写回文件
with open(filename, 'w') as file:
    file.writelines(new_lines)
