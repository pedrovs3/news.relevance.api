import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict

# Baixar os recursos do NLTK
nltk.download('wordnet')
nltk.download('omw-1.4')


def preprocess_text(text: str) -> str:
    """Lematiza o texto e remove caracteres desnecessários."""
    lemmatizer = WordNetLemmatizer()
    return " ".join([lemmatizer.lemmatize(word.lower(), pos='n') for word in text.split()])


def expand_with_synonyms(keywords: List[str]) -> List[str]:
    """
    Expande palavras-chave com sinônimos do WordNet.
    """
    expanded_keywords = set(keywords)
    for keyword in keywords:
        synonyms = wordnet.synsets(keyword)
        for syn in synonyms:
            for lemma in syn.lemmas():
                expanded_keywords.add(lemma.name())
    return list(expanded_keywords)


def combine_texts(news: List[Dict[str, str]]) -> List[str]:
    """Combina título e conteúdo das notícias com pré-processamento."""
    return [preprocess_text(f"{article['title']} {article['content']}") for article in news]


def rank_news(user_keywords: List[str], news: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Classifica notícias com base em relevância usando TF-IDF e similaridade de cosseno.
    """
    if not user_keywords or not news:
        return []

    # Expande as palavras-chave
    expanded_keywords = expand_with_synonyms(user_keywords)

    # Pré-processa textos
    documents = combine_texts(news)
    user_query = preprocess_text(" ".join(expanded_keywords))

    # Ajustar peso das palavras-chave (repetição)
    user_query_weighted = " ".join([user_query] * 5)

    # Cria matriz TF-IDF com ajustes
    vectorizer = TfidfVectorizer(
        stop_words='english',
        max_features=5000,
        sublinear_tf=True,
        max_df=0.85
    )
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Vetoriza a consulta do usuário
    user_vector = vectorizer.transform([user_query_weighted])

    # Calcula similaridades
    relevance_scores = cosine_similarity(user_vector, tfidf_matrix).flatten()

    # Ordena por relevância
    ranked_news = [
        {**news[idx], "relevance": round(score, 2)}  # Arredonda para 2 casas decimais
        for idx, score in enumerate(relevance_scores)
    ]
    ranked_news.sort(key=lambda x: x["relevance"], reverse=True)

    return ranked_news
