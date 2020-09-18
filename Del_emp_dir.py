import os


def del_emp_dir(path):
    for (root, dirs, files) in os.walk(path):
        for item in dirs:
            dir = os.path.join(root, item)
            try:
                os.rmdir(dir)
                print(dir)
            except Exception as e:
                print('Exception', e)
                # pass


if __name__ == '__main__':
    dir = r'C:\Users\ct\Downloads\yf_study\yf_paperdata\Del_empdir_tes'
    del_emp_dir(dir)
