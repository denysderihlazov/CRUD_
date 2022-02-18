<template>
    <div class="container">
        <Container />
    </div>
</template>

<script>
import Container from './components/Container.vue'

export default {
    name: 'App',
    components: {
        Container
    }
}
</script>

<style>

body {
    background: #020631;
    font: 14px 'Nunito', sans-serif;
    background: url("../media/bg.svg") center/cover;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
}


</style>
