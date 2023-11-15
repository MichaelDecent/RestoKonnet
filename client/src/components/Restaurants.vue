<script setup>
    import { onMounted, ref } from "vue";
    import axios from "axios"; // Import axios here
    import { useRouter } from "vue-router";

    const router = useRouter();
    const restaurants = ref([]);

    const getRestaurants = async () => {
        try {
        // const token = localStorage.getItem('token');
        // const headers = { 'Authorization': `Bearer ${token}` };

        // Use axios.get to make a GET request
        const response = await axios.get('https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1/restaurants');
        //.console.log(response)
        restaurants.value = response.data
        } catch (error) {
            console.error(error);
        }
    }

    onMounted(() => {
        getRestaurants()
    })
</script>

<template>
    <div class="lg:mt-16 mt-5 relative lg:mx-10 lg:grid lg:grid-cols-4 pb-5 gap-4 w-1120px md:w-85vw overflow-x-auto rounded-lg flex flex-wrap">
        <div v-for="resto in restaurants" :key="resto.id"
        class=" w-96 h-96 border border-rgreen-100 rounded-lg overflow-hidden mt-5 shadow-lg hover:shadow-2xl transform hover:scale-105 transition-transform duration-300 ease-in-out">
            <img class="w-full h-3/4" :src="resto.image" alt="Card Image">
            <div class=" h-1/4 px-2 py-4 bg-white flex items-center justify-between">
                <span class="font-bold lg:text-xl mb-2 w-auto mt-3">{{ resto.name }}</span>
                <button @click=" router.push(`/restaurants/${resto.id}`)" class="bg-rgreen-100 hover:bg-ryellow text-white font-semibold p-2 rounded transform hover:scale-105 transition-transform duration-300 ease-in-out">View Menu</button>
            </div>
        </div>
    </div>
    <div class="flex justify-end mr-20 mb-5">
        <button class="bg-rgreen-100 hover:text-ryellow text-white font-semibold p-2 rounded transform hover:scale-105 transition-transform duration-300 ease-in-out mt-5" >View More</button>
    </div>
</template>