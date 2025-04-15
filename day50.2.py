f =open('duck2.txt', 'w')
lines =['line 1\n', 'line2\n', 'line3\n']
f.writelines(lines)
f.close()