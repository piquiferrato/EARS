<template>
  <div class="container">
    <!-- <technicalMenu></technicalMenu> -->
    <!-- <userMenu></userMenu> -->
    <!-- <login></login> -->
    <router-view></router-view>
  </div>
</template>

<script>
import login from './components/Login.vue';
import userMenu from './components/UserMenu.vue';
import technicalMenu from './components/TechnicalMenu.vue';
export default {

  components: {},
  data() {
    return {}
  }
}
</script>

<style>
.backgroundColor {
  background-color: #2699FB;
}

.whiteText {
  color: #FFFFFF;

}

.hover:hover {
  background-color: #2699FB;
  color: #FFFFFF;
  border: 1px solid #FFFFFF;
  transition: background-color 0.5s, color 0.5s, border 0.5s;
}

.boldText {
  font-weight: bold;
}

.btnNavigationBorder {
  border: 1px solid #2699FB;
}

.whiteBackground {
  background-color: #FFFFFF;
}

.textColor {
  color: #2699FB;
}

#logOut {
  padding-left: 10px;
}
</style>
