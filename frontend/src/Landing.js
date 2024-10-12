import React from 'react';
import "./Landing.css"
import HeaderComponent from './sections/Header/HeaderComponent';
import FooterComponent from "./sections/Footer/FooterComponent";

function Landing() {

    const launchApp = () => {
        window.location.href = '/main';
        console.log("clicked")
    }

    return (
        <div>
            <HeaderComponent/>
            <div>
                <div id="welcome">
                    <h1 id="welcome-header">Welcome to the GuitarGuitar Wizard</h1>
                    <button id="start-button" onClick={launchApp}>Start</button>
                </div>

                <div className="steps-section">

                    <div className="step-div">
                        <h2 className="step-header">Step 1</h2>
                        <h4 className="step-text">Enter the music genre you're interested in</h4>
                    </div>

                    <div className="step-div">
                        <h2 className="step-header">Step 2</h2>
                        <h4 className="step-text">Choose some artists you like the sound of</h4>
                    </div>

                    <div className="step-div">
                        <h2 className="step-header">Step 3</h2>
                        <h4 className="step-text">View guitars recommended by you</h4>
                    </div>
                </div>
            </div>
            <FooterComponent/>
        </div>
    )
}

export default Landing;