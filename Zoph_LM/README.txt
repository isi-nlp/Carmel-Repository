README

Both files can just be plaintext files

LanguageModel.py creates the WFSA and 

To run simply type:

bash LanguageModel.sh <Train.data> <Smooth.data> <size of model> <outfile> <counts to be excluded>

counts to be excluded defaults to zero if no specified input

The output WFSA defaults to Trained.wfsa

env variables: 
CARMEL can be set if your carmel is not ./carmel
SEPARATOR can be set to make the word separator something other than "_"
TMPDIR can be set to construct temporary files in something other than /tmp
