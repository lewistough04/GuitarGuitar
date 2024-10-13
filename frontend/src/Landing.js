import React from 'react';
import "./Landing.css"
import logoImage from './assets/monkey-wizard.png'

function Landing() {

    const launchApp = () => {
        window.location.href = '/main';
        console.log("clicked")
    }

    return (
        <body>
            <div id="welcome">
                <h1 id="welcome-header">Welcome to the GuitarGuitar Wizard</h1>
                <button id="start-button" onClick={launchApp}>Start</button>
            </div>

            <div className="steps-section">

                <div className="step-div">
                    <h2 className="step-header">Step 1</h2>
                    <h4 className="step-text">Pick a music genre you're interested in</h4>
                </div>

                <div className="step-div">
                    <h2 className="step-header">Step 2</h2>
                    <h4 className="step-text">Choose your favourite artists</h4>
                </div>

                <div className="step-div">
                    <h2 className="step-header">Step 3</h2>
                    <h4 className="step-text">View equipment recommended for you</h4>
                </div>
            </div>
            <div className='lander-image-container'>
                <img className='lander-image' src={logoImage} alt="Landing Page" />
            </div>
        </body>
    )
}

export default Landing;