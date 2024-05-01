<script setup>
import Logo2 from "../components/Logo2.vue"
import { useAuthStore } from '../stores/AuthStore'
import { useRouter } from "vue-router";


const authStore = useAuthStore()

const { user } = defineProps(['user'])

const router = useRouter()

const logout = () => {
    router.push('/')
    authStore.logout()
}



</script>

<template>
    <div class="flex md:flex-row justify-between items-center md:mx-auto max-w-screen-xl p-4">
        <div>
            <Logo2 />
        </div>
        <ul class="flex items-center">
            <li>
                <RouterLink :to="'/dashboard/' + user.id">
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
                   
                    <li class="cursor-pointer px-3 py-2 text-sm text-gray-500 hover:bg-ryellow hover:text-white"><button
                            @click.prevent="_logout()">Logout</button></li>
                </ul>
            </li>
        </ul>
    </div>
</template>