#import setuptools

#setuptools.setup(name="project-tmp-rep")

# from project_tmp_rep.project import func_from_project

# if __name__ == "__main__":
#     print(func_from_project())
from lib_tmp_rep.func_lib import func_from_lib

def func_from_project():
    return func_from_lib() + 1
