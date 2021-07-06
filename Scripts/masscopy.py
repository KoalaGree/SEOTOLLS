import os
import shutil
import datetime

now = str(datetime.datetime.now())[:19]
now = now.replace(":","_")

src_dir="/home/koalagree/Documents/SEOTOLLS/index.html"
dst_dir="/home/koalagree/Documents/SEOTOLLS/index_"+str(now)+".html"
shutil.copy(src_dir,dst_dir)
