import "./GenreComponent.css"
import React, { useEffect, useState } from "react";
import Axios from "axios";

function GenreComponent({ onNext }){

    const [genres, setGenres] = useState(["Rock & Roll", "Pop", "Country", "Acid-House"]);
    const [selectedGenre, setSelectedGenre] = useState('');

    useEffect(() => {
        const fetchGenres = async () => {
            const response = await Axios.get('http://localhost:8000/api/genres/');
            setGenres(response.data);
        };

        fetchGenres();
    }, []);

    function handleGenreChange(genre){
        setSelectedGenre(genre);
        console.log("Selected genre: ", genre);
    }

    const handleNext = async () => {
        if (selectedGenre) {
            const response = await Axios.post('http://localhost:8000/api/artists/', { name: selectedGenre });
            console.log('PUT response:', response.data);
            onNext();
        } else {
            console.log("No genre selected.");
        }
    };

    return(
        <div className="main-div">
            <h1 className="survey-title">What is your favourite genre!</h1>
            <ul className="genres-list">
            {genres.map((genre, index) => (
                <li key={index}> 
                    <button className={`genre-button ${selectedGenre === genre.name ? 'selected' : ''}`}
                            onClick={() => handleGenreChange(genre.name)}>
                        {genre.name}
                    </button>
                </li>
            ))}
            </ul>
            <div className="button-container">
                <button className="button prev-page" onClick={onNext}>Go Back</button>
                <button className="button next-page" onClick={handleNext}>Next</button>
            </div>
        </div>
    );
}

export default GenreComponent;