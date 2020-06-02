import firebase_admin
from firebase_admin import credentials, db, exceptions


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
    def _reference(reference: str):
        return db.reference(reference)

    def _reference_string(self, reference: str):
        return self._reference(reference).get()

    def get(self, reference: str):
        ref_str = self._reference_string(reference)
        if not ref_str:
            raise ReferenceNotFoundException
        else:
            return ref_str

    def add(self, reference: str, node_dict: dict):
        # Check if the node already exists in the <reference> node
        child_str = self._reference(reference).child(*node_dict).get()
        if not child_str:
            self._reference(reference).update(node_dict)
        else:
            raise ElementAlreadyExistsError

    def update(self, reference: str, node_dict: dict):
        ref_str = self._reference(reference).child(*node_dict).get()
        if not ref_str:
            raise ReferenceNotFoundException
        else:
            self._reference(reference).update(node_dict)

    def set(self, reference: str, node_dict: dict):
        """
        Overwrites everything inside the <reference> node with <node_dict>.

        :param reference: [str]
        :param node_dict: [str]
        :return:
        """

        # ref_str = self._reference_string(reference)
        # if not ref_str:
        #     raise ReferenceNotFoundException
        # else:
        #     self._reference(reference).set(node_dict)
        self._reference(reference).set(node_dict)

    def delete(self, reference: str):
        ref_str = self._reference_string(reference)
        if not ref_str:
            raise ReferenceNotFoundException
        else:
            self._reference(reference).delete()


class ReferenceNotFoundException(Exception):
    def __init__(self, message="Reference not found in the data base"):
        self.code = 400
        self.message = message
        self.error_dict = {
            "code": self.code,
            "message": self.message
        }
        super().__init__(self.message)


class ElementAlreadyExistsError(Exception):
    def __init__(self, message="The element already exists in the database"):
        self.code = 200
        self.message = message
        self.error_dict = {
            "code": self.code,
            "message": self.message
        }
        super().__init__(self.message)