from main import *

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
        # think that this is not possible to do becasue when two seperate patterns of intsert/delete are found with the same cost
    # one of the test cases has the first one found to be correct and the other test case has the second so no matter which you keep one will be wrong 
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])

