"""
لائیو نیوز ٹی وی — Live News TV

"Urdu broadsheet" design: newsprint ground with grain, double rules,
square corners, ink type. Tap a channel → YouTube /live opens (one tap).
RTL, Nastaliq type, big tap targets.

Run:
    streamlit run streamlit_news_tv.py --server.port 8501 --server.address 0.0.0.0
Tablet: http://<computer-ip>:8501  (same Wi-Fi)
"""

from datetime import datetime
import streamlit as st

# ---------------------------------------------------------------------------
# چینلز (براہ راست YouTube /live links)
# ---------------------------------------------------------------------------
CHANNELS = [
    ("جیو نیوز",      "https://www.youtube.com/@geonews/live",                       "جیو"),
    ("اے آر وائی نیوز", "https://www.youtube.com/channel/UCMmpLL2ucRHAXbNHiCPyIyg/live", "اے آر وائی"),
    ("سما ٹی وی",     "https://www.youtube.com/@samaatvofficial/live",                "سما"),
    ("ڈان نیوز",      "https://www.youtube.com/channel/UCaxR-D8FjZ-2otbU0_Y2grg/live", "ڈان"),
    ("ایکسپریس نیوز", "https://www.youtube.com/channel/UCTur7oM6mLL0rM2k0znuZpQ/live", "ایکسپریس"),
    ("بول نیوز",      "https://www.youtube.com/@bolnewsofficial/live",                "بول"),
    ("دنیا نیوز",     "https://www.youtube.com/@dunyanewsofficial/live",              "دنیا"),
    ("ہم نیوز",       "https://www.youtube.com/@HUMNewsPakistan/live",                "ہم"),
    ("پبلک نیوز",     "https://www.youtube.com/@publicnewspk/live",                   "پبلک"),
]
NUM_CHANNELS = len(CHANNELS)
URDU_DIGITS = ["", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"]

URDU_WEEKDAYS = ["پیر", "منگل", "بدھ", "جمعرات", "جمعہ", "ہفتہ", "اتوار"]   # Mon..Sun
URDU_MONTHS = ["جنوری", "فروری", "مارچ", "اپریل", "مئی", "جون", "جولائی",
               "اگست", "ستمبر", "اکتوبر", "نومبر", "دسمبر"]


def urdu_digits(n: int) -> str:
    return "".join(URDU_DIGITS[int(d)] for d in str(n))


def urdu_date() -> str:
    now = datetime.now()
    return f"{URDU_WEEKDAYS[now.weekday()]}، {urdu_digits(now.day)} {URDU_MONTHS[now.month - 1]} {urdu_digits(now.year)}"


st.set_page_config(
    page_title="لائیو نیوز ٹی وی",
    page_icon="📺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.html("""
<style>
@font-face{ font-family:'Noto Nastaliq Urdu'; font-weight:400; font-style:normal; font-display:swap; src:url('app/static/urdu-400.ttf') format('truetype'); }
@font-face{ font-family:'Noto Nastaliq Urdu'; font-weight:700; font-style:normal; font-display:swap; src:url('app/static/urdu-700.ttf') format('truetype'); }
:root{
    --paper:#F5F1E6;
    --paper-2:#EFEAD9;
    --ink:#1F1F1B;
    --muted:#57534A;
    --red:#C0392B;
    --rule:#1F1F1B;
    --rule-soft:#C9C4B2;
}
.block-container{
    max-width:920px;
    padding:0 1.4rem 2rem 1.4rem;
    direction:rtl;
    text-align:right;
    background-color:var(--paper);
    background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='140' height='140'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='140' height='140' filter='url(%23n)' opacity='0.05'/%3E%3C/svg%3E");
}
html, body, .stMarkdown, p, div, span, a, button, label{
    font-family:'Noto Nastaliq Urdu', serif !important;
    direction:rtl;
}
#MainMenu, footer, header{ visibility:hidden; }

/* ══ masthead — newspaper nameplate ══════════════════════ */
.masthead{
    border-top:1px solid var(--rule);
    border-bottom:3px double var(--rule);
    padding:.55rem .2rem .7rem;
    margin:.35rem 0 .9rem;
}
.masthead .top-row{
    display:flex; justify-content:space-between; align-items:baseline;
    font-size:1.05rem; color:var(--muted); padding:0 .2rem .35rem;
    border-bottom:1px solid var(--rule-soft); margin-bottom:.5rem;
}
.masthead h1.nameplate{
    font-family:'Noto Nastaliq Urdu', serif !important;
    font-size:3.4rem; font-weight:700; color:var(--ink);
    text-align:center; line-height:1.9; margin:0;
    letter-spacing:0;
}
.masthead .tagline{
    text-align:center; font-size:1.15rem; color:var(--muted);
    line-height:2; margin-top:.1rem;
}
.live-flag{
    display:inline-flex; align-items:center; gap:.4rem;
    color:var(--red); font-weight:700;
}
.live-dot{
    width:.75rem; height:.75rem; border-radius:50%;
    background:var(--red); display:inline-block;
    animation:pulse 1.6s ease-in-out infinite;
}
@keyframes pulse{
    0%,100%{ box-shadow:0 0 0 0 rgba(192,57,43,.5); }
    50%{ box-shadow:0 0 0 .35rem rgba(192,57,43,.15); }
}
@media (prefers-reduced-motion: reduce){ .live-dot{ animation:none; } }

/* ══ headline — today's channel ══════════════════════════ */
.hero{
    padding:.2rem .2rem .9rem;
    border-bottom:3px double var(--rule);
    margin-bottom:1.1rem;
}
.hero .kicker{
    color:var(--red); font-size:1.15rem; font-weight:700;
    letter-spacing:0; line-height:2;
}
.hero h1{
    font-family:'Noto Nastaliq Urdu', serif !important;
    font-size:3.6rem; font-weight:700; color:var(--ink);
    line-height:2; margin:.1rem 0 .15rem;
}
.hero .sub{
    display:flex; align-items:center; gap:.8rem;
    font-size:1.2rem; color:var(--muted);
}
.hero .sub .no-badge{
    border:1.5px solid var(--ink); color:var(--ink);
    font-size:1.05rem; font-weight:700; padding:0 .5rem;
    border-radius:2px; line-height:1.9;
}

/* ══ the one bold action — a red insert ═════════════════ */
.live-btn, .live-btn:visited{
    display:block; text-align:center; text-decoration:none;
    color:#F5F1E6 !important; background:var(--red);
    font-size:1.9rem; font-weight:700; line-height:2.2;
    padding:.85rem 1rem; border-radius:3px;
    border:none;
    box-shadow:0 .35rem 0 #8E2418;
    margin:.3rem 0 1.3rem;
    touch-action:manipulation; user-select:none;
    transition:transform .12s ease, box-shadow .12s ease;
}
.live-btn:hover{ background:#A93226; }
.live-btn:active{ transform:translateY(.2rem); box-shadow:0 .15rem 0 #8E2418; }
.live-btn:focus-visible{ outline:3px solid var(--ink); outline-offset:3px; }

/* ══ quiet remote — telegraph-style keys ═════════════════ */
.stButton > button{
    width:100%;
    font-size:1.3rem !important; font-weight:600 !important; line-height:2.2;
    padding:.35rem .4rem !important;
    background:transparent !important; color:var(--ink) !important;
    border:1px solid var(--rule-soft) !important; border-radius:3px !important;
    box-shadow:none !important;
}
.stButton > button:hover{ background:var(--paper-2) !important; border-color:var(--ink) !important; }
.stButton > button:focus-visible{ outline:3px solid var(--ink) !important; outline-offset:2px; }

/* ══ channel guide — TV listings page ═════════════════════ */
.guide{
    border-top:1px solid var(--rule);
    border-bottom:1px solid var(--rule);
    padding:.35rem 0;
}
.guide a, .guide a:visited{
    display:flex; align-items:baseline; gap:1.1rem;
    padding:.62rem .35rem; text-decoration:none !important;
    border-bottom:1px dotted var(--rule-soft);
    color:var(--ink) !important;
}
.guide a:last-child{ border-bottom:none; }
.guide a:hover{ background:var(--paper-2); }
.guide a:focus-visible{ outline:3px solid var(--ink); outline-offset:-3px; }
.guide .no{ font-size:1.4rem; color:var(--muted); min-width:2.2rem; font-weight:700; }
.guide .nm{ font-size:1.7rem; font-weight:600; line-height:2.1; }
.guide a.current .nm{ color:var(--red); }
.guide a.current .no{ color:var(--red); }
.guide a.current .no::after{ content:" ●"; font-size:.9rem; }

/* ══ voice mode ═════════════════════════════════════════ */
.voice-bar{
    border:1.5px solid var(--ink);
    background:var(--paper-2);
    border-radius:3px;
    padding:.7rem .9rem;
    margin:0 0 1.1rem;
}
.voice-bar .voice-title{
    font-size:1.5rem; font-weight:700; color:var(--ink); line-height:2;
}
.voice-bar .voice-status{
    font-size:1.35rem; color:var(--muted); line-height:2; min-height:2em;
}
.voice-bar .voice-hint{
    font-size:1rem; color:var(--muted); line-height:2;
}
.mic-on-btn{
    display:block; width:100%; text-align:center; cursor:pointer;
    font-family:'Noto Nastaliq Urdu', serif;
    font-size:1.6rem; font-weight:700; line-height:2.2;
    color:#F5F1E6; background:var(--ink);
    border:none; border-radius:3px; padding:.6rem .8rem;
    margin:.35rem 0 .2rem;
    touch-action:manipulation;
}
.mic-on-btn:active{ background:var(--green); }

@media (max-width: 640px){
    .masthead h1.nameplate{ font-size:2.3rem; }
    .hero h1{ font-size:2.3rem; }
    .live-btn{ font-size:1.5rem; }
    .guide .nm{ font-size:1.4rem; }
}
</style>
""")

# ---------------------------------------------------------------------------
# حالت
# ---------------------------------------------------------------------------
if "power" not in st.session_state:
    st.session_state.power = True
if "ch_idx" not in st.session_state:
    st.session_state.ch_idx = 0
if "voice" not in st.session_state:
    st.session_state.voice = False

name, live_url, short = CHANNELS[st.session_state.ch_idx]

# ---------- masthead — newspaper nameplate ----------
st.html(f"""
<div class="masthead">
    <div class="top-row">
        <span>{urdu_date()}</span>
        <span class="live-flag"><span class="live-dot"></span> براہ راست</span>
    </div>
    <h1 class="nameplate">پاکستان لائیو</h1>
    <div class="tagline">ہر خبر، زندہ نشریات</div>
</div>
""")

if not st.session_state.power:
    st.html(
        """
        <div class="hero" style="text-align:center; padding:2.5rem .4rem;">
            <h1 style="color:#57534A;">بند ہے</h1>
            <p style="font-size:1.4rem;color:#57534A;">نیچے پاور دباएं</p>
        </div>
        """
    )
    if st.button("⏻ پاور", key="power_only"):
        st.session_state.power = True
        st.rerun()
    st.stop()

# ---------- headline — the channel on air ----------
st.html(f"""
<div class="hero">
    <div class="kicker">آج کی نشریات</div>
    <h1>{name}</h1>
    <div class="sub">
        <span class="no-badge">چینل {urdu_digits(st.session_state.ch_idx+1)}</span>
        <span>اس وقت براہ راست دکھائی جا رہا ہے</span>
    </div>
</div>
""")

# ---------- the one bold action ----------
st.html(
    f'<a class="live-btn" href="{live_url}" target="_blank" rel="noopener noreferrer">▶ ابھی دیکھیں</a>'
)

# ---------- quiet remote ----------
r1, r2, r3 = st.columns(3)
with r1:
    if st.button("⏻ پاور", key="remote_power"):
        st.session_state.power = False
        st.rerun()
with r2:
    if st.button("اگلا چینل", key="remote_ch_up"):
        st.session_state.ch_idx = (st.session_state.ch_idx + 1) % NUM_CHANNELS
        st.rerun()
with r3:
    if st.button("پچھلا چینل", key="remote_ch_down"):
        st.session_state.ch_idx = (st.session_state.ch_idx - 1) % NUM_CHANNELS
        st.rerun()

st.html("<div style='height:10px'></div>")

# ---------- voice mode — trigger word "ٹی وی" / "channel" + channel name ----------
v1, v2 = st.columns([1, 3])
with v1:
    if st.button("🎤 آواز" + ("  ✕" if st.session_state.voice else "  آن"), key="voice_toggle"):
        st.session_state.voice = not st.session_state.voice
        st.rerun()

if st.session_state.voice:
    st.html("""
<div class="voice-bar">
    <div class="voice-title">🎤 آواز فعال ہے</div>
    <div class="voice-status" id="voiceStatus">مائیکروفون آن کرنے کے لیے نیچے دبائیں</div>
    <button class="mic-on-btn" id="micStartBtn">مائیکروفون آن کریں</button>
    <div class="voice-hint">بولنے کا طریقہ: <b>ٹی وی جیو</b> · <b>ٹی وی اے آر وائی</b> · <b>ٹی وی سما</b> · <b>ٹی وی ڈان</b> · <b>ٹی وی دنیا</b></div>
</div>
<script>
(function(){
    // stop any previous listener first
    if (window.__voiceRec) { try { window.__voiceRec.stop(); } catch(e){} window.__voiceRec = null; }

    var statusEl = document.getElementById('voiceStatus');
    var startBtn = document.getElementById('micStartBtn');
    if (!statusEl || !startBtn) return;
    var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SR) {
        statusEl.textContent = 'یہ براؤزر آواز کی شناخت سپورٹ نہیں کرتا (Chrome استعمال کریں)';
        startBtn.style.display = 'none';
        return;
    }

    var CHANNELS = [
        { keys: ['جیو', 'geo'],                 url: 'https://www.youtube.com/@geonews/live',                       name: 'جیو نیوز' },
        { keys: ['اے آر وائی', 'اے آر ى', 'ary'], url: 'https://www.youtube.com/channel/UCMmpLL2ucRHAXbNHiCPyIyg/live', name: 'اے آر وائی نیوز' },
        { keys: ['سما', 'samaa', 'sama'],        url: 'https://www.youtube.com/@samaatvofficial/live',                name: 'سما ٹی وی' },
        { keys: ['ڈان', 'dawn'],                 url: 'https://www.youtube.com/channel/UCaxR-D8FjZ-2otbU0_Y2grg/live', name: 'ڈان نیوز' },
        { keys: ['ایکسپریس', 'express'],         url: 'https://www.youtube.com/channel/UCTur7oM6mLL0rM2k0znuZpQ/live', name: 'ایکسپریس نیوز' },
        { keys: ['بول', 'bol'],                  url: 'https://www.youtube.com/@bolnewsofficial/live',                name: 'بول نیوز' },
        { keys: ['دنیا', 'dunya', 'duniya'],     url: 'https://www.youtube.com/@dunyanewsofficial/live',              name: 'دنیا نیوز' },
        { keys: ['ہم', 'hum'],                   url: 'https://www.youtube.com/@HUMNewsPakistan/live',                name: 'ہم نیوز' },
        { keys: ['پبلک', 'public'],              url: 'https://www.youtube.com/@publicnewspk/live',                   name: 'پبلک نیوز' }
    ];
    var TRIGGERS = ['ٹی وی', 'tv', 'چینل', 'channel', 'ٹیوی'];

    function findChannel(text) {
        var t = text.toLowerCase();
        for (var i = 0; i < CHANNELS.length; i++) {
            var keys = CHANNELS[i].keys;
            for (var j = 0; j < keys.length; j++) {
                if (t.indexOf(keys[j].toLowerCase()) !== -1) return CHANNELS[i];
            }
        }
        return null;
    }
    function hasTrigger(text) {
        var t = text.toLowerCase();
        for (var i = 0; i < TRIGGERS.length; i++) {
            if (t.indexOf(TRIGGERS[i].toLowerCase()) !== -1) return true;
        }
        return false;
    }

    var rec = new SR();
    window.__voiceRec = rec;
    rec.lang = 'ur-PK';
    rec.continuous = true;
    rec.interimResults = false;
    rec.maxAlternatives = 2;

    rec.onstart = function() { statusEl.textContent = 'سن رہا ہوں… بولیں: ٹی وی جیو'; };
    rec.onresult = function(event) {
        for (var i = event.resultIndex; i < event.results.length; i++) {
            var result = event.results[i];
            if (!result.isFinal) continue;
            for (var alt = 0; alt < result.length; alt++) {
                var said = result[alt].transcript.trim();
                var lower = said.toLowerCase();
                var ch = findChannel(lower);
                if (ch) {
                    statusEl.textContent = ch.name + ' کھول رہا ہوں…';
                    window.location.href = ch.url;
                    return;
                }
            }
            statusEl.textContent = 'سنا: "' + said + '" — چینل سمجھ نہیں آیا';
        }
    };
    var fatal = false;
    var FATAL = ['not-allowed','service-not-allowed','language-not-supported','network','audio-capture'];

    rec.onerror = function(event) {
        var e = event.error;
        var msg = {
            'not-allowed': 'مائیکروفون کی اجازت نہیں دی گئی — براؤزر سیٹنگز میں اجازت دیں',
            'service-not-allowed': 'آواز کی شناخت کی سروس بلاک ہے (انٹرنیٹ یا گوگل سروس)',
            'language-not-supported': 'یہ براؤزر اردو آواز سپورٹ نہیں کرتا',
            'network': 'گوگل سروس تک رابطہ نہیں — انٹرنیٹ چیک کریں (یا آف لائن موڈ چاہیے)',
            'audio-capture': 'مائیکروفون نہیں ملا — کوئی اور ایپ استعمال کر رہی ہے؟',
            'no-speech': 'کچھ سنائی نہیں دیا…'
        }[e] || ('خرابی: ' + e);
        statusEl.textContent = msg;
        if (FATAL.indexOf(e) !== -1) {
            fatal = true;
            startBtn.style.display = 'block';
            startBtn.textContent = 'دوبارہ کوشش کریں';
            try { rec.stop(); } catch (_e) {}
        }
    };
    rec.onend = function() {
        if (fatal) return;
        setTimeout(function() { try { rec.start(); } catch (e) {} }, 500);
    };

    startBtn.addEventListener('click', function() {
        fatal = false;
        try {
            rec.start();
            startBtn.style.display = 'none';
            statusEl.textContent = 'سن رہا ہوں… بولیں: ٹی وی جیو';
        } catch (e) {
            statusEl.textContent = 'مائیکروفون شروع نہیں ہو سکا — صفحہ ری فریش کریں';
        }
    });
})();
</script>
""", unsafe_allow_javascript=True)
else:
    st.html("""
<script>
    if (window.__voiceRec) { try { window.__voiceRec.stop(); } catch(e){} window.__voiceRec = null; }
</script>
""", unsafe_allow_javascript=True)

# ---------- channel guide — TV listings page ----------
rows = []
for i, (ch_name, ch_url, _short) in enumerate(CHANNELS):
    cur = " current" if i == st.session_state.ch_idx else ""
    rows.append(
        f'<a class="guide-row{cur}" href="{ch_url}" target="_blank" rel="noopener noreferrer">'
        f'<span class="no">{urdu_digits(i+1)}</span>'
        f'<span class="nm">{ch_name}</span>'
        f'</a>'
    )
st.html('<div class="guide">' + "".join(rows) + "</div>")
