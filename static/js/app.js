/*
https://vuejs.org/v2/guide/components.html
https://vuejs.org/v2/guide/forms.html
*/


Vue.component('mattbox' , {
	template: '\
	<div id="mattbox-template" v-on:click="inc">hello <p>{{ mattnew }}</p> {{ counter }}\
	<select v-model="selected" name="sometext" size="5">\
	 <option v-for="option in items" v-bind:value="option.value">\
    {{ option.text }}\
  	</option>\
	  </select><span>Selected: {{ selected }}</span></div>',
	
	data: function() {return {
		mattnew: "sdfsddsfs",
		items: [
		{text: 'one', value: 'a'},
		{text: 'two', value: 'abb'}],
		counter: 0,
		selected: 'a',
	}},

	methods: {
		inc: function(event) {  this.counter = this.counter + 1; this.mattnew = "aaaaa"}
	}

});

$(function() {
	var app1 = new Vue({
	  el: '#app'
	});
});