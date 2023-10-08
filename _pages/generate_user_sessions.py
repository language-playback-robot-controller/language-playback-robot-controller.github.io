TEMPLATE = """
## User {N} 
<style>
.tabset > input[type="radio"] { position: absolute; left: -200vw; }
.tabset .tab-panel { display: none; }
.tabset > input:first-child:checked ~ .tab-panels > .tab-panel:first-child,
.tabset > input:nth-child(3):checked ~ .tab-panels > .tab-panel:nth-child(2),
.tabset > input:nth-child(5):checked ~ .tab-panels > .tab-panel:nth-child(3),
.tabset > input:nth-child(7):checked ~ .tab-panels > .tab-panel:nth-child(4),
.tabset > input:nth-child(9):checked ~ .tab-panels > .tab-panel:nth-child(5),
.tabset > input:nth-child(11):checked ~ .tab-panels > .tab-panel:nth-child(6) { display: block; }
.tabset > label { position: relative; display: inline-block; padding: 15px 15px 25px; border: 1px solid transparent; border-bottom: 0; cursor: pointer; font-weight: 600; }
.tabset > label::after { content: ""; position: absolute; left: 15px; bottom: 10px; width: 22px; height: 4px; background: #8d8d8d; }
input:focus-visible + label { outline: 2px solid rgba(242,120,75,0.95); border-radius: 3px; }
.tabset > label:hover, .tabset > input:focus + label, .tabset > input:checked + label { color: rgba(242,120,75,0.95); }
.tabset > label:hover::after, .tabset > input:focus + label::after, .tabset > input:checked + label::after { background: rgba(242,120,75,0.95); }
.tabset > input:checked + label { border-color: black; border-width: 2px; border-bottom: 1px solid #fff; margin-bottom: -1px; }
.tab-panel { padding: 30px 0; border-top: 2px solid black; }
</style>
<table style="table-layout:fixed;width:100%;">
    <tr><th style="width:33.333%">AC</th><th style="width:33.333%">LC-noAP</th><th style="width:33.333%">LC</th></tr>
    <tr>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u{N}_ac.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u{N}_lcnoap.webm" type="video/webm">
            </video>
        </td>
        <td>
            <video class="video-js" style="display:block;width:100%;height:fit-content;" controls preload="auto">
                <source src="/videos/user_sessions/u{N}_lc.webm" type="video/webm">
            </video>
        </td>
    </tr>
</table>
<div class="tabset table-wrap" style="">
    <input type="radio" name="tabset" id="tab1" aria-controls="ac">
    <label for="tab1">AC</label>
    <input type="radio" name="tabset" id="tab2" aria-controls="lcnoap">
    <label for="tab2">LC-noAP</label>
    <input type="radio" name="tabset" id="tab3" aria-controls="lc" checked>
    <label for="tab3">LC</label>
    <div class="tab-panels">
        <section id="marzen" class="tab-panel" style="margin:0">
            <img src="/images/plots/u{N}_ac.svg" width="100%">
        </section>
        <section id="rauchbier" class="tab-panel" style="margin:0">
            <img src="/images/plots/u{N}_lcnoap.svg" width="100%">
        </section>
        <section id="dunkles" class="tab-panel" style="margin:0">
            <img src="/images/plots/u{N}_lc.svg" width="100%">
        </section>
    </div>
</div>
"""


def format_template(user_num):
    return (
        TEMPLATE.replace("{N}", str(user_num))
        .replace("tabset", f"tabset{user_num}")
        .replace("tab-panel", f"tab-panel{user_num}")
        .replace("tab1", f"tab1-{user_num}")
        .replace("tab2", f"tab2-{user_num}")
        .replace("tab3", f"tab3-{user_num}")
    )


def main():
    with open("user-sessions.md", "r") as f:
        content = f.readlines()
        for i, line in enumerate(content):
            if line.strip() == "<!-- GENERATED -->":
                content = content[: i + 1]
                break
    with open("user-sessions.md", "w") as f:
        for line in content:
            f.write(line)
        for user_num in range(1, 13):
            f.write(format_template(user_num))


if __name__ == "__main__":
    main()
