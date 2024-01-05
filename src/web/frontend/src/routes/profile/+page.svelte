<script>
    import { onMount } from 'svelte';

    let username = '';
    let password = '';

    let access_token = '';
    let expires_in = '';
    let token_type = '';

    let user_profile = {};

    let logged_in = false;

    const CLIENT_ID = 'a6e889c6521040a797bdda3dbb27b451';
    const SPOTIFY_AUTHORIZE_ENPOINT = 'https://accounts.spotify.com/authorize'
    const REDIRECT_URI_AFTER_LOGIN = 'http://localhost:5173/profile';
    const SPACE_DELIMITER = '%20';
    const SCOPES = ['user-top-read', 'playlist-read-private'];
    const SCOPES_URI_PARAM = SCOPES.join(SPACE_DELIMITER);

    const AUTHORIZE_URI = `${SPOTIFY_AUTHORIZE_ENPOINT}?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI_AFTER_LOGIN}&scope=${SCOPES_URI_PARAM}&response_type=token&show_dialog=true`

    onMount(async() => {
        console.log('on mount');
        if (window.location.href.includes('access_token')) {
            console.log('hash exists');
            let params = getReturnedParamsFromSpotifyAuth(window.location.hash);
            // console.log(params)
            access_token = params.access_token;
            expires_in = params.expires_in;
            token_type = params.token_type;
            getProfile()
        }
        // if (typeof window !== 'undefined') {
        //     if (window.location.href.includes('access_token')) {
        //         console.log('hash exists');
        //         let params = getReturnedParamsFromSpotifyAuth(window.location.hash);
        //         access_token = params.access_token;
        //         expires_in = params.expires_in;
        //         token_type = params.token_type;
        //         getProfile()
        //     }
        // }
    })

    const handleLogin = () => {
        if (typeof window !== "undefined") {
            console.log('Handle Login Test')
            window.location = AUTHORIZE_URI;
        }

    }

    const getReturnedParamsFromSpotifyAuth = (hash) => {
        console.log('Get Returned params from Spotify Auth');
        // console.log(hash);
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
        console.log('Get Profile Test 1')
        try {
            console.log('Get Profile Test In Try')
			// let url = `http://127.0.0.1:8000/account-analysis/?access_token=${access_token}`
			let url = `http://127.0.0.1:8000/get-profile/?access_token=${access_token}`

            console.log('Fetching User Profile')
			const response = await fetch(url, {
                method: 'GET',
                mode: 'cors',
            })

			if (!response.ok) {
				throw new Error('Network response was not ok.');
			}

			const jsonResponse = await response.json();
			user_profile = jsonResponse.profile;
            console.log(user_profile);
            logged_in = true;

		} catch (error) {
			// Handle any errors that occurred during the fetch request.
			console.error('Error fetching data:', error);
		}
    }

    // $: console.log(window.location.hash)

    // $: if (window.location.hash) {
    //     let params = getReturnedParamsFromSpotifyAuth(window.location.hash);
    //     access_token = params.access_token;
    //     expires_in = params.expires_in;
    //     token_type = params.token_type;
    //     console.log('access token' + access_token)
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
    {#if logged_in === false}
    <div class='login-button-div'>
        <button on:click={handleLogin}>Login</button>
    </div>
    {:else}
    <div class='profile-div'>
        <div class='profile-image-div'>
            <img src={user_profile.images[1].url} alt="Italian Trulli" class="profile-image">
        </div>
        <div class='profile-name-div'>
            {user_profile.display_name}
        </div>
        <div class='followers-div'>
            Followers: {user_profile.followers.total}
        </div>
    </div>
    {/if}

</div>

<style>
    .profile-body {
        margin-top: 65px;
    }

    .profile-div {
        height: 120px;
        display: flex;
        align-items: center;
        background-color: var(--color-dark-gray);
        border-radius: 20px;
    }

    .profile-image-div {
        width: 20%;
    }

    .profile-image {
        width: 100px;
        height: 100px;
        border-radius: 5px;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

    .profile-name-div {
        width: 40%;
        text-align: center;
        font-size: 30px;
    }

    .followers-div {
        width: 40%;
        text-align: center;
        font-size: 20px;
    }
</style>