import React, { useState } from 'react';
import { Card } from 'react-bootstrap';

function Store() {
  // Replace this with actual data
  const [products, setProducts] = useState([
    { id: 1, name: 'T-shirts', description: 'This is product 1', price: '$100' },
    { id: 2, name: 'wildlife figures', description: 'This is product 2', price: '$200' },
    // Add more products as needed
  ]);

  return (
    <div>
      <h2>OUR STORE</h2>
      {products.map((product) => (
        <Card key={product.id} style={{ width: '18rem' }}>
          <Card.Body>
            <Card.Title>{product.name}</Card.Title>
            <Card.Text>{product.description}</Card.Text>
            <Card.Text>{product.price}</Card.Text>
          </Card.Body>
        </Card>
      ))}
    </div>
  );
}

export default Store;
