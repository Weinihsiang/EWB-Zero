import React, { useState, useEffect } from 'react';

function DataDisplay() {
    const [data, setData] = useState([]);

    useEffect(() => {
        // Fetch data from Flask API when the component mounts
        fetchData();
    }, []);

    const fetchData = async () => {
        try {
            const response = await fetch(`${process.env.BACKEND_BASE_URL}/get_data`); // Fetch data from Flask API
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const jsonData = await response.json(); // Parse response as JSON
            setData(jsonData); // Update state with fetched data
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
        }
    };

    return (
        <div>
            <h1>Data Display</h1>
            <div>
                {data.map((item, index) => (
                    <div key={index}>
                        <p>Name: {item.name}</p>
                        <p>Location: {item.location}</p>
                        <p>Price: {item.price}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default DataDisplay;
