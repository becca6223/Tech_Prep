def lengthOfLongestSubstring(s):
        #There is a better way of implementing it
        """
        :type s: str
        :rtype: int
        """
        cur_str = ""
        max_length = 0 #original max length is 0
        start_pos = 0 #the starting position of the current longest substring 
        
        for loc, cur_char in enumerate(s):
            if cur_char not in cur_str:
                cur_str += cur_char 
            else: 
                rep_char_pos = cur_str.find(cur_char)
                cur_length = len(cur_str)
                max_length = cur_length if cur_length > max_length else max_length 
                cur_str += cur_char
                cur_str = cur_str[rep_char_pos + 1:] 
        
        final_len = len(cur_str)        
        return max_length if max_length > final_len else final_len

if __name__ == "__main__":
    s = ""
    length = lengthOfLongestSubstring(s)
    print(length)