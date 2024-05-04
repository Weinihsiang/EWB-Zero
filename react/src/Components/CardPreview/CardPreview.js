// Mock data for the cards
import styles from "./CardPreview.module.css"
import { useState } from "react";
import axios from "axios";

export default function CardPreview({name, location, price, setProductDetails, index}) {
  const [email, setEmail] = useState('');

  const handleSubmit = async () => {
    try {
      // Send email request to your Flask server
      const response = await axios.post(`${process.env.REACT_APP_BACKEND_URL}/send_email`, { email });
      console.log('Email request sent successfully:', response.data);
      // Handle any success response here
    } catch (error) {
      console.error('Error sending email request:', error);
      // Handle any error here
    }
  };

  return (
    <div className={styles.card}>
      <img src="" className={styles.image} onClick={() => {setProductDetails(index)}} />
      <div className={styles.info}v>
        <h4>{name}</h4>
        <span>{location}</span>
        <span>{price}</span>
        <input
          type="email"
          placeholder="Enter your email address"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <button type="submit" onClick={handleSubmit}>Send Request</button>
      </div>
    </div>
  )
}
