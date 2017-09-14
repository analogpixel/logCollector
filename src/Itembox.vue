<template>
    <div id="itembox">
    <div id="mattbox-template" v-on:click="inc">hello <p>{{ mattnew }}</p> {{ counter }}
    <select v-model="selected" name="sometext" size="5">
    <option v-for="option in items" v-bind:value="option.value">
    {{ option.text }} {{ counter }}
    </option>
    </select><span>Selected: {{ selected }}</span>
    <br>
    <button v-on:click="notify()">click me</button>
    </div>
</div>
</template>

<script>
export default {
    name: 'itembox',

    props: ['eventName'],

	data() {return {
                mattnew: "sdfsddsfs",
                items: [
                {text: 'one', value: 'a'},
                {text: 'two', value: 'abb'}],
                counter: 0,
                selected: 'a',
        }
    },

    watch: {
        // <itembox event-name=tester></itembox>
        'selected': function(val, oldValue) { this.$parent.$emit(this.eventName, val); }
    },

    methods: {
        inc: function() {console.log("inc"); this.counter = this.counter + 1;}, 
        notify: function() { console.log("sending message"); this.$parent.$emit('tester', '123'); }
    }

}

 //window.Links.components['app'] = module.exports;

</script>

<style>
.message {
  color: blue;
}
</style>
