# Financial QA Agent with RAG Pipeline

This project implements a Retrieval-Augmented Generation (RAG) pipeline with agentic capabilities to answer simple and complex financial questions about Google, Microsoft, and NVIDIA using their SEC 10-K filings. It leverages LangChain, Chroma, HuggingFace models, and Groq LLM for multi-step reasoning and query decomposition.[file:1]

---

## Overview

- **Purpose:**  
  Quickly answer both simple and comparative financial queries on major tech companies by extracting and synthesizing information from their recent 10-K filings.[file:1]
- **Core technologies:**  
  Python, LangChain, ChromaDB, HuggingFace Embeddings, Groq LLM[file:1]

---

## Architecture Diagram

System architecture of the Financial QA RAG pipeline:

[generated_image:2]

---

## Features

- End-to-end vector-based RAG pipeline over PDF documents[file:1]
- Chunking, embedding, and retrieval optimized for financial filings[file:1]
- Agentic system for query decomposition and multi-step retrieval[file:1]
- JSON output with sources for all answers[file:1]
- CLI-based user interaction[file:1]
- Easily extendable for other filings or companies[file:1]

---

## Assignment Scope

This project was built as part of an AI Engineering assignment. The scope includes:[file:1]

- Companies: Google, Microsoft, NVIDIA
- Documents: 2022, 2023, 2024 10-K filings
- Query types: Direct metrics, year-over-year comparisons, cross-company analysis, and comparative multi-aspect analysis

---

## Pipeline Details

- **Parsing & Chunking:**  
  10-K filings are parsed using `PyPDFLoader` and chunked (1000/200 tokens) with `RecursiveCharacterTextSplitter`[file:1]
- **Embedding:**  
  Uses `sentence-transformers/all-MiniLM-L6-v2` via HuggingFace
- **Vector Store:**  
  ChromaDB stores all document vectors and provides top-k retrieval
- **Agent & Query Engine:**  
  Groq's LLM (`gpt-oss-120b`) plus custom system prompts enable multi-step reasoning, sub-query orchestration, and answer synthesis
- **Output format:**  
  Answers are concise, sourced from filings, and output as JSON

---

## Requirements

- Python 3.9+
- pip dependencies (see `requirements.txt`):  
  - langchain, langchain_huggingface, chromadb, langchain_groq, python-dotenv, etc.
- Groq API key for LLM endpoint
- 10-K PDFs downloaded in the `10k_pdf/` folder

---

## Quickstart


---

## How to Run the Project Step-by-Step

1. **Install dependencies:**  
   All Python dependencies are listed in `requirements.txt`. Make sure your Python version is 3.9 or newer.

2. **Prepare the data:**  
   Already downloaded in `10k_pdf`.

3. **API Key setup:**  
   Obtain your Groq API key and create a `.env` file in the root of the project with the contents:
   `groq_api_key=YOUR_GROQ_API_KEY`

4. **Start the pipeline:**  
    Run the main script using: `python main.py`

5. **Ask Questions:**  
    When prompted, type your financial question about any of the three companies' filings (for example:  
    - "What was Microsoft's total revenue in 2023?"  
    - "Compare cloud revenue growth between Google and Microsoft in 2022 and 2023."  
    )  
    The system will respond with a concise, sourced answer from the filings.

6. **Exit:**  
    Type `q` and press Enter in the CLI to exit the application.

## Example Queries

- What was Microsoft’s total revenue in 2023?
- How did NVIDIA’s data center revenue grow from 2022 to 2023?
- Which company had the highest operating margin in 2023?
- What percentage of Google’s revenue came from cloud in 2023?
- Compare the AI strategies of Google, Microsoft, and NVIDIA as discussed in their 2024 10-Ks

---

## Design Decisions

- **Chunking:** Recursive splitter chosen to balance context and retrieval efficiency[file:1]
- **Embeddings:** MiniLM selected for its speed and competitive retrieval accuracy
- **Agentic approach:** Prompt-based decomposition for multi-step and comparative queries
- **Vector Store:** ChromaDB for seamless in-memory and persistent operation
- **LLM:** Groq’s open-source LLM for reliable fast inference

---

## Limitations & Future Work

- Limited to single-turn questions (no conversational memory)[file:1]
- Parsing of financial tables is not supported out-of-the-box
- Multi-document reasoning limited to simple aggregation and comparison

---

