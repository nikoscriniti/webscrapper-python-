# set up virtual enviroment:  python3 -m venv ai
# to go into virtual...: source ai/bin/activate 
# install dependencies: pip3 install 
'''

1. streamlit --> ui/frontend DOWNLOADED, very simiple python way to crate a UI, makes it easy to interact with LLMS
2. Selenium --> doing webscrappping --> selenium allows to automate a webbrower and grab all the information and pass it through an LLM (SOMETHHING LIKE CHAT GPT, thats where the other project comes from, going to create my own machine learning algorithm)
3. Langchain --> parsing (by using "ai") to search through the "ai" material 

'''


Definition of Virtual enviroment: 
- A virtual environment in Python is like having a separate, isolated workspace where you can install specific dependencies for a project without affecting other projects or your system-wide Python installation.
- You create an isolated workspace (a virtual environment) for each project.
- Inside this virtual environment, you can install exactly the dependencies you need, with the specific versions required.



Chrome Driver:
# downlaod for whatever operating system you have
# the version needs to match YOUR system (update chrome to newest version, and download newest verison) 
- https://googlechromelabs.github.io chrome-for-testing/#stable
# click [latest] stable
# if you have m2 chip mac download  mac-arm64


For Parsing 
- downlaod OLLAMA # this will be changed later to my own indivdual LLM
- 

Ollama (LLM):
- downlaod ollama (mac in this case): https://ollama.com/download
- open comand prompt, type: ollama 
- have to downlaod an ollmaa 3.1 (isnt too many gb): https://github.com/ollama/ollama)
- it will ask for a prompt (in terminal): ollama run llama3.1


Usage:
Run the Streamlit Web Scraper:

streamlit run webscrapper.py
Using the Interface:

1.  Enter a website URL in the provided text box.
2. Click "Scrape Site" to start scraping.
3. Expand "View DOM Content" to see the parsed content.
4. Modifying Parsing Logic:

- To adjust the content parsing logic, modify scraper.py and parse.py according to