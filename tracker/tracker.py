import cv2
from ultralytics import YOLO
import numpy as np
import imutils
from collections import defaultdict, deque
from utils import Estimation

estimation = Estimation()

class Tracker:
    def __init__(self, vehicles_ids=[2, 3, 5, 7]):
        self.vehicles_ids = vehicles_ids
        self.track_history = defaultdict(lambda: [])
        self.id_dict = {}
        self.data_deque = {}
        self.speed_line_queue = {}
        self.object_counter = {}
        self.object_counter1 = {}
        self.line = [(100, 500), (1050, 500)]
        self.color = (0, 255, 0)
        self.thickness = 2
        self.font = cv2.FONT_HERSHEY_PLAIN
        self.font_scale = 1.3

    def read_video(self, frame, model):
        frame = imutils.resize(frame, height=720)
        results = model.track(frame, persist=True, verbose=False)[0]
        bboxes = np.array(results.boxes.data.tolist(), dtype="int")
        for box in bboxes:
            x1, y1, x2, y2, track_id, score, class_id = box
            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)
            class_name = results.names[int(class_id)].upper()
            if class_id in self.vehicles_ids:
                track = self.track_history[track_id]
                track.append((cx, cy))
                if len(track) > 15:
                    track.pop(0)
                
                self.id_dict[track_id] = (cx, cy)
                if track_id not in self.data_deque:  
                    self.data_deque[track_id] = deque(maxlen=64)
                    self.speed_line_queue[track_id] = []

                self.data_deque[track_id].appendleft((cx, cy))

                if len(self.data_deque[track_id]) >= 2:
                    direction = estimation.get_direction(self.data_deque[track_id][0], self.data_deque[track_id][1])
                    object_speed = estimation.estimate_speed(self.data_deque[track_id][1], self.data_deque[track_id][0])
                    self.speed_line_queue[track_id].append(object_speed)
                    if estimation.intersect(self.data_deque[track_id][0], self.data_deque[track_id][1], self.line[0], self.line[1]):
                        if "South" in direction:
                            self.object_counter[class_name] += 1
                        if "North" in direction:
                            self.object_counter1[class_name] += 1

                points = np.hstack(track).astype("int32").reshape((-1, 1, 2))
                cv2.polylines(frame, [points], isClosed=False, color=self.color, thickness=self.thickness)

                try:
                    speed_text = f" {sum(self.speed_line_queue[track_id]) // len(self.speed_line_queue[track_id])} km/h"
                    text = f"{track_id} {class_name}{speed_text}"
                    cv2.putText(frame, text, (x1, y1 - 5), self.font, self.font_scale, self.color, self.thickness, cv2.LINE_AA)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), self.color, self.thickness)
                except:
                    text = f"{track_id} {class_name}"
                    cv2.putText(frame, text, (x1, y1 - 5), self.font, self.font_scale, self.color, self.thickness, cv2.LINE_AA)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), self.color, self.thickness)

        return frame