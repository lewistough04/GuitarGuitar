import "./GenreComponent.css"
import React, { useEffect, useState } from "react";
import Axios from "axios";

function GenreComponent(){

    const [genres, setGenres] = useState(["Rock & Roll", "Pop", "Country", "Acid-House"]);
    const [selectedGenre, setSelectedGenre] = useState('');
    const [error, setError] = useState([]);
    const [loading, setLoading] = useState([]);

    useEffect(() => {
        const fetchGenres = async () => {
            try {
                const response = await Axios.get('http://localhost:8000/api/genres/');
                setGenres(response.data);
            } catch (error) {
                setError(error);
            } finally {
                setLoading(false);
            }
        };

        fetchGenres();
    }, []);

    function handleGenreChange(genre){
        setSelectedGenre(genre);
        console.log("Selected genre: ", genre);
    }

    if (loading) return <div className="error-message">Loading genres...</div>;
    if (error) return <div className="error-message">Error fetching genres: {error.message}</div>;

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
            <button className="next-page">Next</button>
        </div>
    );
}

export default GenreComponent;