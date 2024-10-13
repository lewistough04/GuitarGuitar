import React from 'react';
import { BrowserRouter, Route, Routes, useNavigate } from 'react-router-dom';
import './App.css';
import HeaderComponent from './sections/Header/HeaderComponent';
import FooterComponent from './sections/Footer/FooterComponent';
import ParentComponent from './sections/Survey/ParentComponent';

function App() {
  return (
    <div className="app-container">
      <HeaderComponent />
      <div className="parent-component">
        <ParentComponent />
      </div>
      <FooterComponent />
    </div>
  );
}

export default App;