## Sample Output
                 "Document(id=""cd5d29ce-0990-4e25-9558-76bfcf90e347",
               "metadata="{
                  "creationdate":"2025-09-17T18:25:20+0larity of gaming, esports, content creation and streaming; the demand for new and upgraded systems to support the increase in\nremote work; and the ability of end users to engage in cryptocurrency mining.\n31"")",
                  "Document(id=""cd5d29ce-0990-4e25-9558-76bfcf90e347",
                  "metadata="{
                     "creationdate":"2025-09-17T18:25:20+0of end users to engage in cryptocurrency mining.\n31"")",
                     "Document(id=""cd5d29ce-0990-4e25-9558-76bfcf90e347",
                     "metadata="{
                        "creationdate":"2025-09-17T18:25:20+00:00",
                        "total_pages":144,
                        "creator":"pdftk 2.02 - www.pdftk.com",
                        "page":36,
                        "page_label":"37",
                        "producer":"itext-paulo-155 (itextpdf.sf.net-lowagie.com)",
                        "moddate":"2025-09-17T18:25:20+00:00",
                        "source":"10k_pdf\\n22.pdf"
                     },
                     "page_content=""Table of Contents\nRevenue\nRevenue by Reportable Segments\nYear Ended\nJanuary 30,\n2022\nJanuary 31,\n2021\n$\nChange\n%\nChange\n($ in millions)\nGraphics\n$\n15,868 \n$\n9,834 \n$\n6,034 \n61 \n%\nCompute & Networking\nded\nJanuary 30,\n2022\nJanuary 31,\n2021\n$\nChange\n%\nChange\n($ in millions)\nGraphics\n$\n15,868 \n$\n9,834 \n$\n6,034 \n61 \n%\nCompute & Networking\n11,046 \n6,841 \n4,205 \n61 \n%\nTotal\n$\n26,914 \n$\n16,675 \n$\n10,239 \n61 \n%\nGraphics - \nGraphics segment revenue increased by 61% in ﬁscal year 20n11,046 \n6,841 \n4,205 \n61 \n%\nTotal\n$\n26,914 \n$\n16,675 \n$\n10,239 \n61 \n%\nGraphics - \nGraphics segment revenue increased by 61% in ﬁscal year 2022 compared to ﬁscal year 2021. We continue to beneﬁt\nfrom strong demand for NVIDIA Ampere architecture products, and believe the increase in Gaming revenue during ﬁscal year 2022\nresulted from a combination of factors, including: the ramp of new RTX 30 Series GPUs; the release of new games supporting ray\ntracing; the rising popularity of gaming, esports, content creation and streaming; the demand for new and upgraded systems to\nsupport the increase in remote work; and the ability of end users to engage in cryptocurrency mining.\nCompute & Networking - \nCompute & Networking segment revenue increased by 61% in ﬁscal year 2022 compared to ﬁscal year"")",
                     "Document(id=""e86127b4-f971-45c3-a6d5-0b9ed304130c",
                     "metadata="{
                        "source":"10k_pdf\\n22.pdf",
                        "page":69,
                        "moddate":"2025-09-17T18:25:20+00:00",
                        "creator":"pdftk 2.02 - www.pdftk.com",
                        "page_label":"70",
                        "creationdate":"2025-09-17T18:25:20+00:00",
                        "total_pages":144,
                        "producer":"itext-paulo-155 (itextpdf.sf.net-lowagie.com)"
                     },
                     "page_content=""Table of Contents\nNVIDIA CORPORATION AND SUBSIDIARIES\nNOTES TO THE CONSOLIDATED FINANCIAL STATEMENTS\n(Continued)\n \nJanuary 30,\n2022\nJanuary 31,\n2021\n(In millions)\nAccrued and Other Current Liabilities:\nCustomer program accruals\n$\n1,000\n \n$\n630\n \nAccrued payroll and related expenses\n409\n \n297\n \nDeferred revenue (1)\n300\n \n288\n \nExcess inventory purchase obligations\n196\n \n52\n \nOther\n647\n \n510\n \nTotal accrued and other current liabilities\n$\n2,552\n \n$\n1,777\n \n(1)\nDeferred revenue primarily includes customer advances and deferrals related to license and development arrangements, support for hardware and software, and\ncloud services.\n \nJanuary 30,\n2022\nJanuary 31,\n2021\n(In millions)\nOther Long-Term Liabilities:\nIncome tax payable (1)\n$\n980\n \n$\n836\n \nDeferred income tax\n245\n \n241\n \nDeferred revenue (2)\n202\n \n163\n \nOther\n126\n \n135\n \nTotal other long-term liabilities\n$\n1,553\n \n$\n1,375\n \n(1)"")"
                  ],
                  "answer":"NVIDIA’s total revenue for fiscal year\u202f2022 was\u202f$26.914\u202fbillion (approximately\u202f$26.91\u202fbillion). This represented a 61\u202f% increase over the prior year."
               }
