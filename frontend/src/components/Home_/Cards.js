import React from 'react'

function Cards(props) {
  return (
    <div>
        {props.posts.map(post => {
            return (
                <div className="container" key={post.id}>
                <div className="card" style={{justifyContent: 'center'}}>
                    <div className="card-body">
                        <ul>
                            <div className="card-title">
                                <div className="per-name">{post.post_author}</div>
                                <hr/>
                            </div>
                        </ul>
                    </div>

                    <div className="card-content">
                        <div className="card-text">
                            <span>{post.post_text}</span>
                        </div>

                        <div className="icons">
                            <div className="react">
                                <img src="./black_love.png" alt="black-love" height="20" width="20"/>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            )
        })}
        
    </div>
  )
}

export default Cards