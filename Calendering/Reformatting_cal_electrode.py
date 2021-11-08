
path_Dried = r'Dried_electrode.atom'
with open(path_Dried, 'r') as p:
    lines = p.readlines()
    p.close()

number_atoms_safe = str(lines[3].split('\n')[0])
print(number_atoms_safe)

path_original = r'coord_out_electrode.data'
path_new = r'coord_out_electrode_safe.data'
new_file = open(path_new, 'a')
i = 0
with open(path_original, 'r') as f:
    for line in f.readlines():
        if i == 2:
            splitted_line = line.split(' ')
            if str(splitted_line[0]) == number_atoms_safe:
                new_line = line
                print('re-formatting not needed')
            if str(splitted_line[0]) != number_atoms_safe:
                print(str(splitted_line[0]))
                new_line = number_atoms_safe + ' ' + str(splitted_line[1])
                print('re-formatting needed')
        if i != 2:
            new_line = line
        new_file.write(new_line)
        i += 1
f.close()
new_file.close()