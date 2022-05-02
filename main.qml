import QtQuick
import QtQuick.Window
import QtWebEngine

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")
    id : win
    WebEngineView {
        id : web
        anchors.fill: parent
        url: "https://www.qt.io"
    }
}
