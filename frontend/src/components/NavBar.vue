<template>
    <div class='navbar-container'>
        <h1>{{Msg}}</h1>
        <img src="https://www.clipartmax.com/png/middle/32-321763_search-icon-free-png.png" alt="" class="search">
    </div>
</template>

<script>
export default {
    name: 'NavBar',
    props: {
        Msg: String
    },
}
</script>

<style scoped>
/*#D0A85C rosa   #0BC6E3  azul   #111111  preto*/
.navbar-container {
    height: 100%;
    width: 6vh;
    background-color:  #D0A85C;
    transition: 400ms;
    position: absolute;
}

.navbar-container:hover {
    background-color: blueviolet;
    width: 12vh;
}

.search {
    width: 6vh;
}
</style>