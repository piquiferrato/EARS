<template>
<div class="col-8 centerForm">
  <form v-on:submit.prevent id="form">
    <label>Tipo de pedido</label>
    <div class="form-group">
      <select required name="" class="form-control" id="select" v-model="requisition.type">
        <option value="REQUERIMIENTO">Requerimiento</option>
        <option value="ERROR">Error</option>
      </select>
    </div>
    <label>Asunto</label>
    <input required type="text" id="asunto" class="form-control" v-model="requisition.subject">
    <label>Fecha</label>
    <input required type="date" class="form-control" v-model="requisition.date">
    <label>Detalle</label>
    <textarea class="form-control" rows="5" v-model="requisition.details"></textarea>
    <label>Prioridad</label>
    <div class="form-group">
      <select required name="" class="form-control" id="select" v-model="requisition.priority">
        <option value="baja">Baja</option>
        <option value="media">Media</option>
        <option value="alta">Alta</option>
      </select>
    </div>
    <label>Sistema</label>
    <div required class="form-group">
      <select name="" class="form-control" id="select"  v-model="requisition.affected_system">
        <option value="administration">Administracion</option>
        <option value="stock">Stock</option>
        <option value="human resources">Recurso Humanos</option>
      </select>
    </div>
    <label>Modulo</label>
    <div required class="form-group">
      <select name="" class="form-control" id="select" v-model="requisition.module">
        <option value="uno">uno</option>
        <option value="dos">dos</option>
        <option value="tres">tres</option>
      </select>
    </div>
    <label for="inputFile">Archivo adjunto</label>
    <input id="inputFile" type="file" >
    <button type="submit" class="btn btn-primary form-control boldText" v-on:click="send">ENVIAR</button>
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
        type: '',
        author: sessionStorage.getItem('idUser'),
        subject: '',
        date: '',
        details: '',
        priority: '',
        affected_system: '',
        module: '',
        attached_file: null
      }
    }
  },
  methods: {
    send() {
      axios.post('http://127.0.0.1:8000/requisitions/', {
          type: this.requisition.type,
          author: this.requisition.author,
          subject: this.requisition.subject,
          date: this.requisition.date,
          details: this.requisition.details,
          priority: this.requisition.priority,
          affected_system: this.requisition.affected_system,
          module: this.requisition.module,
          attached_file: this.requisition.attached_file
        })
        .then((data) => {
          EventBus.$emit('change_section');
        })
        .catch((error) => {
          console.log(error.response);
        });
    }

  }
}
</script>
<style>
#inputFile {
  width: 0.1px;
  height: 0.1px;
  opacity: 0;
  overflow: hidden;
  position: absolute;
  z-index: -1;
}

label[for="inputFile"] {
  font-size: 14px;
  font-weight: 600;
  color: #FFFFFF;
  background-color: #2699FB;
  display: inline-block;
  cursor: pointer;
  padding: 15px 40px !important;
  text-transform: uppercase;
  width: fit-content;
  text-align: center;
}

.formWidth {
  width: 80%;
}

.centerForm {
  margin: 0 auto;
}
</style>
