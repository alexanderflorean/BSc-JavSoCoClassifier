# BSc-project structure 

#### Notes
* think as being in the readers shoes

# Introduction (~5p)
* Project goal 
  * Research questions
* Project motivation
* Expected results
* Summary of results 
* Ethics
* Work split
* The dissertation layout

# Background (~10p)
(relevant background info)
* ML:
  * overview of ML
  * ML text classification
* necessary steps for creating a classifier
  * Collection of data
  * preprocessing of data 
    * input selection (parsing, NLP)  
      * relevant information to extract
    * feature representation
  * Training Classifiers 
    * Naive Bayes
    * Support Vector Machines
    * MaxEnt
  * Evaluation  
    * Metrics, explain the metrics
      * Precision
      * Accuracy
      * Recall
      * Confusion Matrix
      * Classification report
  * Testing

* Chapter summary
 
# Design (~15p)
* Tools used, and motivation behind the choices
* Programs that will be used for this lab, and motivation for them 
  * jabref
  * prom
  * teammates
* approach, on how we designed our workflow  
  * jupyter
    * motivation
  * scripts
  * folders/structures
* The steps
  * Collection of data 
    * Method & structure of collecting the data
    * reasoning
  * Pre-processing
    * Extracting information
    * Parsing
      * NLP
      * Regular expression
    * Feature representation
      * CountVector
      * TfidVector
  * Training models
    * parameters
      * Stratified k-fold
      * Absolute size test sample
    * Classifiers
      * Naive-Bayes
      * MaxEnt
      * SVM
  * Model evaluation
  * Model testing
* Chapter summary

# Implementation (~15p)
(show implementation)
* Collection of data 
  * Method & structure of collecting the data
  * reasoning
* Pre-processing
  * Extracting information (GatherData.py)
  * Parsing (Preprocess.py)
    * NLP
    * Regular expression
    * Feature representation
      * CountVector
      * Tf-idf
* Training models
  * parameters
    * Stratified k-fold
    * Absolute size test sample
  * Classifiers
    * Naive-Bayes
    * MaxEnt
    * SVM
* Model evaluation
* Model testing
* the actual testing

* Chapter summary

# Results/Evaluation (~10p)
* Summarise main results
* Give details of the results
  * Pre-processing 
    * feature representation
    * systems 
      * jabref
      * teammates
      * prom
  * Train size, percentage
    * systems 
      * jabref
      * teammates
      * prom
  * Train size, number of files
    * systems 
      * jabref
      * teammates
      * prom
  * Classifier, summarise classifier results
* Implementation evaluation (expected vs actual results)
* Chapter summary

# Conclusion (~5p)
* conclusion
* project evaluation
* problems, how would you do this next time?
* Limitations of the project
* Future work
* Concluding remarks

----
* References
* Appendices
