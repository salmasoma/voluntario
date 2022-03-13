import { createApp } from "vue";
import App from "./App.vue";
import router from "./router/index";
import "./index.css";
import 'v-calendar/dist/style.css';

createApp(App).use(router).mount("#app");
