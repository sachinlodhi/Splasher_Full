# Splasher
> Python script to download and set wallpapers on windows from Unsplash
<hr>

### Table of Content

- **What**
- **Why**
- **How**
- **Usage**
- **Constraints**
---

### _What?_
This is a simple script written in Python to download the wallpapers of desired resolution and set as 
background on _Windows(32bit/64bit)_.

### _Why?_
I have been literally fascinated with customization of the
desktop environment and one day I have been looking for the automatic wallpaper changer for _Windows_.
After exploring many options I could conclude that none of the options I tried were _free_ or they had some 
different kind of limitations.
So I decided to write a simple python script which would allow user to select the type of the wallpaper 
from the one of the biggest library of the photos i.e. _UNSPLASH_.

[Check _Unsplash_ here](https://www.Unsplash.com "Unsplash")

![Unsplash](https://unsplash.com/favicon.ico "Unsplash")
***
### _How?_

When I was exploring the idea to build something on my own then I search for _Unsplash API_ though I did not get 
exactly _API_ for fetching wallpapers from _Unsplash_ but I found _Source_ which is built for small and low-traffic applications.
Some use case scenario of _Source_ is as follows:

- _Getting Random photo from specific **User**_
  
  
***Parameters***
```http request
https://source.unsplash.com/user/{USERNAME}
```
***Example***
```http request
https://source.unsplash.com/user/erondu/1600x900
```

- _Getting Random photo from **Collection**_
  
  
***Parameters***
```http request
https://source.unsplash.com/collection/{COLLECTION ID}
```
***Example***
```http request
https://source.unsplash.com/collection/190727/1600x900
```

- _Getting Photo from **Random Search Term**_
  
  
***Parameters***
```http request
https://source.unsplash.com/featured/?{KEYWORD},{KEYWORD}
```
***Example***
```http request
https://source.unsplash.com/1600x900/?california,USA
```
*_**Optionally, to specify a size, place it after the base URL.**_

>Read more about **Source** [here](https://source.unsplash.com/ "Source")

There were many more use cases but I employed last two depicted ones:
1. From a random source With Search Terms
2. From Random Collection ID


***


### _Usage_

1. Download the Zip file from the [repository](https://github.com/sachinlodhi/Splasher) or clone the repository using 
following command in command prompt. _Make Sure Git is installed_.
   
```commandline
git clone https://github.com/sachinlodhi/Splasher.git
```

2. Extract the downloaded zip file to your desired location.
3. Open command prompt at the same location where you just extracted the zip file.
4. Now type the following command in command prompt:
```commandline
pip install -r requirements.txt
```

5. Once requirements are installed type the command according to the following usage syntax:
- For using Random mode with tags
```commandline
python [-s random] [-i Seconds OPTIONAL] [-t1 Tag1 OPTIONAL] [-t2 Tag2 OPTIONAL] [-r Resolution OPTIONAL] [-v Verbosity Optional] 
```

- _Example_
  
```python -s random -i 60 -t1 california -t2 USA -r 1920*1080 -v ON```

- For using Random mode with Collection ID
```commandline
python [-s collection] [-i Seconds OPTIONAL] [-c_id CollectionId Optional] [-r Resolution OPTIONAL] [-v Verbosity Optional] 
```
- _Example_
  
```python -s collection -c_id 19542 -r 1920*1080 -v ON```


### _Constraints_
The limit of requests that can be sent to the **Source** is 50 requests (MAX) per hour.
So set the time interval keeping that in mind so that the request limit is not
exceeded. 
- Limit exceeding may lead to the blocking of IP by Unplash Server. 
