from setuptools import setup, find_packages

setup(
    name='speech_transformer',
    packages = find_packages(),
    version='1.0',
    description='Speech Transformer for Speech Recognition',
    author='Soohwan Kim',
    author_email='sh951011@gmail.com',
    url='https://github.com/martinssmariana/speech_transformer',
    install_requires=[
        'torch>=1.4.0',
        'numpy',
    ],
    keywords=['asr', 'speech_recognition', 'conformer', 'end-to-end'],
    python_requires='>=3.6'
)
