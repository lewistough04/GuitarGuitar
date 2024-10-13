import "./ReturnComponent.css"
import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import Axios from "axios";

function ReturnComponent(){
    const location = useLocation();
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

    if (guitars.length === 0) {
        return <div className="loading-gear">Loading gear...</div>;
    }

    const currentGuitar = guitars[guitarIndex];

    return(
        <>
        <div className="return-div">
            <div>
                <img
                    src={currentGuitar.image_urls}
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
        <button className="next-button" onClick={nextGuitar}>Next</button>
        </>
    );
}

export default ReturnComponent;