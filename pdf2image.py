import os
from os import write
import shutil
import scandir
import fitz

def wirte_image(filename):
    doc = fitz.open(filename.path)
    pg_num = doc.pageCount
    fmt = f'{{0:0{len(str(pg_num))}d}}'
    for pg in range(pg_num):
        page = doc[pg]
        page_num = fmt.format(pg + 1)
        img_name = f'{filename.name.split(".")[0]}_{page_num}.jpg'
        yield page,img_name

def get_image(dir_path):
    os.scandir()
    filenames = os.scandir(dir_path)
    for filename in filenames:
        if filename.name.split('.')[-1] == 'pdf':
            # print(f'转转转换{filename.name},请稍等...')
            yield filename

if __name__ == '__main__':
    dir_path = r'.'
    for filename in get_image(dir_path):
        print(f'正在转换{filename.name}，请稍等……')
        file_dir = os.path.join(dir_path, filename.name.split('.')[0])
        if not os.path.exists(file_dir):
            # shutil.rmtree(file_dir)
            os.mkdir(file_dir)
        for page,imgname in wirte_image(filename):
            pm = page.getPixmap()
            pg_full_name = os.path.join(file_dir, dir_path, imgname)
            print(f'图片提取到{pg_full_name}')
            pm.writeImage( pg_full_name)
    input('按任意键退出……')