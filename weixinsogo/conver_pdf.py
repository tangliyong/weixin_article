import pdfkit

def save_pdf(content, file_name):
    # html模版，转换pdf使用
    html_template = """

    <!DOCTYPE html>

    <html lang="en">

    <head>

        <meta charset="UTF-8">

    </head>

    <body>

    {content}

    </body>

    </html>



    """

    options = {

        'page-size': 'Letter',

        'margin-top': '0.75in',

        'margin-right': '0.75in',

        'margin-bottom': '0.75in',

        'margin-left': '0.75in',

        'encoding': "UTF-8",

        'custom-header': [

            ('Accept-Encoding', 'gzip')

        ],

        'cookie': [

            ('cookie-name1', 'cookie-value1'),

            ('cookie-name2', 'cookie-value2'),

        ],

        'outline-depth': 10,

    }

    html = html_template.format (content=content)

    pdfkit.from_string (html, file_name, options=options)