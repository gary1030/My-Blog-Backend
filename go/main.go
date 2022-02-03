package main

import (
    "net/http"

    "github.com/gin-gonic/gin"
)

type post struct {
    ID     string  `json:"id"`
    Title  string  `json:"title"`
    Content string  `json:"content"`
	Arthur string `json:"arthur"`
}

var posts = []post{
    {ID: "1", Title: "Blue Train", Content: "Hello", Arthur: "John Coltrane"},
    {ID: "2", Title: "Jeru", Content: "Hello", Arthur: "Gerry Mulligan"},
    {ID: "3", Title: "Sarah Vaughan and Clifford Brown", Content: "Hello", Arthur: "Sarah Vaughan"},
}

func main() {
    router := gin.Default()
    router.GET("/posts", getPosts)
	router.GET("/post/:id", getPost)
	router.POST("/post", addPost)

    router.Run("localhost:8080")
}

// getPosts responds with the list of all posts as JSON.
func getPosts(c *gin.Context) {
    c.IndentedJSON(http.StatusOK, posts)
}

// adds a post from JSON received in the request body.
func addPost(c *gin.Context) {
    var newPost post

    // Call BindJSON to bind the received JSON to newPost.
    if err := c.BindJSON(&newPost); err != nil {
        return
    }

    // Add the new album to the slice.
    posts = append(posts, newPost)
    c.IndentedJSON(http.StatusCreated, newPost)
}

// getPostByID
// parameter sent by the client, then returns that post as a response.
// http://localhost:8080/post/2
func getPost(c *gin.Context) {
    id := c.Param("id")

    // Loop over the list of posts, looking for a post whose ID value matches the parameter.
    for _, a := range posts {
        if a.ID == id {
            c.IndentedJSON(http.StatusOK, a)
            return
        }
    }
    c.IndentedJSON(http.StatusNotFound, gin.H{"message": "post not found"})
}

