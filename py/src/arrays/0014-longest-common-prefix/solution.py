from typing import List

class Solution:
    def min_len_word(pos_word: int, strs: List[str]) -> int:
        # Safety first, check if the list is empty
        # If it is, we can return 0 as there are no words to compare
        # This prevents any index errors when trying to access elements in an empty list
        # For examble, IndexError: list index out of range if we try to access strs[0] when strs is empty
        if not strs:
            return 0

        min_len_word = len(strs[0])

        while pos_word < len(strs) - 1:
            if len(strs[pos_word + 1]) < min_len_word:
                min_len_word = len(strs[pos_word + 1])
            pos_word += 1

        return min_len_word

    def longest_common_prefix(self, strs: List[str]) -> str:
        # Safety first, check if the list is empty
        # If it is, we can return an empty string as there are no words to compare
        # This prevents any index errors when trying to access elements in an empty list
        # For example, IndexError: list index out of range if we try to access strs[0] when strs is empty
        if not strs:
            return ""
    
        first_word = strs[0]

        if len(strs) == 1:
            return strs[0]

        prefix_cmn_long: List[str] = []
         
        min_len_word = Solution.min_len_word(0, strs)

        # If the minimum length word is 0, it means at least one of the strings is empty
        # For example, strs = ["flower", "", "flight"]
        # In this case, the longest common prefix is also an empty string
        if min_len_word == 0:
            return ""
        
        pos_char = 0
        first_word = strs[0]
        # Outer loop: We need to compare characters at the same position across all words
        while pos_char < min_len_word:
            pos_word = 0
            # Inner Loop: We need to compare the character at pos_char across all words
            while pos_word < len(strs) - 1:

                current_word = strs[pos_word]
                next_word = strs[pos_word + 1]

                # If mismatch at first char => "", else return what we built
                if current_word[pos_char] != next_word[pos_char]:
                    return "".join(prefix_cmn_long)
                pos_word += 1
    
            # If we got here, char matches across all words for this position
            prefix_cmn_long.append(first_word[pos_char])
            pos_char += 1

        return "".join(prefix_cmn_long)
    

strs = ["flower","flow","flight"]
print(Solution().longest_common_prefix(strs))