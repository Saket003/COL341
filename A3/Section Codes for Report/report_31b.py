import time
from TakeInput import take_input
from sklearn import tree
from confusion import confusion

#Input Set
train_path = "data/train"
feature_vector, output_vector = take_input(train_path,2000)
validation_path = "data/validation"
feature_val, output_val = take_input(validation_path,400)

'''Gini Index'''
begin = time.time()
clf = tree.DecisionTreeClassifier(criterion='gini',max_depth=10,min_samples_split=7,random_state=0)
clf.fit(feature_vector,output_vector)
end = time.time()
print(f"Time taken is {end - begin} seconds")

confusion(feature_vector,output_vector,clf)
confusion(feature_val,output_val,clf)

'''Information Gain'''
begin = time.time()
clf = tree.DecisionTreeClassifier(criterion='entropy',max_depth=10,min_samples_split=7,random_state=0) 
clf.fit(feature_vector,output_vector)
end = time.time()
print(f"Time taken is {end - begin} seconds")

confusion(feature_vector,output_vector,clf)
confusion(feature_val,output_val,clf)