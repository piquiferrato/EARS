<template>
<div class="row">
  <div class="form-group col-6 col-sm-6 col-md-4">
    <label for="">Ordenar por</label>
    <select class="form-control" v-model="orderBy" v-on:change="load(state)">
          <option value="priority">Prioridad</option>
          <option value="date">Fecha</option>
        </select>
  </div>
  <div class="form-group col-6 col-sm-6 col-md-4">
    <label for="">De manera</label>
    <select class="form-control" v-model="orderType"  v-if="!dateOrder" v-on:change="load(state)">
          <option value="0">Creciente</option>
          <option value="1">Decreciente</option>
        </select>
    <select class="form-control" v-model="orderType"  v-if="dateOrder" v-on:change="load(state)">
          <option value="0">Nuevo-Viejo</option>
          <option value="1">Viejo-Nuevo</option>
        </select>
  </div>
  <div class=" col-sm-6 col-md-4 marginButtonSearch">
    <button type="button" class="btn btn-primary form-control" v-on:click="advance_search">Busqueda Avanzada</button>
  </div>
</div>
</template>
<script>
import EventBus from '../bus/eventBus.js'
export default {
  data() {
    return {
      orderBy: 'priority',
      orderType: '1',
      dateOrder: false,
      system: null,
      module: null,
      advanceSearch: false,
      state: null
    }
  },
  mounted() {
    EventBus.$on('status_current', (status) => {
      this.state = status
      console.log(status);
    })
  },
  methods: {
    load(state) {
      this.activate_date_order()
      EventBus.$emit('load_select', state)
    },
    activate_date_order() {
      if (this.orderBy === 'date') {
        this.dateOrder = true
      } else {
        this.dateOrder = false
      }
    },
    advance_search() {
      EventBus.$emit('advance_search')
    }
  }
}
</script>
<style lang="scss" scoped>
</style>
