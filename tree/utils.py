import itertools

from nltk.tree import Tree


def find_np(tree):
    """
    Find  NP
    """
    nps = []
    for subtree in tree.subtrees(filter=lambda t: t.label() == 'NP'):
        nps.append(subtree)
    return nps


def generate_permutations(nps):
    """
    Generate NP phrases.
    """
    np_lists = []
    for np in nps:
        np_lists.append([child for child in np])
    permutations = []
    for np_permutation in itertools.product(*np_lists):
        permutation = tuple(np_permutation)
        new_tree = Tree('S', permutation)
        permutations.append(str(new_tree).replace("\n", ""))
    return permutations
