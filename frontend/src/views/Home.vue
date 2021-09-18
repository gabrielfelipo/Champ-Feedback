<template>
    <body>
        <NavBar/>
        <div id="gradient"/>
        <div id="image"/>
        <div id="effect-right"/>
        <div id="effect-left"/>
    </body>
</template>

<script>
import NavBar from '@/components/NavBar'
export default {
    name: 'app',
    components: {
    NavBar,
    },
}
</script>

<style>
#gradient {
    position: absolute;
    height: 100%;
    width: 100%;
    z-index: -5;
    background-color: #537895; 
    background-image: linear-gradient(to right top, #181037, #18153e, #181b45, #18204c, #162653, #152a59, #142d5f, #123165, #11346c, #103873, #0e3b7a, #0c3f81);
}
#image {
    position: absolute;
    background-image: url('C:/Users/felipo/Documents/Estudo/Champions/frontend/src/assets/ashe_background.png');
    background-repeat: no-repeat;
    background-position: 100% 103%;
    background-size: 135vh;
    height: 100%;
    width: 100%;
    z-index: 0;
    opacity: 70%;
    transform: scaleX(-1);
}
#effect-right {
    position: absolute;
    background-image: url('C:/Users/felipo/Documents/Estudo/Champions/frontend/src/assets/oct-right.png');
    z-index: -1;
    right: 0%;
    top: 0%;
    height: 100%;
    width: 100%;
    background-size: 135vh;
    background-position: 100% 85%;
    background-repeat: no-repeat;
    opacity: 12%;
}
#effect-left {
    position: absolute;
    background-image: url('C:/Users/felipo/Documents/Estudo/Champions/frontend/src/assets/oct-left.png');
    z-index: -1;
    left: 0%;
    bottom: 0%;
    height: 100%;
    width: 100%;
    background-size: 135vh;
    background-position: -3% 85%;
    background-repeat: no-repeat;
    opacity: 9%;
}
</style>