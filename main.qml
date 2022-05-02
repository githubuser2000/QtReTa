import QtQuick
import QtQuick.Window
import QtWebEngine

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("ReTa")
    id : win
    visibility: "Maximized"
    WebEngineView {
        id : web
        visible: true
        anchors.fill: parent
        url: ""
    }
}
