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
            let addy = web.url.toString().substring(0, "http://127.0.0.1:1313/".length);
            let addy2 = web.url.toString().substring(0, "http://127.0.0.1/".length);
            let addy3 = web.url.toString().substring(0, "http://127.0.0.1:8888/".length);
            //console.log("Host-Adresse:", "http://127.0.0.1:1313/" == addy);
            //console.log("addy3 anfang:", addy3);
            //console.log("addy3 anfang:",  "http://127.0.0.1:8888/");
            if (addy2 == "http://127.0.0.1/" || addy == "http://127.0.0.1:1313/") {
                icon.source = "qrc:/hugo.png";
            } else
                if (addy3 == "http://127.0.0.1:8888/" || addy3 == "http://localhost:8888/") {
                    //console.log("addy3 ja:", addy3);
                    icon.source = "qrc:/python.png";
                } else
                    if (web.url.toString().includes("youtube")) {
                        //console.log("addy3 ja:", addy3);
                        icon.source = "qrc:/youtube.png";
                    } else {
                        //console.log("addy2 ja");
                        icon.source = "qrc:/Jupiter.png";
                    }
            return icon.source
        }
    }

}
