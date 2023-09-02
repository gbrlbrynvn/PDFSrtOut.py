<h1>Python Script: Sort and Output PDF using .csv file</h1>

<h2>Description</h2>
I worked with a client that required me to go through thousands of PDFs, containing personal and insurance information of thousands of their clients. I was given a separate excel file containing the names of their clients and my task was to collect and cut all the sections for each person and combine those sections into a separate PDF file. I made this Python script to automate everything and saving hours of manual work.
<br />

<h2>Language and Libraries Used</h2>

- <b>Python</b>
- <b>PyPDF2</b>
- <b>pandas</b>

<h2>Environments Used </h2>

- <b>Visual Studio Code</b>

<h2>Script </h2>

- <b>[PDFSrtOut.py](https://github.com/gbrlbrynvn/PDFSrtOut.py/blob/main/PDFSrtOut.py)</b>


<h2>Program walk-through:</h2>

<p align="center">
Make sure the script, the main PDF file, and the .csv file containing the required information is in the same folder: <br/>
<img src="https://i.imgur.com/hlvz7lp.png" height="80%" width="80%"/>
<br />
<br />
Once you run the script, it will use the variables in NameFile.csv and read through the MainPDF file using said variables.  <br/>
It will generate the PDFs that contain the required information, until all the variables in NameFile.csv have been used:  <br/>
<img src="https://i.imgur.com/eD7DhoC.png" height="80%" width="80%"/>
<br />

<br />
<b>This project is easily configurable and scalable and may prove useful for a lot more situations.<br />
I'll definitely work on more Python scripts with real-world applications!</b>
</p>
