**base/status**
----
  fetches list of most recent messages

* **URL**

  /rock/base/status.py:n

* **Method:**

  GET

*  **URL Params**

   **Optional:**

   `n=[numeric]` : the number of records to return (or 1 if not specified)

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `[
    {
        "course": "12",
        "imei": "300234010753370",
        "lat": "39.59755",
        "lng": "-104.93283",
        "momsn": "0",
        "speed": "5",
        "text": "",
        "time": "2017-03-27 09:39:53.013743"
    }, ... ]`

* **Error Response:**

  * **Code:** 200 <br />
    **Content:** `[{ "error" : "example error message" }]`

* **Sample Call:**

  <_Just a sample call to your endpoint in a runnable format ($.ajax call or a curl request) - this makes life easier and more predictable._>

* **Notes:**

  <_This is where all uncertainties, commentary, discussion etc. can go. I recommend timestamping and identifying oneself when leaving comments here._>
