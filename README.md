# OpenCV - Getting started

This is basic repository showing how to get started with OpenCV in Python and C++.

### Python

`pip install opencv-python`


### C++

To retrieve OpenCV for use with C++, either:

#### Manually fetch OpenCV (preferred)
1. Download from https://opencv.org/releases/
2. Run self-extracting archive and extract to a suitable location
3. Create an environmental variable named `OpenCV_DIR` pointing to `/build`
4. Add `/bin` folder to PATH (e.g. `.../build/x64/vc16/bin`)

#### Utilize vcpkg (using manifest mode)
Call CMake with `-DCMAKE_TOOLCHAIN_FILE=[path to vcpkg]/scripts/buildsystems/vcpkg.cmake`

> Under MinGW you'll need to specify the vcpkg triplet:
>
>-DVCPKG_TARGET_TRIPLET=x64-mingw-[static|dynamic]  # choose either `static` or `dynamic`. <br>
>-DVCPKG_HOST_TRIPLET=x64-mingw-[static|dynamic]    # <-- needed only if MSVC cannot be found.

---
## Link to tutorials

- [Detection of ArUco Markers](https://docs.opencv.org/4.x/d5/dae/tutorial_aruco_detection.html)
- [Calibration with ArUco and ChArUco](https://docs.opencv.org/4.x/da/d13/tutorial_aruco_calibration.html)
