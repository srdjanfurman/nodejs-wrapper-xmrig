{
	"targets": [
		{
			"target_name": "xmrigCpu",
			"include_dirs": [
				"src",
				"<!(node -e \"require('nan')\")",
				"src/3rdparty",
				"src/3rdparty/libcpuid",
				"src/base/kernel/interfaces",
				"src/base/io/json",
				"src/backend/common/interfaces"
			],
			"sources": [
				"src/xmrig.cpp",
				"src/Mem.cpp",
				"src/NodeApp.cpp",
				"src/NodeXmrigCpu.cpp",
				"src/Summary.cpp",
				
				"src/base/io/Console.cpp",
				"src/base/io/log/backends/ConsoleLog.cpp",
				"src/base/io/log/backends/FileLog.cpp",
				"src/base/io/log/Log.cpp",
				"src/base/io/Watcher.cpp",
				"src/base/net/stratum/Client.cpp",
				"src/base/net/stratum/Job.cpp",
				"src/base/net/stratum/Pool.cpp",
				"src/base/net/stratum/strategies/FailoverStrategy.cpp",
				"src/base/net/stratum/strategies/SinglePoolStrategy.cpp",
				
				"src/core/config/Config.cpp",
				"src/core/config/ConfigTransform.cpp",
				"src/core/Miner.cpp",
				"src/core/Controller.cpp",
				
				"src/net/Network.cpp",
				"src/net/NetworkState.cpp",
				"src/net/JobResults.cpp",
				"src/net/strategies/DonateStrategy.cpp",
				
				"src/base/kernel/config/BaseConfig.cpp",
				"src/base/kernel/config/BaseTransform.cpp",
				"src/base/kernel/Platform.cpp",
				"src/base/kernel/Base.cpp",
				"src/base/kernel/Process.cpp",
				"src/base/tools/Arguments.cpp",
				"src/base/tools/String.cpp",
				"src/base/tools/Timer.cpp",
				"src/base/tools/Buffer.cpp",
				"src/base/net/http/Http.cpp",
				"src/base/net/stratum/Pools.cpp",
				"src/base/net/stratum/Url.cpp",
				"src/base/net/stratum/BaseClient.cpp",
				"src/base/net/dns/Dns.cpp",
				"src/base/net/dns/DnsRecord.cpp",
				"src/base/io/json/JsonChain.cpp",
				"src/base/io/json/Json.cpp",
				"src/base/io/json/Json_unix.cpp",
				"src/base/io/json/JsonRequest.cpp",

				"src/backend/cpu/platform/BasicCpuInfo.cpp",
				"src/backend/cpu/CpuThread.cpp",
				"src/backend/cpu/CpuThreads.cpp",
				"src/backend/cpu/Cpu.cpp",
				"src/backend/cpu/CpuConfig.cpp",
				"src/backend/cpu/CpuBackend.cpp",
				"src/backend/cpu/CpuLaunchData.cpp",
				"src/backend/cpu/CpuWorker.cpp",
				"src/backend/common/Threads.cpp",
				"src/backend/common/Hashrate.cpp",
				"src/backend/common/Worker.cpp",
				"src/backend/common/Workers.cpp",

				"src/crypto/common/keccak.cpp",
				"src/crypto/common/Nonce.cpp",
				"src/crypto/common/VirtualMemory.cpp",
				"src/crypto/common/VirtualMemory_unix.cpp",
				"src/crypto/common/MemoryPool.cpp",
				"src/crypto/common/Algorithm.cpp",
				"src/crypto/common/Coin.c",
				
				"src/crypto/rx/Rx.cpp",
				"src/crypto/rx/RxVm.cpp",
				"src/crypto/rx/RxAlgo.cpp",
				"src/crypto/rx/RxCache.cpp",
				"src/crypto/rx/RxQueue.cpp",
				"src/crypto/rx/RxConfig.cpp",
				"src/crypto/rx/RxDataset.cpp",
				"src/crypto/rx/RxConfig_basic.cpp",
				"src/crypto/rx/RxBasicStorage.cpp",
				"src/crypto/rx/RxNUMAStorage.cpp",

				"src/3rdparty/libcpuid/asm-bits.c",
				"src/3rdparty/libcpuid/recog_amd.c",
				"src/3rdparty/libcpuid/recog_intel.c",
				"src/3rdparty/libcpuid/libcpuid_util.c",
				"src/3rdparty/libcpuid/cpuid_main.c"
			],
			'cflags!': [
				'-pthread'
			],
			'cflags': [
				"-maes"
			],
			'cflags_cc!': [
				'-std=gnu++0x'
			],
			"cflags_cc": [
				"-std=c++11",
				"-maes",
				"-Wno-unused-variable"
			],
			'defines': [
				'UNICODE',
				'RAPIDJSON_SSE2',
				'XMRIG_NO_HTTPD',
				'XMRIG_NO_API',
				'_GNU_SOURCE',
				'XMRIG_ALGO_RANDOMX'
				
			],
			'conditions': [
				[
					'OS=="win"',
					{
						'sources': [
							'res/app.rc',
							'src/App_win.cpp',
							'src/base/kernel/Platform_win.cpp',
							'src/Cpu_win.cpp',
							'src/Mem_win.cpp',
							'src/3rdparty/libcpuid/masm-x64.asm'
						],
						"defines": [
							"WIN32"
						],
						"link_settings": {
							"libraries": [
								"-lws2_32",
								"-lpsapi",
								"-liphlpapi",
								"-luserenv"
							]
						}
					},
					'OS=="mac"',
					{
						'sources': [
							'src/App_unix.cpp',
							'src/base/kernel/Platform_mac.cpp',
							'src/Cpu_mac.cpp',
							'src/Mem_unix.cpp'
						],
						'xcode_settings':
						{
							'OTHER_CFLAGS': ['-maes']
						}

					},
					'OS=="linux"',
					{
						'sources': [
							'src/App_unix.cpp',
							'src/base/kernel/Platform_unix.cpp',
							'src/Cpu_mac.cpp',
							'src/Mem_unix.cpp'
						],
						'defines': [
							'NDEBUG',
							'XMRIG_NO_IPBC',
							'__STDC_FORMAT_MACROS'
						],
						"link_settings": {
							"libraries": [
								"-lrt"
							]
						}
					}
				]
			]
		}
	]
}
