def area_of_intersection(blx1, bly1, trx1, try1, blx2, bly2, trx2, try2):
    if(blx1 >= trx2) or (trx1 <= blx2) or (bly1 >= try2) or (try1 <= bly2):
        return 0
    else:
        try:
            return(max(blx1, blx2) - min(trx1, trx2))*(max(bly1,bly2) - min(try1,try2))
        except OverflowError:
            return -1

##======================================
print(str(area_of_intersection(0,2,5,10,3,1,20,15)))
