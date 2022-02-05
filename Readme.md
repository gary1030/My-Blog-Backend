# My Blog Backend

### 1. Build virtual environment
```
python -m venv blog-env
./blog-env/Scripts/activate
```
### 2. Install required packages
```
pip install fastapi
pip install "uvicorn[standard]"
pip install sqlalchemy
pip install psycopg2
```
### 3. Start the server
```
uvicorn main:app --reload
```

## Description
This is a simple backend development about a blog app. You can publish your post and comment anonymously.

### Endpoints
* POST /post/
  Create a new post.
* GET /posts/
  Get all posts.
* GET /post/{post_id}
  Get post by specific id.
* POST /comment/
  Create a new comment under a post.
* GET /comments/{post_id}
  Get all comments under a post.

