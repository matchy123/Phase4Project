import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Routes, Route, NavLink } from 'react-router-dom';
import Animal from './components/Animal';
import Store from './components/Store';
import Contact from './components/Contact';

function App() {
  return (
    <Router>
      <div className="app">
        <nav>
          <ul>
            <li><NavLink to="/about">ABOUT US</NavLink></li>
            <li><NavLink to="/animals">OUR ANIMALS</NavLink></li>
            <li><NavLink to="/store">OUR STORE</NavLink></li>
            <li><NavLink to="/contact">CONTACT</NavLink></li>
          </ul>
        </nav>

        {/* Main content with the dog image and tagline */}
        <div className="main-content">
          <div className="tagline">
            <h1>Happiness is closer than you think</h1>
            <NavLink to="/about"><button>Let's Go!</button></NavLink>
          </div>
          <div className="dog-image"></div> {/* This could be a background image */}
        </div>

        {/* Route components */}
        <Routes>
          <Route path="/about" element={<About />} />
          <Route path="/animals" element={<Animal />} />
          <Route path="/store" element={<Store />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>

        <div className="footer">
          <NavLink to="/about" className="text-decoration-none text-white">About Us</NavLink>
          <br />
          <NavLink to="/contact" className="text-decoration-none text-white">Contact Us</NavLink>
        </div>
      </div>
    </Router>
  );
};

function About() {
  return (
    <div className="about-section">
      <div className="dog-image"></div> {/* Background image of the dog "Pappi" */}
      <div className="about-text">
        <h2>ABOUT US</h2>
        <p>My name is Pappi, and I'm going to tell you about our project!</p>
      </div>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));

export default App;
