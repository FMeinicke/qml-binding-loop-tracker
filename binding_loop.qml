import QtQuick 2.0

Rectangle {
    width: childrenRect.width
    Text {
        text: parent.width > 10 ? "Hello World" : "Hi"
    }
}
