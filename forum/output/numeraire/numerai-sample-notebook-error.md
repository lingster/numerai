---
title: "Numerai Sample Notebook Error"
category: Numeraire
url: https://forum.numer.ai/t/numerai-sample-notebook-error/6284
created_at: 2023-04-08T12:09:53.707000+00:00
last_posted_at: 2023-05-27T21:28:01.616000+00:00
posts_count: 12
views: 1268
tags: []
---

# Numerai Sample Notebook Error

---

### Post #1 — **grumpycatzz** | 2023-04-08 12:09 UTC

I have not changed anything in code except adding my public id , key and model id  
I am getting this error on last line of code where we upload predictions using numeri API.

[![error1](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/cfc16801a47381974b7dbd2235f316d0f6e9ee70.png)error11017×366 22.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/cfc16801a47381974b7dbd2235f316d0f6e9ee70.png> "error1")
    
    
    SSLWantWriteError                         Traceback (most recent call last)
    File ~\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\connectionpool.py:703, in HTTPConnectionPool.urlopen(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)
        702 # Make the request on the httplib connection object.
    --> 703 httplib_response = self._make_request(
        704     conn,
        705     method,
        706     url,
        707     timeout=timeout_obj,
        708     body=body,
        709     headers=headers,
        710     chunked=chunked,
        711 )
        713 # If we're going to release the connection in ``finally:``, then
        714 # the response doesn't need to know about the connection. Otherwise
        715 # it will also try to release it and we'll have a double-release
        716 # mess.
    
    File ~\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\connectionpool.py:398, in HTTPConnectionPool._make_request(self, conn, method, url, timeout, chunked, **httplib_request_kw)
        397     else:
    --> 398         conn.request(method, url, **httplib_request_kw)
        400 # We are swallowing BrokenPipeError (errno.EPIPE) since the server is
        401 # legitimately able to close the connection after sending a valid response.
        402 # With this behaviour, the received response is still readable.
    
    File ~\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\connection.py:244, in HTTPConnection.request(self, method, url, body, headers)
        243     headers["User-Agent"] = _get_default_user_agent()
    --> 244 super(HTTPConnection, self).request(method, url, body=body, headers=headers)
    
    File ~\AppData\Local\Programs\Python\Python311\Lib\http\client.py:1283, in HTTPConnection.request(self, method, url, body, headers, encode_chunked)
       1282 """Send a complete request to the server."""
    -> 1283 self._send_request(method, url, body, headers, encode_chunked)
    
    File ~\AppData\Local\Programs\Python\Python311\Lib\http\client.py:1329, in HTTPConnection._send_request(self, method, url, body, headers, encode_chunked)
       1328     body = _encode(body, 'body')
    -> 1329 self.endheaders(body, encode_chunked=encode_chunked)
    
    File ~\AppData\Local\Programs\Python\Python311\Lib\http\client.py:1278, in HTTPConnection.endheaders(self, message_body, encode_chunked)
       1277     raise CannotSendHeader()
    -> 1278 self._send_output(message_body, encode_chunked=encode_chunked)
    
    File ~\AppData\Local\Programs\Python\Python311\Lib\http\client.py:1077, in HTTPConnection._send_output(self, message_body, encode_chunked)
       1075         chunk = f'{len(chunk):X}\r\n'.encode('ascii') + chunk \
       1076             + b'\r\n'
    -> 1077     self.send(chunk)
       1079 if encode_chunked and self._http_vsn == 11:
       1080     # end chunked transfer
    
    File ~\AppData\Local\Programs\Python\Python311\Lib\http\client.py:999, in HTTPConnection.send(self, data)
        998 try:
    --> 999     self.sock.sendall(data)
       1000 except TypeError:
    
    File ~\AppData\Local\Programs\Python\Python311\Lib\ssl.py:1241, in SSLSocket.sendall(self, data, flags)
       1240 while count < amount:
    -> 1241     v = self.send(byte_view[count:])
       1242     count += v
    
    File ~\AppData\Local\Programs\Python\Python311\Lib\ssl.py:1210, in SSLSocket.send(self, data, flags)
       1207         raise ValueError(
       1208             "non-zero flags not allowed in calls to send() on %s" %
       1209             self.__class__)
    -> 1210     return self._sslobj.write(data)
       1211 else:
    
    SSLWantWriteError: The operation did not complete (write) (_ssl.c:2423)

