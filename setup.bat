:: Prerequisites:
:: 1. Python3.7(32bit) or above already set as environment variable
:: 2. pip already installed
:: 3. You'd better do these two steps first -> 1) git config --global user.email "your email address" 
::	2)git config --global user.name "your name"
:: 4. Have access to those gitlab projects
:: 5. Please run this script under the current folder， pwd should be "pyfunctest"


	@echo off
	echo //Note !!! ixexplorer is a customized standard lib, please do not use pyixexplorer
	:Get_package_from_gitlab
	if not exist CommonUtil git clone http://10.38.174.192:8080/xgong/commonutil.git  
	::if not exist ixexplorer git clone http://10.38.174.192:8080/muxiang/ixexplorer.git
	if not exist FPGAWrapperServer git clone http://10.38.174.192:8080/muxiang/fpgawrapperserver.git
	if not exist FPGAWrapperClient git clone http://10.38.174.192:8080/muxiang/fpgawrapperclient.git
	if not exist PyDut git clone http://10.38.174.192:8080/muxiang/pydut.git
	if not exist FunctionTestRunner git clone http://10.38.174.192:8080/muxiang/functiontestrunner.git
	if not exist PyIxia\BasePktGen git clone http://10.38.174.192:8080/muxiang/basepktgen.git
	if not exist PyIxia\IxePktGenn git clone http://10.38.174.192:8080/muxiang/ixepktgen.git
	
	:: Rename those folders, python script is case-sensitive
	:correct_folder_names
	ren commonutil CommonUtil
	ren fpgawrapperclient FPGAWrapperClient
	ren pydut PyDut
	ren functiontestrunner FunctionTestRunner
	ren fpgawrapperserver FPGAWrapperServer
	

	:Install_python_packages
	:: NOTE !!! Some of those packages are stick to the old version
	python -m pip install ixexplorer-0.2.0.tar.gz
	
	:use_sample_config_file
	move config.json CommonUtil\config.json
	
	if not exist PyIxia goto Pre1
	goto Main
		

	:Main
	
	goto End

	:Pre1
	md PyIxia
	move ixepktgen PyIxia\IxePktGen
	move basepktgen PyIxia\BasePktGen
	goto Main
	
	:End
	echo.