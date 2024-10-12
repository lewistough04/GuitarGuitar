import logo from './assets/media/long-logo.png'
import React from 'react';
import './App.css';
import SurveyComponent from './sections/Survey/SurveyComponent';
import ReturnComponent from './sections/Return/ReturnComponent';

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
      <SurveyComponent/>
      <ReturnComponent/>
    </div>
  );
}

export default App;
