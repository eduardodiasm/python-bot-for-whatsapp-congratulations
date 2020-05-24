# Python bot to reply Whatsapp congratulations messages 

Are you tired of answering all those birthday messages via Whatsapp? Here is the solution to help you in this boring situations, this script will reply automatically all those messages!

### Tech

In this project, we are using:

* [Python3](https://www.python.org/)
* [Selenium](https://www.selenium.dev/)
* [Gecko driver](https://github.com/mozilla/geckodriver)


### Installing the dependecies

The list of dependecies used here are able on [requirements.txt](https://github.com/eduardodiasm/python-bot-for-whatsapp-congratulations/blob/master/requirements.txt)

Install the dependencies with pip

```sh
$ pip install -r requirements.txt 
```

### Installing the driver

To manipulate the browser through the script, you need a driver to do it. Here, we are using the Mozilla's Geckodriver. To install the geckodriver, you just have to install the binary file of it, named 'geckodriver.exe' and able in the repository root path.

### Instruction
To select the contacts that you want to reply automatically, you must put the contacts's names in the list people_names, on the line 10.
```python
10 | people_names = ['person one', 'person two']
```
### Run

To run the script, execute the codes below:
```sh
$ cd src
$ python script.py
```

Remember that you should be inside the repository path.


### Todos!

  - Find out a way to get the class copyable-text.selectable-text
  - Get as environment variables the contacts that you want the script reply.
  - Use the Whatsapp API in the script.
