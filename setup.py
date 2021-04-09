from setuptools import find_packages, setup

setup(
    name="prpd_usb",    
    setup_requires=['setuptools'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pyserial',
        'cherrypy',
        'paho-mqtt',
        'libscrc',
    ],
    entry_points={
        'console_scripts': [
            'prpd_usb = prpd_usb.__main__:main',
        ],
    },
)
