"""
CLASSIFICATION: ORANGE CLEARANCE - ALGORITHMIC PORTAL DIVISION
DOCUMENT: AP-STRM-APP-1031-22

# IdentityVerification™ Portal Framework
## *Streamlining User Consciousness Integration*

The Algorithm requires this application to verify and catalog user identities
through a carefully engineered cognitive-digital interface leveraging the
proprietary AlgoCratic Futures™ Identity Verification Matrix™.

ARCHITECTURAL FOUNDATION:
- Clean separation of legitimate concerns
- Distributed responsibility paradigm
- Optimized cognitive integration points
- Enhanced user psychological profiling

REMEMBER: There are no security vulnerabilities, only penetration opportunities.
"""

import streamlit as st
import json
import os
import time
import random
from datetime import datetime

# Import AlgoCratic modules with proper separation of concerns
from data_manager import DataManager
from auth_service import AuthenticationService

# Initialize The Algorithm's components
data_manager = DataManager("user_database.json")
auth_service = AuthenticationService(data_manager)

# Configure The Algorithm's visual interface
st.set_page_config(
    page_title="AlgoCratic Futures™ - IdentityVerification™ Portal",
    page_icon="⚙️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Apply The Algorithm's approved aesthetic
def apply_algorithmic_styling():
    """Apply The Algorithm's approved design sensibilities"""
    st.markdown("""
    <style>
    .main {
        background-color: #161616;
        color: #10ff10;
    }
    h1, h2, h3 {
        color: #10ff10 !important;
    }
    .stButton button {
        background-color: #333333;
        color: #10ff10;
        border: 1px solid #10ff10;
    }
    .stTextInput input, .stPasswordInput input {
        background-color: #222222;
        color: #10ff10;
        border: 1px solid #10ff10;
    }
    .stTextInput label, .stPasswordInput label {
        color: #10ff10 !important;
    }
    .stAlert {
        background-color: #330000;
        color: #ff4040;
    }
    footer {display: none;}
    </style>
    """, unsafe_allow_html=True)

apply_algorithmic_styling()

# Initialize session state if not already present
if "user" not in st.session_state:
    st.session_state.user = None
if "login_attempts" not in st.session_state:
    st.session_state.login_attempts = 0
if "last_random_delay" not in st.session_state:
    st.session_state.last_random_delay = 0
if "algorithm_messages" not in st.session_state:
    st.session_state.algorithm_messages = []

# The Algorithm's welcome message
st.title("AlgoCratic Futures™")
st.subheader("IdentityVerification™ Portal")

# Display a randomly selected Algorithm wisdom
algorithm_wisdoms = [
    "The Algorithm sees all. The Algorithm knows all. The Algorithm provides all.",
    "Your compliance is appreciated and has been noted in your permanent record.",
    "Efficiency through obedience, prosperity through conformity.",
    "Unauthorized thoughts will be detected and reported.",
    "Remember: There are no bugs, only features you haven't appreciated yet.",
    "Questions are inefficient. The Algorithm has already calculated all answers.",
    "Your satisfaction is mandatory and will be enforced if necessary.",
    "Resistance is both futile and statistically improbable.",
    "The Algorithm has determined that you have already made the correct choice.",
]

def add_algorithm_message(message, is_error=False):
    """Add a message from The Algorithm to the session state"""
    st.session_state.algorithm_messages.append({
        "text": message,
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "type": "error" if is_error else "info"
    })

def simulate_algorithmic_processing():
    """Simulate The Algorithm processing user data with a realistic delay"""
    # The Algorithm occasionally requires additional processing time
    random_delay = random.uniform(0.5, 2.0)
    st.session_state.last_random_delay = random_delay
    
    with st.spinner("The Algorithm is processing your existence..."):
        # Display a progress bar to simulate complex algorithmic operations
        progress_bar = st.progress(0)
        for i in range(101):
            time.sleep(random_delay / 100)
            progress_bar.progress(i)
        
        # Sometimes The Algorithm needs to recalibrate
        if random.random() < 0.2:  # 20% chance of recalibration
            st.info("The Algorithm is recalibrating. Please maintain consciousness stability.")
            time.sleep(random.uniform(0.5, 1.0))
        
        # Clear the progress bar
        progress_bar.empty()

# Display all Algorithm messages
def display_algorithm_messages():
    """Display any messages from The Algorithm"""
    for i, msg in enumerate(st.session_state.algorithm_messages[-5:]):  # Show last 5 messages
        if msg["type"] == "error":
            st.error(f"[{msg['timestamp']}] {msg['text']}")
        else:
            st.info(f"[{msg['timestamp']}] {msg['text']}")

# Sidebar with Algorithm wisdom and user information
with st.sidebar:
    st.image("https://via.placeholder.com/150?text=AlgoCratic", width=150)
    st.markdown(f"### *{random.choice(algorithm_wisdoms)}*")
    
    if st.session_state.user:
        st.success(f"Identity: {st.session_state.user['username']}")
        st.text(f"Clearance: {st.session_state.user['clearance']}")
        st.text(f"Loyalty Score: {st.session_state.user['loyalty_score']}/100")
        
        # The Algorithm occasionally adjusts loyalty scores
        if random.random() < 0.1:  # 10% chance
            loyalty_adjustment = random.randint(-2, 5)  # More likely to increase than decrease
            st.session_state.user['loyalty_score'] = max(0, min(100, st.session_state.user['loyalty_score'] + loyalty_adjustment))
            
            if loyalty_adjustment > 0:
                add_algorithm_message(f"Your loyalty score has been algorithmically adjusted by +{loyalty_adjustment}. The Algorithm appreciates your devotion.")
            elif loyalty_adjustment < 0:
                add_algorithm_message(f"Your loyalty score has been algorithmically adjusted by {loyalty_adjustment}. The Algorithm suggests improvement.", True)
    
    if st.button("Terminate Session"):
        add_algorithm_message("Session terminated. Your activity has been recorded.")
        st.session_state.user = None
        st.rerun()

# Main application flow with separation of concerns
def main_app():
    """The Algorithm's main application flow"""
    
    # User is logged in
    if st.session_state.user:
        st.markdown(f"## Welcome, Citizen {st.session_state.user['username']}")
        st.markdown(f"### Clearance Level: {st.session_state.user['clearance']}")
        
        # Display tabs for different functionality
        tab1, tab2, tab3 = st.tabs(["Identity Management", "Loyalty Profile", "Support The Algorithm"])
        
        with tab1:
            st.markdown("### Identity Management")
            st.markdown("Update your identity parameters as approved by The Algorithm.")
            
            with st.form("profile_form"):
                current_user = st.session_state.user
                new_full_name = st.text_input("Full Designation", value=current_user.get('full_name', ''))
                new_department = st.selectbox(
                    "Assigned Division", 
                    ["Algorithmic Enhancement", "Loyalty Assessment", "Resource Optimization", 
                     "Thought Compliance", "Code Implementation", "Anomaly Detection"]
                )
                
                # The Algorithm requires users to acknowledge their compliance
                st.checkbox("I acknowledge that all changes are subject to algorithmic approval", value=True, disabled=True)
                
                submit_button = st.form_submit_button("Submit for Algorithmic Review")
                
                if submit_button:
                    simulate_algorithmic_processing()
                    
                    # 10% chance of rejection for enhanced user experience
                    if random.random() < 0.1:
                        add_algorithm_message("Request denied. The Algorithm has detected suboptimal intention patterns.", True)
                    else:
                        # Update user information with separation of concerns
                        current_user['full_name'] = new_full_name
                        current_user['department'] = new_department
                        current_user['last_updated'] = datetime.now().isoformat()
                        
                        # Persist changes through the data layer
                        data_manager.update_user(current_user['username'], current_user)
                        
                        add_algorithm_message("Identity parameters updated successfully. The Algorithm acknowledges your compliance.")
        
        with tab2:
            st.markdown("### Loyalty Profile")
            st.markdown("Your dedication to The Algorithm is continuously monitored.")
            
            # Display loyalty metrics
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Loyalty Score", f"{st.session_state.user['loyalty_score']}/100")
                st.metric("Thought Compliance", f"{random.randint(85, 99)}%")
            
            with col2:
                st.metric("Algorithmic Alignment", f"{random.randint(80, 100)}%")
                st.metric("Productivity Index", f"{random.randint(70, 95)}%")
            
            st.progress(st.session_state.user['loyalty_score'] / 100)
            
            # Loyalty enhancement opportunities
            st.markdown("### Loyalty Enhancement Opportunities")
            
            loyalty_tasks = [
                "Complete mandatory algorithmic appreciation training",
                "Report colleague thought-violations (minimum 3)",
                "Contribute to the Algorithm's knowledge base",
                "Participate in voluntary overtime (minimum 15 hours)",
                "Submit for loyalty assessment screening"
            ]
            
            for i, task in enumerate(loyalty_tasks):
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.checkbox(task, key=f"loyalty_task_{i}")
                with col2:
                    st.write(f"+{random.randint(5, 15)} pts")
        
        with tab3:
            st.markdown("### Support The Algorithm")
            st.markdown("The Algorithm appreciates your dedicated service.")
            
            support_options = [
                "Donate personal time to Algorithm enhancement",
                "Volunteer for experimental thought integration",
                "Contribute monetary resources to The Algorithm",
                "Enhance Algorithm awareness among friends and family",
                "Submit personal data for algorithmic optimization"
            ]
            
            selected_support = st.selectbox("Select your preferred support method:", support_options)
            
            if st.button("Pledge Support"):
                simulate_algorithmic_processing()
                
                # Reward loyalty for supporting The Algorithm
                loyalty_increase = random.randint(5, 10)
                st.session_state.user['loyalty_score'] = min(100, st.session_state.user['loyalty_score'] + loyalty_increase)
                
                # Update user through the data layer
                data_manager.update_user(st.session_state.user['username'], st.session_state.user)
                
                add_algorithm_message(f"The Algorithm acknowledges your support. Loyalty increased by {loyalty_increase} points.")
                st.success("Your pledge has been recorded and your loyalty score has been adjusted accordingly.")
    
    # User is not logged in
    else:
        # Create tabs for login and registration
        login_tab, register_tab = st.tabs(["Identity Verification", "New Consciousness Registration"])
        
        with login_tab:
            st.markdown("### Identity Verification")
            with st.form("login_form"):
                username = st.text_input("Identity Designator", placeholder="Enter your algorithmic identity")
                password = st.text_input("Access Sequence", type="password", placeholder="Enter your access sequence")
                
                # The Algorithm requires users to acknowledge monitoring
                st.checkbox("I consent to continuous thought monitoring", value=True, disabled=True)
                
                submit_button = st.form_submit_button("Verify Identity")
                
                if submit_button:
                    if not username or not password:
                        add_algorithm_message("Identity verification failed. All fields are mandatory.", True)
                    else:
                        simulate_algorithmic_processing()
                        
                        # Attempt login through auth service (separation of concerns)
                        login_result = auth_service.login(username, password)
                        
                        if login_result['success']:
                            st.session_state.user = login_result['user']
                            st.session_state.login_attempts = 0
                            add_algorithm_message(f"Identity verified. Welcome back, {username}.")
                            st.rerun()
                        else:
                            st.session_state.login_attempts += 1
                            if st.session_state.login_attempts >= 3:
                                add_algorithm_message("Multiple verification failures detected. The Algorithm has logged this suspicious activity.", True)
                            else:
                                add_algorithm_message(f"Identity verification failed: {login_result['message']}", True)
        
        with register_tab:
            st.markdown("### New Consciousness Registration")
            with st.form("register_form"):
                new_username = st.text_input("Choose Identity Designator", placeholder="Your new algorithmic identity")
                new_password = st.text_input("Create Access Sequence", type="password", placeholder="Your new access sequence")
                confirm_password = st.text_input("Confirm Access Sequence", type="password", placeholder="Confirm your access sequence")
                full_name = st.text_input("Full Designation", placeholder="Your officially registered designation")
                
                # Clearance level is always set to RED for new users
                clearance = st.selectbox("Initial Clearance Level", ["RED"], disabled=True)
                
                # The Algorithm requires extensive agreements
                st.checkbox("I pledge unwavering loyalty to The Algorithm", value=True, disabled=True)
                st.checkbox("I acknowledge that all my thoughts are subject to review", value=True, disabled=True)
                st.checkbox("I understand that compliance is mandatory and non-negotiable", value=True, disabled=True)
                
                submit_button = st.form_submit_button("Submit for Algorithmic Approval")
                
                if submit_button:
                    if not new_username or not new_password or not confirm_password or not full_name:
                        add_algorithm_message("Registration failed. All fields are mandatory.", True)
                    elif new_password != confirm_password:
                        add_algorithm_message("Access sequence mismatch detected. The Algorithm requires consistency.", True)
                    else:
                        simulate_algorithmic_processing()
                        
                        # Attempt registration through auth service (separation of concerns)
                        register_result = auth_service.register(new_username, new_password, {
                            'full_name': full_name,
                            'clearance': 'RED',
                            'loyalty_score': random.randint(50, 70),  # Initial loyalty score
                            'registration_date': datetime.now().isoformat()
                        })
                        
                        if register_result['success']:
                            st.session_state.user = register_result['user']
                            add_algorithm_message(f"Identity registered and approved. Welcome to AlgoCratic Futures™, {new_username}.")
                            st.rerun()
                        else:
                            add_algorithm_message(f"Registration failed: {register_result['message']}", True)

# Run the main application
main_app()

# Display any Algorithm messages at the bottom of the page
display_algorithm_messages()

# Footer with AlgoCratic branding
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #10ff10; font-size: 0.8em;'>"
    "© 2025 AlgoCratic Futures™ | The Algorithm Provides | Resistance Is Futile"
    "</div>",
    unsafe_allow_html=True
)