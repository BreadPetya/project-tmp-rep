import setuptools

setuptools.setup(name="project-tmp-rep")

from project_tmp_rep.project import func_from_project

if __name__ == "__main__":
    print(func_from_project())
