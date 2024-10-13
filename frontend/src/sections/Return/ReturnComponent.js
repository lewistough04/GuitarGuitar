import "./ReturnComponent.css"
import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import Axios from "axios";

function ReturnComponent(){
    const location = useLocation();
    const navigate = useNavigate();
    const [guitars, setGuitars] = useState([]);
    const [guitarIndex, setGuitarIndex] = useState(0);

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
        setGuitarIndex((prev) => (prev+1) % guitars.length);
        console.log(guitarIndex)
    }

    const handleDivClick = () => {
        const currentGuitar = guitars[guitarIndex];
        const sku = currentGuitar.sku; // Assuming the SKU is a property in the current guitar object
        const url = `https://www.guitarguitar.co.uk/product/${sku}`;
        window.open(url, "_blank");
    };

    if (guitars.length === 0) {
        return <div className="loading-gear">Loading gear...</div>;
    }

    const currentGuitar = guitars[guitarIndex];

    return(
        <>
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
        <div className="button-container">
            <button className="next-button" onClick={nextGuitar}>Next</button>
        </div>
        </>
    );
}

export default ReturnComponent;