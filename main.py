import os
from PIL import Image
from PyPDF4 import PdfFileMerger
import shutil


# 防止字符串乱码
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

class AllImagesToPdf:

    def __init__(self):
        self.imgs_path = ""  # 将所有的图片放到此文件夹中
        self.pdfs_path = ""  # 将所有转换后的pdf放到此文件夹,一个中继文件夹
        self.save_path = ""  #存放路径,包括文件名

        self.img_path =""#单个图片的文件路径

    def set_imgs_path(self,path):
        self.imgs_path=path
    def set_pdfs_path(self,path):
        self.pdfs_path=path
    def set_save_path(self,path):
        self.save_path=path
    def set_img_path(self,path):
        self.img_path=path

    def __del__(self):
        # print("debug","对象已销毁")
        pass


    def img_to_pdf(self):#单个文件转换PDF
        fp = self.img_path
        obj_img = Image.open(fp)
        save_img_path = os.path.join(self.pdfs_path, self.img_path.split(".")[0] + ".pdf")  # 拼接pdf的路径和名称
        obj_img.save(save_img_path)  # 保存为pdf
        fp.close()


        pass

    def imgs_to_pdfs(self):#目录下所有的PDF图片存PDF
        imgs_path = self.imgs_path
        imgs_list = os.listdir(imgs_path)
        for img_name in imgs_list:
            if ".jpg" in img_name:
                read_img_path = os.path.join(self.imgs_path,img_name)
                fp = open(read_img_path,'rb')
                obj_img = Image.open(fp)  # 打开指定路径下的图片
                save_img_path = os.path.join(self.pdfs_path,img_name.split(".")[0]+".pdf")  # 拼接pdf的路径和名称
                obj_img.save(save_img_path)  # 保存为pdf
                fp.close()
                print(save_img_path+"saved!")

    def all_pdfs_to_pdf(self):#PDF合并
        pdf_merger = PdfFileMerger()  # 创建PdfFileMerger对象，用来合并pdf文件
        pdfs_path = self.pdfs_path
        pdfs_list = os.listdir(pdfs_path)
        pdfs_path_list = []
        for pdf_name in pdfs_list:
            if pdf_name.endswith(".pdf"):
                pdf_merger.append(os.path.join(pdfs_path,pdf_name))
        pdf_merger.write(self.save_path)
        pdf_merger.close()
                # pdfs_path_list.append(os.path.join(self.pdfs_path,pdf_name))
        # print(pdfs_path_list)
        
        # for file_path in pdfs_path_list:
        #     fp = open(file_path,'rb')

def delete_all_files_in_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


def run():
    imgs_path="E:/PersonalTestData/IMGs/"
    pdfs_path="E:/PersonalTestData/PDFs/"
    save_path="E:/PersonalTestData/sum.pdf"
    bot = AllImagesToPdf()
    
    bot.set_imgs_path(imgs_path)
    bot.set_pdfs_path(pdfs_path)
    bot.set_save_path(save_path)

    bot.imgs_to_pdfs()
    bot.all_pdfs_to_pdf()

if __name__ =="__main__":
    run()