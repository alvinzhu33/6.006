def convert_to_char(k):
    mod = k % 27
    if mod == 26:
        return ' '
    return chr(97 + mod)

def sort(A):
    if A[0] > A[1]:
        A[0],A[1] = A[1], A[0];
    if A[0] > A[2]:
        A[0],A[2] = A[2], A[0];
    if A[1] > A[2]:
        A[1],A[2] = A[2], A[1];
    return tuple(A);


def decode_message(sequence):
    '''
    Decode hidden message based on permutation of triples
    Input:  list of non-negative integers
    Output: string corresponding to hidden message
    '''
    values = {};
    secret = "";
    for index in range(2, len(sequence)):
        original = (sequence[index-2], sequence[index-1], sequence[index-0])
        order = sort([sequence[index-2], sequence[index-1], sequence[index-0]]);
        if order in values:
            if original not in values[order]:
                values[order].add(original);
                if len(values[order]) == 6:
                    secret += convert_to_char(original[0]+original[1]+original[2]);
        else:
            values[order] = {(original)};
    return(secret);
