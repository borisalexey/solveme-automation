
def test_something(get_number):
    assert 1 == 1
    print(get_number)


# import requests
#
# from configuration import SERVICE_URL
#
# from src.baseclasses.response import Response
# #from src.schemas.post import POST_SCHEMA
# from src.pydantic_schemas.post import Post
#
# def test_get_posts():
#     r = requests.get(url=SERVICE_URL)
#     response = Response(r)
#     response.assert_status_code(200).validate(Post)

