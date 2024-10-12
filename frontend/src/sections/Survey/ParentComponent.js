import React, { useState } from 'react';
import GenreComponent from './GenreComponent';
import ArtistSelectionComponent from './ArtistSelectionComponent';

const ParentComponent = () => {
    const [currentComponent, setCurrentComponent] = useState('genre'); 

    const goToNextComponent = () => {
        setCurrentComponent('artist');
    }
    return (
        <div>
            {currentComponent === 'genre' && (
                <GenreComponent onNext={goToNextComponent} />
            )}
            {currentComponent === 'artist' && <ArtistSelectionComponent/>}
        </div>
    );
};

export default ParentComponent;