<template>
  <b-navbar class="mb-3 border-bottom shadow-sm" toggleable="md" type="light" variant="white">
    <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

    <b-navbar-brand to="/">
      <img
        src="../assets/logo.svg"
        width="30"
        height="30"
        class="d-inline-block align-top"
        alt="logo"
      >
      HoneyBadgers
    </b-navbar-brand>

    <b-collapse is-nav id="nav_collapse">
      <b-navbar-nav>
        <b-nav-item href="#" to="/dashboard">
          <font-awesome-icon class="mr-1" icon="home" fixed-width/>Dashboard
        </b-nav-item>
        <b-nav-item href="#" to="/profile">
          <font-awesome-icon class="mr-1" icon="user" fixed-width/>Profile
        </b-nav-item>
        <b-nav-item href="#" to="/settings">
          <font-awesome-icon class="mr-1" icon="cog" fixed-width/>Settings
        </b-nav-item>
      </b-navbar-nav>
      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form @submit="onSubmit">
          <b-input-group>
            <b-form-input required v-model="query" size="sm" type="text" placeholder="Search"/>
            <b-input-group-append>
              <b-button size="sm" class="my-sm-0 mr-sm-3" variant="secondary" type="submit">
                <font-awesome-icon icon="search"/>
              </b-button>
            </b-input-group-append>
          </b-input-group>
        </b-nav-form>

        <b-nav-form @submit="onSemanticSubmit">
          <b-input-group>
            <b-form-input required v-model="semanticQuery" size="sm" type="text" placeholder="Keyword for semantic search"/>
            <b-input-group-append>
              <b-button size="sm" class="my-sm-0 mr-sm-3" variant="secondary" type="submit">
                <font-awesome-icon icon="search"/>
              </b-button>
            </b-input-group-append>
          </b-input-group>
        </b-nav-form>

        <b-nav-form class="mr-1">
          <b-form-radio-group
            buttons
            button-variant="outline-primary"
            size="sm"
            v-model="role"
            :options="roleOptions"
            name="radioBtnOutline"
          />
        </b-nav-form>

        <b-nav-item-dropdown right>
          <template slot="text">
            <font-awesome-icon icon="sign-out-alt" fixed-width/>
          </template>
          <b-dropdown-item @click="logout">
            <font-awesome-icon class="mr-1" icon="sign-out-alt" fixed-width/>Log out
          </b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  name: "NavigationBar",
  data() {
    return {
      role: this.$root.$data.role,
      roleOptions: [
        { text: "Client", value: "client" },
        { text: "Freelancer", value: "freelancer" }
      ],
      query: "",
      semanticQuery: ""
    };
  },
  created() {
    if (!this.$axios.defaults.headers.common["Authorization"]) {
      const token = sessionStorage.getItem("token");
      if (token) {
        this.$axios.defaults.headers.common["Authorization"] = token;
      } else {
        this.$router.replace("/");
      }
    }
  },
  watch: {
    role: function(newRole, oldRole) {
      this.$root.$data.role = newRole;
      sessionStorage.setItem("role", newRole);
      this.$axios
        .patch(`/user/register/${this.$root.$data.user_id}/`, {
          role: newRole == "freelancer" ? 0 : 1
        })
        .then(response => {
          this.$root.$emit('rolechange');
        })
        .catch(err => {
          // eslint-disable-next-line
          console.log(err);
        });
    }
  },
  methods: {
    logout() {
      delete this.$axios.defaults.headers.common["Authorization"];
      sessionStorage.removeItem("token");
      sessionStorage.removeItem("user_id");
      this.$router.push("/");
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$router.push("/search/" + this.query);
    },
    onSemanticSubmit(evt) {
      evt.preventDefault();
      this.$router.push("/semantic-search/" + this.semanticQuery);
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
