import React, { useEffect, useState } from "react";
import Axios from "axios";
import "./ArtistSelectionComponent.css"

function ArtistSelectionComponent({onNext}){
    const [artists, setArtists] = useState([]);
    const [selectedArtists, setSelectedArtists] = useState([]);

    useEffect(() => {
        const fetchArtists = async () => {
            try {
                const response = await Axios.get('http://localhost:8000/api/artists/'); 
                setArtists(response.data);
            } catch (error) {
                console.error("Error fetching artists:", error);
            }
        };

        fetchArtists();
    }, []);

    const handleArtistChange = (artist) => {
        if (selectedArtists.includes(artist)) {
            setSelectedArtists(selectedArtists.filter(a => a !== artist));
        } else {
            setSelectedArtists([...selectedArtists, artist]);
        }
        console.log("Selected artists: ", selectedArtists);
    };

    const handleNext = async () => {
        if (selectedArtists.length > 0) {
            try {
                const response = await Axios.put('http://localhost:8000/api/selected-artists/', {
                    artists: selectedArtists 
                });
                console.log('PUT response:', response.data);
                onNext(); 
            } catch (error) {
                console.error("Error submitting artists:", error);
            }
        } else {
            console.log("No artists selected.");
        }
    };

    return(
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
                <button className="button prev-page" onClick={onNext}>Go Back</button>
                <button className="button next-page" onClick={handleNext}>Next</button>
            </div>
        </div>
    );
}

export default ArtistSelectionComponent;