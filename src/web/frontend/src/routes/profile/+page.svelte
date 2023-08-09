<script>

    let username = '';
    let password = '';
</script>

<svelte:head>
	<title>Profile</title>
	<meta name="Profile" content="Profile" />
</svelte:head>

<div class='profile-body'>
    <div class='login-form'>
        <label for='username'>Username</label>
        <input class='username-input' id='username' placeholder="Username..." bind:value={username}/>

        <label for='password'>Password</label>
        <input class='password-input' id='password' placeholder="Password..." bind:value={password}/>
    </div>
</div>

<style>
    .profile-body {
        margin-top: 65px;
    }
</style>