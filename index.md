---
layout: index
title: 'Language-Grounded Control for Coordinated Robot Motion and Speech'
subtitle: "
Recent advancements have enabled human-robot collaboration through physical assistance and verbal guidance. However, limitations persist in coordinating robots' physical motions and speech in response to real-time changes in human behavior during collaborative contact tasks. We first derive principles from analyzing physical therapists' movements and speech during patient exercises. These principles are translated into control objectives to: 1) guide users through trajectories, 2) control motion and speech pace to align completion times with varying user cooperation, and 3) dynamically paraphrase speech along the trajectory.
We then propose a Language Controller that synchronizes motion and speech, modulating both based on user cooperation. Experiments with 12 users show the Language Controller successfully aligns motion and speech compared to baselines. This provides a framework for fluent human-robot collaboration."
---

<script src="https://vjs.zencdn.net/8.0.4/video.min.js"></script>

<center>
    <video class="video-js" style="display:block;width:40%;height:fit-content;" controls preload="auto">
        <source src="/videos/user_sessions/u8_lc.webm" type="video/webm">
    </video>
</center>
<span style="font-size:medium;">
Robot is seen interacting with a user participant using our language controller on a desired trajectory which was inspired by the therapy session "shoulder external rotation''. Interactions and Results for all the users are available in <a href="{{ item.url | relative_url }}/user-sessions">user sessions</a>.</span>

<center style="margin-top:2em;margin-bottom:2em">
    <img src="/images/language-control-diagram.svg" style="width:50%;"/>
    <span style="font-size:medium;">
    The Control Scheme of Language Controller.</span>
</center>

    
## Results

<!--#### Evaluating solvers on a set of static poses-->
<br/><br/>
<center>
    <img src="/images/plots/summary.svg" style="width:50%;"/>
</center>
<span style="font-size:medium;">
Violin plot of the distributions of metrics for 3 controllers across all 12 user sessions. Blue bars indicate min, median, and max of a distribution. Consistent distributions of cooperation for all controllers show that all controllers deliver similar physical experience to the users; On this ground, LC exhibits less audio-motion misalignment (both actual and predicted) than LC-noAR which exhibits significantly less variation in misalignment than the AC baseline. Adaptive paraphrasing allows LC to maintain a more natural speed of speech most of the time than LC-noAR, as shown by a more concentrated peak around the default rate of 1 in audio rate distribution. Overall, LC best aligns the robot's speech with motion. See <a href="{{ item.url | relative_url }}/user-sessions">results for all user sessions</a>.</span>

## Code
Refer to the [Language Controller repository](https://github.com/language-playback-robot-controller/language-playback-robot-controller) for the codebase of our language controller and baselines.


