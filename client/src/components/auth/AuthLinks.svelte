<script lang="ts">
	import { auth } from '$s/auth';
</script>

{#if $auth.user}
	<a
		class="font-medium text-gray-600 hover:text-gray-400"
		href="/auth/signout">Sign Out</a
	>
{:else}
	<a
		class="font-medium text-gray-600 hover:text-gray-400"
		href="/auth/signin">Login</a
	>
	<a
		class="font-medium text-gray-600 hover:text-gray-400"
		href="/auth/signup">Sign Up</a
	>
{/if}
