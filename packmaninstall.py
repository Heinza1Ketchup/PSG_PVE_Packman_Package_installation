import os
import subprocess
from datetime import datetime

now = datetime.now()

arr = ['PSG_PVE_Site_Detection_Package', 'PSG_PVE_Path_modification_Package', 'PSG_PVE_Startup_NetworkDrive_Map_Package', 'PSG_PVE_Duplicate_Path_Removal_Package'
, 'PSG_PVE_Python36_Package', 'PSG_PVE_NGA_Prod_Baremetal_Package', 'PSG_PVE_Anaconda3_Package', 'PSG_PVE_ActiveTCL_Package', 'PSG_PVE_Allegro_Free_Physical_Viewers_Package', 
'PSG_PVE_AutoIt_Package', 'PSG_PVE_Microsoft_VCRuntime_2015_Package', 'PSG_PVE_Arduino_Package', 'PSG_PVE_Capture2Text_Package', 'PSG_PVE_CLEDemo1000_Package', 
'PSG_PVE_gVim_Package', 'PSG_PVE_IZArc_Package', 'PSG_PVE_Lecroy_Startup_Removal_Package', 'PSG_PVE_Lecroy_Wavepulser_Package', 'PSG_PVE_WebPowerSwitch_Package', 
'PSG_PVE_Perforce_Package', 'PSG_PVE_PyScripter_Package', 'PSG_PVE_SiliconThermal_Controller_Package', 'PSG_PVE_WinSCP_Package', 'PSG_PVE_Sublime_Text3_Package', 
'PSG_PVE_Thermal_Control_Driver_Package', 'PSG_PVE_ThinkPad_LAN_to_USB_Package', 'PSG_PVE_Keysight_IO_LibSuite_Package', 'PSG_PVE_Keysight_IO_Bugfix_Package', 
'PSG_PVE_LabVIEW_2016_Package', 'PSG_PVE_NI-VISA_Package', 'PSG_PVE_NI-4882_Package', 'PSG_PVE_LabView_Patch_Package', 'PSG_PVE_Lecroy_PE_Tracer_Package',
'PSG_PVE_LTPowerPlay_Package', 'PSG_PVE_OpenSSH_Package', 'PSG_PVE_SiLab_ClockBuilder_Pro_Package', 'PSG_PVE_wubj_Package', 
'PSG_PVE_MAX31730_Package', 'PSG_PVE_TeraTerm_Package', 'PSG_PVE_ADI_Power_Studio_Package', 'PSG_PVE_PyCCA_GUNDERSONROCK_SV_Package', 'PSG_PVE_CP210x_USB_Driver_Package', 
'PSG_PVE_FT232_Driver_Package', 'PSG_PVE_cURL_Package', 'PSG_PVE_pysv_checkout', 'PSG_PVE_pysv_checkout_git', 'PSG_PVE_pysv_checkout_path_commands', 'PSG_PVE_pysv_checkout_githooks',
'PSG_PVE_7Zip_Package', 'PSG_PVE_OpenJDK_Package', 'PSG_PVE_WinZip_uninstaller_Package', 'PSG_PVE_Adobe_AcrobatReaderDC_Package', 'PSG_PVE_Putty_Package', 
'PSG_PVE_WireShark_Package', 'PSG_PVE_VEP_Pitboss_SystemChecker_Package', 'PSG_PVE_Bonjour_Uninstaller_Package', 'PSG_PVE_StickyPad_Uninstaller_Package', 'PSG_PVE_MX183000A_Package',
'Dediprog', 'PSG_PVE_VEP_Pitboss_SystemChecker_Package', 'PSG_PVE_TTK2_Package', 'SysCfg', 'RAMP', 'PowerSplitter', 'OpenDebug', 'Latte', 'WebCAM_Viewer', 'NotepadPlusPlus_V7']

def subprocess_cmd(command, package):
	process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	proc_stdout = process.communicate()[0]
	#print(proc_stdout)
	return_code = process.poll()
	while True:
		if return_code is not None:
			now = datetime.now()
			print("==========", package, "==========")
			print("installation finished at", now)
			break
	return


subprocess_cmd('\\amr.corp.intel.com\ec\proj\ha\sa\sa_laboratory\SA_FM_SYNC\TMT_SW\Bronze\Packman\install.bat', 'Packman CLI')
subprocess_cmd('packman install --name PVE_Packman_Check', 'Packman Check')

for x in range(68):
	subprocess_cmd('packman install --name' + ' ' + str(arr[x]), arr[x])

