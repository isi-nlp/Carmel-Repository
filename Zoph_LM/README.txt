
This build a language model using interpolation smoothing, using EM to set 
interpolation weights.  Contexts are binned, one backoff weight per bin.

Input files are:
  Training text file (used for n-gram count collection)
  Smoothing text file (used for EM setting of backoff weights)
  N-gram order

Output files are:
  Trained WFSA

LanguageModel.py creates the WFSA. 

To run simply type:

bash LanguageModel.sh <Train.data> <Smooth.data> <size of model> <outfile> <counts to be excluded>

(counts to be excluded defaults to zero if no specified input)

The output WFSA defaults to Trained.wfsa.

env variables: 
  CARMEL can be set if your carmel is not ./carmel
  SEPARATOR can be set to make the word separator something other than "_"
  TMPDIR can be set to construct temporary files in something other than /tmp

