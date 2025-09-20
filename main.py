import os
import logging
import json
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

# Settings
load_dotenv()
PDF_FOLDER = "10k_pdf"
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_and_parse_pdfs(folder):
    all_docs = []
    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            path = os.path.join(folder, filename)
            logging.info(f"Parsing PDF: {filename}")
            loader = PyPDFLoader(path)
            docs = loader.load()
            all_docs.extend(docs)
    logging.info(f"Total documents loaded: {len(all_docs)}")
    return all_docs

def main():
    docs = load_and_parse_pdfs(PDF_FOLDER)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
    retriever = vectorstore.as_retriever()

    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer "
        "the question. If you don't know the answer, say that you "
        "don't know. Use three sentences maximum and keep the "
        "answer concise."
        "\n\n"
        "{context}"
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )

    # getting LLM 
    llm=ChatGroq(groq_api_key=os.environ['groq_api_key'],model_name="openai/gpt-oss-120b")

    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    print("Type 'q' to exit.")
    while True:
        query = input("\nEnter your question: ").strip()
        if query.lower() == 'q':
            print("Exiting.")
            break
        answer = rag_chain.invoke({"input": query})
        print(f"\nAnswer:\n{answer} ")
        # print(json.dumps(answer, indent=2))


if __name__ == "__main__":
    main()

