```r
create_folds <- function(data, k) {
  data <- as.data.frame(data)
  set.seed(12)
  indices <- sample(seq_len(nrow(data)))
  folds <- split(indices, cut(seq_along(indices), breaks = k, labels = FALSE))
  names(folds) <- paste0("Fold", seq_len(k))
  return(folds)
}

cross_validation <- function(data, k) {
  folds <- create_folds(data, k)
  
  metrics <- data.frame(Accuracy = numeric(k), Precision = numeric(k), Sensitivity = numeric(k), Specificity = numeric(k))
  
  for (i in seq_along(folds)) {
    test_indices <- folds[[i]]
    train_indices <- setdiff(seq_len(nrow(data)), test_indices)
    
    train_data <- data[train_indices, ]
    test_data <- data[test_indices, ]
    
    
    model <- rpart(inclinacion_peligrosa ~ ., data = train_data, method = "class")
    predictions <- predict(model, test_data, type = "class")
    
    confusion <- confusionMatrix(predictions, test_data$inclinacion_peligrosa)
    
    metrics$Accuracy[i] <- confusion$overall["Accuracy"]
    metrics$Precision[i] <- confusion$byClass["Pos Pred Value"]
    metrics$Sensitivity[i] <- confusion$byClass["Sensitivity"]
    metrics$Specificity[i] <- confusion$byClass["Specificity"]
  }
  
  results <- data.frame(
    Metric = c("Accuracy", "Precision", "Sensitivity", "Specificity"),
    Mean = colMeans(metrics),
    SD = apply(metrics, 2, sd)
  )
  
  return(results)
}
```


| Métrica     | Media  | Desviación Estándar |
|-------------|--------|---------------------|
| **Accuracy**   | 0.78   | 0.05                |
| **Precision**  | 0.00   | 0.00                |
| **Sensitivity**| NA   | NA               |
| **Specificity**| 0.75   | 0.02                |