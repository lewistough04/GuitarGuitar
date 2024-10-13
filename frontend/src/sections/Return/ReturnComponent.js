import "./ReturnComponent.css"
import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import Axios from "axios";

function ReturnComponent(){
    const location = useLocation();
    const navigate = useNavigate();
    const [guitars, setGuitars] = useState([]);
    const [guitarIndex, setGuitarIndex] = useState(0);
    const [maxPrice, setMaxPrice] = useState(2000);

    useEffect(() => {
        const fetchGuitars = async () => {
            try {
                const artistNames = location.state?.artists || []; 
                const response = await Axios.post("http://localhost:8000/api/gear/", { artists: artistNames });
                setGuitars(response.data);
            } catch (error) {
                console.error("Error fetching guitar data:", error);
            }
        };

        fetchGuitars();
    }, [location.state]);

    const nextGuitar = () => {
        const filteredGuitars = guitars.filter(guitar => guitar.price <= maxPrice);
        
        setGuitarIndex((prevIndex) => (prevIndex + 1) % filteredGuitars.length);
        console.log(guitarIndex);
    };

    const handleDivClick = () => {
        const filteredGuitars = guitars.filter(guitar => guitar.price <= maxPrice);

        if (filteredGuitars.length > 0) {
            const currentGuitar = filteredGuitars[guitarIndex];
            const sku = currentGuitar.sku; // Assuming the SKU is a property in the current guitar object
            const url = `https://www.guitarguitar.co.uk/product/${sku}`;
            window.open(url, "_blank");
        }
    };

    const filteredGuitars = guitars.filter(guitar => guitar.price <= maxPrice);

    // if (filteredGuitars.length === 0) {
    //     return <div className="loading-gear">Nothing found within this price range!</div>;
    // }

    const currentGuitar = filteredGuitars[guitarIndex % filteredGuitars.length];

    return (
        <>
            <div className="filter-section">
                <label>
                    Max Price: £{maxPrice} 
                    <input
                        type="range"
                        min="0"
                        max="2000"
                        value={maxPrice}
                        onChange={e => setMaxPrice(Number(e.target.value))}
                    />
                </label>
            </div>

            {filteredGuitars.length === 0 ? (
                <div className="loading-gear">No guitars found within this price range!</div>
            ) : (
                <div className="return-div" onClick={handleDivClick} style={{ cursor: 'pointer' }}>
                    <div>
                        <img
                            src={currentGuitar.picture_main}
                            className="guitar-image"
                            alt={currentGuitar.item_name}
                        />
                    </div>

                    <div className="guitar-text">
                        <h2>{currentGuitar.item_name}</h2>
                        <h4>
                            {currentGuitar.price
                                ? currentGuitar.price.toLocaleString(undefined, {
                                    style: "currency",
                                    currency: "GBP",
                                  })
                                : "Price not available"}
                        </h4>
                        <p className="guitar-description">{currentGuitar.productDetail}</p>
                    </div>
                </div>
            )}

            <div className="button-container">
                <button className="next-button" onClick={nextGuitar} disabled={filteredGuitars.length === 0}>
                    Next
                </button>
            </div>
        </>
    );
}

export default ReturnComponent;