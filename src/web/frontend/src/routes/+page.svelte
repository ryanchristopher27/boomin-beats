<script>
	import Counter from './Counter.svelte';
	import welcome from '$lib/images/svelte-welcome.webp';
	import welcome_fallback from '$lib/images/svelte-welcome.png';

	let searchValue = '';

	let selectedTitle = '';
	let selectedArtists = [];
	let selectedId = '';

	let isSelected = false;

	let tracks = [];

	const myHeaders = new Headers();
	myHeaders.append("Access-Control-Allow-Origin", "http://127.0.0.1:8000/spotify-login/");

	async function getSearchSongs() {
		try {
			let url = `http://127.0.0.1:8000/spotify-login/?searchValue=${searchValue}`

			const response = await fetch(url)

			if (!response.ok) {
				throw new Error('Network response was not ok.');
			}

			const jsonResponse = await response.json()
			tracks = jsonResponse.tracks
			selectedTitle = tracks[0].title
			selectedArtists = tracks[0].artists
			selectedId = tracks[0].id
			// searchValue = selectedSong
		} catch (error) {
			// Handle any errors that occurred during the fetch request.
			console.error('Error fetching data:', error);
		}
	}

	let updatedSelectedSong = (selectedTrack, index) => {
		isSelected = true;
		searchValue = selectedTrack;
		// for (let i = 0; i < tracks.length; i++) {
		// 	if (tracks[i].title == selectedTrack) {
		// 		selectedId = tracks[i].id;
		// 		selectedTrack = tracks[i]
		// 	}
		// }
		selectedTitle = tracks[index].title
		selectedArtists = tracks[index].artists
		selectedId = tracks[index].id
		console.log('Search Value: ', searchValue)
		console.log('selected Title: ', selectedTitle)
		console.log('selected Artists: ', selectedArtists)
		console.log('selected ID: ', selectedId)

		tracks = []
	}

	$: embedUrl = `https://open.spotify.com/embed/track/${selectedId}?utm_source=generator&theme=0`

	$: console.log(tracks)

</script>

<svelte:head>
	<title>Search</title>
	<meta name="description" content="Song Search" />
</svelte:head>

<section>
	<div id='searchbar'>
		<input type="text" placeholder="Search.." bind:value={searchValue} on:change={getSearchSongs} on:input={getSearchSongs}>
		{#if tracks.length > 0}
		{#each tracks as track, i}
			<option value={track.title} on:click={() => {updatedSelectedSong(track.title, i)}}>{track.title} By: {track.artists[0]}</option>
			<!-- <div class='search_dropdown' bind:value={track.title}>{track.title} By: {track.artists[0]}</div> -->
			<!-- <a  on:click={updatedSelectedSong}>{track.title} By: {track.artists[0]}</a>  -->
		{/each}
		{/if}
		<!-- {#if tracks.length > 0}
		<select name='search-dropdown' id='search-dropdown' bind:value={selectedSong} on:change={updatedSelectedSong}>
			{#each tracks as track}
				<option value={track.title}>{track.title} By: {track.artists[0]}</option> 
			{/each}
		</select>
		{/if} -->
		<!-- <button value="Test" on:click={getSearchSongs}>Fetch SearchSongs</button> -->
	</div>

	<!-- {#if isSelected}
	<iframe style="border-radius:12px" src={embedUrl} width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
	{/if} -->

	{#if isSelected}
	<div id='selected-song-div'>
		<h2>Selected Song</h2>
		<p id='selected-song-title'>{selectedTitle}</p>
		<p id='selected-song-artist'>{selectedArtists}</p>
		<p id='selected-song-id'>{selectedId}</p>
	</div>
	{/if}
	
	<button id='get-recs-button'>Get Recommendations</button>

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
