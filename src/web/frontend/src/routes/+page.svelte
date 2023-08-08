<script>
	import { Recommendations } from "$lib";

	let searchValue = '';

	let selectedTitle = '';
	let selectedArtists = [];
	let selectedId = '';

	let isSelected = false;

	let tracks = [];

	let showRecommendations = false;

	const myHeaders = new Headers();
	myHeaders.append("Access-Control-Allow-Origin", "http://127.0.0.1:8000/search/");

	async function getSearchSongs() {
		try {
			let url = `http://127.0.0.1:8000/search/?searchValue=${searchValue}`

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
		selectedTitle = tracks[index].title
		selectedArtists = tracks[index].artists
		selectedId = tracks[index].id
		console.log('Search Value: ', searchValue)
		console.log('selected Title: ', selectedTitle)
		console.log('selected Artists: ', selectedArtists)
		console.log('selected ID: ', selectedId)

		tracks = []
	}

	let getRecommendations = () => {
		console.log('Get Recommendations')
		showRecommendations = true;
	}

	$: embedUrl = `https://open.spotify.com/embed/track/${selectedId}?utm_source=generator&theme=0`

	$: console.log(tracks)

	$: console.log(selectedTitle, selectedId)

</script>

<svelte:head>
	<title>Search</title>
	<meta name="description" content="Song Search" />
</svelte:head>

<div class='body-div'>
	<div class='search-div'>
		<!-- <input type="text" placeholder="Search.." bind:value={searchValue} on:change={getSearchSongs} on:input={getSearchSongs}>
		{#if tracks.length > 0}
		{#each tracks as track, i}
			<option value={track.title} on:click={() => {updatedSelectedSong(track.title, i)}}>{track.title} By: {track.artists[0]}</option>
		{/each}
		{/if} -->

		<input class="searchbar" list="searchbar" name="searchbar" placeholder="Search.." bind:value={searchValue} on:change={getSearchSongs} on:input={getSearchSongs} />
		<datalist id="searchbar">
		{#each tracks as track, i}
			<option value={track.title} on:click={() => {updatedSelectedSong(track.title, i)}}>{track.title} By: {track.artists[0]}</option>
		{/each}
		</datalist>
		<button id='get-recs-button' on:click={() => {getRecommendations()}}>Get Recs</button>
	</div>
	

	<Recommendations track_id={selectedId} number_of_songs={25} show_tracks={showRecommendations} />

</div>

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

	.body-div {
		/* display: flex; */
		/* height: 100vh; */
		width: 100%;
		background-color: var(--color-dark-gray);
		min-width: 500px;
	}

	.search-div {
		display: flex;
		width: 80%;
		margin-left: 10%;
	}

	.searchbar {
		height: 24px;
		width: 90%;
		min-width: 292px;
		margin: 10px 0 0 0;
		background-color: var(--color-dark-gray);
		color: var(--color-light-blue);
		border: 2px solid var(--color-light-blue);
		border-radius: 10px;
	}

	#get-recs-button {
		height: 30px;
		width: 10%;
		margin: 10px 0 0 10px;
		min-width: 90px;
		background-color: var(--color-dark-gray);
		color: var(--color-light-blue);
		border: 2px solid var(--color-light-blue);
		border-radius: 10px;
	}

	#get-recs-button:hover {
		background-color: var(--color-light-blue);
		color: var(--color-dark-gray);
	}

</style>
