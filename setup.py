from setuptools import setup, find_packages
try:
    from azure_bdist_wheel import cmdclass
except ImportError:
    from distutils import log as logger
    logger.warn("Wheel is not available, disabling bdist_wheel hook")

VERSION = '0.0.1'

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: MIT License',
]

DEPENDENCIES = [
    "adal==1.2.5",
    "msrestazure==0.6.4",
    "azure-mgmt-containerservice==9.4.0",
    "pyyaml==5.3.1",
    "argparse==1.4.0",
    "azure-cli==2.14.1"
]

setup(
    name='aksauth',
    version=VERSION,
    description='Microsoft Azure Command-Line Tools AKSAuth Extension',
    author='Adrian Hynes',
    author_email='adrianhynes@gmail.com',
    url='https://github.com/aido123/aksauth',
    long_description='Connect to your AKS RBAC Cluster Non Interactively',
    license='MIT',
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    install_requires=DEPENDENCIES,
    package_data={'azext_aksauth': ['azext_metadata.json']},
)
