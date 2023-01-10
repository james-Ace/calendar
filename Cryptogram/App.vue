<script>
	export default {

		onLaunch: function() {
			
		},
		onShow: function() {
			console.log('App Show')
		},
		onHide: function() {
			console.log('App Hide')
		}
	}
</script>

<style>
	/*每个页面公共css */
	.bar{
		height: var(--status-bar-height);
		background: #fff;
	}
	.content {
		display: flex;
		flex-direction: column;
		background-color: #f5f5f5;
		height: 100vh;
	}
</style>
