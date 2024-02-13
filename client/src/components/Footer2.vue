<script setup>
    import Logo2 from "../components/Logo2.vue"
</script>
<template>
    <div class="border-y border-white flex justify-between items-center lg:mt-10 md:mx-auto max-w-screen-xl px-4">
        <div class="my-20">
            <Logo2/>
        </div>
        <div class=" my-16">
                <a class="flex gap-3 my-2" href="">
                    <img src="../img/icons/round-place-white.png" alt="">
                    <span class="text-white  hover:text-ryellow transition duration-300 ease-in-out">345 Faulconer Drive, Suite 4 • Charlottesville, CA, 12345</span>
                </a>
                <a class="flex gap-3 my-2" href="">
                    <img src="../img/icons/round-phone-white.png" alt="">
                    <span class="text-white  hover:text-ryellow transition duration-300 ease-in-out">(+123) 456-7890</span>
                </a>
                <div class="flex gap-5 items-center mt-8 ml-2">
                    <p class="text-white">Social Media</p>
                    <a href="">
                        <img class="transform hover:scale-150 transition-transform duration-300 ease-in-out" src="../img/icons/linkedin white.png" alt="">
                    </a>
                    <a href="">
                        <img class="transform hover:scale-150 transition-transform duration-300 ease-in-out" src="../img/icons/facebook white.png" alt="">
                    </a>
                    <a href="">
                        <img class="transform hover:scale-150 transition-transform duration-300 ease-in-out" src="../img/icons/instagram white.png" alt="">
                    </a>
                    <a href="">
                        <img class="transform hover:scale-150 transition-transform duration-300 ease-in-out" src="../img/icons/twitter white.png" alt="">
                    </a>
                    <a href="">
                        <img class="transform hover:scale-150 transition-transform duration-300 ease-in-out" src="../img/icons/youtube color.1.png" alt="">
                    </a>
                </div>
        </div>
    </div>
    <div>
        <ul class="flex gap-10 text-white lg:mb-20 md:mx-auto max-w-screen-xl px-4 mb-10">
            <li class="hover:text-ryellow">ABOUT US</li>
            <li class="hover:text-ryellow">CONTACT US</li>
            <li class="hover:text-ryellow">HELP</li>
        </ul>
    </div>
</template>