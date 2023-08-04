<script>
    export let track_id = '';
    export let show_tracks = false;
    export let number_of_songs = 25;

    let recommendations = Array();

    let recommendations_ids = Array();

    async function getRecommendations() {
		try {
			let url = `http://127.0.0.1:8000/get-recommendations/?trackId=${track_id}&numberOfSongs=${number_of_songs}`

			const response = await fetch(url)

			if (!response.ok) {
				throw new Error('Network response was not ok.');
			}

			const jsonResponse = await response.json();
            recommendations = jsonResponse.tracks;

            recommendations_ids = recommendations.map((track) => {
                return track.id
            })
		} catch (error) {
			// Handle any errors that occurred during the fetch request.
			console.error('Error fetching data:', error);
		}
	}

    $: if (show_tracks) {
        getRecommendations()
    }

    $: console.log('Recommendations: ', recommendations)
    $: console.log(recommendations_ids)
</script>

<div id='recs-wrapper-div'>
    <div>Test</div>
    {#if show_tracks}
    {#each recommendations as track}
    <!-- <div>
        {track.title}
    </div> -->
    <iframe style="border-radius:12px" src={`https://open.spotify.com/embed/track/${track.id}?utm_source=generator&theme=0`} width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    <!-- <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/4Tjh34RS4ACZ6f6srlDBg8?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe> -->
    {/each}
    {/if}
</div>

<style>
    #recs-wrapper-div {
        height: auto;
    }
</style>