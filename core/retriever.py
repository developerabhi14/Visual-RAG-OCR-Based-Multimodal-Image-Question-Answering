from core.embed_store import load_or_create_db

def get_relevant_context_from_query(query: str, top_k: int = 5) -> str:
    """
    Given a query, fetch the most relevant context chunks from the Chroma DB.
    """
    context = ""
    
    # Load existing vector DB
    vectorstore = load_or_create_db()
    
    # Perform similarity search
    search_results = vectorstore.similarity_search(query, k=top_k)
    
    # Combine results into a single context string
    for result in search_results:
        context += result.page_content + "\n"

    return context.strip()
