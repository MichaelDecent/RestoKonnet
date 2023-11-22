<script setup>
    import RestoNav from "../components/RestoNav.vue"
    import Footer2 from "../components/Footer2.vue"
    import Restaurants from "../components/Restaurants.vue"
    import { useRouter, useRoute } from "vue-router";
    import { ref, onMounted } from "vue"
    import axios from "axios";



    const customerData = ref({})
    const currentPath = ref("")
    const route = useRoute()

    currentPath.value = route.path

     // get vendors data
     const getCustomerData = async () => {
        try {
            const response = await axios.get(`https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1${currentPath.value}`)
            customerData.value = response.data
        } catch(error) {
            alert(error)
        }
    };

    onMounted(() => {
        getCustomerData()
    });

    
</script>

<template>
    <section class="">
        <div class="bg-rgreen-100 border">
            <RestoNav/>
            <div class="my-24">
                <div class="flex justify-center mb-5">
                    <p class="text-4xl text-white font-extrabold break-words">Welcome! {{ customerData.name }}</p>
                </div>
                <div class="flex justify-center">
                    <div class="flex gap-2 bg-white p-3 rounded-3xl w-96">
                        <button>
                            <img src="../img/icons/search.png" alt="">
                        </button>
                        <input type="text" name="search" id="search" class="p-1" placeholder="search">
                    </div>
                </div>
            </div>     
        </div>
        <div class="lg:mx-60 mx-5 my-5">
            <h2 class="text-rgreen-100 text-2xl lg:text-4xl font-poppins font-semibold break-words">Explore Restaurants</h2>
            <Restaurants/>
            
        </div>
        <div class="bg-rgreen-100 border">
            <Footer2/>
        </div>
    </section>
</template>