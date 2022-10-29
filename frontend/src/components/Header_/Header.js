import React from 'react'
import { useNavigate } from 'react-router-dom'
import './Header.css'
import { useCookies } from 'react-cookie'
import { Link } from 'react-router-dom';

function Header() {

  let navigate = useNavigate()
  const [token, setToken, removeToken] = useCookies(['myToken'])

  const logoutSubmitted = () => {
    removeToken(['myToken'])
    // setToken("myToken", "undefined")
    navigate('/login')
  }
  return (
    <div>
      <section class="navigation">
        <div class="nav-container">
          <div class="brand">
          <h1>DSM</h1>
          </div>
          <nav>
            <div class="nav-mobile"><a id="navbar-toggle" href="#!"><span></span></a></div>
            <ul class="nav-list">
              
              <li>
                <button className='Link'  onClick={logoutSubmitted}>Logout</button>
              </li>
            </ul>
          </nav>
        </div>
      </section>
    </div>
  )
}

export default Header
