import cv2
import os

def save_last_frames(video_path, out_prefix, n_frames=5):
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if frame_count < 10:
        cap.release()
        return
    start = int(frame_count * 0.8)
    end = frame_count - 1
    chosen = list(range(start, min(end, start + n_frames)))
    for idx in chosen:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out_path = f'{out_prefix}_frame{idx}.png'
            cv2.imwrite(out_path, cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR))
    cap.release()

if __name__ == '__main__':
    happy_left_path = 'stimuli_figures/frames_for_selection/happy_left_frame53.png'
    # Orijinal video yolunu bul
    video_dir = 'videos/StudyVideos'
    for fname in os.listdir(video_dir):
        if fname.startswith('happy') and '_left_' in fname and fname.endswith('.mp4'):
            video_path = os.path.join(video_dir, fname)
            break
    out_prefix = 'stimuli_figures/frames_for_selection/happy_left_last'
    save_last_frames(video_path, out_prefix, n_frames=5)
    print('happy left için sonlara yakın kareler kaydedildi.')
