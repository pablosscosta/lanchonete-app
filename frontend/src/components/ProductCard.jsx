import React from "react";

function ProductCard({produto}){
    return(
        <div className="product-card">
            <img src={produto.imagem} alt={produto.nome} />
            <h3>{produto.nome}</h3>
            <p>{produto.descricao}</p>
            <p>Preço: R$ {produto.preco}</p>
            <p>{produto.disponivel ? "Disponível": "Indisponível"}</p>            
        </div>
    );
}

export default ProductCard;