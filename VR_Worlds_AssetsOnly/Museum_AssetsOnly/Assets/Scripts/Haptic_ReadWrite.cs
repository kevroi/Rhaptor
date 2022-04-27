/**
 * Ardity (Serial Communication for Arduino + Unity)
 * Author: Daniel Wilches <dwilches@gmail.com>
 *
 * This work is released under the Creative Commons Attributions license.
 * https://creativecommons.org/licenses/by/2.0/
 */

using UnityEngine;
// using System;
using System.Collections;
using System.IO;
using System.Collections.Generic;
using System.Linq;

/**
 * Sample for reading using polling by yourself, and writing too.
 */
public class Haptic_ReadWrite : MonoBehaviour
{
    public SerialController serialController;

    // Initialization
    void Start()
    {
        serialController = GameObject.Find("SerialController").GetComponent<SerialController>();

        // Delete any previous log files
        string filePath = @"D:\Kevin\VR_Worlds\Museum\Assets\Scripts\log.txt";
        if (File.Exists(filePath))
        {
            try
            {
                File.Delete(filePath);
                File.WriteAllLines(filePath, new string[0]);
            }
            catch (System.Exception)
            {
                Debug.Log("Deletion of previous log failed");
            }
        }
        else
        {
            Debug.Log("No previous log found. Creating new log.");
            File.WriteAllLines(filePath, new string[0]);
        }

        Debug.Log("Initialised serialController. Commencing communication...");
    }

    // Executed each frame
    void Update()
    {
        //---------------------------------------------------------------------
        // Send data
        //---------------------------------------------------------------------

        // If you press one of these keys send it to the serial device. A
        // sample serial device that accepts this input is given in the README.
        // if (Input.GetKeyDown(KeyCode.A))
        // {
        //     Debug.Log("Sending A");
        //     serialController.SendSerialMessage("A");
        // }

        // if (Input.GetKeyDown(KeyCode.Z))
        // {
        //     Debug.Log("Sending Z");
        //     serialController.SendSerialMessage("Z");
        // }

        Debug.Log("Sending A");
        serialController.SendSerialMessage("A");

        Vector3 position = UnityEngine.XR.InputTracking.GetLocalPosition(UnityEngine.XR.XRNode.Head);
        Quaternion orientation = UnityEngine.XR.InputTracking.GetLocalRotation(UnityEngine.XR.XRNode.Head);
        string posString = position.ToString();
        string pos = posString.Substring(posString.IndexOf("(")+1, posString.IndexOf(")")-1);
        string oriString = orientation.ToString();
        string ori = oriString.Substring(oriString.IndexOf("(")+1, oriString.IndexOf(")")-1);
        Debug.Log(pos);
        Debug.Log(ori);

        string filePath = @"D:\Kevin\VR_Worlds\Museum\Assets\Scripts\log.txt";
        // Read existing Contents of the existing file
        List<string> lines = new List<string>();
        lines = File.ReadAllLines(filePath).ToList();
        // Add the new position and orientation
        lines.Add(pos + ", " + ori);
        // save to file
        File.WriteAllLines(filePath, lines);

        // serialController.SendSerialMessage(position.ToString());


        //---------------------------------------------------------------------
        // Receive data
        //---------------------------------------------------------------------

        string message = serialController.ReadSerialMessage();

        if (message == null)
            return;

        // Check if the message is plain data or a connect/disconnect event.
        if (ReferenceEquals(message, SerialController.SERIAL_DEVICE_CONNECTED))
            Debug.Log("Connection established");
        else if (ReferenceEquals(message, SerialController.SERIAL_DEVICE_DISCONNECTED))
            Debug.Log("Connection attempt failed or disconnection detected");
        else
            Debug.Log("Message arrived: " + message);
    }
}
