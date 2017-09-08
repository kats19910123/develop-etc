# _*_ coding: utf-8 _*_
import zipfile

def main():
    # ZIP圧縮するファイルのリスト
    filelist = ["aaa.txt", "bbb.txt", "ccc.txt"]
    # ZIP圧縮の設定
    zip1 = zipfile.ZipFile("test.zip", "w", zipfile.ZIP_STORED)
    # ZIP圧縮
    for i, filename in enumerate(filelist):
        zip1.write(filename)
    #ZIPを閉じる
    zip1.close()
    
if __name__ == "__main__":
    main()