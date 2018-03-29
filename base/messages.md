**base/messages**
----
  fetches list of most recent messages

* **URL**

  /rock/base/messages.py:n

* **Method:**

  GET

*  **URL Params**

   **Optional:**

   `n=[numeric]` : the number of records to return (or 1 if not specified)

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `[ {
      "text": "Example mobile-originated (MO) message",
      "time": "2017-04-03 08:57:00.543910",
      "type": "MO"
    },
    {
      "text": "Example mobile-terminated (MT) message",
      "time": "2017-04-03 09:01:00.543910",
      "type": "MT"
    }, ... ]`

* **Error Response:**

  * **Code:** 200 <br />
    **Content:** `[{ "error" : "example error message" }]`

* **Sample Call:**

  <_Just a sample call to your endpoint in a runnable format ($.ajax call or a curl request) - this makes life easier and more predictable._>

* **Notes:**

  <_This is where all uncertainties, commentary, discussion etc. can go. I recommend timestamping and identifying oneself when leaving comments here._>
