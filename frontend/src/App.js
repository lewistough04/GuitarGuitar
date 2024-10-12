import logo from './assets/media/long-logo.png'
import './App.css';
import SurveyComponent from './sections/Survey/SurveyComponent';
import ReturnComponent from './sections/Return/ReturnComponent';
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Welcome to the sample screen for Guitar Guitar
        </p>
        <a
          className="App-link"
          href="https://www.guitarguitar.co.uk/"
          target="_blank"
          rel="noopener noreferrer"
        >
          Go To Guitar Guitar!
        </a>
      </header>
      <SurveyComponent/>
      <ReturnComponent/>
    </div>
  );
}

export default App;
