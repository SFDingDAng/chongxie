import re

# 要删除的行的模式
pattern_to_delete = "^http[s]?:\/\/magev6\.if\.qidian\.com\/argus\/api\/v1\/bookshelf\/refresh url reject-200"

# 要替换的字符串
string_to_replace = "https://raw.githubusercontent.com/Yu9191/Rewrite/main/Qidian_my.js"

# 替换后的字符串
replacement_string = "https://raw.githubusercontent.com/SFDingDAng/chongxie/main/Qidian_my.js"

# 要处理的文件名
filename = "chongxie.txt"

# 读取文件内容
with open(filename, 'r') as file:
    lines = file.readlines()

# 删除特定行并替换指定字符串
new_lines = []
for line in lines:
    if not re.match(pattern_to_delete, line):
        # 如果这行不是要删除的行，替换字符串
        new_lines.append(re.sub(string_to_replace, replacement_string, line))
    # 如果这行是要删除的行，则不执行任何操作，即不将其加入到new_lines中

# 将处理后的内容写回文件
with open(filename, 'w') as file:
    file.writelines(new_lines)
