from setuptools import find_packages, setup

install_requires = [
    'ConfigArgParse==1.2.3'
]

dependency_links = [

]

entry_points={
    'console_scripts': [
        'kafkacatRunner=kafkacatRunner.app:main',
    ],
}

setup(
    name='kafkacatRunner',
    version='1.0.0',
    description='Audit Intelligence Kafkacat command builder',
    author='Daniel Larrea',
    author_email='daniel.larrea@drilliginfo.com',
    packages=find_packages('kafkacatRunner'),
    package_dir={'':'src'},
    package_data={},
    install_requires=install_requires,
    dependency_links=dependency_links,
    entry_points=entry_points,
    zip_safe=True
)
