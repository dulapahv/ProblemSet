A = [i*2 for i in range(95,110,2) if len(str(i))>2]
print(len(A))

text = "AAAAABBB"
A = [i+3 for i in text if i=="a"]
print(len(A))

A = [i-5 for i in range(1,5)]
print(len(A))

A = [i/2 for i in range(1,19) if i%3 == 0]
print(len(A))