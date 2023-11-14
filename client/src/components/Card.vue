<script setup>
import { useRouter } from "vue-router";
import { defineProps } from 'vue';

const router = useRouter();
const {resto} = defineProps(['resto'])

const viewMenu = () => {
    router.push(`/restaurants/${resto.id}`)
}
</script>

<template>
    <div class="max-w-xs rounded-lg overflow-hidden mt-5 shadow-lg hover:shadow-2xl transform hover:scale-105 transition-transform duration-300 ease-in-out">
        <img class="w-full" :src="resto.image" alt="Card Image">
        <div class="px-2 py-4 bg-white flex items-center justify-between">
            <span class="font-bold lg:text-xl mb-2 w-auto mt-3">{{ resto.name }}</span>
            <button @click="viewMenu" class="bg-rgreen-100 hover:bg-ryellow text-white font-semibold p-2 rounded transform hover:scale-105 transition-transform duration-300 ease-in-out">View Menu</button>
        </div>
    </div>
</template>