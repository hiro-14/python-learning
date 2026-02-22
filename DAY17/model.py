from sklearn.metrics import precision_score, recall_score, confusion_matrix

# 予測
y_pred = model.predict(X_test)

# 混同行列
cm = confusison_metrix(y_test, y_pred)
print("confusion Matrix:\n", cm)

# precision
precision = pricision_score(y_test, y_pred)
print("Pricison:", precision)

# recall
recall = recall_score(y_test, y_pred)
print("Recall:", recall)
