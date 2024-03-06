# OpenScience
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10780485.svg)](https://doi.org/10.5281/zenodo.10780485)

## Description
Assesments for Artificial Intelligence And Open Science In Research Software Engineering
* **Assesment 1. Grobid Analysis with best practices:** Create a Gobrid client which will perform an analysis over 10 open-access articles. The program will:
  - Draw a keyword cloud based on the words found in the abstract of your papers.
  - Create a visualization showing the number of ﬁgures per article.
  - Create a list of the links found in each paper.

## Requirements
  * Python 3 (See [Python Downloads](https://www.python.org/downloads/) for instalation)
  * Docker (See [Docker Downloads](https://docs.docker.com/get-docker/) for instalation)
  * Grobid Server (See [Grobid Documentation](https://grobid.readthedocs.io/en/latest/Grobid-docker/) for more detailed instalation)
    * Full image instalation:  
    ```
    docker run --rm --gpus all --init --ulimit core=0 -p 8070:8070 grobid/grobid:0.8.0
    ```
    * Lightweight image instalation:
    ```
    docker run --rm --init --ulimit core=0 -p 8070:8070 lfoppiano/grobid:0.8.0
    ```
  * Grobid Python Client (See [Grobid Client Python Github](https://github.com/kermitt2/grobid_client_python/tree/master) for more detailed instalation)
    ```
    git clone https://github.com/kermitt2/grobid_client_python
    cd grobid_client_python
    python3 setup.py install
    ```

## Installation instructions
1. Clone this repository
    ```
    git clone https://github.com/jorgesaenzdemiera/OpenScience
    cd OpenScience
    ```
2. Create a Virtual Environment with all the required libraries
   ```
   python -m venv grobid
   
   # En Windows
   .\grobid\Scripts\activate
   # En macOS/Linux
   source grobid/bin/activate
   
   pip install -r requirements.txt
    ```

## Execution instructions
1. Include the articles you want to analyze in the input folder
2. Run the Grobid Server
3. Run the Grobid Client
4. Keep the necessary information of the Analysis (Output file will be removed after the next execution of the Client)

## Running example
See the example with [10 computer vision articles](https://github.com/jorgesaenzdemiera/OpenScience/tree/main/Assesment%201.%20Grobid%20Analysis/input) in the repository.

[Output after execution](https://github.com/jorgesaenzdemiera/OpenScience/tree/main/Assesment%201.%20Grobid%20Analysis/output) include:
  * An image featuring the word cloud generated from the abstract of each article processed with Grobid.
  * An histogram showing the number of figures per article.
  * A text file with all the links that appear in each one of the articles.

## Preferred citation
Use [CITATION.cff](https://github.com/jorgesaenzdemiera/OpenScience/blob/main/CITATION.cff)

