<template>
    <div id="app">
        <img alt="Vue logo" src="./assets/logo.png">
        <Test />
    </div>
    <div id="visa">
        <h1>Vue Visa Application</h1>
        <form>
            <label for="first name">First Name:</label>
            <input type="text" required>
            <br>
            <label for="last name">Last Name:</label>
            <input type="text" required>
            <br>
            <label for="country">Nationality:</label>
            <input type="text" required>
            <br>
            <label for="passport number">Passport Number:</label>
            <input type="text" required>

            <label for="duration">Duration of stay:</label>
            <input type="text" required>

            <h2>Preview Application Details</h2>
            <p>First Name: </p>
            <p>Last Name: </p>
            <p>Nationality: </p>
            <p>Passport Number: </p>
            <p>Duration: </p>

        </form>
    </div>
</template>
<script>
import Test from './components/Test.vue'
export default {
    name: 'app',
    components: {
        Test
    }
}
</script>
<style>
#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}

#visa {
    margin: 20px auto;
    max-width: 700px;
}

label {
    display: block;
    margin: 20px 0 10px;
}

input {
    font-size: 30px;
    border: 1px double rgb(102, 97, 96);
    border-radius: 4px;
}
</style>