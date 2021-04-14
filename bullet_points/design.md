# Design 

* __Research questions (RQ)(subsection):__
  1. Is it possible to map architectural concerns through machine learning?  
      * Answ: This will be answered by implementing the model


  __Sub-research questions:__  
  2. How does different input data affect the results?
      * Answ: Will experiment with different input by:
        * Keep train size and other parameters static, change only pre-processing settings 
        * compare the different metrics to extract conclusions.  
          * Metrics: accuracy, precision, recall, f1-score, prediction probability
        * To find the best input, take the methods from above and, 
          * compare the inputs against each other.
        * Will also check which feature representations works the best:
          * This is done by comparing the Tf-idf against Bag of words 
            against each other.
            
            
  3. How does different train size affect the results?
      * Answ: We will look at how the metics changes in two cases:
        * Keep all parameters static except percentage/quantity size
          * When we vary the percentage size of the training data
          * When we vary the quantity of training files for the dataset


  4. Which of the chosen classifiers is the best one for the task?
      * what hyperparameters, limitations (not changing hyperparameters throughout the experiment) 
      * Choose the best result from RQ 2, and everything else static
      * Comparision between metrics, F1 score, accuracy, prediction probabilites. 


* Subject systems (subsection):
    * Were provided with 3 open-sourced systems that already had their 
      software architectural concerns mapped.
      * Then we just need to find a way to import this information to our system
    * JabRef:
      * A cross-platform citation and reference management software.
      * Uses BibTeX and BibLatex
      * JabRef - Java, Alver, Batada, Reference
    * TEAMMATES:
      * A online Peer Feedback System for student team projects.
    * ProM:
      * Is a extensible framework for Process Mining which provides means for 
        analysis and monitoring of real-life processes.
    * Table figure (containing):
      * System names
      * version
      * lines of code
      * quantity of files
      * quantity of concerns

