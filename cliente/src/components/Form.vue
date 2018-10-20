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
      <!-- <select required name="" class="form-control" id="select" v-model="requisition.priority">
        <option value="3">Baja</option>
        <option value="2">Media</option>
        <option value="1">Alta</option>
      </select> -->
      <v-select label="name" :options="requisition.priority" :on-change="priorityId" :searchable="false"></v-select>
    </div>
    <label>Sistema</label>
    <div class="form-group">
      <!-- <select required name="" class="form-control" id="select"  v-model="requisition.affectedSystem" v-on:change="moduleSystem($event.target.value)">
        <option v-for="(system, index) in requisition.system" :key="index" value="1">{{ system.name }}</option>
      </select> -->
      <v-select label="name" :options="requisition.system" :on-change="moduleSystem" :searchable="false"></v-select>
    </div>
    <div v-if="moduleSelect">
      <label >Modulo</label>
      <div class="form-group">
        <!-- <select required name="" class="form-control" id="select" v-model="requisition.affectedModule" >
          <option v-for="(module, index) in requisition.module" :key="index" value="module">{{ module.name }}</option>
        </select> -->
        <v-select label="name" :options="requisition.module" :on-change="moduleId" :searchable="false"></v-select>
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
      moduleSelect: false,

      requisition: {
        type: '',
        author: sessionStorage.getItem('idUser'),
        subject: '',
        date: '',
        details: '',
        priority: null,
        affectedSystem: '',
        affectedModule: null,
        system: null,
        module: null,
        attached_file: null,
        status: '1'
      }
    }
  },
  mounted() {
    //La API devuelve todos los sistemas
    axios.get('http://127.0.0.1:8000/requisitions/systems')
      .then((response) => {
        this.requisition.system = response.data
      })
      .catch((error) => {
        console.log(error);
      });
    //La API devuelve todas las prioridades
    axios.get('http://127.0.0.1:8000/priority/')
      .then((response) => {
        this.requisition.priority = response.data
        // console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      });

  },
  computed: {
    id() {
      console.log();
    }
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
          module: this.requisition.affectedModule,
          attached_file: this.requisition.attached_file,
          status: this.requisition.status
        })
        .then((data) => {
          EventBus.$emit('change_section');
        })
        .catch((error) => {
          console.log(error.response);
        });
    },
    moduleSystem(systemId) {
      this.requisition.affectedSystem = systemId.id;
      axios.get('http://127.0.0.1:8000/requisitions/modules/system/' + systemId.id + '/')
        .then((response) => {
          this.requisition.module = response.data
          this.moduleSelect = true
          console.log(this.requisition.module);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    moduleId(module) {
      this.requisition.affectedModule = module.id;
    },
    priorityId(priority) {
      // console.log(priority.id);
      this.requisition.priority = priority.id;
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
