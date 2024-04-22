import React from "react"
import { SocketContext, socket } from "./contexts/SocketContext";
import Header from "./components/Header";
import Footer from "./components/Footer";
import STSection from "./components/STSection";
import { Container } from "@mui/material";

function App() {
  return (
      <SocketContext.Provider value={socket}>
        <div className="App">
          <Header/>
          <Container maxWidth="md">
            <STSection/>
          </Container>
          <Footer/>
        </div>
      </SocketContext.Provider>
  );
}

export default App;
