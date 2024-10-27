# to test/run main fucntion:  streamlit run webscrapper.py

#step 1
# -- streamlit UI 
# to run the streamlit --> streamlit run webscrapper.py 
import streamlit as st
from scraper import scrape_website, extract_body_content, clean_body_content, split_dom_content
from parse import parse_with_ollama
st.title("WEBSCRAPPING")
url = st.text_input("Enter a website URL")

if st.button("Scrape Site"): 
    st.write("Scraping the website")
 
# step 2: actual webscrapping
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

   #store in session for streamlit
    st.session_state.dom_content = cleaned_content

    #expander to view more content (a button that will toggle what is shown in...)
    with st.expander("view dom content"):
        st.text_area("dom content", cleaned_content, height=300)

    
    ''' now assking the user what actual information they want from the site'''
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            # Parse the content with Ollama
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            st.write(parsed_result)