#coding=utf-8

from sklearn.cluster import KMeans 
from sklearn.cluster import AgglomerativeClustering as AC
from sklearn.cluster import MeanShift
data_path = 'data/'

result_filepath = data_path + 'result.txt'

train_filepath = data_path + 'pheno_emaize.txt'

train_X = []
with open(train_filepath, 'r') as f:
    line = f.readline()
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
# kmeans cluster
cluster = KMeans(n_clusters=2, random_state=170)
y_pred = cluster.fit_predict(train_X)
y_test = cluster.predict(test_X)

# allomerative clustering
ac_cluster = AC(n_clusters=2)
t_ac = train_X[:]
t_ac.extend(test_X)
y_pred_ac = ac_cluster.fit_predict(t_ac)
# y_test_ac = ac_cluster.predict(test_X)

# MeanShift clustering
ms_cluster = MeanShift()
y_pred_ms = ms_cluster.fit_predict(t_ac)

def write_result(filename, test_set, predict_set):
	with open(filename, 'w') as f:
	    i = 1
	    for y in test_set:
	        f.write( '\t'.join(['L%04d'%(i),str(y)]) )
       		f.write('\n')
       		i += 1
	    for y in predict_set:
	        f.write( '\t'.join(['L%04d'%(i),str(y)+'\n']))
	        i += 1
write_result("result.txt", y_pred, y_test)
write_result("result_ac.txt", y_pred_ac, [])
write_result("result_ms.txt", y_pred_ms, [])