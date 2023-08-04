import React, { useEffect, useState } from 'react';

const API_URL = 'https://api.example.com/data';

function MyComponent() {
    // Set up state to store the data
    const [data, setData] = useState(null);

    // Set up the component to make an API call when it mounts
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(API_URL);
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                const data = await response.json();
                setData(data);
            } catch (error) {
                console.error(error);
            }
        };
        fetchData();
    }, []);

    // Render the data into the DOM
    return (
        <div>
            <p>{data ? data.name : 'Loading...'}</p>
        </div>
    );
}

export default MyComponent;