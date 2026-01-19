# Beseri Security Scanner

A lightweight Python tool that detects hardcoded secrets and tokens inside source files.
Can be used manually or as a Git pre-commit hook.

## Features
- Detects AWS, Google, JWT, private keys, slack tokens, and generic API keys
- Recursive directory scanning
- Non-zero exit on secret detection (CI/CD & hooks)
- Flexible and easy-to-extend regex patterns

## Usage
```
python3 scanner.py .
```

- minor update @ 2026-01-10 21:00:57.465603
- minor update @ 2026-01-10 21:00:57.707805
- minor update @ 2026-01-10 21:00:58.481686
- minor update @ 2026-01-10 21:00:58.753395
- minor update @ 2026-01-10 21:00:59.007304
- minor update @ 2026-01-10 21:00:59.499664
- minor update @ 2026-01-10 21:00:59.750683
- minor update @ 2026-01-10 21:01:00.770743
- minor update @ 2026-01-11 17:18:27.236735
- minor update @ 2026-01-11 17:18:32.475518
- minor update @ 2026-01-11 17:18:46.919906
- minor update @ 2026-01-11 17:19:02.366014
- minor update @ 2026-01-11 17:19:14.805561
- minor update @ 2026-01-11 19:16:57.369498
- minor update @ 2026-01-11 19:17:08.791367
- minor update @ 2026-01-11 22:20:56.016466
- minor update @ 2026-01-11 22:20:59.303749
- minor update @ 2026-01-12 05:30:58.532212
- minor update @ 2026-01-12 05:31:04.787570
- minor update @ 2026-01-12 05:31:19.246080
- minor update @ 2026-01-12 06:39:08.161217
- minor update @ 2026-01-12 06:39:15.375901
- minor update @ 2026-01-12 06:39:22.583053
- minor update @ 2026-01-12 06:39:26.800590
- minor update @ 2026-01-12 06:39:35.013085
- minor update @ 2026-01-12 06:39:37.225640
- minor update @ 2026-01-12 16:28:42.099333
- minor update @ 2026-01-12 16:28:47.384624
- minor update @ 2026-01-12 16:28:50.641568
- minor update @ 2026-01-12 16:28:53.900880
- minor update @ 2026-01-12 16:29:07.418390
- minor update @ 2026-01-12 19:21:15.049397
- minor update @ 2026-01-12 19:21:19.310605
- minor update @ 2026-01-13 04:41:06.496250
- minor update @ 2026-01-13 04:41:13.069073
- minor update @ 2026-01-13 07:25:57.404431
- minor update @ 2026-01-13 07:25:59.712862
- minor update @ 2026-01-13 07:26:09.970320
- minor update @ 2026-01-13 07:26:17.236182
- minor update @ 2026-01-13 07:26:25.517866
- minor update @ 2026-01-13 07:26:34.769221
- minor update @ 2026-01-13 07:26:50.276718
- minor update @ 2026-01-14 15:28:05.178578
- minor update @ 2026-01-14 15:28:09.508047
- minor update @ 2026-01-14 15:28:26.182208
- minor update @ 2026-01-14 15:28:35.505879
- minor update @ 2026-01-14 15:28:43.817952
- minor update @ 2026-01-14 15:28:54.140443
- minor update @ 2026-01-14 21:23:34.041994
- minor update @ 2026-01-14 21:23:41.348156
- minor update @ 2026-01-14 23:19:20.624248
- minor update @ 2026-01-14 23:19:54.157437
- minor update @ 2026-01-14 23:20:04.452466
- minor update @ 2026-01-15 05:27:36.479807
- minor update @ 2026-01-15 05:27:54.423995
- minor update @ 2026-01-15 05:28:01.693382
- minor update @ 2026-01-15 15:27:42.840477
- minor update @ 2026-01-15 15:27:58.758206
- minor update @ 2026-01-15 17:33:22.407133
- minor update @ 2026-01-15 17:33:36.401565
- minor update @ 2026-01-16 05:26:45.911858
- minor update @ 2026-01-16 05:27:09.734729
- minor update @ 2026-01-16 05:27:14.992673
- minor update @ 2026-01-16 05:27:20.255104
- minor update @ 2026-01-16 22:22:38.891141
- minor update @ 2026-01-17 05:21:22.067083
- minor update @ 2026-01-17 05:21:42.282893
- minor update @ 2026-01-17 05:21:48.859213
- minor update @ 2026-01-17 05:22:03.440944
- minor update @ 2026-01-17 05:22:05.740500
- minor update @ 2026-01-17 06:32:41.322767
- minor update @ 2026-01-17 06:32:48.995061
- minor update @ 2026-01-17 06:32:55.886232
- minor update @ 2026-01-17 06:33:23.010453
- minor update @ 2026-01-18 11:17:48.318070
- minor update @ 2026-01-18 11:17:54.666861
- minor update @ 2026-01-18 11:17:59.976590
- minor update @ 2026-01-18 11:18:13.603170
- minor update @ 2026-01-18 20:24:25.439201
- minor update @ 2026-01-18 20:24:35.083876
- minor update @ 2026-01-18 20:24:42.360499
- minor update @ 2026-01-18 20:24:50.619208
- minor update @ 2026-01-18 20:24:57.384885
- minor update @ 2026-01-18 20:25:06.651506
- minor update @ 2026-01-18 20:25:25.168970
- minor update @ 2026-01-18 20:25:34.428048
- minor update @ 2026-01-18 22:20:39.039865
- minor update @ 2026-01-18 22:20:51.959800
- minor update @ 2026-01-18 22:20:57.218345
- minor update @ 2026-01-18 22:21:07.988184
- minor update @ 2026-01-18 22:21:15.517678
- minor update @ 2026-01-19 05:32:56.094602
- minor update @ 2026-01-19 05:33:04.408148
- minor update @ 2026-01-19 05:33:32.189045
- minor update @ 2026-01-19 05:33:41.716608
- minor update @ 2026-01-19 05:33:46.982778
- minor update @ 2026-01-19 10:31:07.019031
- minor update @ 2026-01-19 10:31:11.380834
- minor update @ 2026-01-19 10:31:29.731869
- minor update @ 2026-01-19 19:19:57.720797
- minor update @ 2026-01-19 19:20:06.241627
- minor update @ 2026-01-19 19:20:14.500558