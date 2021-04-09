@staticmethod
def graphsearch(fringe, explored, istate, succ, goaltest):
    fringe.add_to_fringe(istate)
    while True:
        