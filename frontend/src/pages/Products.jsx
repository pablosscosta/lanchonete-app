import React, { useState } from 'react';
import CategoryFilter from '../components/CategoryFilter';
import ProductsList from '../components/ProductsList';

function Products() {
  const [selectedCategory, setSelectedCategory] = useState('');

  return (
    <div>
      <h1>Nossos Produtos</h1>
      
      <ProductsList
        selectedCategory={selectedCategory}
      />
    </div>
  );
}

export default Products;
