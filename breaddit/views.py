from django.db import connection
from django.http import JsonResponse


def dictfetchall(cursor):
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def comments(request, post_id):
    """
    Get all comments for a post, along with the user who created the comment.

    :param request: HttpRequest
    :param post_id:
    :return:
    """

    post_comment_sql = (
        "SELECT id, body, created_at, updated_at, author_id "
        "FROM breaddit_comment "
        "WHERE post_id = {} and status <> 'deleted'"
    ).format(post_id)

    with connection.cursor() as cursor:
        cursor.execute(post_comment_sql)
        comments = dictfetchall(cursor)

    users = []

    for comment in comments:
        user_sql = (
            "SELECT id, username, email, first_name, last_name "
            "FROM auth_user "
            "WHERE id = {user_id} and is_active = True"
        ).format(user_id=comment['author_id'])

        with connection.cursor() as cursor:
            cursor.execute(user_sql)
            user = dictfetchall(cursor)[0]
            users.append(user)

    response = {
        "comments": []
    }

    for comment in comments:

        user = [user for user in users if user['id'] == comment['author_id']][0]

        response['comments'].append({
            "id": comment['id'],
            "body": comment['body'],
            "created_at": comment['created_at'].isoformat(),
            "updated_at": comment['updated_at'].isoformat(),
            "user": {
                "id": user['id'],
                "username": user['username'],
                "email": user['email'],
                "first_name": user['first_name'],
                "last_name": user['last_name'],
            }
        })

    return JsonResponse(comments, safe=False)
