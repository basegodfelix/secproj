import setuptools
import os

try:
    path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(path, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setuptools.setup(
    name="SecProj",
    version="1.0.0",
    author="Felix Hernandez",
    description="Simple tools to help you secure your projects in a more simple manner, allowing for simple and secure development.",
    packages=["secproj"],
    install_requires=["cryptography","python-dotenv"],
    url="https://github.com/basegodfelix/secproj",
    long_description = long_description,
    long_description_context_type = 'text/markdown',
    license="MIT"
)