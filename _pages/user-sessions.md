---
permalink: /user-sessions/
title: User Sessions
subtitle: "The user study had 12 participants (7 males, 5 females, mean age 23). The UR5 robot guided users through a predefined trajectory demonstrated by the therapist. Users sat beside the robot, placed their hand on the desk. The robot guided their hand along the trajectory with speech instructions while users varied resistance arbitrarily."
---


<script src="https://vjs.zencdn.net/8.0.4/video.min.js"></script>

## Control Schemes Evaluated and Compared
* **Admittance Controller with Decoupled Audio (AC)**: This baseline is a pure admittance controller. The audio is a single prerecorded audio file that starts simultaneously with the trajectory. Physical and Audio Paces are not modulated at all.
* **Language Controller without Adaptive Paraphrasing (LC-noAP)**: Our controller but without the ability to adaptively paraphrase the speech.
* **Language Controller (LC)**: Our controller with adaptive paraphrasing by traversing a phrase graph.


<!-- GENERATED -->

## User 1 
<style>
.tabset1 > input[type="radio"] { position: absolute; left: -200vw; }
.tabset1 .tab-panel1 { display: none; }
.tabset1 > input:first-child:checked ~ .tab-panel1s > .tab-panel1:first-child,
.tabset1 > input:nth-child(3):checked ~ .tab-panel1s > .tab-panel1:nth-child(2),
.tabset1 > input:nth-child(5):checked ~ .tab-panel1s > .tab-panel1:nth-child(3),
.tabset1 > input:nth-child(7):checked ~ .tab-panel1s > .tab-panel1:nth-child(4),
.tabset1 > input:nth-child(9):checked ~ .tab-panel1s > .tab-panel1:nth-child(5),
.tabset1 > input:nth-child(11):checked ~ .tab-panel1s > .tab-panel1:nth-child(6) { display: block; }
.tabset1 > label { position: relative; display: inline-block; padding: 15px 15px 25px; border: 1px solid transparent; border-bottom: 0; cursor: pointer; font-weight: 600; }
.tabset1 > label::after { content: ""; position: absolute; left: 15px; bottom: 10px; width: 22px; height: 4px; background: #8d8d8d; }
input:focus-visible + label { outline: 2px solid rgba(242,120,75,0.95); border-radius: 3px; }
.tabset1 > label:hover, .tabset1 > input:focus + label, .tabset1 > input:checked + label { color: rgba(242,120,75,0.95); }
.tabset1 > label:hover::after, .tabset1 > input:focus + label::after, .tabset1 > input:checked + label::after { background: rgba(242,120,75,0.95); }
.tabset1 > input:checked + label { border-color: black; border-width: 2px; border-bottom: 1px solid #fff; margin-bottom: -1px; }
.tab-panel1 { padding: 30px 0; border-top: 2px solid black; }
</style>
<table style="table-layout:fixed;width:100%;">
    <tr><th style="width:33.333%">AC</th><th style="width:33.333%">LC-noAP</th><th style="width:33.333%">LC</th></tr>
    <tr>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u1_ac.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u1_lcnoap.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u1_lc.webm" type="video/webm">
            </video>
        </td>
    </tr>
</table>
<div class="tabset1 table-wrap" style="">
    <input type="radio" name="tabset1" id="tab1-1" aria-controls="ac">
    <label for="tab1-1">AC</label>
    <input type="radio" name="tabset1" id="tab2-1" aria-controls="lcnoap">
    <label for="tab2-1">LC-noAP</label>
    <input type="radio" name="tabset1" id="tab3-1" aria-controls="lc" checked>
    <label for="tab3-1">LC</label>
    <div class="tab-panel1s">
        <section id="marzen" class="tab-panel1" style="margin:0">
            <img src="/images/plots/u1_ac.svg" width="100%">
        </section>
        <section id="rauchbier" class="tab-panel1" style="margin:0">
            <img src="/images/plots/u1_lcnoap.svg" width="100%">
        </section>
        <section id="dunkles" class="tab-panel1" style="margin:0">
            <img src="/images/plots/u1_lc.svg" width="100%">
        </section>
    </div>
</div>

## User 2 
<style>
.tabset2 > input[type="radio"] { position: absolute; left: -200vw; }
.tabset2 .tab-panel2 { display: none; }
.tabset2 > input:first-child:checked ~ .tab-panel2s > .tab-panel2:first-child,
.tabset2 > input:nth-child(3):checked ~ .tab-panel2s > .tab-panel2:nth-child(2),
.tabset2 > input:nth-child(5):checked ~ .tab-panel2s > .tab-panel2:nth-child(3),
.tabset2 > input:nth-child(7):checked ~ .tab-panel2s > .tab-panel2:nth-child(4),
.tabset2 > input:nth-child(9):checked ~ .tab-panel2s > .tab-panel2:nth-child(5),
.tabset2 > input:nth-child(11):checked ~ .tab-panel2s > .tab-panel2:nth-child(6) { display: block; }
.tabset2 > label { position: relative; display: inline-block; padding: 15px 15px 25px; border: 1px solid transparent; border-bottom: 0; cursor: pointer; font-weight: 600; }
.tabset2 > label::after { content: ""; position: absolute; left: 15px; bottom: 10px; width: 22px; height: 4px; background: #8d8d8d; }
input:focus-visible + label { outline: 2px solid rgba(242,120,75,0.95); border-radius: 3px; }
.tabset2 > label:hover, .tabset2 > input:focus + label, .tabset2 > input:checked + label { color: rgba(242,120,75,0.95); }
.tabset2 > label:hover::after, .tabset2 > input:focus + label::after, .tabset2 > input:checked + label::after { background: rgba(242,120,75,0.95); }
.tabset2 > input:checked + label { border-color: black; border-width: 2px; border-bottom: 1px solid #fff; margin-bottom: -1px; }
.tab-panel2 { padding: 30px 0; border-top: 2px solid black; }
</style>
<table style="table-layout:fixed;width:100%;">
    <tr><th style="width:33.333%">AC</th><th style="width:33.333%">LC-noAP</th><th style="width:33.333%">LC</th></tr>
    <tr>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u2_ac.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u2_lcnoap.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u2_lc.webm" type="video/webm">
            </video>
        </td>
    </tr>
</table>
<div class="tabset2 table-wrap" style="">
    <input type="radio" name="tabset2" id="tab1-2" aria-controls="ac">
    <label for="tab1-2">AC</label>
    <input type="radio" name="tabset2" id="tab2-2" aria-controls="lcnoap">
    <label for="tab2-2">LC-noAP</label>
    <input type="radio" name="tabset2" id="tab3-2" aria-controls="lc" checked>
    <label for="tab3-2">LC</label>
    <div class="tab-panel2s">
        <section id="marzen" class="tab-panel2" style="margin:0">
            <img src="/images/plots/u2_ac.svg" width="100%">
        </section>
        <section id="rauchbier" class="tab-panel2" style="margin:0">
            <img src="/images/plots/u2_lcnoap.svg" width="100%">
        </section>
        <section id="dunkles" class="tab-panel2" style="margin:0">
            <img src="/images/plots/u2_lc.svg" width="100%">
        </section>
    </div>
</div>

## User 3 
<style>
.tabset3 > input[type="radio"] { position: absolute; left: -200vw; }
.tabset3 .tab-panel3 { display: none; }
.tabset3 > input:first-child:checked ~ .tab-panel3s > .tab-panel3:first-child,
.tabset3 > input:nth-child(3):checked ~ .tab-panel3s > .tab-panel3:nth-child(2),
.tabset3 > input:nth-child(5):checked ~ .tab-panel3s > .tab-panel3:nth-child(3),
.tabset3 > input:nth-child(7):checked ~ .tab-panel3s > .tab-panel3:nth-child(4),
.tabset3 > input:nth-child(9):checked ~ .tab-panel3s > .tab-panel3:nth-child(5),
.tabset3 > input:nth-child(11):checked ~ .tab-panel3s > .tab-panel3:nth-child(6) { display: block; }
.tabset3 > label { position: relative; display: inline-block; padding: 15px 15px 25px; border: 1px solid transparent; border-bottom: 0; cursor: pointer; font-weight: 600; }
.tabset3 > label::after { content: ""; position: absolute; left: 15px; bottom: 10px; width: 22px; height: 4px; background: #8d8d8d; }
input:focus-visible + label { outline: 2px solid rgba(242,120,75,0.95); border-radius: 3px; }
.tabset3 > label:hover, .tabset3 > input:focus + label, .tabset3 > input:checked + label { color: rgba(242,120,75,0.95); }
.tabset3 > label:hover::after, .tabset3 > input:focus + label::after, .tabset3 > input:checked + label::after { background: rgba(242,120,75,0.95); }
.tabset3 > input:checked + label { border-color: black; border-width: 2px; border-bottom: 1px solid #fff; margin-bottom: -1px; }
.tab-panel3 { padding: 30px 0; border-top: 2px solid black; }
</style>
<table style="table-layout:fixed;width:100%;">
    <tr><th style="width:33.333%">AC</th><th style="width:33.333%">LC-noAP</th><th style="width:33.333%">LC</th></tr>
    <tr>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u3_ac.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u3_lcnoap.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u3_lc.webm" type="video/webm">
            </video>
        </td>
    </tr>
</table>
<div class="tabset3 table-wrap" style="">
    <input type="radio" name="tabset3" id="tab1-3" aria-controls="ac">
    <label for="tab1-3">AC</label>
    <input type="radio" name="tabset3" id="tab2-3" aria-controls="lcnoap">
    <label for="tab2-3">LC-noAP</label>
    <input type="radio" name="tabset3" id="tab3-3" aria-controls="lc" checked>
    <label for="tab3-3">LC</label>
    <div class="tab-panel3s">
        <section id="marzen" class="tab-panel3" style="margin:0">
            <img src="/images/plots/u3_ac.svg" width="100%">
        </section>
        <section id="rauchbier" class="tab-panel3" style="margin:0">
            <img src="/images/plots/u3_lcnoap.svg" width="100%">
        </section>
        <section id="dunkles" class="tab-panel3" style="margin:0">
            <img src="/images/plots/u3_lc.svg" width="100%">
        </section>
    </div>
</div>

## User 4 
<style>
.tabset4 > input[type="radio"] { position: absolute; left: -200vw; }
.tabset4 .tab-panel4 { display: none; }
.tabset4 > input:first-child:checked ~ .tab-panel4s > .tab-panel4:first-child,
.tabset4 > input:nth-child(3):checked ~ .tab-panel4s > .tab-panel4:nth-child(2),
.tabset4 > input:nth-child(5):checked ~ .tab-panel4s > .tab-panel4:nth-child(3),
.tabset4 > input:nth-child(7):checked ~ .tab-panel4s > .tab-panel4:nth-child(4),
.tabset4 > input:nth-child(9):checked ~ .tab-panel4s > .tab-panel4:nth-child(5),
.tabset4 > input:nth-child(11):checked ~ .tab-panel4s > .tab-panel4:nth-child(6) { display: block; }
.tabset4 > label { position: relative; display: inline-block; padding: 15px 15px 25px; border: 1px solid transparent; border-bottom: 0; cursor: pointer; font-weight: 600; }
.tabset4 > label::after { content: ""; position: absolute; left: 15px; bottom: 10px; width: 22px; height: 4px; background: #8d8d8d; }
input:focus-visible + label { outline: 2px solid rgba(242,120,75,0.95); border-radius: 3px; }
.tabset4 > label:hover, .tabset4 > input:focus + label, .tabset4 > input:checked + label { color: rgba(242,120,75,0.95); }
.tabset4 > label:hover::after, .tabset4 > input:focus + label::after, .tabset4 > input:checked + label::after { background: rgba(242,120,75,0.95); }
.tabset4 > input:checked + label { border-color: black; border-width: 2px; border-bottom: 1px solid #fff; margin-bottom: -1px; }
.tab-panel4 { padding: 30px 0; border-top: 2px solid black; }
</style>
<table style="table-layout:fixed;width:100%;">
    <tr><th style="width:33.333%">AC</th><th style="width:33.333%">LC-noAP</th><th style="width:33.333%">LC</th></tr>
    <tr>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u4_ac.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u4_lcnoap.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u4_lc.webm" type="video/webm">
            </video>
        </td>
    </tr>
</table>
<div class="tabset4 table-wrap" style="">
    <input type="radio" name="tabset4" id="tab1-4" aria-controls="ac">
    <label for="tab1-4">AC</label>
    <input type="radio" name="tabset4" id="tab2-4" aria-controls="lcnoap">
    <label for="tab2-4">LC-noAP</label>
    <input type="radio" name="tabset4" id="tab3-4" aria-controls="lc" checked>
    <label for="tab3-4">LC</label>
    <div class="tab-panel4s">
        <section id="marzen" class="tab-panel4" style="margin:0">
            <img src="/images/plots/u4_ac.svg" width="100%">
        </section>
        <section id="rauchbier" class="tab-panel4" style="margin:0">
            <img src="/images/plots/u4_lcnoap.svg" width="100%">
        </section>
        <section id="dunkles" class="tab-panel4" style="margin:0">
            <img src="/images/plots/u4_lc.svg" width="100%">
        </section>
    </div>
</div>

## User 5 
<style>
.tabset5 > input[type="radio"] { position: absolute; left: -200vw; }
.tabset5 .tab-panel5 { display: none; }
.tabset5 > input:first-child:checked ~ .tab-panel5s > .tab-panel5:first-child,
.tabset5 > input:nth-child(3):checked ~ .tab-panel5s > .tab-panel5:nth-child(2),
.tabset5 > input:nth-child(5):checked ~ .tab-panel5s > .tab-panel5:nth-child(3),
.tabset5 > input:nth-child(7):checked ~ .tab-panel5s > .tab-panel5:nth-child(4),
.tabset5 > input:nth-child(9):checked ~ .tab-panel5s > .tab-panel5:nth-child(5),
.tabset5 > input:nth-child(11):checked ~ .tab-panel5s > .tab-panel5:nth-child(6) { display: block; }
.tabset5 > label { position: relative; display: inline-block; padding: 15px 15px 25px; border: 1px solid transparent; border-bottom: 0; cursor: pointer; font-weight: 600; }
.tabset5 > label::after { content: ""; position: absolute; left: 15px; bottom: 10px; width: 22px; height: 4px; background: #8d8d8d; }
input:focus-visible + label { outline: 2px solid rgba(242,120,75,0.95); border-radius: 3px; }
.tabset5 > label:hover, .tabset5 > input:focus + label, .tabset5 > input:checked + label { color: rgba(242,120,75,0.95); }
.tabset5 > label:hover::after, .tabset5 > input:focus + label::after, .tabset5 > input:checked + label::after { background: rgba(242,120,75,0.95); }
.tabset5 > input:checked + label { border-color: black; border-width: 2px; border-bottom: 1px solid #fff; margin-bottom: -1px; }
.tab-panel5 { padding: 30px 0; border-top: 2px solid black; }
</style>
<table style="table-layout:fixed;width:100%;">
    <tr><th style="width:33.333%">AC</th><th style="width:33.333%">LC-noAP</th><th style="width:33.333%">LC</th></tr>
    <tr>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u5_ac.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u5_lcnoap.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u5_lc.webm" type="video/webm">
            </video>
        </td>
    </tr>
</table>
<div class="tabset5 table-wrap" style="">
    <input type="radio" name="tabset5" id="tab1-5" aria-controls="ac">
    <label for="tab1-5">AC</label>
    <input type="radio" name="tabset5" id="tab2-5" aria-controls="lcnoap">
    <label for="tab2-5">LC-noAP</label>
    <input type="radio" name="tabset5" id="tab3-5" aria-controls="lc" checked>
    <label for="tab3-5">LC</label>
    <div class="tab-panel5s">
        <section id="marzen" class="tab-panel5" style="margin:0">
            <img src="/images/plots/u5_ac.svg" width="100%">
        </section>
        <section id="rauchbier" class="tab-panel5" style="margin:0">
            <img src="/images/plots/u5_lcnoap.svg" width="100%">
        </section>
        <section id="dunkles" class="tab-panel5" style="margin:0">
            <img src="/images/plots/u5_lc.svg" width="100%">
        </section>
    </div>
</div>

## User 6 
<style>
.tabset6 > input[type="radio"] { position: absolute; left: -200vw; }
.tabset6 .tab-panel6 { display: none; }
.tabset6 > input:first-child:checked ~ .tab-panel6s > .tab-panel6:first-child,
.tabset6 > input:nth-child(3):checked ~ .tab-panel6s > .tab-panel6:nth-child(2),
.tabset6 > input:nth-child(5):checked ~ .tab-panel6s > .tab-panel6:nth-child(3),
.tabset6 > input:nth-child(7):checked ~ .tab-panel6s > .tab-panel6:nth-child(4),
.tabset6 > input:nth-child(9):checked ~ .tab-panel6s > .tab-panel6:nth-child(5),
.tabset6 > input:nth-child(11):checked ~ .tab-panel6s > .tab-panel6:nth-child(6) { display: block; }
.tabset6 > label { position: relative; display: inline-block; padding: 15px 15px 25px; border: 1px solid transparent; border-bottom: 0; cursor: pointer; font-weight: 600; }
.tabset6 > label::after { content: ""; position: absolute; left: 15px; bottom: 10px; width: 22px; height: 4px; background: #8d8d8d; }
input:focus-visible + label { outline: 2px solid rgba(242,120,75,0.95); border-radius: 3px; }
.tabset6 > label:hover, .tabset6 > input:focus + label, .tabset6 > input:checked + label { color: rgba(242,120,75,0.95); }
.tabset6 > label:hover::after, .tabset6 > input:focus + label::after, .tabset6 > input:checked + label::after { background: rgba(242,120,75,0.95); }
.tabset6 > input:checked + label { border-color: black; border-width: 2px; border-bottom: 1px solid #fff; margin-bottom: -1px; }
.tab-panel6 { padding: 30px 0; border-top: 2px solid black; }
</style>
<table style="table-layout:fixed;width:100%;">
    <tr><th style="width:33.333%">AC</th><th style="width:33.333%">LC-noAP</th><th style="width:33.333%">LC</th></tr>
    <tr>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u6_ac.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u6_lcnoap.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u6_lc.webm" type="video/webm">
            </video>
        </td>
    </tr>
</table>
<div class="tabset6 table-wrap" style="">
    <input type="radio" name="tabset6" id="tab1-6" aria-controls="ac">
    <label for="tab1-6">AC</label>
    <input type="radio" name="tabset6" id="tab2-6" aria-controls="lcnoap">
    <label for="tab2-6">LC-noAP</label>
    <input type="radio" name="tabset6" id="tab3-6" aria-controls="lc" checked>
    <label for="tab3-6">LC</label>
    <div class="tab-panel6s">
        <section id="marzen" class="tab-panel6" style="margin:0">
            <img src="/images/plots/u6_ac.svg" width="100%">
        </section>
        <section id="rauchbier" class="tab-panel6" style="margin:0">
            <img src="/images/plots/u6_lcnoap.svg" width="100%">
        </section>
        <section id="dunkles" class="tab-panel6" style="margin:0">
            <img src="/images/plots/u6_lc.svg" width="100%">
        </section>
    </div>
</div>

## User 7 
<style>
.tabset7 > input[type="radio"] { position: absolute; left: -200vw; }
.tabset7 .tab-panel7 { display: none; }
.tabset7 > input:first-child:checked ~ .tab-panel7s > .tab-panel7:first-child,
.tabset7 > input:nth-child(3):checked ~ .tab-panel7s > .tab-panel7:nth-child(2),
.tabset7 > input:nth-child(5):checked ~ .tab-panel7s > .tab-panel7:nth-child(3),
.tabset7 > input:nth-child(7):checked ~ .tab-panel7s > .tab-panel7:nth-child(4),
.tabset7 > input:nth-child(9):checked ~ .tab-panel7s > .tab-panel7:nth-child(5),
.tabset7 > input:nth-child(11):checked ~ .tab-panel7s > .tab-panel7:nth-child(6) { display: block; }
.tabset7 > label { position: relative; display: inline-block; padding: 15px 15px 25px; border: 1px solid transparent; border-bottom: 0; cursor: pointer; font-weight: 600; }
.tabset7 > label::after { content: ""; position: absolute; left: 15px; bottom: 10px; width: 22px; height: 4px; background: #8d8d8d; }
input:focus-visible + label { outline: 2px solid rgba(242,120,75,0.95); border-radius: 3px; }
.tabset7 > label:hover, .tabset7 > input:focus + label, .tabset7 > input:checked + label { color: rgba(242,120,75,0.95); }
.tabset7 > label:hover::after, .tabset7 > input:focus + label::after, .tabset7 > input:checked + label::after { background: rgba(242,120,75,0.95); }
.tabset7 > input:checked + label { border-color: black; border-width: 2px; border-bottom: 1px solid #fff; margin-bottom: -1px; }
.tab-panel7 { padding: 30px 0; border-top: 2px solid black; }
</style>
<table style="table-layout:fixed;width:100%;">
    <tr><th style="width:33.333%">AC</th><th style="width:33.333%">LC-noAP</th><th style="width:33.333%">LC</th></tr>
    <tr>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u7_ac.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u7_lcnoap.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u7_lc.webm" type="video/webm">
            </video>
        </td>
    </tr>
</table>
<div class="tabset7 table-wrap" style="">
    <input type="radio" name="tabset7" id="tab1-7" aria-controls="ac">
    <label for="tab1-7">AC</label>
    <input type="radio" name="tabset7" id="tab2-7" aria-controls="lcnoap">
    <label for="tab2-7">LC-noAP</label>
    <input type="radio" name="tabset7" id="tab3-7" aria-controls="lc" checked>
    <label for="tab3-7">LC</label>
    <div class="tab-panel7s">
        <section id="marzen" class="tab-panel7" style="margin:0">
            <img src="/images/plots/u7_ac.svg" width="100%">
        </section>
        <section id="rauchbier" class="tab-panel7" style="margin:0">
            <img src="/images/plots/u7_lcnoap.svg" width="100%">
        </section>
        <section id="dunkles" class="tab-panel7" style="margin:0">
            <img src="/images/plots/u7_lc.svg" width="100%">
        </section>
    </div>
</div>

## User 8 
<style>
.tabset8 > input[type="radio"] { position: absolute; left: -200vw; }
.tabset8 .tab-panel8 { display: none; }
.tabset8 > input:first-child:checked ~ .tab-panel8s > .tab-panel8:first-child,
.tabset8 > input:nth-child(3):checked ~ .tab-panel8s > .tab-panel8:nth-child(2),
.tabset8 > input:nth-child(5):checked ~ .tab-panel8s > .tab-panel8:nth-child(3),
.tabset8 > input:nth-child(7):checked ~ .tab-panel8s > .tab-panel8:nth-child(4),
.tabset8 > input:nth-child(9):checked ~ .tab-panel8s > .tab-panel8:nth-child(5),
.tabset8 > input:nth-child(11):checked ~ .tab-panel8s > .tab-panel8:nth-child(6) { display: block; }
.tabset8 > label { position: relative; display: inline-block; padding: 15px 15px 25px; border: 1px solid transparent; border-bottom: 0; cursor: pointer; font-weight: 600; }
.tabset8 > label::after { content: ""; position: absolute; left: 15px; bottom: 10px; width: 22px; height: 4px; background: #8d8d8d; }
input:focus-visible + label { outline: 2px solid rgba(242,120,75,0.95); border-radius: 3px; }
.tabset8 > label:hover, .tabset8 > input:focus + label, .tabset8 > input:checked + label { color: rgba(242,120,75,0.95); }
.tabset8 > label:hover::after, .tabset8 > input:focus + label::after, .tabset8 > input:checked + label::after { background: rgba(242,120,75,0.95); }
.tabset8 > input:checked + label { border-color: black; border-width: 2px; border-bottom: 1px solid #fff; margin-bottom: -1px; }
.tab-panel8 { padding: 30px 0; border-top: 2px solid black; }
</style>
<table style="table-layout:fixed;width:100%;">
    <tr><th style="width:33.333%">AC</th><th style="width:33.333%">LC-noAP</th><th style="width:33.333%">LC</th></tr>
    <tr>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u8_ac.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u8_lcnoap.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u8_lc.webm" type="video/webm">
            </video>
        </td>
    </tr>
</table>
<div class="tabset8 table-wrap" style="">
    <input type="radio" name="tabset8" id="tab1-8" aria-controls="ac">
    <label for="tab1-8">AC</label>
    <input type="radio" name="tabset8" id="tab2-8" aria-controls="lcnoap">
    <label for="tab2-8">LC-noAP</label>
    <input type="radio" name="tabset8" id="tab3-8" aria-controls="lc" checked>
    <label for="tab3-8">LC</label>
    <div class="tab-panel8s">
        <section id="marzen" class="tab-panel8" style="margin:0">
            <img src="/images/plots/u8_ac.svg" width="100%">
        </section>
        <section id="rauchbier" class="tab-panel8" style="margin:0">
            <img src="/images/plots/u8_lcnoap.svg" width="100%">
        </section>
        <section id="dunkles" class="tab-panel8" style="margin:0">
            <img src="/images/plots/u8_lc.svg" width="100%">
        </section>
    </div>
</div>

## User 9 
<style>
.tabset9 > input[type="radio"] { position: absolute; left: -200vw; }
.tabset9 .tab-panel9 { display: none; }
.tabset9 > input:first-child:checked ~ .tab-panel9s > .tab-panel9:first-child,
.tabset9 > input:nth-child(3):checked ~ .tab-panel9s > .tab-panel9:nth-child(2),
.tabset9 > input:nth-child(5):checked ~ .tab-panel9s > .tab-panel9:nth-child(3),
.tabset9 > input:nth-child(7):checked ~ .tab-panel9s > .tab-panel9:nth-child(4),
.tabset9 > input:nth-child(9):checked ~ .tab-panel9s > .tab-panel9:nth-child(5),
.tabset9 > input:nth-child(11):checked ~ .tab-panel9s > .tab-panel9:nth-child(6) { display: block; }
.tabset9 > label { position: relative; display: inline-block; padding: 15px 15px 25px; border: 1px solid transparent; border-bottom: 0; cursor: pointer; font-weight: 600; }
.tabset9 > label::after { content: ""; position: absolute; left: 15px; bottom: 10px; width: 22px; height: 4px; background: #8d8d8d; }
input:focus-visible + label { outline: 2px solid rgba(242,120,75,0.95); border-radius: 3px; }
.tabset9 > label:hover, .tabset9 > input:focus + label, .tabset9 > input:checked + label { color: rgba(242,120,75,0.95); }
.tabset9 > label:hover::after, .tabset9 > input:focus + label::after, .tabset9 > input:checked + label::after { background: rgba(242,120,75,0.95); }
.tabset9 > input:checked + label { border-color: black; border-width: 2px; border-bottom: 1px solid #fff; margin-bottom: -1px; }
.tab-panel9 { padding: 30px 0; border-top: 2px solid black; }
</style>
<table style="table-layout:fixed;width:100%;">
    <tr><th style="width:33.333%">AC</th><th style="width:33.333%">LC-noAP</th><th style="width:33.333%">LC</th></tr>
    <tr>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u9_ac.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u9_lcnoap.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u9_lc.webm" type="video/webm">
            </video>
        </td>
    </tr>
</table>
<div class="tabset9 table-wrap" style="">
    <input type="radio" name="tabset9" id="tab1-9" aria-controls="ac">
    <label for="tab1-9">AC</label>
    <input type="radio" name="tabset9" id="tab2-9" aria-controls="lcnoap">
    <label for="tab2-9">LC-noAP</label>
    <input type="radio" name="tabset9" id="tab3-9" aria-controls="lc" checked>
    <label for="tab3-9">LC</label>
    <div class="tab-panel9s">
        <section id="marzen" class="tab-panel9" style="margin:0">
            <img src="/images/plots/u9_ac.svg" width="100%">
        </section>
        <section id="rauchbier" class="tab-panel9" style="margin:0">
            <img src="/images/plots/u9_lcnoap.svg" width="100%">
        </section>
        <section id="dunkles" class="tab-panel9" style="margin:0">
            <img src="/images/plots/u9_lc.svg" width="100%">
        </section>
    </div>
</div>

## User 10 
<style>
.tabset10 > input[type="radio"] { position: absolute; left: -200vw; }
.tabset10 .tab-panel10 { display: none; }
.tabset10 > input:first-child:checked ~ .tab-panel10s > .tab-panel10:first-child,
.tabset10 > input:nth-child(3):checked ~ .tab-panel10s > .tab-panel10:nth-child(2),
.tabset10 > input:nth-child(5):checked ~ .tab-panel10s > .tab-panel10:nth-child(3),
.tabset10 > input:nth-child(7):checked ~ .tab-panel10s > .tab-panel10:nth-child(4),
.tabset10 > input:nth-child(9):checked ~ .tab-panel10s > .tab-panel10:nth-child(5),
.tabset10 > input:nth-child(11):checked ~ .tab-panel10s > .tab-panel10:nth-child(6) { display: block; }
.tabset10 > label { position: relative; display: inline-block; padding: 15px 15px 25px; border: 1px solid transparent; border-bottom: 0; cursor: pointer; font-weight: 600; }
.tabset10 > label::after { content: ""; position: absolute; left: 15px; bottom: 10px; width: 22px; height: 4px; background: #8d8d8d; }
input:focus-visible + label { outline: 2px solid rgba(242,120,75,0.95); border-radius: 3px; }
.tabset10 > label:hover, .tabset10 > input:focus + label, .tabset10 > input:checked + label { color: rgba(242,120,75,0.95); }
.tabset10 > label:hover::after, .tabset10 > input:focus + label::after, .tabset10 > input:checked + label::after { background: rgba(242,120,75,0.95); }
.tabset10 > input:checked + label { border-color: black; border-width: 2px; border-bottom: 1px solid #fff; margin-bottom: -1px; }
.tab-panel10 { padding: 30px 0; border-top: 2px solid black; }
</style>
<table style="table-layout:fixed;width:100%;">
    <tr><th style="width:33.333%">AC</th><th style="width:33.333%">LC-noAP</th><th style="width:33.333%">LC</th></tr>
    <tr>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u10_ac.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u10_lcnoap.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u10_lc.webm" type="video/webm">
            </video>
        </td>
    </tr>
</table>
<div class="tabset10 table-wrap" style="">
    <input type="radio" name="tabset10" id="tab1-10" aria-controls="ac">
    <label for="tab1-10">AC</label>
    <input type="radio" name="tabset10" id="tab2-10" aria-controls="lcnoap">
    <label for="tab2-10">LC-noAP</label>
    <input type="radio" name="tabset10" id="tab3-10" aria-controls="lc" checked>
    <label for="tab3-10">LC</label>
    <div class="tab-panel10s">
        <section id="marzen" class="tab-panel10" style="margin:0">
            <img src="/images/plots/u10_ac.svg" width="100%">
        </section>
        <section id="rauchbier" class="tab-panel10" style="margin:0">
            <img src="/images/plots/u10_lcnoap.svg" width="100%">
        </section>
        <section id="dunkles" class="tab-panel10" style="margin:0">
            <img src="/images/plots/u10_lc.svg" width="100%">
        </section>
    </div>
</div>

## User 11 
<style>
.tabset11 > input[type="radio"] { position: absolute; left: -200vw; }
.tabset11 .tab-panel11 { display: none; }
.tabset11 > input:first-child:checked ~ .tab-panel11s > .tab-panel11:first-child,
.tabset11 > input:nth-child(3):checked ~ .tab-panel11s > .tab-panel11:nth-child(2),
.tabset11 > input:nth-child(5):checked ~ .tab-panel11s > .tab-panel11:nth-child(3),
.tabset11 > input:nth-child(7):checked ~ .tab-panel11s > .tab-panel11:nth-child(4),
.tabset11 > input:nth-child(9):checked ~ .tab-panel11s > .tab-panel11:nth-child(5),
.tabset11 > input:nth-child(11):checked ~ .tab-panel11s > .tab-panel11:nth-child(6) { display: block; }
.tabset11 > label { position: relative; display: inline-block; padding: 15px 15px 25px; border: 1px solid transparent; border-bottom: 0; cursor: pointer; font-weight: 600; }
.tabset11 > label::after { content: ""; position: absolute; left: 15px; bottom: 10px; width: 22px; height: 4px; background: #8d8d8d; }
input:focus-visible + label { outline: 2px solid rgba(242,120,75,0.95); border-radius: 3px; }
.tabset11 > label:hover, .tabset11 > input:focus + label, .tabset11 > input:checked + label { color: rgba(242,120,75,0.95); }
.tabset11 > label:hover::after, .tabset11 > input:focus + label::after, .tabset11 > input:checked + label::after { background: rgba(242,120,75,0.95); }
.tabset11 > input:checked + label { border-color: black; border-width: 2px; border-bottom: 1px solid #fff; margin-bottom: -1px; }
.tab-panel11 { padding: 30px 0; border-top: 2px solid black; }
</style>
<table style="table-layout:fixed;width:100%;">
    <tr><th style="width:33.333%">AC</th><th style="width:33.333%">LC-noAP</th><th style="width:33.333%">LC</th></tr>
    <tr>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u11_ac.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u11_lcnoap.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u11_lc.webm" type="video/webm">
            </video>
        </td>
    </tr>
</table>
<div class="tabset11 table-wrap" style="">
    <input type="radio" name="tabset11" id="tab1-11" aria-controls="ac">
    <label for="tab1-11">AC</label>
    <input type="radio" name="tabset11" id="tab2-11" aria-controls="lcnoap">
    <label for="tab2-11">LC-noAP</label>
    <input type="radio" name="tabset11" id="tab3-11" aria-controls="lc" checked>
    <label for="tab3-11">LC</label>
    <div class="tab-panel11s">
        <section id="marzen" class="tab-panel11" style="margin:0">
            <img src="/images/plots/u11_ac.svg" width="100%">
        </section>
        <section id="rauchbier" class="tab-panel11" style="margin:0">
            <img src="/images/plots/u11_lcnoap.svg" width="100%">
        </section>
        <section id="dunkles" class="tab-panel11" style="margin:0">
            <img src="/images/plots/u11_lc.svg" width="100%">
        </section>
    </div>
</div>

## User 12 
<style>
.tabset12 > input[type="radio"] { position: absolute; left: -200vw; }
.tabset12 .tab-panel12 { display: none; }
.tabset12 > input:first-child:checked ~ .tab-panel12s > .tab-panel12:first-child,
.tabset12 > input:nth-child(3):checked ~ .tab-panel12s > .tab-panel12:nth-child(2),
.tabset12 > input:nth-child(5):checked ~ .tab-panel12s > .tab-panel12:nth-child(3),
.tabset12 > input:nth-child(7):checked ~ .tab-panel12s > .tab-panel12:nth-child(4),
.tabset12 > input:nth-child(9):checked ~ .tab-panel12s > .tab-panel12:nth-child(5),
.tabset12 > input:nth-child(11):checked ~ .tab-panel12s > .tab-panel12:nth-child(6) { display: block; }
.tabset12 > label { position: relative; display: inline-block; padding: 15px 15px 25px; border: 1px solid transparent; border-bottom: 0; cursor: pointer; font-weight: 600; }
.tabset12 > label::after { content: ""; position: absolute; left: 15px; bottom: 10px; width: 22px; height: 4px; background: #8d8d8d; }
input:focus-visible + label { outline: 2px solid rgba(242,120,75,0.95); border-radius: 3px; }
.tabset12 > label:hover, .tabset12 > input:focus + label, .tabset12 > input:checked + label { color: rgba(242,120,75,0.95); }
.tabset12 > label:hover::after, .tabset12 > input:focus + label::after, .tabset12 > input:checked + label::after { background: rgba(242,120,75,0.95); }
.tabset12 > input:checked + label { border-color: black; border-width: 2px; border-bottom: 1px solid #fff; margin-bottom: -1px; }
.tab-panel12 { padding: 30px 0; border-top: 2px solid black; }
</style>
<table style="table-layout:fixed;width:100%;">
    <tr><th style="width:33.333%">AC</th><th style="width:33.333%">LC-noAP</th><th style="width:33.333%">LC</th></tr>
    <tr>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u12_ac.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u12_lcnoap.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u12_lc.webm" type="video/webm">
            </video>
        </td>
    </tr>
</table>
<div class="tabset12 table-wrap" style="">
    <input type="radio" name="tabset12" id="tab1-12" aria-controls="ac">
    <label for="tab1-12">AC</label>
    <input type="radio" name="tabset12" id="tab2-12" aria-controls="lcnoap">
    <label for="tab2-12">LC-noAP</label>
    <input type="radio" name="tabset12" id="tab3-12" aria-controls="lc" checked>
    <label for="tab3-12">LC</label>
    <div class="tab-panel12s">
        <section id="marzen" class="tab-panel12" style="margin:0">
            <img src="/images/plots/u12_ac.svg" width="100%">
        </section>
        <section id="rauchbier" class="tab-panel12" style="margin:0">
            <img src="/images/plots/u12_lcnoap.svg" width="100%">
        </section>
        <section id="dunkles" class="tab-panel12" style="margin:0">
            <img src="/images/plots/u12_lc.svg" width="100%">
        </section>
    </div>
</div>
