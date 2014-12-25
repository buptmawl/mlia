from numpy import *
import operator

def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels

def classfy0(inX, dataSet, labels, k):
	dataSetSize=dataSet.shape[0]
	diffMat=tile(inX,(dataSetSize,1))-dataSet
	sqDiffMat=diffMat**2
	sqDistances=sqDiffMat.sum(axis=1)
	sortEdIndex = sqDistances.argsort() #distance min 
	classCount={}
	for i in range(k):
		voteLabel=labels[sortEdIndex[i]]
		classCount[voteLabel] = classCount.get(voteLabel,0)+1

	sortedClassCount=sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]

trainset,labels=createDataSet()
#print trainset,labels
inData = array([0,1])
result = classfy0(inData, trainset, labels,2)
print "input is " 
print inData 
print "retsult: " + result

