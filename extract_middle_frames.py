import cv2
import os
import random

emotions = ['angry', 'happy', 'sad', 'surprise']
poses = ['front', 'left']
data_dir = 'videos/StudyVideos'
output_dir = 'stimuli_figures/frames_for_selection'
os.makedirs(output_dir, exist_ok=True)

video_dict = {}
for emotion in emotions:
    video_dict[emotion] = {}
    for pose in poses:
        for fname in os.listdir(data_dir):
            if fname.startswith(f'{emotion}') and f'_{pose}_' in fname and fname.endswith('.mp4'):
                video_dict[emotion][pose] = os.path.join(data_dir, fname)
                break

def save_middle_frames(video_path, out_prefix, n_frames=5):
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if frame_count < 10:
        cap.release()
        return
    start = int(frame_count * 0.4)
    end = int(frame_count * 0.6)
    chosen = sorted(random.sample(range(start, end), n_frames))
    for idx in chosen:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out_path = f'{out_prefix}_frame{idx}.png'
            cv2.imwrite(out_path, cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR))
    cap.release()

if __name__ == '__main__':
    for emotion in emotions:
        for pose in poses:
            video_path = video_dict[emotion].get(pose)
            if video_path:
                out_prefix = os.path.join(output_dir, f'{emotion}_{pose}')
                save_middle_frames(video_path, out_prefix, n_frames=5)
    print('Ortalardan kareler kaydedildi. "stimuli_figures/frames_for_selection" klasörüne bakabilirsin.')
