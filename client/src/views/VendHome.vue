<script setup>
import Logo2 from "../components/Logo2.vue"
import Footer2 from "../components/Footer2.vue"
import Cust_SignIn from "./Cust_SignIn.vue";
import { onMounted, ref } from "vue";
import { useAuthStore } from "../stores/AuthStore";
import axios from "axios";
import { useRoute } from 'vue-router';
import { useRouter } from "vue-router";
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { ExclamationTriangleIcon } from '@heroicons/vue/24/outline'

const open = ref(true)
const authStore = useAuthStore();
const restaurant = ref({});
const items = ref([]);
const vendorId = ref("")
const route = useRoute();
const currentPath = ref('');
const baseUrl = ref('https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1')
const currentUser = ref(authStore.currentUser)

vendorId.value = localStorage.getItem('vendor_id')
currentPath.value = route.path;

const router = useRouter()

// retrieves a details of a particular restaurant
const get_restaurants = async () => {
    try {
        // const token = localStorage.getItem('token');
        // const headers = { 'Authorization': `Bearer ${token}` };

        // Use axios.get to make a GET request
        const response = await axios.get(`${baseUrl.value}/${currentPath.value}/restaurants`);
        restaurant.value = response.data
        console.log(restaurant.value.id)

        // Call get_items after restaurant.value is populated
        await get_items();
    } catch (error) {
        console.error(error);
    }
}

// retrieves all customers item
const get_items = async () => {
    try {
        // Use axios.get to make a GET request
        const response = await axios.get(`${baseUrl.value}/restaurants/${restaurant.value.id}/items`);
        items.value = response.data
    } catch (error) {
        console.error(error);
    }
}

const vendor_logout = async () => {
    try {
        const token = localStorage.getItem('token');
        const headers = { 'Authorization': `Bearer ${token}` };

        // Use axios.delete to make a DELETE request
        const response = await axios.delete(`${baseUrl.value}/vendors/logout`, { headers });
        router.push("/");
    }
    catch (error) {
        console.error(error);
        alert("Failed to logout");
    }
}


const routeToDashboard = () => {
    router.push(`${currentPath.value}/restaurants`)
}

onMounted(() => {
    currentPath.value = route.path;
    get_restaurants()
});
</script>

<template>
    <!-- <div v-if="authStore.isAuthenticated"> -->
        <div class="bg-rgreen-100 border">
            <!-- <RestoNav :user="currentUser" /> -->
            <div class="flex md:flex-row justify-between items-center md:mx-auto max-w-screen-xl p-4">
                <div>
                    <Logo2 />
                </div>
                <ul class="flex items-center">
                    <li>
                        <RouterLink :to="currentPath + '/restaurants/'">
                            <label for="select-1" class="flex cursor-pointer select-none p-2">
                                <img class="w-10" src="../img/icons/online-shopping-store.png" alt="">
                            </label>
                        </RouterLink>
                    </li>
                    <li>
                        <input class="peer hidden" type="checkbox" name="select-1" id="select-1" />
                        <label for="select-1" class="flex cursor-pointer select-none p-2">
                            <img class="w-7 md:w-auto" src="../img/icons/Ellipse 4.png" alt="">
                        </label>
                        <ul
                            class="max-h-0 select-none flex-col overflow-hidden rounded-b-lg shadow-xl transition-all duration-300 peer-checked:max-h-56 peer-checked:py-3 bg-white">
                            <li class="cursor-pointer px-3 py-2 text-sm text-gray-500 hover:bg-gray-100">Profile</li>

                            <li
                                class="cursor-pointer px-3 py-2 text-sm text-gray-500 hover:bg-ryellow hover:text-white">
                                <button @click.prevent="vendor_logout()">Logout</button>
                            </li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
        <div>
            <TransitionRoot as="template" :show="open" v-if="restaurant.message">
                <Dialog as="div" class="relative z-10" @close="open = false">
                    <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0"
                        enter-to="opacity-100" leave="ease-in duration-200" leave-from="opacity-100"
                        leave-to="opacity-0">
                        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
                    </TransitionChild>

                    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
                        <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
                            <TransitionChild as="template" enter="ease-out duration-300"
                                enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                                enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
                                leave-from="opacity-100 translate-y-0 sm:scale-100"
                                leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
                                <DialogPanel
                                    class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
                                    <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                                        <div class="sm:flex sm:items-start">
                                            <div
                                                class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-green-100 sm:mx-0 sm:h-10 sm:w-10">
                                                <ExclamationTriangleIcon class="h-6 w-6 text-green-600"
                                                    aria-hidden="true" />
                                            </div>
                                            <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                                                <DialogTitle as="h3"
                                                    class="text-base font-semibold leading-6 text-gray-900">No
                                                    Restaurant!
                                                </DialogTitle>
                                                <div class="mt-2">
                                                    <p class="text-sm text-gray-500">Do you want to create a restaurant?
                                                    </p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                                        <button type="button"
                                            class="inline-flex w-full justify-center rounded-md bg-rgreen-100 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-ryellow sm:ml-3 sm:w-auto"
                                            @click="routeToDashboard()">Got to Dashboard</button>
                                        <button type="button"
                                            class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                                            @click="open = false" ref="cancelButtonRef">Cancel</button>
                                    </div>
                                </DialogPanel>
                            </TransitionChild>
                        </div>
                    </div>
                </Dialog>
            </TransitionRoot>
            <div class="flex flex-wrap justify-center  lg:justify-between md:mx-auto max-w-screen-xl p-4">
                <div class="lg:w-1/2">
                    <div class="w-96 h-96 lg:h-96 lg:w-full rounded-lg overflow-hidden mt-5 shadow-lg hover:shadow-2xl">
                        <img class="w-full h-full" :src="restaurant.image" alt="Card Image">
                    </div>
                    <div class="px-2 py-4 bg-white">
                        <h1 class="font-extrabold lg:text-4xl mb-2 w-auto mt-3">{{ restaurant.name }}</h1>
                        <p class="text-xl text-gray-600">{{ restaurant.address }}</p>
                    </div>
                </div>
            </div>
            <section class="bg-white py-12 text-gray-700 sm:py-16 lg:py-20">
                <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
                    <div class="mx-auto max-w-md text-center">
                        <h2 class="font-serif text-2xl font-bold sm:text-3xl">Available Delicacies</h2>
                    </div>
                    <div v-if="items.length == 0" class=" text-center text-lg text-gray-500 font-medium">
                        <p>No Food Available yet</p>
                    </div>

                    <div v-else class="mt-10 grid grid-cols-2 gap-6 sm:grid-cols-4 sm:gap-4 lg:mt-16">

                        <article v-for="item in items" class="relative flex flex-col overflow-hidden rounded-lg border">
                            <div class="aspect-square overflow-hidden">
                                <img class="h-full w-full object-cover transition-all duration-300 group-hover:scale-125"
                                    :src="item.image" alt="item image" />
                            </div>
                            <div class="my-4 mx-auto flex w-10/12 flex-col items-start justify-between">
                                <div class="mb-2 flex">
                                    <p class="mr-3 text-sm font-semibold">N {{ item.price }}</p>
                                </div>
                                <h3 class="mb-2 text-sm text-gray-400">{{ item.name }}</h3>
                            </div>
                        </article>
                    </div>
                </div>
            </section>
        </div>
        <div class="bg-rgreen-100 border">
            <Footer2 />
        </div>
    <!-- </div> -->
    <!-- <div v-else="authStore.isAuthenticated">
        <Cust_SignIn />
    </div> -->
</template>