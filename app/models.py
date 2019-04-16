class Articles:
    '''
    Articles class to define article objects
    '''
    def __init__(self, title, description, image, timePublished, author, url):
        self.title = title
        self.description = description
        self.image = image
        self.timePublished = timePublished
        self.author = author
        self.url = url




class News:
    '''
    News class to define news objects
    '''
    def __init__(self, name, author, url,description, country,category, id):
        self.name = name
        self.author = author
        self.url = url
        self.description = description
        self.country = country
        self.category = category
        self.id = id
    