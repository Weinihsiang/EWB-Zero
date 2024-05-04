import CardPreview from "./Components/CardPreview/CardPreview.js";
import Header from "./Components/Header/Header.js";
import styles from "./App.module.css";
import {useState, useEffect} from "react";
import Product from "./Components/Product/Product.js";

function App() {

  const [data, setData] = useState([{'name': 'Name', 'location': 'Location Details', 'price': '$5.00'},
  {'name': 'Michael', 'location': 'Location Details', 'price': '$5.00'},
  {'name': 'Name', 'location': 'Location Details', 'price': '$5.00'},
  {'name': 'Name', 'location': 'Location Details', 'price': '$5.00'},
  {'name': 'Name', 'location': 'Location Details', 'price': '$5.00'},
  {'name': 'Name', 'location': 'Location Details', 'price': '$5.00'},
  ]);

  const [productDetails, setProductDetails] = useState(-1);

  useEffect(() => {
      // Fetch data from Flask API when the component mounts
      fetchData();
  }, []);

  const fetchData = async () => {
      try {
          const response = await fetch(`${process.env.BACKEND_BASE_URL}/get_data`); // Fetch data from Flask API
          if (!response.ok) {
              throw new Error('Network response was not ok');
          }
          const jsonData = await response.json(); // Parse response as JSON
          setData(jsonData); // Update state with fetched data
      } catch (error) {
          console.error('There was a problem with the fetch operation:', error);
      }
  };

  return (
    <div className={styles.App}>
        <Header setData={setData} />
        <div className={styles.cards}>
          {data.map((card, index) => (
            <CardPreview name={card.name} location={card.location} price={card.price} key={index} index={index} setProductDetails={setProductDetails} />
          ))}
        </div>
        {productDetails !== -1 && <Product name={data[productDetails].name}
                                           description={data[productDetails].description}
                                           price={data[productDetails].price}
                                           location={data[productDetails].location}
                                           email={data[productDetails].email}
                                           setProductDetails={setProductDetails} />}
    </div>
  );
}

export default App;
