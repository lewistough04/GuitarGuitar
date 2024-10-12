import logo from './media/long-logo.png'
import './App.css';

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
    </div>
  );
}

export default App;
