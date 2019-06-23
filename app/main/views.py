from flask import render_template,redirect,url_for,request
from . import main
from ..models import NewsSource
from ..request import get_news_sources

@main.route('/')
def index():
    '''
    Function that returns the index page and the processed data
    '''

    general_news = get_news_sources('general')
    business_news = get_news_sources('business')
    entertainment_news = get_news_sources('entertainment')
    sports_news = get_news_sources('sports')
    technology_news = get_news_sources('technology')
   

    title = 'Homepage'
    
    return render_template('index.html',title=title, general=general_news, business=business_news, entertainment=entertainment_news, sports=sports_news, technology=technology_news)
