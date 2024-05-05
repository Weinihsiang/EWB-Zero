// Mock data for the cards
import styles from "./CardPreview.module.css"
import { useState } from "react";
import axios from "axios";

export default function CardPreview({image, product, location, price, setProductDetails, index, farmer_email, farmer_name}) {
  const [email, setEmail] = useState('');
  const [success, setSuccess] = useState(false);
  const [isHovered, setIsHovered] = useState(false);

  const handleSubmit = async () => {
    try {
      if (email !== "sent") {
        // Send email request to your Flask server
        axios.post(`${process.env.REACT_APP_BACKEND_URL}/send_email`,
        { user_email: email, farmer_email: farmer_email, farmer_name: farmer_name, product: product }).then((response) => (console.log('Email request sent successfully:', response.data)));
        setEmail('');
        setSuccess(true);
      }
    } catch (error) {
      console.log(error);
      
    }
  };

  return (
    <div className={styles.card}>
      <img
        src={image}
        className={`${styles.image} ${isHovered ? styles.imageHovered : ''}`}
        onClick={() => setProductDetails(index)}
        onMouseEnter={() => setIsHovered(true)}
        onMouseLeave={() => setIsHovered(false)}
      />
      <div className={styles.info}v>
        <h4>{product}</h4>
        <span>{location}</span>
        <span>{price}</span>
        <input
          type="email"
          placeholder="Enter your email address"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <button type="submit" onClick={handleSubmit}>{success ? "Request Sent!" : "Send Request"}</button>
      </div>
    </div>
  )
}
