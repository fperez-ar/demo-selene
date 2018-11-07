from selene.api import s

class comment_box():

    def comment_via_dict(self, contents_dict):
        s('#author').set_value(contents_dict['author'])
        s('#email').set_value(contents_dict['email'])
        s('#comment').set_value(contents_dict['comment'])
        s('#submit').click()

    def comment(self, author, email, comment):
        s('#author').set_value(author)
        s('#email').set_value(email)
        s('#comment').set_value(comment)
        s('#submit').click()
