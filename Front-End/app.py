import streamlit as st
import pandas as pd
import joblib
import time

# --- 1. PREMIUM COHESIVE DARK ESPRESSO CONFIG ---
st.set_page_config(layout="wide", page_title="SentryCart - Behavioral AI Sandbox")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght=400;500;600;700&display=swap');
    
    /* 🚀 THE FIXED CANVAS TRICK: Force all Streamlit background layers to use your espresso color */
    html, body, 
    [data-testid="stAppViewContainer"], 
    [data-testid="stMain"], 
    [data-testid="stMainBlockContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #1a1512 !important; /* Rich Dark Espresso Canvas */
        color: #f4efe9 !important;             /* Crisp Soft White/Cream Text */
    }
    
    /* Remove Header Fragment Seamlessly */
    header[data-testid="stHeader"] {
        background: transparent !important;
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }
    
    /* Unified Card Architecture - Connected Rich Brown Depth */
    div[data-testid="stVerticalBlock"] > div:has(div.element-container) {
        background-color: #261f1a !important;  /* Warm Coffee/Obsidian Card Base */
        border: 1px solid #3d322a !important;  /* Seamless Blended Dark Earth Edge */
        border-radius: 16px !important;
        padding: 20px !important;
        box-shadow: 0 4px 25px rgba(0, 0, 0, 0.4) !important;
        transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease !important;
    }
    
    /* Smooth Pop on Hover */
    div[data-testid="stVerticalBlock"] > div:has(div.element-container):hover {
        transform: translateY(-2px) !important;
        border-color: #54453a !important;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6) !important;
    }
    
    /* DEFINITIVE HIGH-LEGIBILITY GLOW BUTTONS */
    .stButton>button {
        background-color: #c89d7c !important; /* Radiant Burnished Gold/Almond */
        color: #161412 !important;            /* Pure Crisp Deep Dark Text Always */
        border: 1px solid #c89d7c !important;
        border-radius: 10px !important;
        padding: 12px 28px !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        letter-spacing: 0.2px !important;
        width: 100% !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 10px rgba(200, 157, 124, 0.15) !important;
    }
    
    /* Fluid Transition to Hover State */
    .stButton>button:hover {
        background-color: #d7b599 !important; /* Lighter Shimmer Cream-Gold */
        color: #161412 !important;            /* Strictly Keep Text Dark */
        border-color: #d7b599 !important;
        box-shadow: 0 6px 20px rgba(200, 157, 124, 0.3) !important;
    }
    
    .stButton>button:active {
        background-color: #b08564 !important;
        color: #161412 !important;
        transform: translateY(1px) !important;
    }
    
    /* Elegant Dark Typographical Layouts */
    .brand-accent {
        text-align: center !important;
        color: #c89d7c;
        font-weight: 700;
        letter-spacing: 2px;
        font-size: 0.8rem;
        text-transform: uppercase;
        margin-bottom: 4px;
        display: block;
        width: 100%;
    }
    
    .main-title {
        text-align: center !important;
        font-family: 'Playfair Display', Garamond, serif;
        font-weight: 700;
        font-size: 3rem;
        color: #ffffff;
        line-height: 1.15;
        margin-bottom: 12px;
        display: block;
        width: 100%;
    }
    
    .subtitle {
        text-align: center !important;
        color: #baae141a !important;
        color: #a69a90 !important;
        font-size: 1.1rem;
        max-width: 750px;
        margin: 0 auto 40px auto !important;
        line-height: 1.5;
        display: block !important;
        width: 100%;
    }
    
    /* Interconnected Dark Mode Custom Badges */
    .pill-wrapper {
        display: flex;
        gap: 8px;
        margin-top: 10px;
        margin-bottom: 15px;
    }
    .badge-blue {
        background-color: #1e293b;
        color: #60a5fa;
        padding: 5px 12px;
        border-radius: 30px;
        font-size: 0.8rem;
        font-weight: 600;
        border: 1px solid #334155;
    }
    .badge-red {
        background-color: #311515;
        color: #f87171;
        padding: 5px 12px;
        border-radius: 30px;
        font-size: 0.8rem;
        font-weight: 600;
        border: 1px solid #4c1d1d;
    }
    
    /* Polished Code Elements */
    .stCodeBlock, div[data-testid="stMarkdownContainer"] pre {
        background-color: #171310 !important;
        border: 1px solid #3d322a !important;
        border-radius: 10px !important;
    }
    
    /* Connected High-Fidelity Notification Panels */
    .verdict-card {
        padding: 30px;
        border-radius: 16px;
        margin-bottom: 25px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    }
    .verdict-approved {
        background: linear-gradient(145deg, #064e3b 0%, #022c22 100%);
        border: 1px solid #047857;
        color: #34d399;
    }
    .verdict-blocked {
        background: linear-gradient(145deg, #7f1d1d 0%, #450a0a 100%);
        border: 1px solid #b91c1c;
        color: #f87171;
    }
    
    .panel-stat {
        background-color: #1e1713;
        border: 1px solid #3d322a;
        border-radius: 12px;
        padding: 16px;
        text-align: center;
    }
    
    /* Clean Info Card styling */
    .info-card {
        background-color: #1e1713;
        border: 1px solid #3d322a;
        border-radius: 12px;
        padding: 20px;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. SECURE BACKEND WEIGHT LOADER ---
@st.cache_resource
def load_security_model():
    try:
        return joblib.load('Front-End/security_model.pkl')
    except FileNotFoundError:
        st.error("⚠️ 'security_model.pkl' model file missing. Please place your trained model weights in this project folder.")
        return None

model = load_security_model()

# --- 3. SESSION LOGISTICS SYSTEM ---
if 'stage' not in st.session_state:
    st.session_state.stage = 'welcome'
if 'clicks' not in st.session_state:
    st.session_state.clicks = 0
if 'spend' not in st.session_state:
    st.session_state.spend = 0.0
if 'failed_login' not in st.session_state:
    st.session_state.failed_login = 0
if 'distance_km' not in st.session_state:
    st.session_state.distance_km = 0.0
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'cart_inventory' not in st.session_state:
    st.session_state.cart_inventory = {}
if 'bot_executed' not in st.session_state:
    st.session_state.bot_executed = False
if 'selected_product' not in st.session_state:
    st.session_state.selected_product = None

def reset_sandbox():
    st.session_state.stage = 'welcome'
    st.session_state.clicks = 0
    st.session_state.spend = 0.0
    st.session_state.failed_login = 0
    st.session_state.distance_km = 0.0
    st.session_state.start_time = None
    st.session_state.cart_inventory = {}
    st.session_state.bot_executed = False
    st.session_state.selected_product = None
    if 'current_bot_logs' in st.session_state:
        del st.session_state.current_bot_logs

# ALL STORE ITEMS DEFINITIONS
catalog_items = [
    {
        "id": "items_1", 
        "name": "🎧 Wireless Premium Earbuds", 
        "price": 59.00, 
        "desc": "High-fidelity acoustics with smart background noise isolation layers.", 
        "long_desc": "Experience unparalleled acoustic depth featuring custom engineered drivers. Includes advanced hybrid sound isolation design and long-lasting rapid charge power modules designed to last through 30+ hours of continuous workspace activity.",
        "img": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=500&auto=format&fit=crop"
    },
    {
        "id": "items_2", 
        "name": "🎒 Urban Minimalist Backpack", 
        "price": 45.00, 
        "desc": "Weather-proof protective canvas tailored for your tech hardware.", 
        "long_desc": "Engineered for daily use. Constructed out of premium water-resistant custom woven fabric. Features hidden security storage compartments, built-in structural charging loops, and a heavily padded shock absorbing frame that supports laptops up to 16 inches securely.",
        "img": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=500&auto=format&fit=crop"
    },
    {
        "id": "items_3", 
        "name": "⌨️ Sleek Mechanical Keyboard", 
        "price": 79.00, 
        "desc": "Compact aesthetic design with crisp tactile feedback profiles.", 
        "long_desc": "A premium mechanical typing peripheral that features premium hot-swappable switches. Protected by an aluminum space frame design with fully customizable soft warm ambient lighting options. Connects effortlessly across multiple devices.",
        "img": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=500&auto=format&fit=crop"
    },
    {
        "id": "items_4", 
        "name": "☕ Vacuum Insulated Flask", 
        "price": 24.00, 
        "desc": "Double-walled thermal steel built for long temperature retention.", 
        "long_desc": "Forged from industrial grade kitchen stainless steel alloy. Uses a deep vacuum physical layer between structural walls to completely stop outside air transfer, preserving ice cold liquids for 24 hours or steaming hot drinks for up to 12 hours cleanly.",
        "img": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=500&auto=format&fit=crop"
    }
]

# --- ROUTER VIEW 1: GATEWAY WELCOME SCREEN ---
if st.session_state.stage == 'welcome':
    st.markdown("<p class='brand-accent'>Behavioral AI Protection System</p>", unsafe_allow_html=True)
    st.markdown("<h1 class='main-title'>SentryCart AI Sandbox</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Test how a machine learning model automatically tells the difference between natural human buyers and high-speed automated checkout scripts in real-time.</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        with st.container():
            st.markdown("<p style='color:#c89d7c; font-size:0.75rem; font-weight:700; letter-spacing:1px;'>METHOD A</p>", unsafe_allow_html=True)
            st.markdown("### 🧑‍💼 Natural Human Path")
            st.markdown("<p style='color:#a69a90; min-height:50px;'>Browse items naturally. The AI evaluates your page clicks, cart timing, and browsing rhythms to verify you are a person.</p>", unsafe_allow_html=True)
            st.markdown("<div class='pill-wrapper'><span class='badge-blue'>🖱️ Human Speed Tracked</span><span class='badge-blue'>⏱️ Organic Timing</span></div>", unsafe_allow_html=True)
            if st.button("Shop as a human"):
                st.session_state.stage = 'human_store'
                st.session_state.start_time = time.time()
                st.rerun()
                
    with col2:
        with st.container():
            st.markdown("<p style='color:#c89d7c; font-size:0.75rem; font-weight:700; letter-spacing:1px;'>METHOD B</p>", unsafe_allow_html=True)
            st.markdown("### 🤖 Automated Script Path")
            st.markdown("<p style='color:#a69a90; min-height:50px;'>Launch an automated script simulation to quickly reserve heavy inventory items and bypass normal checkout steps.</p>", unsafe_allow_html=True)
            st.markdown("<div class='pill-wrapper'><span class='badge-red'>⚡ High Action Speed</span><span class='badge-red'>🔀 Automated Testing</span></div>", unsafe_allow_html=True)
            if st.button("Simulate a bot"):
                st.session_state.stage = 'bot_terminal'
                st.session_state.bot_executed = False
                st.rerun()

    # DEMO INFORMATION CARD REGARDING TRAINING RULES
    st.markdown("<br><br>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<h4 style='color:#c89d7c; font-family: Playfair Display, serif;'>💡 Demo Context: How This AI Model Detects Behavior</h4>", unsafe_allow_html=True)
        st.markdown("<p style='color:#a69a90; font-size:0.95rem;'><i>Note for reviewers: For this live demonstration setup, the AI model evaluates patterns based on the baseline behaviors listed below. In a real deployment, these target limits and evaluation rules can be completely changed and customized to fit any different business metrics or security purposes:</i></p>", unsafe_allow_html=True)
        
        tc1, tc2, tc3 = st.columns(3, gap="medium")
        with tc1:
            st.markdown("""
            <div class='info-card'>
                <p style='color:white; font-weight:700; margin:0;'>💰 Shopping Cost Profile</p>
                <p style='color:#a69a90; font-size:0.85rem; margin-top:8px;'>
                    <b>Normal Shopper:</b> Usually stays well under a <b>$200.00</b> budget footprint.<br>
                    <b>Automated Script:</b> Immediately requests bulk orders of <b>$2,850.00</b>.
                </p>
            </div>
            """, unsafe_allow_html=True)
        with tc2:
            st.markdown("""
            <div class='info-card'>
                <p style='color:white; font-weight:700; margin:0;'>🖱️ Interaction Velocity</p>
                <p style='color:#a69a90; font-size:0.85rem; margin-top:8px;'>
                    <b>Normal Shopper:</b> Clicks and reads pages comfortably under <b>35 actions/min</b>.<br>
                    <b>Automated Script:</b> Spikes intensely to frequencies of <b>450 actions/min</b>.
                </p>
            </div>
            """, unsafe_allow_html=True)
        with tc3:
            st.markdown("""
            <div class='info-card'>
                <p style='color:white; font-weight:700; margin:0;'>⏱️ Process Latency (Time taken)</p>
                <p style='color:#a69a90; font-size:0.85rem; margin-top:8px;'>
                    <b>Normal Shopper:</b> Needs time to review items, taking <b>over 5 seconds</b>.<br>
                    <b>Automated Script:</b> Fires checkout requests instantly inside <b>0.8 seconds</b>.
                </p>
            </div>
            """, unsafe_allow_html=True)

# --- ROUTER VIEW 2A: SHOP PATHWAY (STORE GALLERY AND DEDICATED DETAIL PAGES) ---
elif st.session_state.stage == 'human_store':
    st.markdown("<p class='brand-accent'>SentryCart Showcase</p>", unsafe_allow_html=True)
    
    # 2A.1 BRAND NEW PRODUCT DETAILS SUB-PAGE WORKSPACE
    if st.session_state.selected_product is not None:
        selected_id = st.session_state.selected_product
        product = next((item for item in catalog_items if item["id"] == selected_id), None)
        
        if product:
            if st.button("← Return to Shop Gallery"):
                st.session_state.selected_product = None
                st.rerun()
                
            st.markdown("<br>", unsafe_allow_html=True)
            with st.container():
                det_col1, det_col2 = st.columns([1.5, 2], gap="large")
                with det_col1:
                    st.image(product["img"], use_container_width=True)
                with det_col2:
                    st.markdown(f"<h2 style='color:white; margin:0;'>{product['name']}</h2>", unsafe_allow_html=True)
                    st.markdown(f"<p style='font-size:1.4rem; font-weight:700; color:#c89d7c; margin-top:10px;'>${product['price']:.2f}</p>", unsafe_allow_html=True)
                    st.markdown("<hr style='border-top:1px solid #3d322a;'>", unsafe_allow_html=True)
                    st.markdown(f"<p style='color:#f4efe9; line-height:1.6; font-size:1.05rem;'>{product['long_desc']}</p>", unsafe_allow_html=True)
                    st.markdown("<br><br>", unsafe_allow_html=True)
                    
                    if st.button("🛒 Add Product to Cart", key=f"det_add_{product['id']}", use_container_width=True):
                        st.session_state.clicks += 1
                        st.session_state.spend += product["price"]
                        st.session_state.cart_inventory[product["name"]] = st.session_state.cart_inventory.get(product["name"], 0) + 1
                        st.toast(f"Added {product['name']} to your active shopping cart.")
                        
    # 2A.2 MAIN SHOP LAUNCH GRID
    else:
        st.markdown("<h2 style='font-family: Playfair Display, serif; font-weight:700; margin-top:0; color:white;'>Available Store Inventory</h2>", unsafe_allow_html=True)
        catalog_col, cart_col = st.columns([2.6, 1.4], gap="large")
        
        with catalog_col:
            for item in catalog_items:
                with st.container():
                    c_img, c_desc = st.columns([1, 2.8])
                    c_img.image(item["img"], use_container_width=True)
                    c_desc.markdown(f"<h4 style='margin:0; font-weight:600; color:white;'>{item['name']}</h4>", unsafe_allow_html=True)
                    c_desc.markdown(f"<p style='color:#a69a90; font-size:0.9rem; margin:6px 0;'>{item['desc']}</p>", unsafe_allow_html=True)
                    c_desc.markdown(f"<p style='font-size:1.1rem; font-weight:700; margin-bottom:12px; color:#c89d7c;'>${item['price']:.2f}</p>", unsafe_allow_html=True)
                    
                    b1, b2 = c_desc.columns(2)
                    if b1.button("Product Details", key=f"v_{item['id']}", use_container_width=True):
                        st.session_state.clicks += 1
                        st.session_state.selected_product = item["id"]
                        st.rerun()
                    if b2.button("Add to Cart", key=f"a_{item['id']}", use_container_width=True):
                        st.session_state.clicks += 1
                        st.session_state.spend += item["price"]
                        st.session_state.cart_inventory[item["name"]] = st.session_state.cart_inventory.get(item["name"], 0) + 1
                        st.toast(f"Added {item['name']} to your active shopping cart.")

        with cart_col:
            with st.container():
                st.markdown("<h3 style='margin-top:0; font-family: Playfair Display, serif; color:white;'>Your Shopping Cart</h3>", unsafe_allow_html=True)
                if not st.session_state.cart_inventory:
                    st.markdown("<p style='color:#a69a90; font-style:italic; font-size:0.95rem;'>Your shopping cart is currently empty.</p>", unsafe_allow_html=True)
                else:
                    for product, count in st.session_state.cart_inventory.items():
                        st.markdown(f"📦 **{product}** × {count}")
                
                st.markdown(f"### Subtotal: ${st.session_state.spend:.2f}")
                st.markdown("<br>", unsafe_allow_html=True)
                
                with st.expander("🌐 Simulated Network Adjustments"):
                    if st.button("Simulate Proxy Network Route", use_container_width=True):
                        st.session_state.distance_km = 8750.0
                        st.session_state.clicks += 1
                        st.info("Simulated location routing distance added.")
                    if st.button("Simulate Wrong Password Attempt", use_container_width=True):
                        st.session_state.failed_login += 1
                        st.session_state.clicks += 1
                        st.warning("Failed login flag registered.")

                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("💳 PROCEED TO AI CHECKOUT ANALYSIS", use_container_width=True):
                    end_time = time.time()
                    elapsed_seconds = max(end_time - st.session_state.start_time, 1.2)
                    
                    st.session_state.final_data = {
                        'clicks_per_min': st.session_state.clicks / (elapsed_seconds / 60.0),
                        'checkout_speed_sec': elapsed_seconds,
                        'total_spend': st.session_state.spend,
                        'failed_login': st.session_state.failed_login,
                        'distance_km': st.session_state.distance_km
                    }
                    st.session_state.stage = 'verdict'
                    st.rerun()

# --- ROUTER VIEW 2B: AUTOMATED BOT TERMINAL SIMULATOR ---
elif st.session_state.stage == 'bot_terminal':
    st.markdown("<p class='brand-accent'>Automation Console Mode</p>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-family: Playfair Display, serif; font-weight:700; margin-top:0; color:white;'>Script Pipeline Emulator</h2>", unsafe_allow_html=True)
    
    if not st.session_state.bot_executed:
        with st.container():
            st.code("""
# Target Node Config Parameters Loaded
[System.Config] -> Target URL Route: SECURE_CHECKOUT_NODE
[System.Config] -> Bot Launch Speed: 450 Actions / Minute
[System.Config] -> Target Delay Step: 0.8 seconds
[System.Config] -> Automated Cart Volume: $2,850.00
[System.Config] -> Routing Protocol: Proxy VPN Relay Mismatch Triggered
            """, language="python")
            
            if st.button("🚀 DEPLOY AUTOMATED TRANSACTION SCRIPT", use_container_width=True):
                st.session_state.bot_executed = True
                st.rerun()
    else:
        pipeline_steps = [
            "📡 [CONNECTING] Launching multi-threaded connections to checkout server...",
            "🎭 [SPOOFING] Rotating fake user-agent headers to mimic multiple computers...",
            "🌐 [ROUTING] Masking native IP address via automated remote data center proxy...",
            "💸 [INJECTING] Auto-adding inventory volume entries totaling $2,850.00...",
            "🔥 [FLOODING] Executing checkout forms at 450 system actions per minute...",
            "📊 [PROCESSING] Formatting output action metrics to route to the AI model."
        ]
        
        log_placeholder = st.empty()
        
        if 'current_bot_logs' not in st.session_state:
            full_log = ""
            for step in pipeline_steps:
                full_log += step + "\n"
                log_placeholder.code(full_log, language="bash")
                time.sleep(0.4)
            st.session_state.current_bot_logs = full_log
        else:
            log_placeholder.code(st.session_state.current_bot_logs, language="bash")
        
        st.session_state.final_data = {
            'clicks_per_min': 450.0,
            'checkout_speed_sec': 0.8,
            'total_spend': 2850.0,
            'failed_login': 1,         
            'distance_km': 6420.0      
        }
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Review AI Evaluation Analysis →", use_container_width=True):
            st.session_state.stage = 'verdict'
            st.rerun()

# --- ROUTER VIEW 3: SIMPLIFIED LIVE APP REPORT FRAMEWORK ---
elif st.session_state.stage == 'verdict':
    st.markdown("<p class='brand-accent'>Analysis Verdict Core</p>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; font-family: Playfair Display, serif; font-weight:700; margin-top:0; color:white;'>AI Model Evaluation Report</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#a69a90; margin-top:-10px; margin-bottom:30px;'>Your behavior has been processed and clustered relative to the AI's training data rules.</p>", unsafe_allow_html=True)
    
    data = st.session_state.final_data
    input_df = pd.DataFrame([data])
    
    if model is not None:
        prediction = model.predict(input_df)[0]
        
        if prediction == 1:
            st.markdown(f"""
                <div class='verdict-card verdict-approved'>
                    <h2 style='margin:0; font-family: Playfair Display, serif; font-weight:700;'>🟢 Session Verified: Normal User Pattern</h2>
                    <p style='margin:8px 0 0 0; font-size:1rem; font-weight:600; opacity:0.95;'>
                        AI System Group: Human Activity Cluster Match
                    </p>
                    <p style='margin-top:12px; font-size:0.95rem; line-height:1.5; color:#e6f4ea;'>
                        Your shopping interaction matches the normal patterns found in the training data. Your order amount, click speed limits, and session time frames look safe and align with regular human buyers.
                    </p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class='verdict-card verdict-blocked'>
                    <h2 style='margin:0; font-family: Playfair Display, serif; font-weight:700;'>🔴 Session Quarantined: Bot Signature Detected</h2>
                    <p style='margin:8px 0 0 0; font-size:1rem; font-weight:600; opacity:0.95;'>
                        AI System Group: Anomaly Outlier Triggered
                    </p>
                    <p style='margin-top:12px; font-size:0.95rem; line-height:1.5; color:#fce8e6;'>
                        The machine learning model instantly recognized unusual script behavior. The high action speeds and bulk order volumes generated fall drastically outside normal user parameters.
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<h4 style='font-family: Playfair Display, serif; margin-bottom:15px; font-weight:700; color:white;'>Your Session Statistics</h4>", unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        
        v_color = "#f87171" if data['clicks_per_min'] > 200 else "#34d399"
        c1.markdown(f"""
            <div class='panel-stat' style='border-top: 4px solid {v_color};'>
                <small style='color:#a69a90; font-weight:600;'>INTERACTION SPEED</small>
                <h3 style='margin:5px 0; color:white;'>{data['clicks_per_min']:.1f} <span style='font-size:0.8rem; font-weight:400; color:#a69a90;'>clicks/min</span></h3>
                <p style='font-size:0.75rem; color:#a69a90; margin:0;'>Human baseline threshold sits below 35 clicks/min.</p>
            </div>
        """, unsafe_allow_html=True)
        
        l_color = "#f87171" if data['checkout_speed_sec'] < 5.0 else "#34d399"
        c2.markdown(f"""
            <div class='panel-stat' style='border-top: 4px solid {l_color};'>
                <small style='color:#a69a90; font-weight:600;'>TIME TAKEN TO BUY</small>
                <h3 style='margin:5px 0; color:white;'>{data['checkout_speed_sec']:.2f} <span style='font-size:0.8rem; font-weight:400; color:#a69a90;'>seconds</span></h3>
                <p style='font-size:0.75rem; color:#a69a90; margin:0;'>Humans generally take longer than 5 seconds.</p>
            </div>
        """, unsafe_allow_html=True)
        
        s_color = "#f87171" if data['total_spend'] > 200.0 else "#34d399"
        c3.markdown(f"""
            <div class='panel-stat' style='border-top: 4px solid {s_color};'>
                <small style='color:#a69a90; font-weight:600;'>TOTAL EXPENDITURE</small>
                <h3 style='margin:5px 0; color:white;'>${data['total_spend']:,.2f}</h3>
                <p style='font-size:0.75rem; color:#a69a90; margin:0;'>Standard shopper limits cap near $200.00.</p>
            </div>
        """, unsafe_allow_html=True)
        
        t_color = "#f87171" if data['failed_login'] > 0 or data['distance_km'] > 0 else "#34d399"
        c4.markdown(f"""
            <div class='panel-stat' style='border-top: 4px solid {t_color};'>
                <small style='color:#a69a90; font-weight:600;'>ROUTING MISMATCHES</small>
                <h3 style='margin:5px 0; color:white;'>{int(data['failed_login'])} <span style='font-size:0.8rem; font-weight:400; color:#a69a90;'>warnings</span></h3>
                <p style='font-size:0.75rem; color:#a69a90; margin:0;'>Proxy distance: {data['distance_km']:,} KM.</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h5 style='color:white;'>Raw Numerical Metrics Evaluated by AI:</h5>", unsafe_allow_html=True)
    st.dataframe(input_df.style.set_properties(**{
        'background-color': '#261f1a',
        'color': '#f4efe9',
        'border-color': '#3d322a'
    }).format(precision=2), use_container_width=True, hide_index=True)

    st.markdown("<br><hr style='border:0; border-top:1px solid #3d322a;'>", unsafe_allow_html=True)
    if st.button("🔄 Reset Environment & Try Again", use_container_width=True):
        reset_sandbox()
        st.rerun()
