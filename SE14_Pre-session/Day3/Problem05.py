no = [str(k) for k in range(10)]
alpha = [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

def text2keys(text):
	text_samp = text.lower()
	key_out = []
	for ch in text_samp:
		for gr in alpha:
			if ch in gr:
				key_out.append(str(alpha.index(gr)) * (gr.index(ch) + 1))
	out = " ".join(key_out)
	return out

def keys2text(keys):
	chars = keys.split()
	out = ''
	for c in chars:
		l = int(c[0])
		p = len(c)
		out += alpha[l][p-1]
	return out

exec(input().strip())