using UnityEngine;
using System.Collections;
using System.IO.Ports;

public class motor : MonoBehaviour {

    public SerialPort serial = new SerialPort ("COM3", 9600);
    private bool motorState = false;

    public void onMotor() {
        if (serial.IsOpen == false) {
            serial.Open ();
        }

        serial.Write("A");
    }

    SerialData.Write("a");
    motorState = false;
}