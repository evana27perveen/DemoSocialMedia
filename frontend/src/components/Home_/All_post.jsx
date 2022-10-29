import React, { useEffect, useState } from 'react'
import Cards from './Cards'
import { useCookies } from 'react-cookie'

const All_post = () => {
    const [posts, setAllPosts] = useState([]);
    const [token, setToken] = useCookies(['myToken'])
    useEffect(() => {
        fetch('http://127.0.0.1:8000/main-api/home-post-api/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                Authorization: "Bearer " + token['myToken']
            }
        })
            .then(resp => resp.json())
            .then(resp => {
                setAllPosts(resp)
            })
            .catch(error => console.log(error))
    }, []);

  return (
    <div>
      <Cards posts={posts} />
    </div>
  )
}

export default All_post
