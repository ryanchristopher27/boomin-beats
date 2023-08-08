<script>
	import { page } from '$app/stores';
	import { BoominBeatsLogo } from '$lib';
	import github from '$lib/images/github.svg';

	export let current_page = 'Home';
</script>

<header>
	<div class="header-div">
		<div class="logo-div">
			<img src={BoominBeatsLogo} alt="SvelteKit" id="boomin-beats-logo"/>
		</div>

		<nav>
			{#if current_page == 'Home'}
			<div class='nav-button-div'>
				<a class="nav-button-active" href="/">Home</a>
			</div>
			{:else}
			<div class='nav-button-div'>
				<a class="nav-button" href="/">Home</a>
			</div>
			{/if}
			<!-- <svg viewBox="0 0 2 3" aria-hidden="true">
				<path d="M0,0 L1,2 C1.5,3 1.5,3 2,3 L2,0 Z" />
			</svg>
			<ul>
				<li aria-current={$page.url.pathname === '/' ? 'page' : undefined}>
					<a href="/">Home</a>
				</li>
			</ul>
			<svg viewBox="0 0 2 3" aria-hidden="true">
				<path d="M0,0 L0,3 C0.5,3 0.5,3 1,2 L2,0 Z" />
			</svg> -->
		</nav>
	</div>
</header>

<style>
	header {
		display: flex;
		justify-content: space-between;
		position: fixed;
		top: 0;
		width: 98%;
		min-width: 800px;
		background-color: var(--color-light-blue);
		/* margin: var(--primary-spacing) var(--primary-spacing) 0 var(--primary-spacing); */
		padding: var(--primary-spacing);
	}

	.header-div {
		display: flex;
		height: 50px;
		background-color: #242424;
		width: 100%;
		min-width: 800px;
		border-bottom: 2px solid var(--color-light-blue);
		border-radius: 20px;
	}

	#boomin-beats-logo {
		height: 40px;
		margin-top: 5px;
		margin-left: 5px;
	}

	.nav-button-div {
		height: 50px;
		/* padding: 10px 0; */
	}

	.nav-button {
		margin: 8px 20px;
		height: 30px;
		border: 2px solid #5ec9ff;
		border-radius: 20px;
	}

	nav {
		display: flex;
		justify-content: center;
		--background: rgba(255, 255, 255, 0.7);
	}

	nav a {
		display: flex;
		/* height: 40px; */
		align-items: center;
		padding: 0 0.5rem;
		color: var(--color-light-blue);
		font-weight: 700;
		font-size: 0.8rem;
		text-transform: uppercase;
		letter-spacing: 0.1em;
		text-decoration: none;
		transition: color 0.2s linear;
	}

	a:hover {
		/* color: var(--color-dark-gray);
		background-color: var(--color-purple); */
		border-color: var(--color-purple);
	}

	.nav-button-active {
		color: var(--color-dark-gray);
		background-color: var(--color-light-blue);
		margin: 8px 20px;
		height: 30px;
		border: 2px solid #5ec9ff;
		border-radius: 20px;
	}
</style>
