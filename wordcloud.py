

from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts

from pytagcloud import create_tag_image, create_html_data, make_tags, LAYOUT_HORIZONTAL, LAYOUTS, LAYOUT_MIX, LAYOUT_VERTICAL, LAYOUT_MOST_HORIZONTAL, LAYOUT_MOST_VERTICAL

YOUR_TEXT = "There are at least 2 packages for creating wordcloud visualization, first to create\
is simply wordcloud, the other one pytagcloud using pygame and simplejson packages as requirements"

tags = make_tags(get_tag_counts(YOUR_TEXT), maxsize=60)

create_tag_image(tags, 'cloud_large.png', size=(900, 600), fontname='Lobster', layout=LAYOUT_HORIZONTAL) #fonts on GitHub/pytagcloud/fonts

import webbrowser
webbrowser.open('cloud_large.png') # see results

