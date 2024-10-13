import "./ReturnComponent.css"
import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";

function ReturnComponent(){

    const guitars = [
        { "SKU_ID": "240409422030008", 
            "ASN": "", 
            "Category": "GUAG_1", 
            "Online": true, 
            "ItemName": "Metropolis Composer Element Electro Acoustic Guitar ", 
            "Title": "", 
            "BrandName": "Godin", 
            "Description": null, 
            "ProductDetail": `The Metropolis Composer LR Baggs Element, which is part of the Godin Acoustic lineup, is absolutely stunning and a real joy to play! It comes in a classic dreadnought size, perfect for that big and full sound.\nThe body is made of a Mahogany construction with a smooth semi-gloss finish—with a solid Mahogany top and back, which are complemented by layered Mahogany sides.\nThis guitar also has a Mahogany neck, so you can be sure to get rich and rounded tones, all the while being very well balanced with the addition of a Richlite fretboard, an Ebony bridge, and a 25.5” scale.\nAlso included is the LR Baggs system for convenient plug-and-play performance. Naturally, the Metropolis Composer LR Baggs Element is made right here in Canada!`,
            "SalesPrice": 939.0, 
            "PictureMain": "https://images.guitarguitar.co.uk/cdn/large/170/240409422030008f.jpg", 
            "QtyInStock": 1, 
            "QtyOnOrder": 10, 
            "Colour": 7, 
            "Pickup": 1, 
            "BodyShape": 10, 
            "CreatedOn": "2024-04-19T11:24:06.757", 
            "ImageUrls": null, 
            "Rating": 10.0, 
            "GlasgowQty": 1, 
            "EdinburghQty": 1, 
            "NewcastleQty": 0 
        }, 
        { "SKU_ID": "240409422030008", 
            "ASN": "", 
            "Category": "GUAG_1", 
            "Online": true, 
            "ItemName": "Metropolis Composer Element Electro Acoustic Guitar ", 
            "Title": "", 
            "BrandName": "Godin", 
            "Description": null, 
            "ProductDetail": "Product 2",
            "SalesPrice": 939.0, 
            "PictureMain": "https://images.guitarguitar.co.uk/cdn/large/170/240409422030008f.jpg", 
            "QtyInStock": 1, 
            "QtyOnOrder": 10, 
            "Colour": 7, 
            "Pickup": 1, 
            "BodyShape": 10, 
            "CreatedOn": "2024-04-19T11:24:06.757", 
            "ImageUrls": null, 
            "Rating": 10.0, 
            "GlasgowQty": 1, 
            "EdinburghQty": 1, 
            "NewcastleQty": 0 
        }
    ];

    // assume i am getting from api and returns in format 
    // array of dictionaries
    const location = useLocation();
    //const guitars = location.state?.gear || [];
    const [guitarIndex, setGuitarIndex] = useState(0);

    const nextGuitar = () => {
        setGuitarIndex((prev => ((prev+1) % guitars.length)));
        console.log(guitarIndex)
    }

    if (guitars.length === 0) {
        return <div>No gear available.</div>;
    }

    const currentGuitar = guitars[guitarIndex];
    //const fetchGuitars = async () => {
      //  const res = await fetch(url);
        //const d = await res.json();
        //return setGuitar(d);
    //}
    
    //useEffect(() => {
      //  fetchGuitars();
    //}, []);

    return(
        <div className="return-div">
            <div>
                <img
                    src={currentGuitar.PictureMain}
                    className="guitar-image"
                    alt={currentGuitar.ItemName}
                />
                <button className="next-button" onClick={nextGuitar}>Next</button>
            </div>

            <div className="guitar-text">
                <h2>{currentGuitar.ItemName}</h2>
                <h4>
                    {currentGuitar.SalesPrice
                        ? currentGuitar.SalesPrice.toLocaleString(undefined, {
                            style: "currency",
                            currency: "GBP",
                          })
                        : "Price not available"}
                </h4>
                <p className="guitar-description">{currentGuitar.ProductDetail}</p>
            </div>
        </div>
    );
}

export default ReturnComponent;