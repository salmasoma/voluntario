import { createWebHistory, createRouter } from "vue-router";
import register from "../pages/register.vue";
import login from "../pages/login.vue";
import dashboard from "../pages/dashboard.vue";

const routes = [
  {
    path: "/register",
    name: "Register",
    component: register,
  },
  {
    path: "/login",
    name: "login",
    component: login,
  },
  {
    path: "/dashboard",
    name: "dashboard",
    component: dashboard,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
