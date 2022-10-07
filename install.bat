
set PIP_FIND_LINKS="https://whls.blob.core.windows.net/unstable/index.html"
pip install lytest simphony sax jax sklearn klayout
pip install "jax[cpu]===0.3.7" -f https://whls.blob.core.windows.net/unstable/index.html --use-deprecated legacy-resolver
pip install gdsfactory==5.38.0
gf tool install

if exist "%USERPROFILE%\Desktop\gdsfactory" (goto SKIP_INSTALL)
cd %USERPROFILE%\Desktop
git clone https://github.com/gdsfactory/gdsfactory.git

:SKIP_INSTALL
echo gdsfactory installed
