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
                        Verify your Email
                    </h1>
                    <p class="md:text-lg text-sm font-normal text-gray-600">
                        We've sent a link to your email address: mark@gmail.com
                        Please follow the link inside to continue.
                    </p>

                    <button type="submit"
                        class=" text-white bg-rgreen-100 hover:bg-ryellow font-semibold rounded-lg lg:text-lg px-5 py-2.5 text-center">
                        Continue
                    </button>
                    <p class="text-sm font-light text-gray-600">
                        Didn't receive an email?
                        <button to="/vendorSignUp" class="font-medium text-rgreen-100 hover:underline hover:text-ryellow">
                            Resend >
                        </button>
                    </p>
                </div>
            </div>
        </div>
    </section>
</template>