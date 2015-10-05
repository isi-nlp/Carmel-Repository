
#============================================================
# EM Symbol clustering
#
# usage:
#   % cluster <n-gram-order> <num-of-clusters> <restarts> <cipher>
#
# <cipher> should be in carmel format, blank line alternating
# with cipher line.
#
# output visualization files:
#   cluster.viterbi
#   cluster.table     /* channel */
#   cluster.fsatable  /* source */
#
# intermediate files:
#   cluster.fsa, cluster.fst (plus trained versions)
#
# everything in this directory was done with:
#   % cluster 3 3 1 english.txt
