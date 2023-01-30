
set PIP_FIND_LINKS="https://whls.blob.core.windows.net/unstable/index.html"
pip install sax jax sklearn
pip install "jaxlib[cuda111]" -f https://whls.blob.core.windows.net/unstable/index.html --use-deprecated legacy-resolver
pip install gdsfactory[full,gmsh,tidy3d,devsim,meow,ray,database]==6.26.0
gf tool install

cd ..\condabin
call conda activate
call conda install -c conda-forge slepc4py=*=complex* -y
call conda install -c conda-forge git spyder -y
if exist "%USERPROFILE%\Desktop\gdsfactory" (goto SKIP_INSTALL)
cd %USERPROFILE%\Desktop
call git clone https://github.com/gdsfactory/gdsfactory.git

:SKIP_INSTALL
echo gdsfactory installed

cd gdsfactory
python shortcuts.py
