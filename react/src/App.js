import CardPreview from "./Components/CardPreview/CardPreview.js";
import Header from "./Components/Header/Header.js";
import styles from "./App.module.css";
import {useState, useEffect} from "react";
import Product from "./Components/Product/Product.js";
import SubmitForm from "./Components/SubmitForm.js/SubmitForm.js";
import axios from "axios";

function App() {

  const [data, setData] = useState([]);

  const [productDetails, setProductDetails] = useState(-1);
  const [form, setForm] = useState(false)

  useEffect(() => {
      // Fetch data from Flask API when the component mounts
      fetchData();
      // importData();
  }, []);

  const fetchData = async () => {
      try {
          const {data} = await axios.post(`${process.env.REACT_APP_BACKEND_URL}/get_data`); // Fetch data from Flask API
          console.log("reached here");
          console.log(data);
          setData(data); // Update state with fetched data
      } catch (error) {
          console.log(error);
      }
  };

  return (
    <div className={styles.App}>
        <Header setData={setData} setForm={setForm} />
        <div className={styles.cards}>
          {data?.map((card, index) => (
            <CardPreview product={card.product}
                         location={card.location}
                         price={card.price}
                         key={index}
                         index={index}
                         setProductDetails={setProductDetails}
                         farmer_email={card.farmer_email}
                         farmer_name={card.farmer_name}
                         image = {card.image}
                          />
          ))}
        </div>
        {productDetails !== -1 && <Product product={data[productDetails].product}
                                           description={data[productDetails].description}
                                           price={data[productDetails].price}
                                           location={data[productDetails].location}
                                           email={data[productDetails].farmer_email}
                                           setProductDetails={setProductDetails} 
                                           farmer_name={data[productDetails].farmer_name}
                                           quantity={data[productDetails].quantity}
                                           image = {data[productDetails].image}
                                           />}
        
        {form && <SubmitForm setForm={setForm} />}
        
        <div className={styles.copyright}>
          
        <p>
          © 2024 Zero Waste Platform, Inc. Thank you so much for saving food by using our platform.
        </p>
      </div>
        
    </div>
  );
}

export default App;
