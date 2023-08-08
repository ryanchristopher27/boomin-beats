<script>
	import { Recommendations } from "$lib";

	let searchValue = '';

	let selectedSong = {};

	// let selectedTitle = '';
	// let selectedArtists = [];
	// let selectedId = '';

	let isSelected = false;

	let tracks = [];
	let trackTitles = [];

	let possibleNumberOfSongs = [10, 25, 50];
	let numberOfSongs = 25;

	// let showRecommendations = false;

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
			trackTitles = tracks.map((track) => track.title)
			// selectedTitle = tracks[0].title
			// selectedArtists = tracks[0].artists
			// selectedId = tracks[0].id

			// searchValue = selectedSong
		} catch (error) {
			// Handle any errors that occurred during the fetch request.
			console.error('Error fetching data:', error);
		}
	}

	let updatedSelectedSong = (selectedTrack) => {
		console.log('Selected Track:', selectedTrack)
		let index = trackTitles.indexOf(selectedTrack)
		isSelected = true;
		searchValue = selectedTrack;
		selectedSong = tracks[index]
		tracks = []
		trackTitles = []
	}

	let getRecommendations = () => {
		console.log('Get Recommendations')
		updatedSelectedSong(searchValue)
	}

	let setNumberOfSongs = (number) => {
		numberOfSongs = number;

	}

	// $: embedUrl = `https://open.spotify.com/embed/track/${selectedSong.id}?utm_source=generator&theme=0`

	$: console.log(tracks)

	$: console.log(selectedSong)

	// $: console.log(selectedTitle, selectedId)

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
			<option value={track.title} on:click={() => {updatedSelectedSong(track.title)}}>{track.title} By: {track.artists[0]}</option>
		{/each}
		</datalist>
		<button id='get-recs-button' on:click={() => {getRecommendations()}}>Get Recs</button>
	</div>
	<div class='number-of-songs-div'>
		{#each possibleNumberOfSongs as num}
		{#if num === numberOfSongs}
		<button class='number-of-songs-button-selected' on:click={() => {setNumberOfSongs(num)}}>{num}</button>
		{:else}
		<button class='number-of-songs-button' on:click={() => {setNumberOfSongs(num)}}>{num}</button>
		{/if}
		{/each}
	</div>
	

	<Recommendations track_id={selectedSong.id} number_of_songs={numberOfSongs} />

</div>

<style>
	/* section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	} */

	.body-div {
		/* display: flex; */
		/* height: 100vh; */
		min-height: 100vh;
		width: 100%;
		background-color: var(--color-dark-gray);
		min-width: 800px;
		border-radius: 20px;
	}

	.search-div {
		display: flex;
		width: 80%;
		min-width: 640px;
		margin-left: 10%;
		margin-top: 20px;
	}

	.searchbar {
		height: 24px;
		width: 90%;
		min-width: 292px;
		/* margin: 20px 0 0 0; */
		background-color: var(--color-dark-gray);
		color: var(--color-light-blue);
		border: 2px solid var(--color-light-blue);
		border-radius: 10px;
	}

	.number-of-songs-div {
		display: flex;
		width: 80%;
		min-width: 640px;

		margin: 20px 0 20px 10%;
	}

	.number-of-songs-button {
		height: 30px;
		width: 10%;
		margin-left: 15%;
		background-color: var(--color-dark-gray);
		color: var(--color-light-blue);
		border: 2px solid var(--color-light-blue);
		border-radius: 10px;
	}

	.number-of-songs-button-selected {
		height: 30px;
		width: 10%;
		margin-left: 15%;
		background-color: var(--color-light-blue);
		color: var(--color-dark-gray);
		border: 2px solid var(--color-light-blue);
		border-radius: 10px;
	}

	#get-recs-button {
		height: 30px;
		width: 10%;
		/* margin: 10px 0 0 10px; */
		margin-left: 10px;
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
