import os
import shutil
import scandir
import fitz

if __name__ == '__main__':
    dir_path = r'.'
    os.scandir()
    filenames = os.scandir(dir_path)
    for filename in filenames:
        if filename.name.split('.')[-1] == 'pdf':
            doc = fitz.open(filename.path)
            pg_num = doc.pageCount
            file_dir = os.path.join(dir_path, filename.name.split('.')[0])
            if os.path.exists(file_dir):
                shutil.rmtree(file_dir)
            if pg_num > 1:
                os.mkdir(file_dir)
                for pg in range(pg_num):
                    page = doc[pg]
                    pm = page.getPixmap()
                    pg_name = os.path.join(file_dir, str(pg + 1)) + '.jpg'
                    pm.writeImage(pg_name)
            else:
                page = doc[0]
                pm = page.getPixmap()
                # pg_name = os.path.join(file_dir, str(pg + 1)) + '.jpg'
                pm.writeImage(os.path.join(dir_path, filename.name.split('.')[0]) + '.jpg')
                