from setuptools import setup

setup(name='notes_cli',
      version='0.2',
      description='command line tool for your notes',
      long_description='Store notes for later and query them to avoid having to leave the shell.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Topic :: Terminals',
      ],
      keywords='notes cli',
      url='https://github.com/bigolu/notes-cli',
      author='Olaolu Biggie Emmanuel',
      author_email='hi@bigo.lu',
      license='MIT',
      packages=['notes_cli'],
      install_requires=[
          'click',
          'fuzzywuzzy',
          'gitdb',
          'GitPython',
          'python-levenshtein',
          'smmap'
      ],
      entry_points = {
          'console_scripts': ['notes=notes_cli.cli:main'],
      },  
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
