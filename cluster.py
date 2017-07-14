#coding=utf-8

from sklearn.cluster import KMeans

data_path = 'data/'

result_filepath = data_path + 'result.txt'

train_filepath = data_path + 'pheno_emaize.txt'

train_X = []
with open(train_filepath, 'r') as f:
    line = f.readline()
    splited_line = line.split('\t')
    while splited_line[0] == 'training':
        train_X.append( list( map( lambda x: float(x), splited_line[3:6]) ) )
        line = f.readline()
        splited_line = line.split('\t')

test_X = []
with open(result_filepath, 'r') as f:
    line = f.readline()
    while line:
        test_X.append( list( map( lambda x: float(x), line.split(' ')) ) )
        line = f.readline()

cluster = KMeans(n_clusters=3, random_state=170)
y_pred = cluster.fit_predict(train_X)
y_test = cluster.predict(test_X)

with open('result', 'w') as f:
    i = 1
    for y in y_pred:
        f.write( '\t'.join(['L%04d'%(i),str(y)]) )
        f.write('\n')
        i += 1
    for y in y_test:
        f.write( '\t'.join(['L%04d'%(i),str(y)+'\n']))
        i += 1

