cat /etc/passwd | grep -v "#" | sed -n 'n;p' | cut -f 1 -d : | rev | sort -r | tr "\n" "," | sed 's/, */, /g' | sed 's/, $/./'
