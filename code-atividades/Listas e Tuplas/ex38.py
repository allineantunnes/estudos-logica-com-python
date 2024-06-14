from setuptools import setup, find_packages

setup (
    name="minha_biblioteca",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        #Dependencias da sua biblioteca (se holver)

#Com a biblioteca organizada desta forma,você pode facilmente distribuí-la usando
#ferramentas como pip ou compartilhá-la no PyPI para que outros possam usar.

    ],
)