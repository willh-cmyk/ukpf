import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='ukpersonalfinance',  
     version='0.1',
     scripts=['basicpersonalfinance'] ,
     author="William Holtam",
     author_email="william.holtam@gmail.com",
     description="A personal finance package for the UK tax system",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/williamholtam/ukpersonalfinance",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GPLv3 License",
         "Operating System :: OS Independent",
     ],
 )