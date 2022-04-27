using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Fallable : MonoBehaviour
{
    public SerialController serialController;

    // Initialization
    void Start()
    {
        serialController = GameObject.Find("SerialController").GetComponent<SerialController>();

        Debug.Log("Initialised serialController. Commencing communication...");
    }

    private void OnTriggerEnter(Collider other)
    {
        Debug.Log("Hit Detected!");
        Debug.Log("Sending H");
        serialController.SendSerialMessage("H");
    }
}
