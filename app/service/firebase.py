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
        return self._reference(reference).push(node_dict)

    def update(self, reference: str, node_dict: dict):
        for child in node_dict:
            ref_str = self._reference(reference).child(child).get()
            if not ref_str:
                raise ReferenceNotFoundException
            self._reference(reference).update(node_dict)

    def set(self, reference: str, node_dict: dict):
        """
        Overwrites everything inside the <reference> node with <node_dict>.

        :param reference: [str]
        :param node_dict: [str]
        :return:
        """
        ref_str = self._reference(reference).child(*node_dict).get()
        if not ref_str:
            raise ReferenceNotFoundException
        else:
            self._reference(reference).set(node_dict)

    def delete(self, reference: str):
        # TODO Check this works
        ref_str = self._reference_string(reference)
        if not ref_str:
            raise ReferenceNotFoundException
        else:
            self._reference(reference).delete()


def update_node_array_formatter(node_id: str, old: dict, new: dict):
    formatted_dict = dict()
    for key, value in new.items():
        new_value = list(set(old.get(key) + value))
        formatted_dict = dict(**formatted_dict,
                              **{'{}/{}'.format(node_id, key): new_value})
    return formatted_dict


class ReferenceNotFoundException(Exception):
    def __init__(self, message="Reference not found in the data base"):
        self.code = 404
        self.message = message
        self.error_dict = {
            "code": self.code,
            "message": self.message
        }
        super().__init__(self.message)


class ElementAlreadyExistsError(Exception):
    def __init__(self, message="The element already exists in the database"):
        self.code = 409
        self.message = message
        self.error_dict = {
            "code": self.code,
            "message": self.message
        }
        super().__init__(self.message)
