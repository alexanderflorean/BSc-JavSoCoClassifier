# BSc-project structure 

# Introduction (~5p)
* Project motivation
* Project goal 
  * Research questions
* Optional: Expected results
* Summary of results 
* Ethics, impact on the society 
  * Generalization can open the doors towards profiling and discrimination
  * Impact on workforce, e.g. makes the dev. Easier for developers?
* Work split 
  * Be clear on who has responsibility on which part, should sum up to 50-50%
  * separation of work
  * (do this later on )
  * have a internal table for this 
* The dissertation layout

# Background (~15-20p)
* Software architecture 
  * overview
  * related work (other works that try the similar mapping)
* ML:
  * overview of ML
  * ML text classification
    * necessary steps for creating a classifier
      * Collection of data
      * data cleaning (look at book Sebastian referenced)
      * preprocessing of data 
        * input selection (parsing, NLP)  
        * feature representation
      * Training Classifiers 
        * (if over 10-15p, keep this short)
        * Naive Bayes 
        * Support Vector Machines
        * MaxEnt
      * Evaluation/Testing
        * k-fold cross validation 
        * Metrics, explain the metrics
          * Precision
          * Accuracy
          * Recall
          * Confusion Matrix
          * Classification report
* Optional: Chapter summary
 
# Experiment design (~15p)
The design of how we are gonna find the answers to the research questions.
(should explain how we collected data, and pre-process)

* Go into detail of the research questions
* Tools used, and motivation behind the choices:
  * jupyter, scikit-learn, et.c.
* Programs that will be used for this lab, and motivation for them 
  * jabref, prom, teammates
* Pre-processing:
  * How we will evaluate the different inputs, and find the better inputs
* Feature representation?, motivate the choice between
      * CountVector or TfidVector?
* Train size evaluation:
  * how we will test which is the optimal train size for the model
* Classifiers:
  * Motivation behind choice of classifiers
  * how we will find the better classifier
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
E.g.:
  * "Findings regarding Research question 1 ... "
* Summarise main results
* Give details of the results
  * Pre-processing 
    * feature representation
    * systems ?
      * Jabref?
      * Teammates?
      * Prom?
  * Train size, percentage
    * systems ?
      * jabref?
      * Teammates?
      * Prom?
  * Train size, number of files
    * systems ?
      * Jabref?
      * Teammates?
      * Prom?
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
