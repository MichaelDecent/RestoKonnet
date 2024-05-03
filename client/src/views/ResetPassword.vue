<script setup>
    import Logo from "../components/Logo.vue";
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
                    <p class="md:text-lg text-sm font-normal text-gray-600">Enter the email address associated with your account. We’ll send you a Token to reset your password.</p>
                    <form @submit.prevent="submitForm" class="space-y-4 md:space-y-6" action="#">
                        <div>
                            <label for="email" class="block mb-2 text-sm font-medium text-gray-900">Email</label>
                            <input v-model="vendorEmail" type="email" name="email" id="email" placeholder="Enter your email" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-ryellow focus:border-ryellow block w-full p-2.5" required>
                        </div>
    
                        <button type="submit" class="w-full text-white bg-rgreen-100 hover:bg-ryellow font-semibold rounded-lg lg:text-lg px-5 py-2.5 text-center">Send Email</button>
                        <p class="text-sm font-light text-gray-600">
                            You didn’t forget your password? <RouterLink to="/vendorSignIn" class="font-medium text-rgreen-100 hover:underline hover:text-ryellow">Sign In ></RouterLink>
                        </p>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>