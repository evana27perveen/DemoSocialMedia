import React, { useState } from 'react'
import { useCookies } from 'react-cookie'

const NewPost = () => {
    const [newPost, setNewPost] = useState("")
    const [token, setToken] = useCookies(['myToken'])

    const handlePostSubmit = e => {
        e.preventDefault()
        console.log(newPost);
        if (newPost != "" || newPost != " ") {
            fetch(`http://127.0.0.1:8000/main-api/add-new-post-api/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token['myToken']
                },
                body: JSON.stringify({
                    'post_text': newPost
                })
            }).then(resp => resp.json())
                .then(resp => {
                    if (resp['id']) {
                        alert("Successfully posted")
                    }
                    else {
                        alert("Failed to post")
                    }
                })
        }
        setNewPost(" ")
    }
    return (
        <div style={{width: '100%'}}>
            <form method="post" onSubmit={handlePostSubmit}>
                <div className="form-group">
                    <textarea className="form-control" name="content" rows={3} onChange={e => setNewPost(e.target.value)} value={newPost} style={{backgroundColor:'#03314b', color:'white'}}></textarea>
                </div>
                <div className="form-group mt-2">
                    <input type="submit" name="Submit" value="Publish" className="form-control" style={{backgroundColor:'white', color:'black', fontWeight:'bold'}} />
                </div>
            </form>
        </div>
    )
}

export default NewPost
