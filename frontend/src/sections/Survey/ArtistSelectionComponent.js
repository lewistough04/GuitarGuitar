import React, { useState } from "react";
import "./GenreComponent.css"

function ArtistSelectionComponent(){

    return(
        <div className="main-div">
            <h1 className="survey-title">What is your favourite genre!</h1>
            <ul className="genres-list">
            {genres.map((genre, index) => (
                <li key={index}> 
                    <button className={`genre-button ${selectedGenre === genre ? 'selected' : ''}`}
                            onClick={() => handleGenreChange(genre)}>
                        {genre}
                    </button>
                </li>
            ))}
            </ul>
        </div>
    );
}

export default ArtistSelectionComponent;