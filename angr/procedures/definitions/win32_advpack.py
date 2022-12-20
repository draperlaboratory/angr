# pylint:disable=line-too-long
import logging

from ...sim_type import SimTypeFunction,     SimTypeShort, SimTypeInt, SimTypeLong, SimTypeLongLong, SimTypeDouble, SimTypeFloat,     SimTypePointer,     SimTypeChar,     SimStruct,     SimTypeFixedSizeArray,     SimTypeBottom,     SimUnion,     SimTypeBool
from ...calling_conventions import SimCCStdcall, SimCCMicrosoftAMD64
from .. import SIM_PROCEDURES as P
from . import SimLibrary


_l = logging.getLogger(name=__name__)


lib = SimLibrary()
lib.set_default_cc('X86', SimCCStdcall)
lib.set_default_cc('AMD64', SimCCMicrosoftAMD64)
lib.set_library_names("advpack.dll")
prototypes = \
    {
        #
        'RunSetupCommandA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hWnd", "szCmdName", "szInfSection", "szDir", "lpszTitle", "phEXE", "dwFlags", "pvReserved"]),
        #
        'RunSetupCommandW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hWnd", "szCmdName", "szInfSection", "szDir", "lpszTitle", "phEXE", "dwFlags", "pvReserved"]),
        #
        'NeedRebootInit': SimTypeFunction([], SimTypeInt(signed=False, label="UInt32")),
        #
        'NeedReboot': SimTypeFunction([SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["dwRebootCheck"]),
        #
        'RebootCheckOnInstallA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hwnd", "pszINF", "pszSec", "dwReserved"]),
        #
        'RebootCheckOnInstallW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hwnd", "pszINF", "pszSec", "dwReserved"]),
        #
        'TranslateInfStringA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pszInfFilename", "pszInstallSection", "pszTranslateSection", "pszTranslateKey", "pszBuffer", "cchBuffer", "pdwRequiredSize", "pvReserved"]),
        #
        'TranslateInfStringW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pszInfFilename", "pszInstallSection", "pszTranslateSection", "pszTranslateKey", "pszBuffer", "cchBuffer", "pdwRequiredSize", "pvReserved"]),
        #
        'RegInstallA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimStruct({"cEntries": SimTypeInt(signed=False, label="UInt32"), "pse": SimTypePointer(SimStruct({"pszName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "pszValue": SimTypePointer(SimTypeChar(label="Byte"), offset=0)}, name="STRENTRYA", pack=False, align=None), offset=0)}, name="STRTABLEA", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hmod", "pszSection", "pstTable"]),
        #
        'RegInstallW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimStruct({"cEntries": SimTypeInt(signed=False, label="UInt32"), "pse": SimTypePointer(SimStruct({"pszName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pszValue": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="STRENTRYW", pack=False, align=None), offset=0)}, name="STRTABLEW", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hmod", "pszSection", "pstTable"]),
        #
        'LaunchINFSectionExW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=True, label="Int32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hwnd", "hInstance", "pszParms", "nShow"]),
        #
        'ExecuteCabA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"pszCab": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "pszInf": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "pszSection": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "szSrcPath": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 260), "dwFlags": SimTypeInt(signed=False, label="UInt32")}, name="CABINFOA", pack=False, align=None), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hwnd", "pCab", "pReserved"]),
        #
        'ExecuteCabW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"pszCab": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pszInf": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pszSection": SimTypePointer(SimTypeChar(label="Char"), offset=0), "szSrcPath": SimTypeFixedSizeArray(SimTypeChar(label="Char"), 260), "dwFlags": SimTypeInt(signed=False, label="UInt32")}, name="CABINFOW", pack=False, align=None), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hwnd", "pCab", "pReserved"]),
        #
        'AdvInstallFileA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hwnd", "lpszSourceDir", "lpszSourceFile", "lpszDestDir", "lpszDestFile", "dwFlags", "dwReserved"]),
        #
        'AdvInstallFileW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hwnd", "lpszSourceDir", "lpszSourceFile", "lpszDestDir", "lpszDestFile", "dwFlags", "dwReserved"]),
        #
        'RegSaveRestoreA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hWnd", "pszTitleString", "hkBckupKey", "pcszRootKey", "pcszSubKey", "pcszValueName", "dwFlags"]),
        #
        'RegSaveRestoreW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hWnd", "pszTitleString", "hkBckupKey", "pcszRootKey", "pcszSubKey", "pcszValueName", "dwFlags"]),
        #
        'RegSaveRestoreOnINFA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hWnd", "pszTitle", "pszINF", "pszSection", "hHKLMBackKey", "hHKCUBackKey", "dwFlags"]),
        #
        'RegSaveRestoreOnINFW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hWnd", "pszTitle", "pszINF", "pszSection", "hHKLMBackKey", "hHKCUBackKey", "dwFlags"]),
        #
        'RegRestoreAllA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hWnd", "pszTitleString", "hkBckupKey"]),
        #
        'RegRestoreAllW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hWnd", "pszTitleString", "hkBckupKey"]),
        #
        'FileSaveRestoreW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hDlg", "lpFileList", "lpDir", "lpBaseName", "dwFlags"]),
        #
        'FileSaveRestoreOnINFA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hWnd", "pszTitle", "pszINF", "pszSection", "pszBackupDir", "pszBaseBackupFile", "dwFlags"]),
        #
        'FileSaveRestoreOnINFW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hWnd", "pszTitle", "pszINF", "pszSection", "pszBackupDir", "pszBaseBackupFile", "dwFlags"]),
        #
        'AddDelBackupEntryA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["lpcszFileList", "lpcszBackupDir", "lpcszBaseName", "dwFlags"]),
        #
        'AddDelBackupEntryW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["lpcszFileList", "lpcszBackupDir", "lpcszBaseName", "dwFlags"]),
        #
        'FileSaveMarkNotExistA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["lpFileList", "lpDir", "lpBaseName"]),
        #
        'FileSaveMarkNotExistW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["lpFileList", "lpDir", "lpBaseName"]),
        #
        'GetVersionFromFileA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=True, label="Int32")], SimTypeInt(signed=True, label="Int32"), arg_names=["lpszFilename", "pdwMSVer", "pdwLSVer", "bVersion"]),
        #
        'GetVersionFromFileW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=True, label="Int32")], SimTypeInt(signed=True, label="Int32"), arg_names=["lpszFilename", "pdwMSVer", "pdwLSVer", "bVersion"]),
        #
        'GetVersionFromFileExA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=True, label="Int32")], SimTypeInt(signed=True, label="Int32"), arg_names=["lpszFilename", "pdwMSVer", "pdwLSVer", "bVersion"]),
        #
        'GetVersionFromFileExW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=True, label="Int32")], SimTypeInt(signed=True, label="Int32"), arg_names=["lpszFilename", "pdwMSVer", "pdwLSVer", "bVersion"]),
        #
        'IsNTAdmin': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["dwReserved", "lpdwReserved"]),
        #
        'DelNodeA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["pszFileOrDirName", "dwFlags"]),
        #
        'DelNodeW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["pszFileOrDirName", "dwFlags"]),
        #
        'DelNodeRunDLL32W': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=True, label="Int32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hwnd", "hInstance", "pszParms", "nShow"]),
        #
        'OpenINFEngineA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pszInfFilename", "pszInstallSection", "dwFlags", "phInf", "pvReserved"]),
        #
        'OpenINFEngineW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pszInfFilename", "pszInstallSection", "dwFlags", "phInf", "pvReserved"]),
        #
        'TranslateInfStringExA': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hInf", "pszInfFilename", "pszTranslateSection", "pszTranslateKey", "pszBuffer", "dwBufferSize", "pdwRequiredSize", "pvReserved"]),
        #
        'TranslateInfStringExW': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hInf", "pszInfFilename", "pszTranslateSection", "pszTranslateKey", "pszBuffer", "dwBufferSize", "pdwRequiredSize", "pvReserved"]),
        #
        'CloseINFEngine': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hInf"]),
        #
        'ExtractFilesA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["pszCabName", "pszExpandDir", "dwFlags", "pszFileList", "lpReserved", "dwReserved"]),
        #
        'ExtractFilesW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["pszCabName", "pszExpandDir", "dwFlags", "pszFileList", "lpReserved", "dwReserved"]),
        #
        'LaunchINFSectionW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=True, label="Int32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hwndOwner", "hInstance", "pszParams", "nShow"]),
        #
        'UserInstStubWrapperA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=True, label="Int32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hwnd", "hInstance", "pszParms", "nShow"]),
        #
        'UserInstStubWrapperW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=True, label="Int32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hwnd", "hInstance", "pszParms", "nShow"]),
        #
        'UserUnInstStubWrapperA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=True, label="Int32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hwnd", "hInstance", "pszParms", "nShow"]),
        #
        'UserUnInstStubWrapperW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=True, label="Int32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hwnd", "hInstance", "pszParms", "nShow"]),
        #
        'SetPerUserSecValuesA': SimTypeFunction([SimTypePointer(SimStruct({"szGUID": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 59), "szDispName": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 128), "szLocale": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 10), "szStub": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 1040), "szVersion": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 32), "szCompID": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 128), "dwIsInstalled": SimTypeInt(signed=False, label="UInt32"), "bRollback": SimTypeInt(signed=True, label="Int32")}, name="PERUSERSECTIONA", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pPerUser"]),
        #
        'SetPerUserSecValuesW': SimTypeFunction([SimTypePointer(SimStruct({"szGUID": SimTypeFixedSizeArray(SimTypeChar(label="Char"), 59), "szDispName": SimTypeFixedSizeArray(SimTypeChar(label="Char"), 128), "szLocale": SimTypeFixedSizeArray(SimTypeChar(label="Char"), 10), "szStub": SimTypeFixedSizeArray(SimTypeChar(label="Char"), 1040), "szVersion": SimTypeFixedSizeArray(SimTypeChar(label="Char"), 32), "szCompID": SimTypeFixedSizeArray(SimTypeChar(label="Char"), 128), "dwIsInstalled": SimTypeInt(signed=False, label="UInt32"), "bRollback": SimTypeInt(signed=True, label="Int32")}, name="PERUSERSECTIONW", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pPerUser"]),
    }

lib.set_prototypes(prototypes)
