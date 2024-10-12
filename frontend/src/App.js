import logo from './assets/media/long-logo.png'
import React from 'react';
import './App.css';
import GenreComponent from './sections/Survey/GenreComponent';
import ReturnComponent from './sections/Return/ReturnComponent';
import FooterComponent from './sections/Footer/FooterComponent';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <a
          className="App-link"
          href="https://www.guitarguitar.co.uk/"
          target="_blank"
          rel="noopener noreferrer"
        >
          <img src={logo} className="App-logo" alt="logo" />
        </a>
      </header>
      <GenreComponent/>
      <ReturnComponent/>
      <FooterComponent/>
    </div>
  );
}

export default App;
