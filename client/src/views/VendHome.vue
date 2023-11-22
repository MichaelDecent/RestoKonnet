<script setup>
    import Restaurant from "../components/Restaurants.vue";
    import Logo2 from "../components/Logo2.vue"
    import Footer2 from "../components/Footer2.vue"
    import { useRouter, useRoute } from "vue-router";
    import { ref, onMounted } from "vue"
    import axios from "axios";

    const router = useRouter()
    const route = useRoute()
    const currentPath = ref("")
    const vendorData = ref({})

    currentPath.value = route.path

    //gets the route to Dashboard Page
    const dashboardRoute = () => {
        router.push(`${route.path}/restaurants`)
    }

    // get vendors data
    const getVendorData = async () => {
        try {
            const response = await axios.get(`https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1${currentPath.value}`)
            vendorData.value = response.data
        } catch(error) {
            alert(error)
        }
    };

    onMounted(() => {
        getVendorData()
    });

</script>

<template>
    <section class="">
        <div class="bg-rgreen-100 border">
            <div class="flex flex-col md:flex-row justify-between items-center lg:mx-60 my-20">
                <div>
                    <Logo2/>
                </div>
                <div class="flex gap-10 items-center">
                    <button @click="dashboardRoute()" class="text-white hover:text-ryellow transition duration-300 ease-in-out relative group text-lg md:text-2xl font-semibold">
                        Dashboard
                        <div class="absolute w-full h-1 bg-ryellow bottom-0 left-0 transform scale-x-0 transition-transform origin-left group-hover:scale-x-100 duration-300 ease-in-out"></div>
                    </button>
                    <button>
                        <img src="../img/icons/Ellipse 4.png" alt="">
                    </button>
                    <button>
                        <img class="pb-2" src="../img/icons/garden_cart.png" alt="">
                    </button>
                </div>
            </div>
            <div class="my-24">
                <div class="flex justify-center mb-5">
                    <p class="text-4xl text-white font-extrabold break-words">Welcome! {{ vendorData.name }}</p>
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
        <div class="lg:mx-60 my-5 mx-5">
            <h2 class="text-rgreen-100 text-2xl lg:text-4xl font-poppins font-semibold break-words">Explore Restaurants</h2>
            <Restaurant/>
           
        </div>
        <div class="bg-rgreen-100 border" >
            <Footer2/>
        </div>
    </section>
</template>