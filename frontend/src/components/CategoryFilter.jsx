import React from "react";

function CategoryFilter({ selectedCategory, onCategoryChange }) {
  const categories = ['TODAS', 'LANCHES', 'BEBIDAS', 'PORCOES', 'SOBREMESAS', 'ADICIONAIS'];

  return (
    <div className="category-filter">
      {categories.map(cat => (
        <button
          key={cat}
          onClick={() => onCategoryChange(cat)}
          className={cat === selectedCategory ? 'active' : ''}
        >
          {cat}
        </button>
      ))}
    </div>
  );
}

export default CategoryFilter;
