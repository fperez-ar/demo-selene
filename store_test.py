from unittest import TestCase
from selene.api import *
from datetime import datetime as dt
from comment_box import comment_box

class store_test(TestCase):
    def setUp(self):
        config.browser_name = 'chrome'
        right_author = 'right author {0}'.format(dt.now())
        msg = 'right comment {0}'.format(dt.now())
        self.right_data = {'author':right_author, 'email':'right@email.com', 'comment':msg}
        self.wrong_data = {'author':'wrong_author', 'email':'wrong@email', 'comment':'wrong comment'}

    def test_email(self):
        # 1. Open http://store.demoqa.com
        browser.open_url('http://store.demoqa.com/')

        # 2. Navigate to 'Sample page'
        sample_page_btn = s('a[href="http://store.demoqa.com/sample-page/"]')
        sample_page_btn.click()

        # 3. Enter a comment with a wrong email
        comment_box_field = comment_box()
        comment_box_field.comment_via_dict(self.wrong_data)

        # 4. Check Error is displayed
        s('#error-page').should(be.in_dom)
        s('#error-page').should(be.visible)

        # 5. Navigate back
        s('a[href]').click()

        # 6. Enter a comment with a correct email
        comment_box_field.comment_via_dict(self.right_data)

        # 7. Check Comment is received
        #    a. Verify user name matches
        for comment_el in ss('li.comment'):
        #   b01. verify user name matches our user
            if comment_el.s('cite.fn').text == self.right_data['author']:
        #     b11. Verify comment text matches
                right_comment = self.right_data['comment']
                comment_el.s('div.comment-body').should(have.exact_text(right_comment))

    def tearDown(self):
        # 8. Shutdown browser
        browser.quit()
