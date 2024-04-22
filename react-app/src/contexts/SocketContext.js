import React from 'react';
import io from 'socket.io-client';

export const socket = io(process.env.REACT_APP_BACKEND_URL, {
    reconnection: true,
    reconnectionDelay: 10000,
    reconnectionAttempts: 5,
}); // adjust URL
export const SocketContext = React.createContext();
