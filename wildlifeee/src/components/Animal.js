import React, { useState } from 'react';

function Animals() {
  // Initialize state with useState hook
  const [animals, setAnimals] = useState(['Lion', 'Tiger', 'Elephant', 'Giraffe']);

  return (
    <div>
      <h2>OUR ANIMALS</h2>
      {animals.map((animal, index) => (
        <div key={index}>
          <h3>{animal}</h3>
        </div>
      ))}
    </div>
  );
}

export default Animals;
