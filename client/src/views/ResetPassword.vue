<script setup>
import { useRouter } from "vue-router";
import { ref } from "vue"; // Import ref for reactive variables
import axios from "axios"; // Import axios for HTTP requests

const router = useRouter();

const BASE_URL = import.meta.env.VUE_APP_BASE_URL; // Access environment variables with import.meta.env

const vendorEmail = ref(""); // Define a reactive variable

const get_reset_password_token = async () => {
    try {
        const formData = new FormData();
        formData.append('email', vendorEmail.value);

        // Use axios.post for a POST request
        const response = await axios.post(`${BASE_URL}/vendors/reset_password`, formData);
        router.push("/UpdatePassword");
        console.log(response.data); // Assuming you want to log the response data

    } catch (error) {
        console.error(error);
        alert(error.message); // Display error message in an alert
    }
};
</script>
<template>
    <section class="min-h-screen bg-rgreen-100">
        <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
            <div class="w-full bg-white rounded-lg shadow md:mt-0 sm:max-w-md xl:p-0">
                <RouterLink to="/" class="flex pt-8 justify-center">
                    <Logo />
                </RouterLink>
                <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                    <h1 class="text-xxl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl">
                        Reset your password
                    </h1>
                    <p class="md:text-lg text-sm font-normal text-gray-600">Enter the email address associated with your
                        account. We’ll send you a Token to reset your password.</p>
                    <form @submit.prevent="get_reset_password_token" class="space-y-4 md:space-y-6" action="#">
                        <div>
                            <label for="email" class="block mb-2 text-sm font-medium text-gray-900">Email</label>
                            <input v-model="vendorEmail" type="email" name="email" id="email"
                                placeholder="Enter your email"
                                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-ryellow focus:border-ryellow block w-full p-2.5"
                                required>
                        </div>

                        <button type="submit"
                            class="w-full text-white bg-rgreen-100 hover:bg-ryellow font-semibold rounded-lg lg:text-lg px-5 py-2.5 text-center">
                            Send Email
                        </button>
                        <p class="text-sm font-light text-gray-600">
                            You didn’t forget your password? <RouterLink to="/vendorSignIn"
                                class="font-medium text-rgreen-100 hover:underline hover:text-ryellow">Sign In >
                            </RouterLink>
                        </p>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>