# Webscraping-Amazon-with-Python
Webscraping the Amazon website using beautifulsoup, requests and xlwt libraries with Python language to receive the products's name and price.

## How it works?

First of all, you have to download the following libraries:

``` pip install pip ```

(*pip* is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes.)

```pip install beautifulsoup4```

(*Beautiful Soup* is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.)

``` pip install requests```

(*Requests* allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method!)

```pip install xlwt```

(This is a library for developers to use to generate spreadsheet files compatible with Microsoft Excel versions 95 to 2003.)

```pip install selenium```

(The *selenium* package is used to automate web browser interaction from Python.)

### After finish the instalation of the libraries ### 

You'll open the project package and open the *principal.py* class (it is the main class of the project where you can run and see the magic happen!)

**The classes**

	- principal.py
		where the project runs;

	- pesquisa.py
		where the pesquisa.py class archive will inherit the amazon.py and will work together the selenium, 
	requests and sys libraries for the treatment of methods;
	
	- amazon.py
		it will use the bs4 from BeautifulSoup librarie to scrap the Amazon website to search for the product,
	 getting the name and price and calling the .tabelaEstrutura() and
	 .salvarTabela() methods inherited from Excel class;
		
	- excel.py
		Here it where the table, name, font-style, insert data and save
	 file methods and creations are, using the xlwt library.


## Some advices ##

In the pesquisa.py in the constructor of the Pesquisa class (specific at the line 9) you have to specify the webdrive you will use. I'm using the chromedriver, but you can choice others webdrivers that you have to make it works, you only need to specify the path where your webdrive is in.

At the line 10 of the class Pesquisa you can see the brazilian address of the Amazon. If you want to change it to the USA version, feel free, but I don't know if it will work, cause the structure of the both websites are differents.

At the line 11 of the principal.py file you can change the name of the archive that will be created after the finish of the operation, the current name file is produto2, you can change it to have more files.

	produto2 >>> produto3 or any name you want.

## And now... ##

If you have some tips or questions to ask me, just send me an email at: dan004.dj@gmail.com

I'll feel happy if you can give me some feedback or help to improve this project.

	~See you soon on the white side of the moon.~
