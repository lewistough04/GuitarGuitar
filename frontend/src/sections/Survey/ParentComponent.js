import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, useNavigate } from 'react-router-dom';
import GenreComponent from './GenreComponent';
import ArtistSelectionComponent from './ArtistSelectionComponent';
import Landing from '../../Landing';

const ParentComponent = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Landing />} />
                <Route path="/main" element={<GenreComponent/ >} />
                <Route path="/:genre/artists" element={<ArtistSelectionComponent />} />
            </Routes>
        </Router>
    );
};

export default ParentComponent;