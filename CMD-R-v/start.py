import GeminiPro as Pro
import GeminiProVision as ProVision

isStop = False
isSeeV = True
versionModel = 1
while not isStop:
    stop = "n"  # Default
    if isSeeV:
        _versionModel = input("\n\nWhich model to use, 1 for GeminiPro, 2 for GeminiProVision: ")
        try:
            versionModel = int(_versionModel)
        except Exception as e:
            print(f"{type(e).__name__}: {e}")
            break

        if type(versionModel) is not int:
            isStop = True
        else:
            m1 = 'Gemini-pro, Generate text from text inputs'
            m2 = 'Gemini-Pro-Vision, Generate text from image and text inputs'
            if versionModel in range(1, 3):
                if versionModel == 1:
                    print(m1)
                else:
                    print(m2)
            isSeeV = False

    if versionModel == 1 and stop != "y":
        _q = str(input("\n\nUser: "))
        ans = Pro.response_generate(_q)
        print(f"\nModel: {ans}")
        print("-" * 91)
    elif versionModel == 2 and stop != "y":
        print("\n\n'Write Proper full Image name.'")
        _l = str(input("Image Name(*): "))
        _q = str(input("User: "))
        if _l:
            _l = f"./resource/images/{_l}"
            ans = ProVision.response_generate(_question=_q, _location=_l)
            print(f"\nModel: {ans}")
        print("-" * 91)
    else:
        print("Stop!")
        isStop = True

    if versionModel in range(1, 3):
        closeModel = str(input("Can we close this model(y/n)?: "))

        if closeModel == "y":
            stop = str(input("Can we stop response(y/n): "))
            if stop == "y":
                isStop = True
            else:
                isSeeV = True
        elif closeModel != "n":
            isStop = True
    else:
        isStop = True
