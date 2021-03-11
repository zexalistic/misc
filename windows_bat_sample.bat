:: Prerequisites:
:: 1. Python3.7(32bit) or above already set as environment variable
:: 2. pip already installed
:: 3. You'd better do these two steps first -> 1) git config --global user.email "your email address" 
::	2)git config --global user.name "your name"
:: 4. Have access to those gitlab projects
:: 5. Please run this script under the current folder


	@echo off
	echo //Note !!! This is a note
	:Get_package_from_gitlab
	if not exist CommonUtil git clone https://github.com/zexalistic/misc
	
	:: Rename those folders in windows, python script is case-sensitive
	:correct_folder_names
	ren commonutil CommonUtil
	

	:Install_python_packages
	:: NOTE !!! Some of those packages are stick to the old version
	python -m pip install ixexplorer-0.2.0.tar.gz
	
	
	if not exist PyIxia goto Pre1
	goto Main
		

	:Main
	
	goto End

	:Pre1
	md PyIxia
	goto Main
	
	:End
	echo.