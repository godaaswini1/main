import pdfplumber
def extract_text_and_tables(pdf_path, page_number):
    with pdfplumber.open(pdf_path) as pdf:
        if page_number < 0 or page_number >= len(pdf.pages):
            return None, None 
        page = pdf.pages[page_number]
        text = page.extract_text()
        tables = page.extract_tables()
        return text, tables
def handle_query(user_query, pdf_path):
    try:
        if "page" in user_query:
            page_number = int(user_query.split("page")[1].split()[0]) - 1  
        else:
            return "Invalid query format. Please specify a page number."
    except (IndexError, ValueError):
        return "Invalid query format. Please specify a valid page number."
    page_text, tables = extract_text_and_tables(pdf_path, page_number)
    if page_text is None:
        return f"The specified page {page_number + 1} does not exist in the PDF."
    response = f"Data from page {page_number + 1}:\n"
    if tables:
        response += "Tables found on this page:\n"
        for i, table in enumerate(tables):
            response += f"\nTable {i + 1}:\n"
            for row in table:
                response += " | ".join(str(cell) for cell in row) + "\n"
    else:
        response += "No tables found on this page."

    return response
if __name__ == "__main__":
    pdf_path = r"C:\Users\godaa\Downloads\table1.pdf" 
    user_query = input("Enter your query: ")
    response = handle_query(user_query, pdf_path)
    print(response)

