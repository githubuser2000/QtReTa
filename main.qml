import QtQuick
import QtQuick.Window
import QtWebEngine
import Qt.labs.platform

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("ReTa Icon")
    id : win
    visibility: "Maximized"
    WebEngineView {
        id : web
        visible: true
        anchors.fill: parent
        url: ""
        //onLoadingChanged : if (loadProgress === 100 )  MyAppEng.entf()
        onLoadingChanged : if (loadProgress === 100 )  tray.updateSystemTrayIcon()

    }
    SystemTrayIcon {
        visible: true
        icon.source: updateSystemTrayIcon();
        //icon.name: "QtReTa"
        //icon.mask: true
        //tooltip : qsTr("ReTa Icon")
        id : tray
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
            updateSystemTrayIcon();
        }
        function updateSystemTrayIcon() {
            console.log("Host-Adresse:", web.url);
            let addy = web.url.toString().substring(0, "http://127.0.0.1:1313/".length);
            let addy2 = web.url.toString().substring(0, "http://127.0.0.1/".length);
            //console.log("Host-Adresse:", "http://127.0.0.1:1313/" == addy);
            if (addy2 == "http://127.0.0.1/" || addy == "http://127.0.0.1:1313/") {
                icon.source = "qrc:/hugo.png";
            } else {
                icon.source = "qrc:/Jupiter.png";
            }
            return icon.source
        }
    }

}
