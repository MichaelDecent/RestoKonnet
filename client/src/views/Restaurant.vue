<script setup>
    import RestoNav from "../components/RestoNav.vue"
    import Footer2 from "../components/Footer2.vue" 
    import { onMounted, ref } from "vue";
    import axios from "axios";
    import { useRoute } from 'vue-router';

    const restaurant = ref({});
    const items = ref([]);
    const cartItems = ref([])
    const customerId = ref("")
    const vendorId = ref("")
    const route = useRoute();
    const currentPath = ref('');
    const total_amount = ref()
    const baseUrl = ref('https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1')
    const currentUser = ref({})
    

    customerId.value = localStorage.getItem('customer_id')
    vendorId.value = localStorage.getItem('vendor_id')
    console.log(customerId.value)
    console.log(vendorId.value)

    // check and retrieve detail of the current user
    const getCurrentUser = async () => {
        try {
            if (customerId.value != null) {
                const response = await axios.get(`${baseUrl.value}/customers/${customerId.value}`)
                currentUser.value = response.data
            } else if (vendorId.value != null) {
                const response = await axios.get(`${baseUrl.value}/vendors/${vendorId.value}`)
                currentUser.value = response.data
            }
            return currentUser.value
        } catch(error) {
            alert(error)
        }
    }

    // calculates total amount
    const calculateTotalAmount = () => {
        total_amount.value = 0
        for (let i = 0; i < cartItems.value.length; i++) {
            total_amount.value += (cartItems.value[i].item_price * cartItems.value[i].count)
        }
        return total_amount.value
    }
      
    // retrieves a details of a particular restaurant
    const get_restaurants = async () => {
    try {
        // const token = localStorage.getItem('token');
        // const headers = { 'Authorization': `Bearer ${token}` };

        // Use axios.get to make a GET request
        const response = await axios.get(`${baseUrl.value}/${currentPath.value}`);
        restaurant.value = response.data
        
        } catch (error) {
            console.error(error);
        }
    }

    // retrives all customers item
    const get_items = async () => {
    try {
        // const token = localStorage.getItem('token');
        // const headers = { 'Authorization': `Bearer ${token}` };

        // Use axios.get to make a GET request
        const response = await axios.get(`${baseUrl.value}/${currentPath.value}/items`);
        items.value = response.data
        
        } catch (error) {
            console.error(error);
        }
    }

    // creates an item in the cart
    const add_to_cart = async (item_name, item_price, count=1) => {
        try {
            const formData = new FormData()
            
            formData.append("item_name", item_name)
            formData.append("item_price", item_price)
            formData.append("count", count)

            if (customerId.value != null) {
                formData.append("customer_id", customerId.value)
                const response = await axios.post(`${baseUrl.value}/${currentPath.value}/cart_items`, formData);
            } else if (vendorId.value != null) {
                formData.append("vendor_id", vendorId.value)
                const response = await axios.post(`${baseUrl.value}/${currentPath.value}/cart_items`, formData);
                console.log(response.data)
            }
            alert("added to cart sucessfully")
            get_cart_items()

        } catch(error) {
            alert(error)
        }
    }

    // retrieves all customer items added to a cart
    const get_cart_items = async () => {
        try {
            const queryParams = {};

            if (customerId.value != null) {
                queryParams.customer_id = customerId.value;
                const response = await axios.get(`${baseUrl.value}/${currentPath.value}/cart_items`, {
                    params: queryParams});
                cartItems.value = response.data
            } else if (vendorId.value != null) {
                queryParams.vendor_id = vendorId.value;
                const response = await axios.get(`${baseUrl.value}/${currentPath.value}/cart_items`, {
                    params: queryParams});
                cartItems.value = response.data
            }
            calculateTotalAmount()

        } catch(error) {
            alert(error)
        }
    }

    // deletes an item fromthe cart
    const remove_from_cart = async (cart_item_id) => {
        try {
            const response = await axios.delete(`${baseUrl.value}/cart_items/${cart_item_id}`)
            alert("deleted successfully")
            get_cart_items()
        } catch(error) {
            alert(error.response.message)
        }
    }

    // creates an order for a aprticular restaurant
    const place_order = async () =>  {
        getCurrentUser()
        try {
            const orderData = {
                items: cartItems.value,
                total_amount: total_amount.value,
                customer: currentUser.value,
            }
            const response = await axios.post(`${baseUrl.value}${currentPath.value}/orders`, orderData);
            alert("Order Sent Successfully")
        }catch(error){
            alert(error)
            console.log(error)

        }
    }

    onMounted( () => {
        currentPath.value = route.path;
        getCurrentUser()
        get_restaurants() 
        get_items()
        get_cart_items()
    });
    
</script>

