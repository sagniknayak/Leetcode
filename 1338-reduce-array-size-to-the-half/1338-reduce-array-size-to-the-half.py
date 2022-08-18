import math
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr_freq = dict()
        for val in arr:
            arr_freq[val] = arr_freq.get(val, 0) + 1
        print(arr_freq)
        freq_as_key = list(arr_freq.values())
        uniq_freq = dict()
        for val in freq_as_key:
            uniq_freq[val] = uniq_freq.get(val,0) + 1
        half = len(arr)/2
        total = 0
        uniq=list(uniq_freq.keys())
        uniq.sort(reverse=True)
        for freq in uniq:
            if half >= uniq_freq[freq]*freq:
                half -= freq*uniq_freq[freq]
                total += uniq_freq[freq]
            else:
                total += math.ceil(half/freq)
                break
        return int(total)
                
                
        