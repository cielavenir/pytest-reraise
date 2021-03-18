from setuptools import setup

setup(
    name='pytest-reraise',
    description='Make multi-threaded pytest test cases fail when they should',
    version='1.0.3.1',
    url='https://github.com/cielavenir/pytest-reraise',
    license='MIT',
    author='cielavenir',
    author_email='cielartisan@gmail.com',
    packages=['pytest_reraise'],
    entry_points={'pytest11': ['reraise = pytest_reraise.reraise']},
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['pytest>=3.0'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
