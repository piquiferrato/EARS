<template>
  <div>
    <div class="col-8 " v-if="editForm">
      <form v-on:submit.prevent id="form">
        <!-- <label>Tipo de pedido</label>
        <div class="form-group">
          <select name="" class="form-control" id="select" v-model="requisitionEdit.type">
            <option value="REQUERIMIENTO">Requerimiento</option>
            <option value="ERROR">Error</option>
          </select>
        </div> -->
        <label>Asunto</label>
        <input type="text" id="asunto" class="form-control" v-model="requisitionEdit.subject">
        <label>Detalle</label>
        <textarea class="form-control" rows="5" v-model="requisitionEdit.details"></textarea>
        <!-- <label>Prioridad</label>
        <div class="form-group">
          <select name="" class="form-control" id="select" v-model="requisitionEdit.priority">
            <option value="3">Baja</option>
            <option value="2">Media</option>
            <option value="1">Alta</option>
          </select>
        </div> -->
        <!-- <label>Sistema</label>
        <div class="form-group">
          <select name="" class="form-control" id="select"  v-model="requisitionEdit.affectedSystem">
            <option value="administration">Administracion</option>
            <option value="stock">Stock</option>
            <option value="human resources">Recurso Humanos</option>
          </select>
        </div>
        <label>Modulo</label>
        <div class="form-group">
          <select name="" class="form-control" id="select" v-model="requisitionEdit.module">
            <option value="uno">uno</option>
            <option value="dos">dos</option>
            <option value="tres">tres</option>
          </select>
        </div> -->
        <label for="inputFile">Archivo adjunto</label>
        <input id="inputFile" type="file" >
        <button type="submit" class="btn btn-primary form-control boldText" v-on:click="update(requisitionEdit.id)">ENVIAR</button>
      </form>
    </div>
  </div>
</template>
<script>
import axios from 'axios';
import EventBus from '../bus/eventBus.js';
export default {
  name: "",
  data() {
    return {
      requisitionEdit: null,
      editForm: false
    }
  },
  mounted() {
    EventBus.$on('edit_form', (requisition) => {
      this.requisitionEdit = null
      console.log(requisition);
      this.editForm = true
      this.requisitionEdit = requisition
    })

  },
  methods: {
    update(id) {
      this.editForm = false;
      this.requisitionSection = true;
      axios.put('http://127.0.0.1:8000/requisitions/update/' + id + '/', {
          type: this.requisitionEdit.type,
          author: this.requisitionEdit.author,
          subject: this.requisitionEdit.subject,
          date: this.requisitionEdit.date,
          details: this.requisitionEdit.details,
          priority: this.requisitionEdit.priority,
          affectedSystem: this.requisitionEdit.affectedSystem,
          module: this.requisitionEdit.module,
          attached_file: this.requisitionEdit.attached_file
        })
        .then((data) => {
          EventBus.$emit('change_section');
          console.log(data);
        })
        .catch((error) => {
          console.log(error.response);
        });
    }
  }
}
</script>
<style lang="scss" scoped>
</style>
