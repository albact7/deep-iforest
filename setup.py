from setuptools import setup, find_packages

setup(
   name='deep_if',
   version='1.1',
   author='Xu, Hongzuo and Pang, Guansong and Wang, Yijie and Wang, Yongjun',
   url='https://github.com/xuhongzuo/deep-iforest',
   packages=find_packages(include=['deep_if', 'deep_if.*']),
   install_requires= [
    "wheel",
    "absl-py==1.1.0",
    "ase==3.22.1",
    "asttokens==2.0.5",
    "astunparse==1.6.3",
    "backcall==0.2.0",
    "cachetools==5.2.0",
    "certifi==2022.5.18.1",
    "charset-normalizer==2.0.12",
    "colorama==0.4.4",
    "cycler==0.11.0",
    "debugpy==1.6.0",
    "decorator==5.1.1",
    "entrypoints==0.4",
    "executing==0.8.3",
    "flatbuffers==1.12",
    "fonttools==4.33.3",
    "gast==0.4.0",
    "google-auth==2.8.0",
    "google-auth-oauthlib==0.4.6",
    "google-pasta==0.2.0",
    "googledrivedownloader==0.4",
    "grpcio==1.46.3",
    "h5py==3.7.0",
    "idna==3.3",
    "importlib-metadata==4.11.4",
    "ipykernel==6.14.0",
    "ipython==8.4.0",
    "isodate==0.6.1",
    "jedi==0.18.1",
    "joblib==1.1.0",
    "jupyter-client==7.3.4",
    "jupyter-core==4.10.0",
    "kiwisolver==1.4.3",
    "libclang==14.0.1",
    "llvmlite==0.38.1",
    "Markdown==3.3.7",
    "matplotlib==3.5.2",
    "matplotlib-inline==0.1.3",
    "nest-asyncio==1.5.5",
    "networkx==2.6.3",
    "numba==0.55.2",
    "numpy==1.21.5",
    "oauthlib==3.2.0",
    "opt-einsum==3.3.0",
    "packaging==21.3",
    "pandas==1.3.5",
    "parso==0.8.3",
    "patsy==0.5.2",
    "pickleshare==0.7.5",
    "Pillow==9.1.1",
    "plotly==5.8.2",
    "plyfile==0.7.4",
    "progressbar==2.5",
    "prompt-toolkit==3.0.29",
    "protobuf==3.19.4",
    "psutil==5.9.1",
    "pure-eval==0.2.2",
    "pyarrow==8.0.0",
    "pyasn1==0.4.8",
    "pyasn1-modules==0.2.8",
    "Pygments==2.12.0",
    "pyod==0.9.7",
    "pyparsing==3.0.9",
    "python-dateutil==2.8.2",
    "pytz==2022.1",
    "pywin32==304",
    "PyYAML==6.0",
    "pyzmq==23.1.0",
    "rdflib==6.1.1",
    "requests==2.28.0",
    "requests-oauthlib==1.3.1",
    "rsa==4.8",
    "scikit-learn==1.0.2",
    "scipy==1.8.1",
    "six==1.16.0",
    "stack-data==0.2.0",
    "statsmodels==0.13.2",
    "tenacity==8.0.1",
    "tensorboard==2.9.1",
    "tensorboard-data-server==0.6.1",
    "tensorboard-plugin-wit==1.8.1",
    "tensorflow==2.9.1",
    "tensorflow-estimator==2.9.0",
    "tensorflow-io-gcs-filesystem==0.26.0",
    "Keras-Applications==1.0.8",
    "Keras-Preprocessing==1.1.2",
    "termcolor==1.1.0",
    "threadpoolctl==3.1.0",
    "torch==1.11.0",
    "torchaudio==0.11.0",
    "torchvision==0.12.0",
    "tornado==6.1",
    "tqdm==4.62.3",
    "traitlets==5.2.2.post1",
    "typing_extensions==4.2.0",
    "urllib3==1.26.9",
    "wcwidth==0.2.5",
    "Werkzeug==2.1.2",
    "wrapt==1.14.1",
    "zipp==3.8.0"
    ]
)