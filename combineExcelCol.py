import xlrd
import xlwt
from pathlib import Path, PurePath
# 导入excel和文件操作库

src_path = './'
p = Path(src_path)
# 获取当前目录下的所有 xls 文件
files = [x for x in p.iterdir() if PurePath(x).match('*.xls')]


dst_path = input('please enter result file name:')