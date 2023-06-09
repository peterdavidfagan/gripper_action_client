from setuptools import setup

package_name = 'gripper_action_client'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Peter David Fagan',
    author_email='peterdavidfagan@gmail.com',
    maintainer='Peter David Fagan',
    maintainer_email='peterdavidfagan@gmail.com',
    keywords=['ROS 2'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Python wrapper around ROS 2 CLI interface for GripperCommand.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
)
