import React from 'react';
import HeaderComponent from './sections/Header/HeaderComponent';
import FooterComponent from './sections/Footer/FooterComponent';
import ParentComponent from './sections/Survey/ParentComponent';

function Main() {

    return (
        <div>
            <HeaderComponent/>
            <ParentComponent/>
            <FooterComponent/>
        </div>
    )
}

export default Main;