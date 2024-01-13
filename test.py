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

# 处理每一行，删除或替换
new_lines = []
for line in lines:
    # 检查是否是要删除的行
    if re.match(pattern_to_delete, line):
        continue  # 不添加到new_lines，即删除该行
    else:
        # 不是要删除的行，检查是否需要替换字符串
        line = re.sub(string_to_replace, replacement_string, line)
        new_lines.append(line)

# 将修改后的内容写回文件
with open(filename, 'w') as file:
    file.writelines(new_lines)
