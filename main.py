import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))



def fast_MED(S, T, MED={}):



    # TODO -  implement top-down memoization
    if (S, T) in MED:
        return MED[(S,T)]

    if S == "":
        result = len(T)
    elif T == "":
        result = len(S)
    elif S[0] == T[0]:
        result = fast_MED(S[1:], T[1:], MED)
    else:

        result = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED))
    MED[(S, T)] = result
    return result




    # Top-down memoized edit distance with alignment
def fast_align_MED(S, T, MED=None):

    top_level = False
    if MED is None:
        MED = {}
        top_level = True
    if (S, T) in MED:
        result = MED[(S, T)]
    elif S == "":
        result = (len(T), ("-" * len(T), T))
    elif T == "":

        result = (len(S), (S, "-" * len(S)))
    elif S[0] == T[0]:

        cost, (align_S, align_T) = fast_align_MED(S[1:], T[1:], MED)
        result = (cost, (S[0] + align_S, T[0] + align_T))
    else:

        insert_cost, (ins_align_S, ins_align_T) = fast_align_MED(S, T[1:], MED)
        option1 = (1 + insert_cost, ('-' + ins_align_S, T[0] + ins_align_T))


        delete_cost, (del_align_S, del_align_T) = fast_align_MED(S[1:], T, MED)
        option2 = (1 + delete_cost, (S[0] + del_align_S, '-' + del_align_T))


        result = option1 if option1[0] <= option2[0] else option2

    # Save the computed result for (S, T)
    MED[(S, T)] = result

    if top_level:
        return result[1]
    else:
        return result





