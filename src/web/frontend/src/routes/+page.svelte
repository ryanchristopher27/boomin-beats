<script>
	import Counter from './Counter.svelte';
	import welcome from '$lib/images/svelte-welcome.webp';
	import welcome_fallback from '$lib/images/svelte-welcome.png';

	let searchValue = ''

	let selectedSong = ''
	let selectedId = ''

	let selectedTrack = {}

	let tracks = []

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
			tracks = jsonResponse.tracks
			selectedSong = tracks[0].title
			selectedTrack = tracks[0]
			selectedId = tracks[0].id
			searchValue = selectedSong
		} catch (error) {
			// Handle any errors that occurred during the fetch request.
			console.error('Error fetching data:', error);
		}
	}

	let updatedSelectedSong = () => {
		searchValue = selectedSong;
		for (let i = 0; i < tracks.length; i++) {
			if (tracks[i].title == selectedSong) {
				selectedId = tracks[i].id;
			}
		}
		console.log('Search Value: ', searchValue)
		console.log('selected ID: ', selectedId)
	}

	$: embedUrl = `https://open.spotify.com/embed/track/${selectedId}?utm_source=generator&theme=0`

	$: console.log(tracks)

</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	<input type="text" placeholder="Search.." bind:value={searchValue}>
	{#if tracks.length > 0}
	<select name='search-dropdown' id='search-dropdown' bind:value={selectedSong} on:change={updatedSelectedSong}>
		{#each tracks as track}
			<option value={track.title}>{track.title} By: {track.artists[0]}</option> 
		{/each}
	</select>
	{/if}
	<button value="Test" on:click={getSearchSongs}>Fetch SearchSongs</button>

	{#if selectedTrack.id}
	<iframe style="border-radius:12px" src={embedUrl} width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
	{/if}
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
