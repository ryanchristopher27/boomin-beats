<script>
    import { onMount } from 'svelte';

    let username = '';
    let password = '';

    let access_token = '';
    let expires_in = '';
    let token_type = '';

    let user_profile = {};

    const CLIENT_ID = 'a6e889c6521040a797bdda3dbb27b451';
    const SPOTIFY_AUTHORIZE_ENPOINT = 'https://accounts.spotify.com/authorize'
    const REDIRECT_URI_AFTER_LOGIN = 'http://localhost:5173/profile';
    const SPACE_DELIMITER = '%20';
    const SCOPES = ['user-top-read', 'playlist-read-private'];
    const SCOPES_URI_PARAM = SCOPES.join(SPACE_DELIMITER);

    const AUTHORIZE_URI = `${SPOTIFY_AUTHORIZE_ENPOINT}?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI_AFTER_LOGIN}&scope=${SCOPES_URI_PARAM}&response_type=token&show_dialog=true`

    onMount(async() => {
        console.log('on mount');
        if (window.location.hash) {
            console.log('hash exists');
            let params = getReturnedParamsFromSpotifyAuth(window.location.hash);
            access_token = params.access_token;
            expires_in = params.expires_in;
            token_type = params.token_type;
            getProfile()
        }
    })

    const handleLogin = () => {
        // if (typeof window !== "undefined") {
            // window.location = AUTHORIZE_URI;
            // console.log('test')
        // }

    }

    const getReturnedParamsFromSpotifyAuth = (hash) => {
        console.log('this is a test');
        console.log(hash);
        const stringAfterHashtag = hash.substring(1);
        const paramsInUrl = stringAfterHashtag.split("&");
        const paramsSplitUp = paramsInUrl.reduce((accumulater, currentValue) => {
            console.log(currentValue);
            const [key, value] = currentValue.split("=");
            accumulater[key] = value;
            return accumulater;
        }, {});

        return paramsSplitUp;
    };

    async function getProfile() {
        try {
			let url = `http://127.0.0.1:8000/account-analysis/?access_token=${access_token}`

            console.log('Fetching User Profile')
			const response = await fetch(url)

			if (!response.ok) {
				throw new Error('Network response was not ok.');
			}

			const jsonResponse = await response.json();
			user_profile = jsonResponse.profile;
            console.log(user_profile);

		} catch (error) {
			// Handle any errors that occurred during the fetch request.
			console.error('Error fetching data:', error);
		}
    }

    $: console.log(window.location.hash)

    // $: if (window.location.hash) {
    //     let params = getReturnedParamsFromSpotifyAuth(window.location.hash);
    //     access_token = params.access_token;
    //     expires_in = params.expires_in;
    //     token_type = params.token_type;
    //     getProfile()
    // }
</script>

<svelte:head>
	<title>Profile</title>
	<meta name="Profile" content="Profile" />
</svelte:head>

<div class='profile-body'>
    <!-- <div class='login-form'>
        <label for='username'>Username</label>
        <input class='username-input' id='username' placeholder="Username..." bind:value={username}/>

        <label for='password'>Password</label>
        <input class='password-input' id='password' placeholder="Password..." bind:value={password}/>
    </div> -->
    <div class='login-button-div'>
        <button on:click={handleLogin}>Login</button>
    </div>
</div>

<style>
    .profile-body {
        margin-top: 65px;
    }
</style>