---

### Post #2 — **ihab** | 2023-04-30 19:11 UTC

Hi folks, I all the sudden started getting the same error a few weeks ago. Have the API been updated and we need to make changes? thank you.
    
    
    2023-04-30 06:10:00,168 INFO numerapi.base_api: uploading predictions...
    
    ---------------------------------------------------------------------------
    timeout                                   Traceback (most recent call last)
    /opt/conda/envs/rapids/lib/python3.8/site-packages/urllib3/connectionpool.py in urlopen(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)
        698             # Make the request on the httplib connection object.
    --> 699             httplib_response = self._make_request(
        700                 conn,
    
    /opt/conda/envs/rapids/lib/python3.8/site-packages/urllib3/connectionpool.py in _make_request(self, conn, method, url, timeout, chunked, **httplib_request_kw)
        393             else:
    --> 394                 conn.request(method, url, **httplib_request_kw)
        395 
    
    /opt/conda/envs/rapids/lib/python3.8/site-packages/urllib3/connection.py in request(self, method, url, body, headers)
        233             headers["User-Agent"] = _get_default_user_agent()
    --> 234         super(HTTPConnection, self).request(method, url, body=body, headers=headers)
        235 
    
    /opt/conda/envs/rapids/lib/python3.8/http/client.py in request(self, method, url, body, headers, encode_chunked)
       1251         """Send a complete request to the server."""
    -> 1252         self._send_request(method, url, body, headers, encode_chunked)
       1253 
    
    /opt/conda/envs/rapids/lib/python3.8/http/client.py in _send_request(self, method, url, body, headers, encode_chunked)
       1297             body = _encode(body, 'body')
    -> 1298         self.endheaders(body, encode_chunked=encode_chunked)
       1299 
    
    /opt/conda/envs/rapids/lib/python3.8/http/client.py in endheaders(self, message_body, encode_chunked)
       1246             raise CannotSendHeader()
    -> 1247         self._send_output(message_body, encode_chunked=encode_chunked)
       1248 
    
    /opt/conda/envs/rapids/lib/python3.8/http/client.py in _send_output(self, message_body, encode_chunked)
       1045                         + b'\r\n'
    -> 1046                 self.send(chunk)
       1047 
    
    /opt/conda/envs/rapids/lib/python3.8/http/client.py in send(self, data)
        967         try:
    --> 968             self.sock.sendall(data)
        969         except TypeError:
    
    /opt/conda/envs/rapids/lib/python3.8/ssl.py in sendall(self, data, flags)
       1203                 while count < amount:
    -> 1204                     v = self.send(byte_view[count:])
       1205                     count += v
    
    /opt/conda/envs/rapids/lib/python3.8/ssl.py in send(self, data, flags)
       1172                     self.__class__)
    -> 1173             return self._sslobj.write(data)
       1174         else:
    
    timeout: The write operation timed out
    
    During handling of the above exception, another exception occurred:
    
    ProtocolError                             Traceback (most recent call last)
    /opt/conda/envs/rapids/lib/python3.8/site-packages/requests/adapters.py in send(self, request, stream, timeout, verify, cert, proxies)
        438             if not chunked:
    --> 439                 resp = conn.urlopen(
        440                     method=request.method,
    
    /opt/conda/envs/rapids/lib/python3.8/site-packages/urllib3/connectionpool.py in urlopen(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)
        754 
    --> 755             retries = retries.increment(
        756                 method, url, error=e, _pool=self, _stacktrace=sys.exc_info()[2]
    
    /opt/conda/envs/rapids/lib/python3.8/site-packages/urllib3/util/retry.py in increment(self, method, url, response, error, _pool, _stacktrace)
        531             if read is False or not self._is_method_retryable(method):
    --> 532                 raise six.reraise(type(error), error, _stacktrace)
        533             elif read is not None:
    
    /opt/conda/envs/rapids/lib/python3.8/site-packages/urllib3/packages/six.py in reraise(tp, value, tb)
        768             if value.__traceback__ is not tb:
    --> 769                 raise value.with_traceback(tb)
        770             raise value
    
    /opt/conda/envs/rapids/lib/python3.8/site-packages/urllib3/connectionpool.py in urlopen(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)
        698             # Make the request on the httplib connection object.
    --> 699             httplib_response = self._make_request(
        700                 conn,
    
    /opt/conda/envs/rapids/lib/python3.8/site-packages/urllib3/connectionpool.py in _make_request(self, conn, method, url, timeout, chunked, **httplib_request_kw)
        393             else:
    --> 394                 conn.request(method, url, **httplib_request_kw)
        395 
    
    /opt/conda/envs/rapids/lib/python3.8/site-packages/urllib3/connection.py in request(self, method, url, body, headers)
        233             headers["User-Agent"] = _get_default_user_agent()
    --> 234         super(HTTPConnection, self).request(method, url, body=body, headers=headers)
        235 
    
    /opt/conda/envs/rapids/lib/python3.8/http/client.py in request(self, method, url, body, headers, encode_chunked)
       1251         """Send a complete request to the server."""
    -> 1252         self._send_request(method, url, body, headers, encode_chunked)
       1253 
    
    /opt/conda/envs/rapids/lib/python3.8/http/client.py in _send_request(self, method, url, body, headers, encode_chunked)
       1297             body = _encode(body, 'body')
    -> 1298         self.endheaders(body, encode_chunked=encode_chunked)
       1299 
    
    /opt/conda/envs/rapids/lib/python3.8/http/client.py in endheaders(self, message_body, encode_chunked)
       1246             raise CannotSendHeader()
    -> 1247         self._send_output(message_body, encode_chunked=encode_chunked)
       1248 
    
    /opt/conda/envs/rapids/lib/python3.8/http/client.py in _send_output(self, message_body, encode_chunked)
       1045                         + b'\r\n'
    -> 1046                 self.send(chunk)
       1047 
    
    /opt/conda/envs/rapids/lib/python3.8/http/client.py in send(self, data)
        967         try:
    --> 968             self.sock.sendall(data)
        969         except TypeError:
    
    /opt/conda/envs/rapids/lib/python3.8/ssl.py in sendall(self, data, flags)
       1203                 while count < amount:
    -> 1204                     v = self.send(byte_view[count:])
       1205                     count += v
    
    /opt/conda/envs/rapids/lib/python3.8/ssl.py in send(self, data, flags)
       1172                     self.__class__)
    -> 1173             return self._sslobj.write(data)
       1174         else:
    
    ProtocolError: ('Connection aborted.', timeout('The write operation timed out'))
    
    During handling of the above exception, another exception occurred:
    
    ConnectionError                           Traceback (most recent call last)
    <timed exec> in <module>
    
    /opt/conda/envs/rapids/lib/python3.8/site-packages/numerapi/numerapi.py in upload_predictions(self, file_path, tournament, model_id, df, data_datestamp, timeout)
        529         headers = {"x_compute_id": os.getenv("NUMERAI_COMPUTE_ID")}
        530         with open(file_path, 'rb') if df is None else buffer_csv as file:
    --> 531             requests.put(
        532                 upload_auth['url'], data=file.read(), headers=headers,
        533                 timeout=timeout)
    
    /opt/conda/envs/rapids/lib/python3.8/site-packages/requests/api.py in put(url, data, **kwargs)
        132     """
        133 
    --> 134     return request('put', url, data=data, **kwargs)
        135 
        136 
    
    /opt/conda/envs/rapids/lib/python3.8/site-packages/requests/api.py in request(method, url, **kwargs)
         59     # cases, and look like a memory leak in others.
         60     with sessions.Session() as session:
    ---> 61         return session.request(method=method, url=url, **kwargs)
         62 
         63 
    
    /opt/conda/envs/rapids/lib/python3.8/site-packages/requests/sessions.py in request(self, method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json)
        540         }
        541         send_kwargs.update(settings)
    --> 542         resp = self.send(prep, **send_kwargs)
        543 
        544         return resp
    
    /opt/conda/envs/rapids/lib/python3.8/site-packages/requests/sessions.py in send(self, request, **kwargs)
        653 
        654         # Send the request
    --> 655         r = adapter.send(request, **kwargs)
        656 
        657         # Total elapsed time of the request (approximately)
    
    /opt/conda/envs/rapids/lib/python3.8/site-packages/requests/adapters.py in send(self, request, stream, timeout, verify, cert, proxies)
        496 
        497         except (ProtocolError, socket.error) as err:
    --> 498             raise ConnectionError(err, request=request)
        499 
        500         except MaxRetryError as e:
    
    ConnectionError: ('Connection aborted.', timeout('The write operation timed out'))

---

### Post #3 — **ihab** | 2023-04-30 19:13 UTC

[@grumpycatzz](</u/grumpycatzz>) Hi, have you found a solution to this? thanks

---

### Post #4 — **shatteredx** | 2023-05-01 01:14 UTC _(reply to #3)_

Did you try updating numerapi?

---

### Post #5 — **ihab** | 2023-05-01 02:49 UTC _(reply to #4)_

I am on the latest 2.14.0

---

### Post #6 — **kgareth** | 2023-05-04 13:37 UTC _(reply to #5)_

Did you get any fix? I am getting a similar error.

---

### Post #7 — **shatteredx** | 2023-05-04 17:14 UTC

The sample notebook works for me although they should probably make a couple changes.

The first cell should change sklearn to scikit-learn. scikit-learn is the correct pip name.
    
    
    # install dependencies
    !pip install pandas scikit-learn numerapi
    

Also they should probably change the tournament data file to the daily data file. Otherwise you get an error on weekdays.
    
    
    # download the latest tournament dataset
    napi = numerapi.NumerAPI()
    napi.download_dataset('v2/numerai_live_data.csv', "live_v2.csv")
    tournament_data = pd.read_csv(f"live_v2.csv")
    

Besides that, it all works. I’m not seeing any SSLWantWriteError or ConnectionError. May want to try updating requests, not sure.

---

### Post #8 — **kgareth** | 2023-05-05 15:46 UTC _(reply to #7)_

Thank you for the information.

The error is given when uploading signal predictions. I did try updating requests but that did not help.  
Uploading the numerai predictions works. Uploading the signal diagnostics also works.

---

### Post #9 — **ihab** | 2023-05-07 05:20 UTC _(reply to #5)_

No. Still get the error.

---

### Post #10 — **jkom** | 2023-05-22 05:10 UTC

Anyone find a solution to this yet? It’s been happening for weeks for me. I can submit on Colab with the exact same script. I’m going to start checking all package versions next. My numerapi package is 2.14.0, same as Colab, at least.

---

### Post #11 — **kgareth** | 2023-05-23 03:18 UTC _(reply to #10)_

Try to increase the timeout value. E.g.

timeout=(600,600)  
napi.upload_predictions(example_signal_output_path, model_id=model_id,timeout=timeout)

---

### Post #12 — **jkom** | 2023-05-27 21:28 UTC

That worked! Thank you!!!
