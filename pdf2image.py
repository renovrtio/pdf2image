import os
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
        # img_name = f'{filename.name.split(".")[0]}_{page_num}.jpg'
        img_name = f'{os.path.splitext(filename.name)[0]}_{page_num}.jpg'
        yield page,img_name

def get_image(dir_path):
    filenames = os.scandir(dir_path)
    for filename in filenames:
        # if filename.name.split('.')[-1] == 'pdf':
        if os.path.splitext(filename.name)[-1].lower() == '.pdf':
            # print(f'转转转换{filename.name},请稍等...')
            yield filename

if __name__ == '__main__':
    dir_path = r'.'
    for filename in get_image(dir_path):
        print(f'正在转换{filename.name}，请稍等……')
        # 去除文件名中的空格
        # file_name = filename.name.split('.')[0].strip()
        file_name = os.path.splitext(filename.name)[0].strip()
        file_dir = os.path.join(dir_path, file_name)
        if not os.path.exists(file_dir):
            # shutil.rmtree(file_dir)
            os.mkdir(file_dir)
        for page,imgname in wirte_image(filename):
            pm = page.getPixmap()
            pg_full_name = os.path.join(file_dir, imgname)
            print(f'图片提取到{pg_full_name}')
            pm.writeImage( pg_full_name)
    input('按任意键退出……')