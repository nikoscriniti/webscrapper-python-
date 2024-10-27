''' Parse using large langague modul (this will be changed to homegrown machinelearning algoritm)'''

# running it locally
from langchain_ollama import OllamaLLM # langchain allows for connecting LLM to code
from langchain_core.prompts import ChatPromptTemplate

# two variables within the tmeplate (dom content and parse_description)
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

model = OllamaLLM(model="llama3")


def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template) # passs template that is written
    chain = prompt | model # pipe it (remember from bash)

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1): # i is starting at 1, so dont need to add 1 at the end when printing out info
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
            # the dom content which is equal to the chunck (one chunk being passed at a time)
        )
        print(f"Parsed batch: {i} of {len(dom_chunks)}") # how many chunks are being parsed (JUST FOR TEST)
        parsed_results.append(response)

    return "\n".join(parsed_results)

