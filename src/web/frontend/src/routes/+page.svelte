<script>
	import Counter from './Counter.svelte';
	import welcome from '$lib/images/svelte-welcome.webp';
	import welcome_fallback from '$lib/images/svelte-welcome.png';

	let searchValue = ''

	let tracks = {}

	const myHeaders = new Headers();
	myHeaders.append("Access-Control-Allow-Origin", "http://127.0.0.1:8000/spotify-login/");

	async function getSearchSongs() {
		try {
			let url = `http://127.0.0.1:8000/spotify-login/?searchValue=${searchValue}`

			const response = await fetch(url)
			// , {
			// 	method: 'GET',
			// 	headers: myHeaders,
			// 	mode: 'cors',
			// })

			if (!response.ok) {
				throw new Error('Network response was not ok.');
			}
			const jsonResponse = await response.json()
			tracks = jsonResponse
		} catch (error) {
			// Handle any errors that occurred during the fetch request.
			console.error('Error fetching data:', error);
		}
	}

	$: console.log(tracks)

</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	<input type="text" placeholder="Search.." bind:value={searchValue}>
	<button value="Test" on:click={getSearchSongs}>Fetch SearchSongs</button>
	<!-- <h1>
		<span class="welcome">
			<picture>
				<source srcset={welcome} type="image/webp" />
				<img src={welcome_fallback} alt="Welcome" />
			</picture>
		</span>

		to your new<br />SvelteKit app
	</h1> -->

	<!-- <h2>
		try editing <strong>src/routes/+page.svelte</strong>
	</h2> -->

	<!-- <Counter /> -->
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	}

	.welcome {
		display: block;
		position: relative;
		width: 100%;
		height: 0;
		padding: 0 0 calc(100% * 495 / 2048) 0;
	}

	.welcome img {
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		display: block;
	}
</style>
