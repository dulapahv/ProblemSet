def LCS(s1, s2):
   temp = []
   for i in range(len(s1)):
       j = len(s1)
       while (j > 0):
           if s1[i:j] in s2:
               if len(temp) <= len(s1[i:j]):
                   temp = s1[i:j]
           j -= 1
   return temp