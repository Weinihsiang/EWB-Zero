import styles from "./Product.module.css"

export default function Product({name, description, price, location, email, setProductDetails}) {
  return (
    <div className={styles.blur}>
      <div>
        <div className={styles.productCard}>
          <div className={styles.info}>
            <h2>{name}</h2>
            <p>Farmer Email: {email}</p>
            <p>Price: {price}</p>
            <p>Location: {location}</p>
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
