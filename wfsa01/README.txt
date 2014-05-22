
This is a letter-bigram model for English.  It accepts sequences of lowercase
letters (a-z), plus space (_).  It uses interpolation smoothing with
unigrams, with letter-specific lambdas trained with EM.

Actually a tranducer that generates English strings from *e*.

String always ends in space (_) !!
