import setuptools

with open ( "README.md" , "r" ) as fh :
    long_description = fh.read()

setuptools . setup (
    name = "GetJsonValue" ,
    version = "0.0.5" ,
    author = "Wanghao" ,
    author_email = "947001731@qq.com" ,
    description = "Gets the value in the JSON data" ,
    long_description = long_description,
    long_description_content_type='text/markdown',
    url = "https://github.com/WangHaoz/GetJsonValue" ,
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3" ,
        'License :: OSI Approved :: Apache Software License',
        "Operating System :: OS Independent" ,
    ],
)