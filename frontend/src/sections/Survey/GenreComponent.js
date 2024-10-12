import "./GenreComponent.css"
import React, { useEffect, useState } from "react";
import Axios from "axios";
import { useNavigate } from 'react-router-dom';

function GenreComponent({ onNext }){

    const [genres, setGenres] = useState([]);
    const [selectedGenre, setSelectedGenre] = useState('');
    const navigate = useNavigate();

    useEffect(() => {
        const fetchGenres = async () => {
            try {
                const response = await Axios.get('http://localhost:8000/api/genres/');
                setGenres(response.data);
            } catch (error) {
                console.error("Error fetching genres:", error);
            }
        };

        fetchGenres();
    }, []);

    const handleGenreChange = (genre) => {
        setSelectedGenre(genre);
        console.log("Selected genre: ", genre);
    }

    const handleNext = async () => {
        if (selectedGenre) {
            navigate(`/${selectedGenre}/artists`)
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
                <button className="next-page" onClick={handleNext}>Next</button>
            </div>
        </div>
    );
}

export default GenreComponent;