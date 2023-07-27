if __name__ == "__main__":

    
    import argparse
    from Gary.garySE.VideoSummarizer import VideoSummarizer

    parser = argparse.ArgumentParser()
    parser.add_argument('--video_path', type=str, help='Video path')
    opt = parser.parse_args()
    video_path = opt.video_path

    vs = VideoSummarizer(video_path=video_path)
    vs.summarize()