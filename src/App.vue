<template>
    <div id="app">
    	This is the Application
    	 <h1>{{ msg }}</h1>
    	 project: {{ project }}<br>
    	 Hostnames: {{ hostnames }}<br>
    	 Paths: {{ paths }}<br>
        <itembox event-name="projectList"></itembox>
        <itembox event-name="hostnames"></itembox>
        <itembox event-name="paths"></itembox>
    </div>

</template>

<script>

import Itembox from './Itembox.vue'

export default {
    name: 'app',
    components: { Itembox },
	data () { return { hostnames: 'none', paths: 'none', project: 'none', msg: 'Welcome to Your Vue.js App' }},
	
	created: function() { 
		this.$on('projectList', function (aa) { this.project = aa } ),
		this.$on('hostnames', function (aa) { this.hostnames = aa } ),
		this.$on('paths', function (aa) { this.paths = aa } )
	}
	
  }

</script>

<style>
.message {
  color: blue;
}
</style>
