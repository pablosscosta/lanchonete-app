import React, { useEffect, useState} from "react";
import api from '../services/api';
import ProductCard from "./ProductCard";

function ProductsList(){
    const [products, setProducts] = useState([]);

    useEffect(() => {
        api.get('produtos/')
            .then(res => setProducts(res.data.results))
            .catch(err => console.error(err));
    }, []);

    return (
        <div className="product-list">
            {products.map((produto) =>(
                <ProductCard key={produto.id} produto={produto}/>
            ))}
        </div>
    );
}

export default ProductsList;