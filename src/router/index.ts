import { createWebHistory, createRouter } from "vue-router";
import register from "../pages/register.vue";

const routes = [
  {
    path: "/register",
    name: "Register",
    component: register,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
