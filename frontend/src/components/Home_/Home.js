import React from 'react'
import Header from '../Header_/Header'
import './Home.css'
import Cards from './Cards'
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import All_post from './All_post';
import NewPost from './NewPost';


const Home = () => {
    return (
        <div>
            <Header />
            <div className="container">
                <div className="row" style={{width: '100%'}}>
                    
                    <div className="" style={{paddingLeft:'4%', paddingRight: '2%'}}>
                    <NewPost />
                    </div>
                    
                </div>
            </div>
            <All_post />
        </div>
    )
}

export default Home