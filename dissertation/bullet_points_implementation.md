# Implementation

* Workflow layout
    * Figure that connects all used scripts and shows the workflows structure
	* Shows how jupyter calls upon scripts 
	* Explain the figure, why we use jupyter to connect the scripts together. 
* Tools and frameworks
    * Tools: 
        * Scikit-learn tools 
        * jupyter lab 
        * NLTK 
        * matplotlib 
        * pandas 
        (Short description and motivation behind use of them)
	* Environment (jupyter lab)
            * Describe how we integrate our scripts into jupyter notebooks. 
            * Benefits: 
                * Visualize the outcome 
                * easy to modify tests
* Collection of data
  * Need to import the mapping information to a table
    * This is done in 2 parts:
      1. preparing the files in a folder structure:
        * Folder for the system:
        * In the system folder, create a folder for each concern and name  
          it according to said concern.
        * Put the files into the concern-folders according to the concern 
          that they belong to. 
      2. reading the files and add them to a dataframe with the columns:
        * "FileName"
        * "Label", which is the concern the file is given that will become 
          the label for the classifier
        * "FileContent", the source code 
* Pre-process
    * Extracting information:
      * How the extractions are done 
        * regular expressions
    * Parser:
      * how the parsing works
      * java keywords and annotations
    * Pre-process 
      * The constructor parameters and the expected output
      * Doesnt change the structure of the table
      * the design of the pre-process settings

* Testing classifiers
	* We use 2 files for this, Evalutaion.py and Testing.py, explain how they are connected
	* specify what we base our tests on ( the pre-processed csv file and training sizes)
	* How we split the data into test and train samples (already written(DRAFT))
	* Classifiers ( What hyperparameters are set, what they stand for (for instance naive bayes alpha value etc..
		       ( and why we do not change them throughout the experiment (keep them static))
	* Model evalutation ( 1. Train the classifier with the training data, and test with test data.
			    ( 2. Metric object is saved with all the relevant metrics (F1 score, confusion matrix, ..),
 
	* Comparision ( After the test, compare the metrics, we integrated to jupyter lab
		      ( Graphical representation with matplotlib) 
		
					
