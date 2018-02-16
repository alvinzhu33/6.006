def find_peak_2D(A, r = None, w = None):
    '''
    Find a peak in a two dimensional array.
    Input: 2D integer array A, subarray indices r, witness w
    '''
    if r is None:
        r = (0, 0, len(A[0]) - 1, len(A) - 1)
    px, py, qx, qy = r  # A[py][px] upper left, A[qy][qx] lower right
    if w is None:
        w = (0, 0)
    wx, wy = w          # A[wy][wx] witness

    width = qx - px + 1;
    height = qy - py + 1;
#    print(height);
#    print(width);
    if height == 1 and width == 1:
        return(px, py);
    if (height ==2 and width == 1) or (height==1 and width==2):
#        print("He");
#        print(A[py][px]);
#        print(A[qy][qx]);
        if A[py][px] > A[qy][qx]:
#            print("First");
            return (px, py);
        else:
#            print("Second")
            return (qx, qy);

    #search vertically A[SEARCH][x]
    if width > height:
        center = (px+qx)//2;
#        print("center: ", center);
        witness = A[px][center]-1;
        for x in range(center-1, center+1):
            for y in range(py, qy+1):
                if A[y][x] > witness:
#                    print("Col", A[y][x]);
                    witness = A[y][x];
#                    print("Witness", witness);
                    w = (x, y);
#                    print(wx, wy);
#        w = (wx, wy);
#        print(w);
#        print();
#        print();
#        print();
        if w[0] == center:
#            print("Width", A[wy][wx]);
#            print(w);
            r = (w[0], py, qx, qy)
        elif w[0] == center - 1:
            r = (px, py, w[0], qy);
        else:
            r = (w[0], py, qx, qy)
        return(find_peak_2D(A, r))
    else:
        center = (py+qy)//2;
#        print("center: ", center -1, center, center +1);
        witness = A[center][px]-1;
        for y in range(center-1, center+1):
            for x in range(px, qx+1):
#                print(A[y][x]);
                if A[y][x] > witness:
#                    print("Row: ", A[y][x]);
                    witness = A[y][x];
                    w = (x, y);
#        print(w);
#        print();
#        print();
#        print();
        if w[1] == center:
#            print("Height", A[wy][wx]);
#            print(w);
            r = (px, w[1], qx, qy)
        elif w[1] == center - 1:
            r = (px, py, qx, w[1]);
        else:
            r = (px, w[1], qx, qy)
        return(find_peak_2D(A, r, w))

#    print("HELLO", A[wy][wx]);
    return w
#print(find_peak_2D(A));