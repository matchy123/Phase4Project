import React from 'react';
import { NavLink } from 'react-router-dom';

function Link({ wildlifeData }) {
    console.log("props")
    console.log(wildelifeData)
  return (
    <div className="">
        <h1>Genre: {wildlifeData.genre}</h1>
        <p>Title: {wildlifeData.Title}</p>
        <h5>Platform: {wildelifeData.Platform}</h5>
        <button>price: {wildlife.price}</button>

        </div>
  );
}

export default wildlifeee;
