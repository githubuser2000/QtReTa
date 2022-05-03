import QtQuick
import QtQuick.Window
import QtWebEngine
import Qt.labs.platform

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
        onLoadingChanged : if (loadProgress === 100 )  MyAppEng.entf()

    }
    SystemTrayIcon {
        visible: true
        icon.source: "qrc:/symbolik3.png"
        //icon.name: "QtReTa"
        //icon.mask: true
        //tooltip : qsTr("Qt ReTa")
        //id : tray
        menu: Menu {
            MenuItem {
                text: qsTr("visible")
                onTriggered: {
                    win.visible = ! win.visible
                }
            }
            MenuItem {
                text: qsTr("Quit")
                onTriggered: Qt.quit()
            }
        }
        onActivated: {
            win.visible = ! win.visible
        }
    }

}
