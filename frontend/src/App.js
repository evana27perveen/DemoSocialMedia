import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import Login from './components/Auths/Login';
import Signup from './components/Auths/Signup';
import OTP from './components/Auths/OTP';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from './components/Home_/Home';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/otp" element={<OTP />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
