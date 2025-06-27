import os
import fitz  # PyMuPDF
import gradio as gr
import traceback
from openai import OpenAI

# Initialize OpenAI client with API key from environment variable
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def extract_text_from_pdf(file):
    """Extract text from uploaded PDF file."""
    doc = fitz.open(file.name)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()  # Clean up resources by closing the document
    return text

def create_prompt(pdf_text):
    """Build the prompt that instructs GPT-4 to extract information and answer questions."""
    instruction = f"""
You are a startup evaluator. From the provided PDF content, extract the following:
- All team member contact information
- Team member qualifications and team size
- Company name
- Location
- A short summary of the idea

Then answer the following five questions clearly:

1. What painful problem is this solving, and for whom?
2. Why is this solution uniquely better than existing alternatives?
3. How big is the market opportunity, and how fast is it growing?
4. What evidence is there that this works (traction, users, pilots)?
5. Why is this team the right one to win?

PDF Content:
\"\"\"
{pdf_text}
\"\"\"
"""
    return instruction

def process_pdfs_with_debug(pdf_files):
    """Process uploaded PDFs and return evaluation results with debug information."""
    all_results = ""
    debug_info = ""
    
    try:
        # Check if OpenAI API key is available
        if not os.environ.get("OPENAI_API_KEY"):
            return "❌ OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.", "Missing API key"
        
        for file in pdf_files:
            text = extract_text_from_pdf(file)
            prompt = create_prompt(text)
            
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,
            )
            
            answer = response.choices[0].message.content
            all_results += f"\n\n---\n📄 **{file.name}**:\n{answer}\n"
            
        return all_results, "✅ No errors"
        
    except Exception as e:
        debug_info = traceback.format_exc()
        return f"❌ An error occurred: {str(e)}", debug_info

# Create Gradio interface
iface = gr.Interface(
    fn=process_pdfs_with_debug,
    inputs=gr.File(
        file_types=[".pdf"], 
        label="Upload PDF Files", 
        file_count="multiple"
    ),
    outputs=[
        gr.Textbox(label="Evaluation Output", lines=20),
        gr.Textbox(label="Debug Output", lines=10)
    ],
    title="🚀 Startup Pitch Deck Analyzer",
    description="Upload one or more PDF pitch decks to get detailed startup evaluations and insights.",
    theme=gr.themes.Soft(),
    examples=None,
    cache_examples=False
)

if __name__ == "__main__":
    iface.launch()