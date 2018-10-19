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
    <div class="form-group">
      <!-- <select required name="" class="form-control" id="select"  v-model="requisition.affectedSystem" v-on:change="moduleSystem($event.target.value)">
        <option v-for="(system, index) in requisition.system" :key="index" value="1">{{ system.name }}</option>
      </select> -->
      <v-select  label="name" :options="system" v-model="requisition.affectedSystem"
       :on-change="moduleSystem(requisition.affectedSystem.id)" :searchable="false"></v-select>
    </div>
    <div v-if="moduleSelect">
      <label >Modulo</label>
      <div class="form-group">
        <!-- <select required name="" class="form-control" id="select" v-model="requisition.affectedModule" >
          <option v-for="(module, index) in requisition.module" :key="index" value="module">{{ module.name }}</option>
        </select> -->
        <v-select  label="name" :options="module" v-model="requisition.affectedModule"
          :searchable="false"></v-select>
      </div>
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
      systemId: null,
      moduleSelect: false,
      system: null,
      module: null,
      requisition: {
        type: '',
        author: sessionStorage.getItem('idUser'),
        subject: '',
        date: '',
        details: '',
        priority: '',
        affectedSystem: '',
        affectedModule: null,
        attached_file: null
      }
    }
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/requisitions/systems')
      .then((response) => {
        this.system = response.data
      })
      .catch((error) => {
        console.log(error);
      });

  },
  computed: {
    // moduleSystem(systemId) {
    //   axios.get('http://127.0.0.1:8000/requisitions/modules' + systemId)
    //     .then((response) => {
    //       console.log("aca");
    //       this.moduleSelect = true
    //       this.requisition.module = response.data
    //     })
    //     .catch((error) => {
    //       console.log(error);
    //     });
    //   }
  },
  methods: {
    send() {
      var self = this;
      axios.post('http://127.0.0.1:8000/requisitions/', {
          type: this.requisition.type,
          author: this.requisition.author,
          subject: this.requisition.subject,
          date: this.requisition.date,
          details: this.requisition.details,
          priority: this.requisition.priority,
          affectedSystem: this.requisition.affectedSystem,
          module: this.requisition.module,
          attached_file: this.requisition.attached_file
        })
        .then((data) => {
          EventBus.$emit('change_section');
        })
        .catch((error) => {
          console.log(error.response);
        });
    },
    moduleSystem(systemId) {
      axios.get('http://127.0.0.1:8000/requisitions/modules/' + systemId + '/')
        .then((response) => {
          this.moduleSelect = true
          this.requisition.module = response.data
          console.log(this.requisition.module);
        })
        .catch((error) => {
          console.log(error);
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
