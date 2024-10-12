import React, { useEffect, useState } from "react";
import Axios from "axios";
import "./ArtistSelectionComponent.css";
import { useNavigate, useLocation } from 'react-router-dom';

function ArtistSelectionComponent() {
    const location = useLocation(); 
    const [artists, setArtists] = useState(location.state?.artists || []); 
    const [selectedArtists, setSelectedArtists] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        if (!artists.length) {
            const fetchArtists = async () => {
                try {
                    const response = await Axios.get('http://localhost:8000/api/artists/');
                    if (Array.isArray(response.data)) {
                        setArtists(response.data);
                    } else if (response.data && response.data.name) {
                        setArtists([response.data]);
                    } else {
                        console.error("Unexpected response format:", response.data);
                    }
                } catch (error) {
                    console.error("Error fetching artists:", error);
                }
            };
            fetchArtists();
        }
    }, [artists]);

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
            try {
                const response = await Axios.put('http://localhost:8000/api/selected-artists/', {
                    artists: selectedArtists
                });
                console.log('PUT response:', response.data);
            } catch (error) {
                console.error("Error submitting artists:", error);
            }
        } else {
            console.log("No artists selected.");
        }
    };

    return (
        <div className="main-div">
            <h1 className="survey-title">Choose your favourite artists!</h1>
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