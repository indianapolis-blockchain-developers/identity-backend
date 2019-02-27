from typing import Tuple, Optional
from flask_restful import Resource, reqparse
from identity_app.models.user import UserModel


class UserV1(Resource):

    # TODO: add created and last_updated dates for all entries
    # TODO: need custom datatypes like email
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='User\'s name')
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help='Email address')


    def get(self, id: Optional[int] = None) -> Tuple[dict, int]:
        """
        Get user or users
        Returns all users if a user id isn't specified
        """

        if id is None:
            # Note: for many records, we would need to paginate here,
            # this is mostly for testing
            return {'users': [user.as_dict() for user in UserModel.all_users()]}, 200

        um = UserModel.user_by_id(id)
        if um:
            return um.as_dict(), 200
        return {'message': 'User not found'}, 404


    def post(self, id: Optional[int] = None) -> Tuple[dict, int]:
        """
        Create a new user
        """

        if id is not None:
            return {'message': 'Do not provide id as URI path for POST.'}, 400

        data = UserV1.parser.parse_args()

        # Because we have naming of resource and data model the same, we can use dictionary expansion
        # to offer the named arguments to the model creation.
        print({**data})
        um = UserModel(**data)
        um.save_to_db()
        return {'message': 'User created'}, 201


    def patch(self, id: Optional[int] = None) -> Tuple[dict, int]:
        """
        Update a user
        PATCH requires item to update, so id is required
        """

        if id is None:
            return {'message': 'Must specify the user id in URI to update.'}, 400

        um = UserModel.user_by_id(id)
        if not um:
            return {'message': 'User not found.'}, 404

        data = UserV1.parser.parse_args()

        # Since properties and resource fields are the same, we can setattr for each field.
        # This would still be possible if you needed a mapping for the value names to translate.
        for key in data:
            setattr(um, key, data[key])
        um.save_to_db()
        return {'message': 'User updated.'}, 200


    def delete(self, id: Optional[int] = None) -> Tuple[dict, int]:
        """
        Delete a user
        Must specify the user's id
        """

        if id is None:
            return {'message': 'You cannot delete all users.'}, 400

        um = UserModel.user_by_id(id)
        if not um:
            return {'message': 'User not found.'}, 404
        um.delete_from_db()
        return {'message': 'User deleted'}, 200
