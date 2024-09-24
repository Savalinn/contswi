from setuptools import setup, find_packages

setup(
    name='contswi',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'contswi = contswi.cli:main',
        ],
    },
    description="A simple kubectl context switcher cli tool",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Savalinn/contswi',  # ide jön a GitHub repo link
    author='Puskás Gábor',
    author_email='pg@0r.hu',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.7',
)
