from fastapi import FastAPI
# from ml import nlp
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/")

def read_main():
    """ Test **Get** Function"""
    return {"message": "Hello World"}

# @app.get("/article/{article_id}")
# def analyze_article(article_id: int,q:str = None):
#     count = 0
#     if q:
#         doc = nlp(q)
#         count=len(doc.ents)
#     return{"article_id":article_id,"previous_id":article_id-1,"q":q, "count":count}

# class Article(BaseModel):
#     content: str
#     comments: List[str]= []
#
# @app.post("/article/")
#
# def analyze_article(articles: List[Article]):
#     """ Analyze an article and extract entities with 🌟 spaCy 🌟
#     Statistical Models *will* have **errors**
#
#     * Extract Entities
#     * Scream Comments
#     """
#

    # ents=[]
    # comments=[]
    # for article in articles:
    #     for comment in article.comments:
    #         comments.append(comment.upper())
    #     doc = nlp(article.content)
    #     for ent in doc.ents:
    #         ents.append({"text":ent.text, "label":ent.label_})
    # return{"ents":ents,"comments":comments}
    # return {"message":article.content,"comments":article.comments,"ents":ents}