<template>
    <div>
        <div class="bg-rgreen-100 border">
            <RestoNav/>
        </div>
        <div class="flex flex-wrap justify-center  lg:justify-between lg:mx-60 mx-5">
            <div class="lg:w-1/2" >
                <div class="w-96 h-96 lg:h-96 lg:w-full rounded-lg overflow-hidden mt-5 shadow-lg hover:shadow-2xl">
                    <img class="w-full h-full" :src="restaurant.image" alt="Card Image">
                </div>
                <div class="px-2 py-4 bg-white">
                    <h1 class="font-extrabold lg:text-4xl mb-2 w-auto mt-3">{{ restaurant.name}}</h1>
                    <p class="text-xl text-gray-600">{{ restaurant.address }}</p>
                </div>
            </div>
            <div class="bg-[#F2FCF2] py-12 sm:py-16 lg:py-20 w-96">
                <div class="mx-auto px-4 sm:px-6 lg:px-8">
                    <div class="flex items-center justify-center">
                        <h1 class="text-2xl font-semibold text-gray-900">Your Cart</h1>
                    </div>
    
                    <div class="mx-auto mt-8 max-w-2xl md:mt-12">
                        <div class="bg-white shadow">
                            <div class="px-4 py-6 sm:px-8 sm:py-10">
                                <div class="flow-root">
                                    <ul  v-for="cart_item in cartItems" class="-my-8">
                                        <li class="flex flex-col space-y-3 py-6 text-left sm:flex-row sm:space-x-5 sm:space-y-0">
                                            <div class="relative flex flex-1 flex-col justify-between">
                                                <div class="sm:col-gap-5 sm:grid sm:grid-cols-2">
                                                    <div class="pr-8 sm:pr-5">
                                                        <p class="text-base font-semibold text-gray-900">{{ cart_item.item_name }}</p>
                                                        <p class="mx-0 mt-1 mb-0 text-sm text-gray-400">{{ cart_item.item_price }}</p>
                                                    </div>
                            
                                                    <div class="mt-4 flex items-end justify-between sm:mt-0 sm:items-start sm:justify-end">
                                                        <div class="sm:order-1">
                                                            <div class="mx-auto flex h-8 items-stretch text-gray-600">
                                                                <button @click="cart_item.count--, calculateTotalAmount()" class="flex items-center justify-center rounded-l-md bg-gray-200 px-4 transition hover:bg-black hover:text-white">-</button>
                                                                     <div class="flex w-full items-center justify-center bg-gray-100 px-4 text-xs uppercase transition">{{ cart_item.count }}</div>
                                                                <button @click="cart_item.count++, calculateTotalAmount()" class="flex items-center justify-center rounded-r-md bg-gray-200 px-4 transition hover:bg-black hover:text-white">+</button>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                          
                                                <div class="flex justify-end sm:bottom-0 sm:top-auto">
                                                    <button @click="remove_from_cart(cart_item.id)" type="button" class="flex rounded p-2 text-center text-gray-500 transition-all duration-200 ease-in-out focus:shadow hover:text-gray-900">
                                                        <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class=""></path>
                                                        </svg>
                                                    </button>
                                                </div>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                  
                                <div class="mt-6 flex items-center justify-between">
                                    <p class="text-sm font-medium text-gray-900">Total</p>
                                    <p class="text-2xl font-semibold text-gray-900"><span class="text-xs font-normal text-gray-400">Naira</span>{{ total_amount }}</p>
                                </div>
                  
                                <div class="mt-6 text-center">
                                    <button @click="place_order()" type="button" class="group inline-flex w-full items-center justify-center rounded-md bg-rgreen-100 px-6 py-4 text-lg font-semibold text-white transition-all duration-200 ease-in-out focus:shadow hover:bg-ryellow">
                                            Place Order
                                        <svg xmlns="http://www.w3.org/2000/svg" class="group-hover:ml-8 ml-4 h-6 w-6 transition-all" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                            <path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6" />
                                        </svg>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="lg:mx-60 mx-5">
            <h2 class="text-rgreen-100 text-2xl lg:text-4xl font-poppins font-semibold break-words mt-5">All Menu</h2>
            <div class="mt-5 relative lg:grid lg:grid-cols-3 justify-center pb-5 lg:gap-32 w-1120px md:w-85vw overflow-x-auto flex flex-wrap">
                <div  v-for="item in items" class="w-96 h-96 border-2 border-rgreen-100 rounded-lg overflow-hidden mt-5 shadow-lg hover:shadow-2xl">
                    <img class="w-full h-3/4 transform hover:scale-105 transition-transform duration-300 ease-in-out" :src="item.image" alt="Card Image">
                    <div class="px-2 py-1 bg-white flex items-center justify-between">
                        <span class="font-bold lg:text-xl mb-2 w-auto mt-3">{{ item.name }}</span>
                        <div class="flex items-center gap-3">
                            <button @click="item.count++" class="text-xl">+</button>
                            <div class="rounded-full bg-[#DAEBDD] w-10 h-10 flex justify-center items-center">
                                <span>{{ item.count }}</span>
                            </div>
                            <button @click="item.count--" class="text-2xl">-</button>
                        </div>
                    </div>
                    <div class="flex justify-between items-center px-3 pb-1">
                        <span class="text-rgreen-100">Price - N{{ item.price }}</span>
                        <button @click="add_to_cart(item.name, item.price, item.count)" class="bg-rgreen-100 hover:text-ryellow text-white font-semibold p-1 rounded transform hover:scale-105 transition-transform duration-300 ease-in-out" >
                            Add to cart
                        </button>
                    </div> 
                </div>
            </div>
           
        </div>
        <div class="bg-rgreen-100 border">
            <Footer2/>
        </div>
    </div>
</template>