import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, useNavigate } from 'react-router-dom';
import GenreComponent from './GenreComponent';
import ArtistSelectionComponent from './ArtistSelectionComponent';

const ParentComponent = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<GenreComponent />} />
                <Route path="/artists" element={<ArtistSelectionComponent />} />
            </Routes>
        </Router>
    );
};

export default ParentComponent;