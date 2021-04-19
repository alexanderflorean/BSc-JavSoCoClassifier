# Design 
* Chapter overview

* __Research questions (RQ)(section):__
(Will define RQ in introduction of background)
  * short text on how they are relevant to the work.
  * How they are used to guide the work
  * RQ's 
    * RQ 1. Is it possible to map architectural concerns through machine learning?  
    * RQ 2. Which input is most suitable for creating a classifier?
    * RQ 3. How large dataset is needed to create a satisfactory classifier?
    * RQ 4. Which of the chosen classifiers is the best one for the task?
    
* RQ:1 (subsection)
  * (1) Is it possible to map architectural concerns through machine learning?  
      * Answ: This will be answered by implementing the model

* RQ:2 (subsection)  
  * (2) Which input is most suitable for creating a classifier?  
    * Answ: Will experiment with different input by:  
        * Keep train size and other parameters static, change only pre-processing settings  
        * compare the different metrics to extract conclusions.   
          * Metrics: accuracy, precision, recall, f1-score, prediction probability   
        * To find the best input, take the methods from above and,   
          * compare the inputs against each other.  
        * Will also look at feature representation:  
          * This is done by comparing the Tf-idf against Bag of words   
            against each other.  
            
* RQ 3 (subsection)
  * (3) How large dataset is needed to create a satisfactory classifier?
    * Answ: We will look at how the metics changes in two cases  
      * Keep all parameters static except percentage/quantity size   
        * When we vary the percentage size of the training data   
          * Motivate, why is it relevant to look at the percentage?  
        * When we vary the quantity of training files for the dataset  
          * Motivate, why is it relevant to look at the number of files?  

* RQ 4 (subsection)
  * (4) Which of the chosen classifiers is the best one for the task?
      * what hyperparameters, limitations (not changing hyperparameters throughout the experiment) 
      * Overall look at previous tests
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
    * (Get reference for this) How large is a large, medium or small system? 
    * Note that the systems are relatively similar in size except for TeamMates  
      which is smaller in the sense of lines of code
      

