import { writable } from "svelte/store";

export const alert = writable("Welcome to the to-do list app!");

export const page = writable('Home');

export const user = writable({});

export const access_token = writable('');

export const logged_in = writable(false);