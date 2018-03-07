def counting_sort(array, k, letter):
    bucket = [0]*k;
    sort = [None]*len(array);
    for wordHis in array:
        bucket[wordHis[1][letter]] += 1;
    for index in range(1,k):
        bucket[index] += bucket[index-1];
    for wordHis in reversed(array):
         sort[bucket[wordHis[1][letter]]-1] = wordHis;
         bucket[wordHis[1][letter]] -= 1;
    return sort;

def sort_anagrams(words):
    '''
    Sort anagrams to appear adjacent to each other in a returned list.
    Input:  list of strings which contain only lower-case letters
    Output: sorted list, with anagrams appearing consecutively
    '''
    histograms = [None]*len(words);
    k=0;
    for index in range(len(words)):
        letterArray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
        for letter in words[index]:
            letterArray[ord(letter)-97]+=1;
            if letterArray[ord(letter)-97] > k:
                k = letterArray[ord(letter)-97];
        histograms[index]=(words[index],letterArray);
    for letter in range(25,-1,-1):
        histograms = counting_sort(histograms, k+1, letter);
    for index in range(len(words)):
        words[index] = histograms[index][0]
    return words
