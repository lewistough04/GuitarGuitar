import React, { useEffect, useState } from "react";
import Axios from "axios";
import "./ArtistSelectionComponent.css";
import { useNavigate, useParams } from 'react-router-dom';


function ArtistSelectionComponent() {
    const { genre } = useParams();
    const [artists, setArtists] = useState([]); 
    const [selectedArtists, setSelectedArtists] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchArtists = async () => {
            try {
                const response = await Axios.get(`http://localhost:8000/api/${genre}/artists/`);
                setArtists(response.data);
                console.log('Fetched artists:', response.data);
            } catch (error) {
                console.error("Error fetching artists:", error);
            }
        };

        fetchArtists(); // Call the fetch function
    }, [genre]);

    useEffect(() => {
        console.log("Selected artists: ", selectedArtists);
    }, [selectedArtists]);

    const handleArtistChange = (artistName) => {
        setSelectedArtists(prevSelected => 
            prevSelected.includes(artistName)
                ? prevSelected.filter(a => a !== artistName)
                : [...prevSelected, artistName]
        );
        console.log("Selected artists: ", selectedArtists);
    };

    const handleNext = async () => {
        if (selectedArtists.length > 0) {
            console.log("Selected artists before POST:", selectedArtists);
            try {
                const response = await Axios.post('http://localhost:8000/api/gear/', {
                    artists: selectedArtists
                });
                console.log('Gear fetched from backend:', response.data);
                navigate('/return', { state: { gear: response.data } });
            } catch (error) {
                console.error("Error submitting artists:", error);
            }
        } else {
            console.log("No artists selected.");
        }
    };

    return (
        <div className="main-div">
            <h1 className="survey-title">Choose your favourite {genre} artists!</h1>
            <ul className="artists-list">
                {artists.map((artist, index) => (
                    <li key={index}>
                        <button 
                            className={`artist-button ${selectedArtists.includes(artist.name) ? 'selected' : ''}`}
                            onClick={() => handleArtistChange(artist.name)}
                        >
                            {artist.name}
                        </button>
                    </li>
                ))}
            </ul>
            <div className="button-container">
                <button className="button prev-page" onClick={() => navigate('/')}>Go Back</button>
                <button className="button next-page" onClick={handleNext}>Finish</button>
            </div>
        </div>
    );
}

export default ArtistSelectionComponent;