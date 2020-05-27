import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class Firebase:
    class __Firebase:
        def __init__(self, arg):
            self.val = arg
            cred = credentials.Certificate("/home/jorge/PycharmProjects/groceries/auth.json")
            firebase_admin.initialize_app(cred, {'databaseURL': 'https://groceries-5674f.firebaseio.com/'})

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self, arg):
        if not Firebase.instance:
            Firebase.instance = Firebase.__Firebase(arg)
        else:
            Firebase.instance.val = arg

    @staticmethod
    def get_reference(reference: str):
        """

        :param reference:
        :return:
        """
        ref = db.reference(reference)
        return ref
