import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bigfastapi",                     # This is the name of the package
    version="0.5.7",                        # The initial release version
    author="BigFastAPI Team",                     # Full name of the author
    author_email="support@rijen.tech",
    description="Adding lots of functionality to FastAPI",
    long_description=long_description,   
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(include=['bigfastapi', 
                                                'bigfastapi.schemas', 
                                                'bigfastapi.models',
                                                'bigfastapi.db',  
                                                'bigfastapi.core',
                                                'bigfastapi.utils', 
                                                'bigfastapi.data']),  

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
    ],                                  
    python_requires='>=3.8',               
    install_requires=['Jinja2', 'fastapi',
                        'wheel',
                        'uvicorn',  
                        'aioredis',
                        'aiosmtplib',
                        'anyio',
                        'alembic',
                        'asgiref',
                        'async-timeout',
                        'blinker',
                        'certifi',
                        'cffi',
                        'charset-normalizer',
                        'click',
                        'dnspython',
                        'email-validator',
                        'fastapi',
                        'fastapi-mail',
                        'fastapi-utils',
                        'greenlet',
                        'h11',
                        'idna',
                        'Jinja2',
                        'MarkupSafe',
                        'packaging',
                        'passlib',
                        'python-jose',
                        'pdfkit',
                        'pycparser',
                        'pydantic',
                        'fastapi_pagination',
                        'PyJWT',
                        'pyparsing',
                        'authlib',
                        'qrcode',
                        'pdfkit',
                        'python-decouple',
                        'python-dotenv',
                        'cryptography',
                        'python-jose[cryptography]',
                        'python-multipart',
                        'PyYAML',
                        'requests',
                        'rfc3986',
                        'six',
                        'sniffio',
                        'sortedcontainers',
                        'SQLAlchemy',
                        'starlette',
                        'typing-extensions',
                        'uvicorn',
                        'watchgod',
                        'websockets',
                        'validators',
                        'pytest',
                        'fastapi-pagination',
                        'qrcode',
                        'itsdangerous'],                 
    url='https://bigfastapi.com',
    keywords='fastapi, bigfastapi, auth',
    package_data={
        'bigfastapi': ['templates/*.*', 'data/*.*', 'templates/email/*.html'],
        'bigfastapi': ['templates/*.*', 'data/*.*', 'templates/landingpage/*.*'],
        # 'bigfastapi': ['data/*.*'],
        # 'bigfastapi': ['templates/email/*.html'],   
    },
    # include_package_data=True,
    project_urls={ 
        'Bug Reports': 'https://github.com/rijentech/bigfastapi',
        'Funding': 'https://bigfastapi.com',
        'Source': 'https://github.com/rijentech/bigfastapi',
    },
)