# NLP_Pdfparser
PDF parser with natural language processing

How to install:
1. Fork this repo
2. Install anaconda distribution: https://www.anaconda.com/products/distribution
     * Make sure you could run anaconda anvigator
     * Make sure you could run 'conda' command in anaconda prompt terminal of our computer
4. Import 'anaconda_env_yiming_pdfparser.yaml' and create a new conda environment via conda navigator
5. Install Pycharm and open this project:
     * select "open existing project" with this project
     * while loading project
     * Link your git account with pycharm: https://www.jetbrains.com/help/pycharm/set-up-a-git-repository.html#put-existing-project-under-Git
6. In Pycharm, Go to File -> Settings. Set up the Project Interpreter with the conda environemnt you just created on step 4
7. Go to org.yiming.configuration, Change the configuration based on your availability
     * FOLDER: folder with input files
     * FILE_NAMES: name of files to be parsed
     * OUTPUT_FOLDER: folder to hold output files
     * WORDS: words to be counted
     * PHRASES: phrases to be counted
7. Go to org.yiming.executor, then run executor.py
