from selene.api import *
from datetime import datetime as dt
from comment_box import comment_box

wrong_data = {'author':'wrong_author', 'email':'wrong@email', 'comment':'wrong comment'}

right_author = 'right author {0}'.format(dt.now())
msg = 'right comment {0}'.format(dt.now())
right_data = {'author':right_author, 'email':'right@email.com', 'comment':msg}

config.browser_name = 'chrome'

# 1. Open http://store.demoqa.com
browser.open_url('http://store.demoqa.com/')

# 2. Navigate to 'Sample page'
sample_page_btn = s('a[href="http://store.demoqa.com/sample-page/"]')
sample_page_btn.click()

# 3. Enter a comment with a wrong email
comment_box_field = comment_box()
comment_box_field.comment_via_dict(wrong_data)

# 4. Check Error is displayed
s('#error-page').should(be.in_dom)
s('#error-page').should(be.visible)

# 5. Navigate back
s('a[href]').click()

# 6. Enter a comment with a correct email
comment_box_field.comment_via_dict(right_data)

# 7. Check Comment is received
#    a. Verify user name matches
for comment_el in ss('li.comment'):

#   b01. verify user name is ok
    if comment_el.s('cite.fn').text == right_data['author']:
#     b11. Verify comment text matches
        comment_el.s('div.comment-body').should(have.exact_text(right_data['comment']))


# 8. Shutdown browser
browser.quit()
