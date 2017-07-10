fname = 'out'

id2features_map = {}

for i in range(6210):
    id2features_map['L%04d' % (i+1)] = []

with open(fname, 'r') as f:
    l = 0
    while 1:
        print('Proccessing %d line' %(l))
        l += 1
        line = f.readline()
        if not line:
            break
        features = line.split(' ')
        if len(features) < 6210:
            continue
        for i in range(6210):
            id2features_map['L%04d' % (i+1)].append(features[i])

    with open('features', 'w') as o:
        for k, v in id2features_map.items():
            o.write(k + ' ' + ' '.join(v))