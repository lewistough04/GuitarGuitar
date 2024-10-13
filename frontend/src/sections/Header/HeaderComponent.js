import './HeaderComponent.css';
import logo from '../../assets/media/long-logo.png'

function HeaderComponent() {
    return (
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
    );
}

export default HeaderComponent;