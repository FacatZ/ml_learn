'''
{'AT': '0', 'AA': '1', 'TT': '2', 'AG': '3', 'GG': '4', 'TG': '5', 'GA': '6', 'G
C': '7', 'CC': '8', 'CG': '9', 'TC': '10', 'TA': '11', 'CT': '12', 'GT': '13', '
CA': '14', 'AC': '15'}
'''

fname_base = 'chr{0}_emaize.genoMat'
counter = 10000

snp2int_map = {}
snp_list = []
snp_counter = 0

with open('out', 'w') as o:
    
    for i in range(1, 11):
        fname = fname_base.format(i)
        c = 0
        print('Processing file %s' % (fname))
        with open(fname, 'r') as f:
            line = f.readline()
            while 1:
                line = f.readline()
                c += 1
                if not line or c >=  counter:
                    break
                snp_l = line.split('\t')
                snp_l[-1] = snp_l[-1].replace('\n', '')
                snp = snp_l[1]
                if snp not in snp_list:
                    snp_list.append(snp)
                    l = snp[0]
                    r = snp[2]
                    if l+r not in snp2int_map:
                        snp2int_map[l+r] = str(snp_counter)
                        snp_counter += 1
                    if l+l not in snp2int_map:
                        snp2int_map[l+l] = str(snp_counter)
                        snp_counter += 1
                    if r+r not in snp2int_map:
                        snp2int_map[r+r] = str(snp_counter)
                        snp_counter += 1
                snp_ll = map(lambda x: snp2int_map[x], snp_l[4:])
                o.write(' '.join(list(snp_ll))+'\n')
print(snp2int_map)

