if exist async_simple (
	cd async_simple
	git pull
	cd ..
) else (
	git clone --recurse-submodules=true git@github.com:alibaba/async_simple.git
)

if exist yomo (
	cd yomo
	git pull
	cd ..
) else (
	git clone --recurse-submodules=true git@github.com:yomorun/yomo.git
)

