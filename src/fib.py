def fibFunction(n):
    print 'n =', n
    if n > 1:
        return n * fibFunction(n - 1)
    else:
        print 'enf of the line'
        return 1
    
    