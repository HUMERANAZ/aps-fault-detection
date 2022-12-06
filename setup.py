from setuptools import find_packages, setup


REQUIREMENT_FILE_NAME="requirements.txt"
def get_requirements() ->list[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list=requirement_file.readlines()
        requirement_list=[requirement_name.replace("\n","") for requirment_name in requirement_list]
    if hyphen_e_dot in requirement_list:
        requirement_list.remove(hyphen_e_dot)
    return requirement_list

    

setup(
    name="sensor",
    version="0.0.1",
    author="humera",
    author_email="humeranaz911@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),

)