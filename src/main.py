import os
import shutil


def copy_file_recursive(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for item in os.listdir(source_dir):
        src_path = os.path.join(source_dir,item)
        dst_path = os.path.join(dest_dir, item)
        print(f" source path: {src_path}")
        print(f"dest path: {dst_path}")
        
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        else:
            copy_file_recursive(src_path, dst_path)

    



def main():
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    os.mkdir("./public")

    copy_file_recursive("./static","./public")


if __name__== '__main__':
    main()
    
    


