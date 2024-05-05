import styles from "./SubmitForm.module.css"
import {useState} from "react"
import axios from "axios"

export default function SubmitForm({setForm}) {

    const [formData, setFormData] = useState({farmer_name: "",
                                      farmer_email: "",
                                      product: "",
                                      description: "",
                                      price: "",
                                      location: "",
                                      quantity: "",
                                      image: ""})

    const [error, setError] = useState("");

    const handleSubmit = async () => {
        try {
            if (formData.farmer_name === "" ||
                formData.farmer_email === "" || 
                formData.product === "" || 
                formData.price === "" || 
                formData.description === "" || 
                formData.image === "" || 
                formData.quantity === "" || 
                formData.location === ""
            ) {
                setError("All fields are required")
            } else {
                const {data} = await axios.post(`${process.env.REACT_APP_BACKEND_URL}/new_product`,
                    {
                        product: formData.product,
                        quantity: formData.quantity,
                        price: formData.price,
                        location: formData.location,
                        description: formData.description,
                        farmer_email: formData.farmer_email,
                        farmer_name: formData.farmer_name,
                        image: formData.image
                    }
                )
                console.log(data);
                setError();
                setFormData({farmer_name: "",
                farmer_email: "",
                product: "",
                description: "",
                price: "",
                location: "",
                quantity: "",
                image: ""});
                setForm(false);
            }
        } catch (error) {
            console.log(error);
        }
    }
  return (
    <div className={styles.blur}>
        <div className={styles.form}>
            <div className={styles.formWrap}>
                <div className={styles.formInputs}>
                    <span>Email</span>
                    <input type="email" onChange={(e) => {
                        setFormData((prev) => ({...prev, farmer_email: e.target.value}))
                    }} />
                    <span>Name</span>
                    <input type="text" onChange={(e) => {
                        setFormData((prev) => ({...prev, farmer_name: e.target.value}))
                    }} />
                    <span>Product Name</span>
                    <input type="text" onChange={(e) => {
                        setFormData((prev) => ({...prev, product: e.target.value}))
                    }} />
                    <span>Description</span>
                    <input type="text" onChange={(e) => {
                        setFormData((prev) => ({...prev, description: e.target.value}))
                    }} />
                    <span>Price</span>
                    <input type="text" onChange={(e) => {
                        setFormData((prev) => ({...prev, price: e.target.value}))
                    }} />
                    <span>Quantity</span>
                    <input type="text" onChange={(e) => {
                        setFormData((prev) => ({...prev, quantity: e.target.value}))
                    }} />
                    <span>Location</span>
                    <input type="text" onChange={(e) => {
                        setFormData((prev) => ({...prev, location: e.target.value}))
                    }} />
                    <span>Image Link</span>
                    <input type="text" onChange={(e) => {
                        setFormData((prev) => ({...prev, image: e.target.value}))
                    }} />
                </div>
                <div className={styles.buttons}>
                    <button onClick={handleSubmit}>Submit</button>
                    <button onClick={() => {
                        setFormData({farmer_name: "",
                                      farmer_email: "",
                                      product: "",
                                      description: "",
                                      price: "",
                                      location: "",
                                      quantity: "",
                                      image: ""});
                        setForm(false);
                    }}>Cancel</button>
                </div>
                <div className={styles.error}>
                    {error}
                </div>
            </div>
        </div>
    </div>
  )
}
