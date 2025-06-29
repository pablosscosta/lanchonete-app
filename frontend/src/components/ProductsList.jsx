import React, { useState, useEffect } from "react";
import api from '../services/api';
import CategoryFilter from './CategoryFilter';
import ProductCard from './ProductCard';

function ProductsList() {
  const [products, setProducts] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('TODAS');

  useEffect(() => {
    let url = 'produtos/';
    if (selectedCategory !== 'TODAS') {
      url += `?categoria=${selectedCategory}`;
    }

    api.get(url)
        .then(res => {
        setProducts(res.data.results);
        })
        .catch(err => console.error(err));
  }, [selectedCategory]);

  return (
    <div>
      <CategoryFilter selectedCategory={selectedCategory} onCategoryChange={setSelectedCategory} />
      <div className="products-grid">
        {products.map(p => <ProductCard key={p.id} produto={p} />)}
      </div>
    </div>
  );
}

export default ProductsList;
