import cv2 as cv
import asyncio

class VideoStream:
    def __init__(self, camera_id, fps):
        print("Open camera")
        self.video = cv.VideoCapture(camera_id)
        self.sleep_fps = 1/fps
        if not self.video.isOpened():
            print("Cannot open camera")
            exit()

    #def face_detection(self, img):

    async def getFrame(self):
        print("Start capturing")
        try:
            while True:
                # Capture frame-by-frame
                ret, frame = self.video.read()
                # if frame is read correctly ret is True
                if not ret:
                    print("Can't receive frame (stream end?). Exiting ...")
                    break

                # Display the resulting frame
                cv.imshow('frame', frame)
                await asyncio.sleep(self.sleep_fps)
                if cv.waitKey(1) == ord('q'):
                    break
        except:
            # Release resources
            print("Error: Video steam cannt capture a frame")
            self.video.release()
            cv.destroyAllWindows()
         # When everything done, release the capture
        self.video.release()
        cv.destroyAllWindows()

if __name__ == "__main__":
    camera_id = 1
    fps = 10
    video_stream = VideoStream(camera_id, fps)
    #task_vs_gf = asyncio.create_task(coro=video_stream.getFrame())

    #await task_vs_gf
    asyncio.run(video_stream.getFrame())


