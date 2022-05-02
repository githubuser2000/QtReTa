import QtQuick
import QtQuick.Window
import QtWebEngine

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("ReTa")
    id : win
    WebEngineView {
        id : web
        visible: true
        anchors.fill: parent
        url: "file:///home/alex/religionen.html"
    }
}
