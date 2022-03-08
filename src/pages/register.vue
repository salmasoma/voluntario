<script setup lang="ts"></script>
<template>
<div class="min-h-screen w-full bg-black flex flex-row justify-center items-center">
    <div class="w-1/4 h-[25rem] p-4 bg-slate-200 rounded-xl flex flex-col justify-evenly">
    <div class="text-2xl">Register</div>
    <div class="flex flex-col gap-2">
        <label>E-mail:</label>
        <input required type="email" class="w-full rounded-md p-1"  />
    </div>
    <div class="flex flex-col gap-2">
        <label>Password:</label>
        <input required type="email" class="w-full rounded-md p-1"  />
    </div>
    <div class="flex flex-col gap-2">
        <label>Confirm Password:</label>
        <input required type="email" class="w-full rounded-md p-1"  />
    </div>
    <div class="w-full mt-4 flex justify-end items-center">
        <button class="bg-black w-full text-white p-2 rounded-md hover:scale-95">
            Register
        </button>
    </div>
    <p class="text-center mt-4 text-xs">
        Already Have an account? <router-link to="/login">Login</router-link>
    </p>
    </div>
</div>
</template>