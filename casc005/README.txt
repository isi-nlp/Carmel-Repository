
#============================================================
# EM Symbol clustering
#
# usage:
#   % cluster <n-gram-order> <num-of-clusters> <text>
#
# <text> should be in carmel format, blank line alternating
# with text line.
#
# output visualization files:
#   cluster.table   -- P(sym | cluster)
#   cluster.res     -- Viterbi assignment of <text> tokens to clusters
#   cluster.viterbi -- Pretty printed, only works if <text> tokens are all single character tokens
#
# intermediate files:
#   cluster.fsa, cluster.fst (plus trained versions)

