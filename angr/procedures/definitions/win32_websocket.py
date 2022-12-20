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
lib.set_library_names("websocket.dll")
prototypes = \
    {
        #
        'WebSocketCreateClientHandle': SimTypeFunction([SimTypePointer(SimStruct({"Type": SimTypeInt(signed=False, label="WEB_SOCKET_PROPERTY_TYPE"), "pvValue": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "ulValueSize": SimTypeInt(signed=False, label="UInt32")}, name="WEB_SOCKET_PROPERTY", pack=False, align=None), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pProperties", "ulPropertyCount", "phWebSocket"]),
        #
        'WebSocketBeginClientHandshake': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeChar(label="Byte"), offset=0), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeChar(label="Byte"), offset=0), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"pcName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ulNameLength": SimTypeInt(signed=False, label="UInt32"), "pcValue": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ulValueLength": SimTypeInt(signed=False, label="UInt32")}, name="WEB_SOCKET_HTTP_HEADER", pack=False, align=None), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimStruct({"pcName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ulNameLength": SimTypeInt(signed=False, label="UInt32"), "pcValue": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ulValueLength": SimTypeInt(signed=False, label="UInt32")}, name="WEB_SOCKET_HTTP_HEADER", pack=False, align=None), offset=0), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hWebSocket", "pszSubprotocols", "ulSubprotocolCount", "pszExtensions", "ulExtensionCount", "pInitialHeaders", "ulInitialHeaderCount", "pAdditionalHeaders", "pulAdditionalHeaderCount"]),
        #
        'WebSocketEndClientHandshake': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"pcName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ulNameLength": SimTypeInt(signed=False, label="UInt32"), "pcValue": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ulValueLength": SimTypeInt(signed=False, label="UInt32")}, name="WEB_SOCKET_HTTP_HEADER", pack=False, align=None), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hWebSocket", "pResponseHeaders", "ulReponseHeaderCount", "pulSelectedExtensions", "pulSelectedExtensionCount", "pulSelectedSubprotocol"]),
        #
        'WebSocketCreateServerHandle': SimTypeFunction([SimTypePointer(SimStruct({"Type": SimTypeInt(signed=False, label="WEB_SOCKET_PROPERTY_TYPE"), "pvValue": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "ulValueSize": SimTypeInt(signed=False, label="UInt32")}, name="WEB_SOCKET_PROPERTY", pack=False, align=None), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pProperties", "ulPropertyCount", "phWebSocket"]),
        #
        'WebSocketBeginServerHandshake': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypePointer(SimTypeChar(label="Byte"), offset=0), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"pcName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ulNameLength": SimTypeInt(signed=False, label="UInt32"), "pcValue": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ulValueLength": SimTypeInt(signed=False, label="UInt32")}, name="WEB_SOCKET_HTTP_HEADER", pack=False, align=None), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimStruct({"pcName": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ulNameLength": SimTypeInt(signed=False, label="UInt32"), "pcValue": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ulValueLength": SimTypeInt(signed=False, label="UInt32")}, name="WEB_SOCKET_HTTP_HEADER", pack=False, align=None), offset=0), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hWebSocket", "pszSubprotocolSelected", "pszExtensionSelected", "ulExtensionSelectedCount", "pRequestHeaders", "ulRequestHeaderCount", "pResponseHeaders", "pulResponseHeaderCount"]),
        #
        'WebSocketEndServerHandshake': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hWebSocket"]),
        #
        'WebSocketSend': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="WEB_SOCKET_BUFFER_TYPE"), SimTypePointer(SimUnion({"Data": SimStruct({"pbBuffer": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ulBufferLength": SimTypeInt(signed=False, label="UInt32")}, name="_Data_e__Struct", pack=False, align=None), "CloseStatus": SimStruct({"pbReason": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ulReasonLength": SimTypeInt(signed=False, label="UInt32"), "usStatus": SimTypeShort(signed=False, label="UInt16")}, name="_CloseStatus_e__Struct", pack=False, align=None)}, name="<anon>", label="None"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hWebSocket", "BufferType", "pBuffer", "Context"]),
        #
        'WebSocketReceive': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimUnion({"Data": SimStruct({"pbBuffer": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ulBufferLength": SimTypeInt(signed=False, label="UInt32")}, name="_Data_e__Struct", pack=False, align=None), "CloseStatus": SimStruct({"pbReason": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ulReasonLength": SimTypeInt(signed=False, label="UInt32"), "usStatus": SimTypeShort(signed=False, label="UInt16")}, name="_CloseStatus_e__Struct", pack=False, align=None)}, name="<anon>", label="None"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hWebSocket", "pBuffer", "pvContext"]),
        #
        'WebSocketGetAction': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="WEB_SOCKET_ACTION_QUEUE"), SimTypePointer(SimUnion({"Data": SimStruct({"pbBuffer": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ulBufferLength": SimTypeInt(signed=False, label="UInt32")}, name="_Data_e__Struct", pack=False, align=None), "CloseStatus": SimStruct({"pbReason": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "ulReasonLength": SimTypeInt(signed=False, label="UInt32"), "usStatus": SimTypeShort(signed=False, label="UInt16")}, name="_CloseStatus_e__Struct", pack=False, align=None)}, name="<anon>", label="None"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="WEB_SOCKET_ACTION"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="WEB_SOCKET_BUFFER_TYPE"), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hWebSocket", "eActionQueue", "pDataBuffers", "pulDataBufferCount", "pAction", "pBufferType", "pvApplicationContext", "pvActionContext"]),
        #
        'WebSocketCompleteAction': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeBottom(label="Void"), arg_names=["hWebSocket", "pvActionContext", "ulBytesTransferred"]),
        #
        'WebSocketAbortHandle': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeBottom(label="Void"), arg_names=["hWebSocket"]),
        #
        'WebSocketDeleteHandle': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeBottom(label="Void"), arg_names=["hWebSocket"]),
        #
        'WebSocketGetGlobalProperty': SimTypeFunction([SimTypeInt(signed=False, label="WEB_SOCKET_PROPERTY_TYPE"), SimTypePointer(SimTypeBottom(label="Void"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["eType", "pvValue", "ulSize"]),
    }

lib.set_prototypes(prototypes)
