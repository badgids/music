from .. permutations import InterestingPermutations, transposePermutation
from .plainChanges import PlainChanges
from sympy.combinatorics import Permutation as p_
from colorama import init
init()
from termcolor import colored

def printPeal(peal,hunts=[0,1]):
    """Print peal with colored numbers. Hunt have also colored background"""
    reset='reset'
    #colors='black',
    #colors='redasd','green','yellow','blue','magenta','cyan'#,'white'
    colors='yellow','magenta','green','red','blue','white','grey','cyan'
    hcolors='on_white','on_blue','on_red','on_grey','on_yellow','on_magenta','on_green','on_cyan'
    final_string=''
    for sequence in peal:
        final_string+=''.join(colored(i,colors[i],hcolors[-(i+1)]) if i in hunts else colored(i,colors[i],"on_white",["bold"]) for i in sequence)+'\n'
    print(final_string)

class Peals(InterestingPermutations):
    """Use permutations to make peals and represent peals as permutations.

    http://www.gutenberg.org/files/18567/18567-h/18567-h.htm"""
    def __init__(self):
        InterestingPermutations.__init__(self)
        self.peals={}
        self.makeRotateHalfs() # original and the rotation r that r*r=e. Alternate r1*r2=e if nelements==odd
        self.makeMirror() # original and miror
        self.makeFullRotations() # original and each rotation clockwise (0->n-1)
        self.makeFullMirrors() # sequences to fit overall sizes or not..
        self.makeOtherFullCycles() # generated by permutations with all elements while not a rotation or a mirror. # non-topological?
        self.canonicalPeal() # with the hunts, etc.
        self.transpositionsPeal(self.peals["rotation_peal"][1])
        self.TwentyAllOver() #
        self.anEightAndForty() #
    def transpositionsPeal(permutation,peal_name="transposition_peal"):
        self.peals[peal_name]=[sympy.combinatorics.Permutation(i) for i in permutation.transpositions()]


