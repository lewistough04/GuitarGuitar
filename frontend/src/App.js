import React from 'react';
import { BrowserRouter, Route, Routes, useNavigate } from 'react-router-dom';
import './App.css';
import Landing from './Landing';
import Main from './Main';
import HeaderComponent from './sections/Header/HeaderComponent';
import GenreComponent from './sections/Survey/GenreComponent';
import ReturnComponent from './sections/Return/ReturnComponent';
import FooterComponent from './sections/Footer/FooterComponent';
import ParentComponent from './sections/Survey/ParentComponent';

function App() {
  return (
    <>
    <HeaderComponent/>
    <ParentComponent/>
    <FooterComponent/>
    </>
  );
}

export default App;
