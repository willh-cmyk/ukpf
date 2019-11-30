import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name="ukpf",
     version="0.1",
     scripts=["payslip.py"],
     author="William Holtam",
     author_email="william.holtam@gmail.com",
     description="A personal finance package for the UK tax system",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/williamholtam/ukpersonalfinance",
     download_url="https://github.com/WilliamHoltam/ukpf/archive/v_01.tar.gz",
     packages=setuptools.find_packages(),
     keywords=["PERSONAL", "FINANCE", "UK", "PAYSLIP"],
     classifiers=[
         "Development Status :: 3 - Alpha",
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: "
         "GNU General Public License v3 or later (GPLv3+)",
         "Operating System :: OS Independent",
     ],
 )
