<script setup>
    import RestoNav from "../components/RestoNav.vue"
    import MenuCard from "../components/MenuCard.vue"
    import Footer2 from "../components/Footer2.vue" 
    import { onMounted, ref } from "vue";
    import axios from "axios"; // Import axios here
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

    const calculateTotalAmount = () => {
        total_amount.value = 0
        for (let i = 0; i < cartItems.value.length; i++) {
            total_amount.value += (cartItems.value[i].item_price * cartItems.value[i].count)
        }
        return total_amount.value
    }
        
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

    const remove_from_cart = async (cart_item_id) => {
        try {
            const response = await axios.delete(`${baseUrl.value}/cart_items/${cart_item_id}`)
            alert("deleted successfully")
            get_cart_items()
        } catch(error) {
            alert(error.response.message)
        }
    }

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

            <!-- <div class="border-2 p-20 bg-[#FAFFFB]">
                <h2 class="text-2xl mb-4 font-bold">My Orders</h2>

                <div class=" w-96">
                    <div class="flex justify-center">
                        <p class="text-2xl font-semibold mb-5 text-rgreen-200">Your Order</p>
                    </div>
                    <div class="flex justify-center">
                        <img class="w-20" src="../img/icons/image 12.png" alt="">
                    </div>
                    <div class="flex justify-center">
                        <span class="text-gray-400">Your cart is empty. Add items to get started</span>
                    </div>
                </div>
                <div>
                    <div v-for="cart_item in cartItems" class="flex items-center justify-between w-full">
                        <div class="text-sm">
                            <span>{{ cart_item.item_name }}</span>
                            <span>{{ cart_item.item_price }}</span>
                            <span>{{ cart_item.count }}</span>
                        </div>
                        <div @click="remove_from_cart(cart_item.id)" class="hover:scale-105 transition-transform duration-300 ease-in-out">
                            <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="20" height="30" viewBox="0 0 100 100">
                                <path fill="#f37e98" d="M25,30l3.645,47.383C28.845,79.988,31.017,82,33.63,82h32.74c2.613,0,4.785-2.012,4.985-4.617L75,30"></path><path fill="#f15b6c" d="M65 38v35c0 1.65-1.35 3-3 3s-3-1.35-3-3V38c0-1.65 1.35-3 3-3S65 36.35 65 38zM53 38v35c0 1.65-1.35 3-3 3s-3-1.35-3-3V38c0-1.65 1.35-3 3-3S53 36.35 53 38zM41 38v35c0 1.65-1.35 3-3 3s-3-1.35-3-3V38c0-1.65 1.35-3 3-3S41 36.35 41 38zM77 24h-4l-1.835-3.058C70.442 19.737 69.14 19 67.735 19h-35.47c-1.405 0-2.707.737-3.43 1.942L27 24h-4c-1.657 0-3 1.343-3 3s1.343 3 3 3h54c1.657 0 3-1.343 3-3S78.657 24 77 24z"></path><path fill="#1f212b" d="M66.37 83H33.63c-3.116 0-5.744-2.434-5.982-5.54l-3.645-47.383 1.994-.154 3.645 47.384C29.801 79.378 31.553 81 33.63 81H66.37c2.077 0 3.829-1.622 3.988-3.692l3.645-47.385 1.994.154-3.645 47.384C72.113 80.566 69.485 83 66.37 83zM56 20c-.552 0-1-.447-1-1v-3c0-.552-.449-1-1-1h-8c-.551 0-1 .448-1 1v3c0 .553-.448 1-1 1s-1-.447-1-1v-3c0-1.654 1.346-3 3-3h8c1.654 0 3 1.346 3 3v3C57 19.553 56.552 20 56 20z"></path><path fill="#1f212b" d="M77,31H23c-2.206,0-4-1.794-4-4s1.794-4,4-4h3.434l1.543-2.572C28.875,18.931,30.518,18,32.265,18h35.471c1.747,0,3.389,0.931,4.287,2.428L73.566,23H77c2.206,0,4,1.794,4,4S79.206,31,77,31z M23,25c-1.103,0-2,0.897-2,2s0.897,2,2,2h54c1.103,0,2-0.897,2-2s-0.897-2-2-2h-4c-0.351,0-0.677-0.185-0.857-0.485l-1.835-3.058C69.769,20.559,68.783,20,67.735,20H32.265c-1.048,0-2.033,0.559-2.572,1.457l-1.835,3.058C27.677,24.815,27.351,25,27,25H23z"></path><path fill="#1f212b" d="M61.5 25h-36c-.276 0-.5-.224-.5-.5s.224-.5.5-.5h36c.276 0 .5.224.5.5S61.776 25 61.5 25zM73.5 25h-5c-.276 0-.5-.224-.5-.5s.224-.5.5-.5h5c.276 0 .5.224.5.5S73.776 25 73.5 25zM66.5 25h-2c-.276 0-.5-.224-.5-.5s.224-.5.5-.5h2c.276 0 .5.224.5.5S66.776 25 66.5 25zM50 76c-1.654 0-3-1.346-3-3V38c0-1.654 1.346-3 3-3s3 1.346 3 3v25.5c0 .276-.224.5-.5.5S52 63.776 52 63.5V38c0-1.103-.897-2-2-2s-2 .897-2 2v35c0 1.103.897 2 2 2s2-.897 2-2v-3.5c0-.276.224-.5.5-.5s.5.224.5.5V73C53 74.654 51.654 76 50 76zM62 76c-1.654 0-3-1.346-3-3V47.5c0-.276.224-.5.5-.5s.5.224.5.5V73c0 1.103.897 2 2 2s2-.897 2-2V38c0-1.103-.897-2-2-2s-2 .897-2 2v1.5c0 .276-.224.5-.5.5S59 39.776 59 39.5V38c0-1.654 1.346-3 3-3s3 1.346 3 3v35C65 74.654 63.654 76 62 76z"></path><path fill="#1f212b" d="M59.5 45c-.276 0-.5-.224-.5-.5v-2c0-.276.224-.5.5-.5s.5.224.5.5v2C60 44.776 59.776 45 59.5 45zM38 76c-1.654 0-3-1.346-3-3V38c0-1.654 1.346-3 3-3s3 1.346 3 3v35C41 74.654 39.654 76 38 76zM38 36c-1.103 0-2 .897-2 2v35c0 1.103.897 2 2 2s2-.897 2-2V38C40 36.897 39.103 36 38 36z"></path>
                            </svg>
                        </div>
                    </div>
                    <div class="flex justify-between mt-10">
                        <span class="font-bold">Total Amount</span>
                        <span>{{ total_amount }}</span>
                    </div>
                    <button @click="place_order()" class=" w-full bg-rgreen-100 hover:text-ryellow text-white font-semibold p-2 rounded transform hover:scale-105 transition-transform duration-300 ease-in-out mt-5" >
                        Place Order
                    </button>
                    </div>
            </div> -->
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