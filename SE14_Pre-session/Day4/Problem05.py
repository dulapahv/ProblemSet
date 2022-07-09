file, selected = input().split(' ')

with open(file, 'r') as f:
	base_pair = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
	data = f.readlines()
	index = 1
	for strand in data:
		nucleotide_count = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
		print(f'DNA Strand #{index}')
		flag = 0
		strand = strand.strip('\n').upper()
		compl = ""
		for nucleotide in strand:
			if nucleotide not in base_pair:
				if index != len(data):
					print('Invalid DNA\n')
				else:
					print('Invalid DNA')
				flag = 1
			else:
				compl += base_pair[nucleotide]
				nucleotide_count[nucleotide] += 1
		compl = compl[::-1]

		index += 1
		if flag == 1:
			continue

		print(f'Reverse Complement: {compl}')
		print(f'Frequency: ', end='')
		for key, value in nucleotide_count.items():
			if key != list(nucleotide_count.keys())[-1]:
				print(f'{key}={value}, ', end='')
			else:
				print(f'{key}={value}', end='')

		interested = 0
		for i in range(1, len(strand)):
			if strand[i - 1] == selected[0] and strand[i] == selected[1]:
				interested += 1
		if index - 1 != len(data):
			print(f'\nInterested Pair Count: {interested}\n')
		else:
			print(f'\nInterested Pair Count: {interested}')
