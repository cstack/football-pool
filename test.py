from sklearn import svm
from sklearn import datasets
import pickle
import os.path

fname = 'models/test.model'
if not os.path.exists(os.path.dirname(fname)):
  print "Making models/ directory"
  os.makedirs(os.path.dirname(fname))

print "Loading dataset"
iris = datasets.load_iris()
X, y = iris.data, iris.target

if os.path.isfile(fname):
  print "Loading existing model"
  clf = pickle.load(open(fname))
else:
  print "Training new model"
  clf = svm.SVC()
  clf.fit(X, y)

  print "Saving model"
  pickle.dump(clf, open(fname, 'wb'))

print "Predicting"
prediction = clf.predict(X)

print prediction