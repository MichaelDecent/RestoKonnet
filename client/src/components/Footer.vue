<script setup>
    import Logo from "../components/Logo.vue"
</script>
<template>
     <div class=" border-y border-rgreen-100 flex lg:justify-between lg:mt-20 items-center">
        <div class="my-20 w-2/4">
            <div class="flex gap-3 overflow-hidden items-center">
                <img src="../img/ramen_dining.png" alt="logo_icon">
                <img class="w-1/2 lg:w-fit h-fit" src="../img/Restokonnet.png" alt="logo">
            </div>
        </div>
        <div class="my-16 w-2/4">
            <a class="flex gap-3 my-2" href="">
                <img class="h-fit" src="../img/icons/round-place-24px.png" alt="">
                <span class="text-rgreen-100  hover:text-ryellow transition duration-300 ease-in-out">345 Faulconer Drive, Suite 4 • Charlottesville, CA, 12345</span>
            </a>
            <a class="flex gap-3 my-2" href="">
                <img src="../img/icons/round-phone-24px.png" alt="">
                <span class="text-rgreen-100  hover:text-ryellow transition duration-300 ease-in-out">(+123) 456-7890</span>
            </a>
            <div class="flex gap-5 items-center mt-8 ml-2">
                <p class="text-rgreen-100">Social Media</p>
                <a href="">
                    <img class="transform hover:scale-150 transition-transform duration-300 ease-in-out" src="../img/icons/linkedin black.1.png" alt="">
                </a>
                <a href="">
                    <img class="transform hover:scale-150 transition-transform duration-300 ease-in-out" src="../img/icons/facebook black.1.png" alt="">
                </a>
                <a href="">
                    <img class="transform hover:scale-150 transition-transform duration-300 ease-in-out" src="../img/icons/twitter black.1.png" alt="">
                </a>
                <a href="">
                    <img class="transform hover:scale-150 transition-transform duration-300 ease-in-out" src="../img/icons/youtube color.1.png" alt="">
                </a>
            </div>
        </div>
    </div>
    <div class="">
        <ul class="flex gap-10 text-rgreen-100 mb-10">
            <li class="hover:text-ryellow">ABOUT US</li>
            <li class="hover:text-ryellow">CONTACT US</li>
            <li class="hover:text-ryellow">HELP</li>
        </ul>
    </div>
</template>