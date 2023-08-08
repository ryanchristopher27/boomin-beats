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

    function millisToMinutesAndSeconds(millis) {
        let minutes = Math.floor(millis / 60000);
        let seconds = ((millis % 60000) / 1000).toFixed(0);
        return (seconds == 60 ? (minutes+1) + ":00" : minutes + ":" + (Number(seconds) < 10 ? "0" : "") + seconds
        );    
    }

    $: if (show_tracks) {
        getRecommendations()
    }

    $: console.log('Recommendations: ', recommendations)
    $: console.log(recommendations_ids)
</script>

<div id='recs-wrapper-div'>
    {#if show_tracks}
    {#each recommendations as track}
    <div class='rec-song-div'>
        <img src={track.image} alt="Image" class="track-image"/>
        <div class='title-artist-div'>
            <div class='title-div'>
                {track.title}
            </div>
            <div class='artist-div'>
                {#if track.explicit === true}
                <div class='explicit-div'>
                    E
                </div>
                {/if}
                {#each track.artists as artist, i}
                <div class='each-artist-div'>
                    {#if i === track.artists.length - 1}
                    {artist}
                    {:else}
                    {artist},
                    {/if}
                </div>
                {/each}
            </div>
        </div>
        <div class='album-div'>
            {track.album}
        </div>
        <div class='duration-div'>
            {millisToMinutesAndSeconds(Number(track.duration_ms))}
        </div>
    </div>
    <hr class='track-splitter'>
    <!-- <iframe style="border-radius:12px" src={`https://open.spotify.com/embed/track/${track.id}?utm_source=generator&theme=0`} width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe> -->
    <!-- <iframe style="border-radius:12px" src={`https://open.spotify.com/embed/track/${track.id}?utm_source=generator`} width="100%" height="76" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe> -->
    {/each}
    {/if}
</div>

<style>
    #recs-wrapper-div {
        height: auto;
        margin-top: 20px;
        margin: 20px 10%;
        min-width: 640px;
    }

    .rec-song-div {
        display: flex;
        height: 64px;
        color: white;
        /* border: 2px solid white; */
        /* vertical-align: middle; */
        align-items: center;
        /* justify-content: center; */
        /* border-bottom: 2px solid var(--color-light-blue); */

    }

    .title-artist-div {
        width: 40%;
        white-space: nowrap;
        overflow: hidden;
        padding: 0 10px;
    }

    .title-div {
        display: table-cell;
        height: 40px;
        width: 100%;
        vertical-align: middle;
        font-weight: bold;
        /* text-align: center; */
    }

    .artist-div {
        display: flex;
        height: 24px;
        width: 100%;
        vertical-align: middle;
        align-items: center;
        /* text-align: center; */
    }

    .explicit-div {
        height: 15px;
        width: 15px;
        margin-right: 5px;
        text-align: center;
        font-size: 12px;
        background-color: white;
        color: var(--color-dark-gray);
        border-radius: 2px;
    }

    .each-artist-div {
        margin-right: 10px;
    }

    .album-div {
        width: 30%;
        padding: 0 10px;
        vertical-align: middle;
        text-align: center;
    }

    .duration-div {
        width: 20%;
        padding: 0 10px;
        vertical-align: middle;
        text-align: center;
    }

    .track-splitter {
        color: white;
    }
</style>