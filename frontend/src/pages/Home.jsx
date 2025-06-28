import React from "react";
import { Link } from "react-router-dom";

function Home() {
    return (
        <div>
            <h1>Welcome to Lanchonete App</h1>
            <nav>
                <Link to="/products">View Products</Link>
            </nav>
        </div>
    );
}

export default Home;