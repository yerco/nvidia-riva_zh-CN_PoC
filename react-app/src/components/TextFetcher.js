import React, { useState, useEffect } from 'react';

export function TextFetcher() {
    const [text, setText] = useState('Loading...');

    useEffect(() => {
        const eventSource = new EventSource(`http://localhost:5001/translation?${new Date().getTime()}`);
        eventSource.onmessage = function(event) {
            console.log("New message received:", event.data)
            setText(event.data);  // Update text whenever a new event is received
        };

        return () => {
            eventSource.close();  // Clean up the event source if the component unmounts
        };
    }, []);

    return <div><h3>{text}</h3></div>;
}
