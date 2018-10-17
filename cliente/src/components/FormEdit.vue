<template>
<div class="col-8 centerForm">
  <form v-on:submit.prevent id="form">
    <label>Tipo de pedido</label>
    <div class="form-group">
      <select name="" class="form-control" id="select" v-model="requisition.type">
        <option value="requerimiento">Requerimiento</option>
        <option value="error">Error</option>
      </select>
    </div>
    <label>Asunto</label>
    <input type="text" id="asunto" class="form-control" v-model="requisition.subject">
    <label>Detalle</label>
    <textarea class="form-control" rows="5" v-model="requisition.details"></textarea>
    <label>Prioridad</label>
    <div class="form-group">
      <select name="" class="form-control" id="select" v-model="requisition.priority">
        <option value="c">Baja</option>
        <option value="b">Media</option>
        <option value="a">Alta</option>
      </select>
    </div>
    <label>Sistema</label>
    <div class="form-group">
      <select name="" class="form-control" id="select"  v-model="requisition.affected_system">
        <option value="administration">Administracion</option>
        <option value="stock">Stock</option>
        <option value="human resources">Recurso Humanos</option>
      </select>
    </div>
    <label>Modulo</label>
    <div class="form-group">
      <select name="" class="form-control" id="select" v-model="requisition.module">
        <option value="uno">uno</option>
        <option value="dos">dos</option>
        <option value="tres">tres</option>
      </select>
    </div>
    <label for="inputFile">Archivo adjunto</label>
    <input id="inputFile" type="file" >
    <button type="submit" class="btn btn-primary form-control boldText" v-on:click="update">ENVIAR</button>
  </form>
</div>
</template>
<script>
import axios from 'axios';
import EventBus from '../bus/eventBus.js';
export default {

  data() {
    return {
      requisition: {
        // type: '',
        // author: sessionStorage.getItem('idUser'),
        // subject: '',
        // date: '',
        // details: '',
        // priority: '',
        // affected_system: '',
        // module: '',
        // attached_file: null
      }
    }
  },
  methods: {
    update() {
      EventBus.$emit('change_section');
      this.requisition = null;
      // axios.post('', {
      //     type: this.requisition.type,
      //     author: this.requisition.author,
      //     subject: this.requisition.subject,
      //     date: this.requisition.date,
      //     details: this.requisition.details,
      //     priority: this.requisition.priority,
      //     affected_system: this.requisition.affected_system,
      //     module: this.requisition.module,
      //     attached_file: this.requisition.attached_file
      //   })
      //   .then((data) => {
      //     EventBus.$emit('change_section');
      //   })
      //   .catch((error) => {
      //     console.log(error.response);
      //   });
    }

  },
  created() {
    EventBus.$on('edit_requisition', (prueba) => {
      // this.requisition = null;
      // this.requisition = response;
      console.log(prueba);
      console.log("arranca");
    });
  }
}
</script>
<style>

</style>
