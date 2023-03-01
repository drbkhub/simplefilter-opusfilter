export PYTHONPATH=$(pwd)
echo PYTHONPATH: $(pwd)
EFLOMAL_PATH=$(find . -wholename "*eflomal/bin")
align=$(find . -wholename "*eflomal*align.py")
makepriors=$(find . -wholename "*eflomal*makepriors.py")

dirname_align=$(dirname "$align")
dirname_priors=$(dirname "$makepriors")

if [[ "$dirname_align" == "$dirname_priors" && "$EFLOMAL_PATH" == "$dirname_priors" ]]; then
    echo "EFLOMAL_PATH: " $EFLOMAL_PATH
    export EFLOMAL_PATH=$EFLOMAL_PATH
else
    echo "aling.py: " $dirname_align  
    echo "makepriors.py: " $dirname_priors
    echo "eflomal root: " $EFLOMAL_PATH
fi

