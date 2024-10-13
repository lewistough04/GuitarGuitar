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
    const [selectedCategory, setSelectedCategory] = useState("")

    useEffect(() => {
        const fetchGuitars = async () => {
            try {
                const artistNames = location.state?.artists || []; 
                const response = await Axios.post("https://api.dyhtg.com/api/gear/", { artists: artistNames });
                setGuitars(response.data);
            } catch (error) {
                console.error("Error fetching guitar data:", error);
            }
        };

        fetchGuitars();
    }, [location.state]);

    const filteredGuitars = guitars.filter(guitar => {
        const withinPriceRange = guitar.price <= maxPrice;
        const matchesCategory = selectedCategory ? guitar.category === selectedCategory : true;
        return withinPriceRange && matchesCategory;
    });

    const nextGuitar = () => {
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
                <label>
                    Category:
                    <select value={selectedCategory} onChange={e => setSelectedCategory(e.target.value)}>
                        <option value="">All</option>
                        <option value="GUBA">Bass Guitars</option>
                        <option value="ACC">Acoustic Guitars</option>
                        <option value="GUEG">Electric Guitars</option>
                        <option value="GUAC">Guitar Accessories</option>
                        <option value="PEDL">Pedals</option>
                        <option value="AMP">Amps</option>
                    </select>
                </label>
            </div>

            {filteredGuitars.length === 0 ? (
                <div className="loading-gear">No items found within these filters!</div>
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