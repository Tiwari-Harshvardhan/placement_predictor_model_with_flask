install anaconda
spyder is one of the tools on which we can make our ml models but a better alternative to spyder is jupyter notebook
we can run code as well as use the markdown feature of the notebook to type comments and headings etc
to run a cell press shift+enter
markdown is a way of writing text; if we use a single hashtag then a first level heading is created, if we use two hashtags, then second level heading/subheading is created
without any hashtag a paragraph type will be created and we can also use html, using which we can add videos and images
<p style="color:red"> Hello</p>
so hello in red color would be printed
so we can run code cell by cell and write a shitload of markdown to describe that code
we can also embed widgets like buttons and all 
importing datasets into the jupyter notebook:
download dataset from kaggle and then in the folder where we created our jupyter notebook open the notebook and select the upload option and select the downloaded dataset from kaggle
import pandas as pd
pd.read_csv('#the path of the dataset. since both the dataset and the file are in the same folder we will simply paste the name of the data set here')
df=pandas.read_csv('aug_train.csv')
