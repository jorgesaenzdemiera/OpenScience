# How problem is solved
We want to  perform an analysis over 10 open-access articles using Grobid. We have the following objectives:
* Draw a keyword cloud based on the abstract information
* Create a visualization showing the number of figures per article
* Create a list of the links found in each paper

The first step followed consists in convert the input PDFs in XML files using Grobid, in this way, we can analyze them from python
For the **Draw a keyword cloud based on the abstract information** objective, we get the abstract of each article by finding the "abstract" tag in the XML. Then, we create a wordcloud image of the abstract using the Wordcloud library.
For the **Create a visualization showing the number of figures per article** objective, we count the number of figures of each article by finding the "figure" tag in the XML. Then, we create an histogram image showing the number of figures per article.
For the **Create a list of the links found in each paper** objective, we get all the links that appear in the XML text by finding text elements complying with the regular expression that stays only with texts starting with "https//". Then, the links are saved in a text file in which each line is a link.