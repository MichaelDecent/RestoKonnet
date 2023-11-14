<script setup>
    import RestoNav from "../components/RestoNav.vue"
    import MenuCard from "../components/MenuCard.vue"
    import Footer2 from "../components/Footer2.vue" 
    import { onMounted, ref } from "vue";
    import axios from "axios"; // Import axios here
    import { useRoute } from 'vue-router';

    const restaurant = ref({});
    const items = ref([]);
    const route = useRoute();
    const currentPath = ref('');

    
    const get_restaurants = async () => {
    try {
        // const token = localStorage.getItem('token');
        // const headers = { 'Authorization': `Bearer ${token}` };

        // Use axios.get to make a GET request
        const response = await axios.get(`https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1${currentPath.value}`);
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
        const response = await axios.get(`https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1${currentPath.value}/items`);
        items.value = response.data
        
        } catch (error) {
            console.error(error);
        }
    }

    onMounted(() => {
        currentPath.value = route.path;
        get_restaurants();
        get_items()
    });
    console.log(restaurant)
    console.log(items)
</script>

<template>
    <section>
        <div class="bg-rgreen-100 p-10">
            <RestoNav/>
        </div>
        <div class="flex justify-between">
            <div class="p-10" >
                <div class="h-96 w-96 rounded-lg overflow-hidden mt-5 shadow-lg hover:shadow-2xl transform hover:scale-105 transition-transform duration-300 ease-in-out">
                    <img class="w-full h-full" :src="restaurant.image" alt="Card Image">
                </div>
                <div class="px-2 py-4 bg-white">
                    <h1 class="font-extrabold lg:text-4xl mb-2 w-auto mt-3">{{ restaurant.name}}</h1>
                    <p class="text-xl text-gray-600">{{ restaurant.address }}</p>
                </div>
            </div>
            <div class="border-2 p-20 bg-[#FAFFFB]">
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
            </div>
        </div>
        <div class=" mt-20">
            <h2 class="text-rgreen-100 text-2xl lg:text-4xl font-poppins font-semibold break-words lg:ml-10 mt-5">All Menu</h2>
            <div class="mt-5 relative lg:mx-10 lg:grid lg:grid-cols-3 pb-5 lg:pl-36 gap-4 w-1120px md:w-85vw overflow-x-auto p-3 flex flex-wrap">
                <div  v-for="item in items" class="w-96 h-96 border-2 border-rgreen-100 rounded-lg overflow-hidden mt-5 shadow-lg hover:shadow-2xl">
                    <img class="w-full h-3/4 transform hover:scale-105 transition-transform duration-300 ease-in-out" :src="item.image" alt="Card Image">
                    <div class="px-2 py-2 bg-white flex items-center justify-between">
                        <span class="font-bold lg:text-xl mb-2 w-auto mt-3">{{ item.name }}</span>
                        <div class="flex items-center gap-3">
                            <button class="text-xl">+</button>
                            <div class="rounded-full bg-[#DAEBDD] w-10 h-10 flex justify-center items-center">
                                <span>2</span>
                            </div>
                            <button class="text-2xl">-</button>
                        </div>
                    </div>
                    <div class="flex justify-end px-3 pb-2">
                        <span class="text-rgreen-100">Price - N{{ item.price }}</span>
                    </div> 
                </div>
            </div>
            <div class="flex justify-end mx-5 p-5">
                <button class="bg-rgreen-100 hover:text-ryellow text-white font-semibold p-2 mr-10 rounded transform hover:scale-105 transition-transform duration-300 ease-in-out mt-5" >
                    View More
                </button>
            </div>
        </div>
        <div class="bg-rgreen-100 p-40">
            <Footer2/>
        </div>
    </section>
</template>