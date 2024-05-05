import styles from "./Product.module.css"

export default function Product({product, description, price, location, email, setProductDetails, farmer_name, quantity}) {
  console.log(description);
  return (
    <div className={styles.blur}>
      <div>
        <div className={styles.productCard}>
          <div className={styles.info}>
            <h2>{product}</h2>
            <p>Farmer's Name: {farmer_name}</p>
            <p>Farmer's Email: {email}</p>
            <p>Price: {price}</p>
            <p>Location: {location}</p>
            <p>Quantity: {quantity}</p>
            <p>Description: {description}</p>
          </div>
          <div>
            <button className={styles.button} onClick={()=>{
              setProductDetails(-1);
            }}>Back</button>
          </div>
            {/* Display more product details as needed */}
        </div>
      </div>
    </div>
    
  )
}
