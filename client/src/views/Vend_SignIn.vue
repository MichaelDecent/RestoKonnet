<script setup>
    import Logo from "../components/Logo.vue";
    import { ref } from "vue";
    import axios from "axios";
    import { useRouter } from "vue-router";

    const vendorEmail = ref("");
    const vendorPassword = ref("");

    const router = useRouter();

    // submit customer details to sign in
    const submitForm = async () => {
        const formData = new FormData()
        formData.append('email', vendorEmail.value)
        formData.append('password', vendorPassword.value)

        try {
            const response = await axios.post('https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1/vendors/login', formData);

            localStorage.setItem('token', response.data.access_token);
            localStorage.setItem('vendor_id', response.data.id)
            const id = response.data.vendor.id
            console.log(response.data.vendor.id)
            router.push(`vendors/${id}`)

        } catch (error) {
            alert(error.response.data.message)
            // if (error.response.data.message === "Email not Verified") {
            //     router.push('/vendors/verify_email')
            // }
            console.log("Login Failed:", error)
        }
    }

</script>

<template>
    <section class="min-h-screen bg-rgreen-100">
        <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
            <div class="w-full bg-white rounded-lg shadow md:mt-0 sm:max-w-md xl:p-0">
                <RouterLink to="/" class="flex pt-8 justify-center">
                    <Logo />  
                </RouterLink>
                <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                    <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl">
                            Sign In
                    </h1>
                    <form @submit.prevent="submitForm" class="space-y-4 md:space-y-6" action="#">
                        <div>
                            <label for="email" class="block mb-2 text-sm font-medium text-gray-900">Email</label>
                            <input v-model="vendorEmail" type="email" name="email" id="email" placeholder="Enter your email" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-ryellow focus:border-ryellow block w-full p-2.5" required>
                        </div>
                        <div>
                            <label for="password" class="block mb-2 text-sm font-medium text-gray-900">Password</label>
                            <input v-model="vendorPassword" type="password" name="password" id="password" placeholder="********" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-ryellow focus:border-ryellow block w-full p-2.5" required>
                        </div>
                        <div class="flex items-center justify-between">
                            <div class="flex items-start">
                                <div class="flex items-center h-5">
                                    <input id="remember" aria-describedby="remember" type="checkbox" class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-ryellow">
                                </div>
                                <div class="ml-3 text-sm">
                                    <label for="remember" class="text-gray-500">Remember me</label>
                                </div>
                            </div>
                            <RouterLink to="/ResetPassword" class="text-sm font-medium text-primary-600 hover:underline">Forgot password?</RouterLink>
                        </div>
                        <button type="submit" class="w-full text-white bg-rgreen-100 hover:bg-ryellow font-semibold rounded-lg lg:text-lg px-5 py-2.5 text-center">Sign in</button>
                        <p class="text-sm font-light text-gray-600">
                            Don’t have an account yet? 
                            <RouterLink to="/vendorSignUp" class="font-medium text-rgreen-100 hover:underline hover:text-ryellow">
                                Sign up >
                            </RouterLink>
                        </p>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>