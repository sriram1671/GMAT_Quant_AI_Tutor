import pandas as pd

def update_performance(log_df, topic, is_correct):
    if topic not in log_df:
        log_df[topic] = [0, 0]  # correct, attempted
    log_df[topic][1] += 1
    if is_correct:
        log_df[topic][0] += 1
    return log_df

def analyze_weaknesses(log_df):
    weaknesses = []
    for topic, (correct, attempted) in log_df.items():
        accuracy = correct / attempted
        if accuracy < 0.6:
            weaknesses.append((topic, accuracy))
    return sorted(weaknesses, key=lambda x: x[1])
