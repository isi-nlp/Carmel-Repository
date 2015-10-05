#Runs the program
#CARMEL=${CARMEL:-/home/knight/carmel-dl2/graehl/carmel/bin/linux64/carmel.static}
CARMEL=${CARMEL:-./carmel}
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
echo ''
echo 'Training Data =' $1
echo 'Smoothing Data =' $2
echo 'Size of Model =' $3
OUTFILE=${4:-Trained.wfsa}
EXCOUNTS=${5:-0}
echo 'Will write to =' $OUTFILE
echo 'Counts to Be Excluded =' $EXCOUNTS
tmpdir=${TMPDIR:-/tmp}
workdir=`mktemp -d $tmpdir/charlm.XXXXXX`;

basewfsa=$workdir/base.wfsa
smoothdata=$workdir/smooth.data
python $DIR/LanguageModel.py $1 $3 $EXCOUNTS -o $basewfsa &&\

python $DIR/helper.py $2 -o $smoothdata &&\

$CARMEL -t -HJ -M 20 -X 0.99999 $smoothdata $basewfsa > $OUTFILE &&\

rm -rf $workdir