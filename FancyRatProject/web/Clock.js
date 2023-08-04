import React, { useEffect, useState } from 'react';

function Clock() {
    // Clock component state
    const [date, setDate] = useState(new Date());

    // Set the timer in the useEffect hook
    useEffect(() => {
        const timer = setInterval(() => {
            setDate(new Date());
        }, 1000);

        return () => clearInterval(timer);
    }, []);

    // Component output
    return (
        <div>
            <h1>Hello, world!</h1>
            <h2>It is {date.toLocaleTimeString()}.</h2>
        </div>
    )
};

export default Clock;
