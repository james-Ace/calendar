<template>
	<view class="content">
		<view class="bar"></view>
		<view class="top">
			<uni-icons class="icons" type="bars" size="26"></uni-icons>
			<h1 class="logo">Cryptogram</h1>
			<uni-icons class="icons" type="search" size="26"></uni-icons>
		</view>
		<!-- top end -->
		<view class="body">
			
			<view class="items" v-for="(item,index) in data">
				<strong>{{item.title}}</strong>
				<uni-tag v-for="tag in item.tag" :text="tag.name" :type="tag.type"></uni-tag>
				<rudon-rowMenuDotDotDot :localdata="options" @change="menuAction($event, index)">
					<uni-icons type="more" class="more" size="28"></uni-icons>
				</rudon-rowMenuDotDotDot>
			</view>
			<!-- items end  -->
		</view>
		<!-- body end -->
		<view class="bottom_nav">
			<button>
				<uni-icons class="icons" type="plusempty" size="24"></uni-icons>
			</button>
		</view>
		<!-- bottom_nav end -->
	</view>
</template>

<script>
	export default {
		data() {
			return {
				data:[
					{
						title: '沃依网站后台账号',
						name: 'admin',
						tag:[{
							type: 'warning',
							name: '网站后台'
						}],
						password: 'admin123'
					},
					{
						title: '沃依网站后台账号',
						name: 'admin',
						tag:[{
							type: 'primary',
							name: '网站后台'
						}],
						password: 'admin123'
					},
					{
						title: '沃依网站后台账号',
						name: 'admin',
						password: 'admin123',
						tag:[{
							type: 'success',
							name: '服务器'
						}],
					},
					{
						title: '沃依网站后台账号',
						name: 'admin',
						password: 'admin123'
					},
					{
						title: '沃依网站后台账号',
						name: 'admin',
						password: 'admin123'
					}
				],
				// 右边菜单内容
				options: [{
						value: 'eye',
						text: '查看'
					},
					{
						value: 'update',
						text: '修改'
					},
					{
						value: 'share',
						text: '分享'
					}
				]
			}
		},
		onLoad() {

		},
		methods: {
			/**
			 * 不同行的不同菜单点击事件
			 * 
			 * @param {Object} action 第一个参数必须传入“$event” | 点击了哪个按钮 | 传入options的value
			 * @param {Number} rowId 第二个参数随意，可以是行ID等
			 */
			menuAction(action, rowId) {
				// 忽略初始化时的传入的空操作
				if (action === '') {
					return
				}else{
					switch (action){
						case 'eye':
							break;
						case 'update':
							break;
						case 'share':
							break;
						default:
							break;
					}
				}
				console.log(rowId)
			}
		}
	}
</script>

<style>
	.top {
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		height: 60rpx;
		padding: 0 20rpx;
		background: #fff;
		border-bottom: 1px solid #f4f4f4;
		padding-bottom: 10rpx;
	}

	.top h1 {
		font-size: 27rpx;
		text-transform: uppercase;
		letter-spacing: 1rpx;
		line-height: 60rpx;
	}

	.top .icons {
		margin-top: 8rpx;
	}

	.bottom_nav {
		position: fixed;
		bottom: 0;
		left: 50%;
		margin-bottom: 40rpx;
		margin-left: -40rpx;
	}

	.bottom_nav button {
		border-radius: 50%;
		width: 100rpx;
		height: 100rpx;
		line-height: 100rpx;
		border: 1rpx solid gold;
		background-color: gold;
	}

	uni-button:after {
		border: none;
	}

	.bottom_nav .icons {
		margin-left: -3rpx;
	}

	.items {
		width: 90%;
		margin: 30rpx auto;
		background-color: #fff;
		padding: 30rpx 15rpx;
		display: flex;
		justify-content: space-between;
		box-shadow: 0 3rpx 8rpx rgba(0, 0, 0, 0.0800);
		border-radius: 12rpx;
	}

	.items strong {
		display: inline-block;
		line-height: 60rpx;
		margin-right: 10%;
		width: 60%;
		overflow: hidden;
		word-break: keep-all;
		text-overflow: ellipsis;
	}

	.items .uni-tag {
		height: 25rpx;
		margin-top: 10rpx;
	}

	.items .more {
		margin-right: -20rpx;
		margin-top: 6rpx;
		transform: rotate(90deg);
	}
</style>
