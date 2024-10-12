import "./SurveyComponent.css"
import React, { useState } from "react";
import Axios from "axios";

function SurveyComponent(){

    const [genres, setGenre] = useState(["Rock & Roll", "Pop", "Country", "Acid-House"]);
    const [selectedGenre, setSelectedGenre] = useState('');

    function handleGenreChange(genre){
        setSelectedGenre(genre);
        console.log("Selected genre: ", genre);
    }

    return(
        <div className="main-div">
            <h1 className="survey-title">What is your favourite genre!</h1>
            <ul className="genres-list">
            {genres.map((genre, index) => (
                <li key={index}> 
                    <button className={`genre-button ${selectedGenre === genre ? 'selected' : ''}`}  // Add 'selected' class if the genre is selected
                            onClick={() => handleGenreChange(genre)}>
                        {genre}
                    </button>
                </li>
            ))}
            </ul>
        </div>
    );
}

export default SurveyComponent;