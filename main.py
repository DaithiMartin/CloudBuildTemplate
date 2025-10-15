import functions_framework

# This decorator registers the function to handle HTTP requests.
@functions_framework.http
def hello_http(request):
    """
    A simple HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
    Returns:
        The response text.
    """
    print("Hello World!")
    return 'Hello, World!'