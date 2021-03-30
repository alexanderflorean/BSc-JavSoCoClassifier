# BSc-project structure
#### Notes
* think as being in the readers shoes

# Introduction (~5p)
  * Project goal 
    * Research questions
  * Project motivation
  * Overview
  * Expected results
  * Summary of results
  * Ethics?
  * The dissertation layout

# Background (~10p)
  * The context of the research,  
(relevant background info)
  * ML:
    * overview of ML
    * ML text classification
  * Pre-processing (belongs in methods?)
    * Java syntax
    * NLP techniques
    * Regular expression
  * Feature representation (not go into specifics?)
    * Bag-of-words (belongs in methods?)
    * Tf-idf (belongs in methods?)
  * Classifiers
    * Naive-Bayes
    * MaxEntropy
    * Support Vector Machine
  * Evaluation, (optional move to methods, depending on flow)
    * K-fold validation
    * Metrics, what they mean, and why use them.
      * Precision
      * Accuracy
      * Recall
      * Confusion Matrix
      * Classification report
  * Programs that will be used for this lab, and motivation for them 
    * jabref
    * prom
    * teammates

# Method (~30p)
Describe in more detail the objective, e.g. that we compare different classifier
Design & implementations

* Collection of data 
  * Method
  * structure
  * Systems
    * Jabref
    * TEAMMATE
    * ProM
* Data extractor
  * Extraction options
  * Parse
    * NLP
    * Regular expression
* Feature vector
  * CountVector (sklearn)
  * TfidVector (sklearn)
* Training
  * Stratified k-fold
  * Absolute test sample
  * Naive-Bayes
  * MaxEnt
  * SVM
* Evaluation

# Results/Evaluation (~10p)
* more on the numbers and the interpretaion of the results

# Discussions

# Conclusion (~5p)

* References
* Appendices
