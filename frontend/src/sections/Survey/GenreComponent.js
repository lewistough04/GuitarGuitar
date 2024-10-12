import "./GenreComponent.css"
import React, { useEffect, useState } from "react";
import Axios from "axios";

function GenreComponent({ onNext }){

    const [genres, setGenres] = useState(["Rock & Roll", "Pop", "Country", "Acid-House"]);
    const [selectedGenre, setSelectedGenre] = useState('');
    const [error, setError] = useState([]);
    const [loading, setLoading] = useState([]);

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
            
            <button className="next-page" onClick={onNext}>Next</button>
        </div>
    );
}

export default GenreComponent;