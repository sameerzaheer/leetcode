#!/usr/bin/python
import sys

class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength=1
        longestSofar=s[0]
        for i in range(0,len(s)):
            #check for an odd palindrome
            r = 1
            while (i-r >= 0) and (i+r < len(s)) and (s[i-r] == s[i+r]):
                r=r+1
            #check if palindrome was longest:
            r= r-1
            if (2*r+1 > maxLength):
                maxLength= 2*r+1
                longestSofar = s[i-r:i+r+1]
                #print(longestSofar + "   " + str(maxLength))
            #check for an even palindrome
            r = 1
            while (i-r+1 >= 0) and (i+r < len(s)) and (s[i-r+1] == s[i+r]):
                r=r+1
            #check if palindrome was longest:
            r= r-1
            if (2*r > maxLength):
                maxLength= 2*r
                longestSofar = s[i-r+1:i+r+1]
                #print(longestSofar + "   " + str(maxLength))

        return longestSofar


def main(argv):
    s = Solution()
    print (argv[0])
    print (s.longestPalindrome(argv[0]))

if __name__ == "__main__":
    main(sys.argv[1:])
