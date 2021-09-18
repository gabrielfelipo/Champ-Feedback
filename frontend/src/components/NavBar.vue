<template>
    <div class='navbar-container'>
        <h1>{{Msg}}</h1>
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
    width: 15vh;
    background-color:  rgba(37, 37, 37, 0.932);
    transition: 400ms;
    position: absolute;
    left: -7.5vh;
    z-index: 1;
}

.navbar-container:hover {
    background-color: #1b1b1bd8;
    left: 0px;
}

.search {
    width: 6vh;
}
</style>