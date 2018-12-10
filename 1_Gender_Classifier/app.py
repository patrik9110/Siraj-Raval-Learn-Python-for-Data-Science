from sklearn import tree

#[altura, peso, talla]
X = [[181,80,44], [177,70,43], [160,60,38], [154,54,37], [166,65,40], [190,90,47], [175,64,39], [177,70,40], [159,55,37], [171,75,42], [181,85,43]]

Y = ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'male', 'female', 'male']
#Los valores de Y estan asociados a los valores de X; el primer valor de X tiene las medidas del primer valor de Y

#El clasificador:
clf = tree.DecisionTreeClassifier()

clf = clf.fit(X, Y)

prediccion = clf.predict([[185, 65, 43]])
print(prediccion)
