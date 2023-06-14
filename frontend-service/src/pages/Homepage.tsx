import React from 'react'
import BaseCard from '../components/BaseCard'
import '../styles/homepage.css'
import { useState, useEffect } from 'react'
function Homepage() {
  const backendURL = 'http://localhost:5000'
  useEffect(() => {
    // fetch(`${backendURL}/`)
    //   .then( res => res.json())
    //   .then( data => console.log(data["message"]))


    fetch( `${backendURL}/relay` , {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        relayNumber: '1'
      },
      body: JSON.stringify({
        relayNumber: '10',
        relayState: 0
      })
    })
    .then ( res => res.json())
    .then ( data => console.log(data["updatedRelayState"]))
  }, [])

  return (
    <div className='homepageContainer'>
      <BaseCard title='Light #1' />
    </div>
  )
}

export default Homepage
