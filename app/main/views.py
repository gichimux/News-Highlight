from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_articles, get_news


#views
@main.route('/')
def index():
    '''
    view root page that returns the index page and its data
    '''
    title = "Home || News Sources"

    all_news = get_news('general')
    sports_news = get_news('sports')
    science_news = get_news('science')
    business_news = get_news('business')
    technology_news = get_news('technology')


    # print(all_news)


    return render_template('index.html', title=title, sports=sports_news, general=all_news, technology=technology_news, business=business_news, science=science_news)

# Views
@main.route('/news/<int:id>')
def news(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    news = get_news(id)

    
    return render_template('index.html', news = news)



@main.route('/articles/<source_id>')
def articles(source_id):
    '''
    function that returns articles by source id
    '''

    article_source = get_articles(source_id)
    title = f'{source_id}| Articles'
    return render_template('articles.html',title =title, name=source_id, news=article_source )