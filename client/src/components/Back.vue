<script>
import { useRouter } from 'vue-router';

export default {
    setup() {
        const router = useRouter();

        const goBack = () => {
            router.go(-1); // This navigates back one step in the history stack
        };

        return {
            goBack
        };
    }
};
</script>

<template>
    <button @click="goBack" class="w-5">
        <img src="@/img/icons/back.png" alt="">
    </button>
</template>