import re
import sys

def rebuild():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # 1. Replace the entire <style> block
    style_start = html.find('<style>')
    style_end = html.find('</style>')
    
    if style_start == -1 or style_end == -1:
        print("Could not find <style> tags")
        return

    new_css = """<style>
    /* ──────────────────────────────────────────────────────────────────
       1. SMART UI - MODERN GLASSMORPHISM DESIGN SYSTEM
       ────────────────────────────────────────────────────────────────── */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Noto+Sans+Tamil:wght@300;400;500;600;700&display=swap');

    :root {
      --primary: #0F172A;
      /* Modern Navy */
      --primary-light: #1E293B;
      --accent: #0EA5E9;
      /* Cyan */
      --accent-light: rgba(14, 165, 233, 0.08);
      --bg: #F8FAFC;
      /* Very light slate */
      --surface: rgba(255, 255, 255, 0.85);
      /* Glassmorphic Surface */
      --surface-solid: #FFFFFF;
      --success: #10B981;
      --success-light: rgba(16, 185, 129, 0.08);
      --warning: #F59E0B;
      --warning-light: rgba(245, 158, 11, 0.08);
      --danger: #EF4444;
      --danger-light: rgba(239, 68, 68, 0.08);
      --info: #3B82F6;
      --info-light: rgba(59, 130, 246, 0.08);
      --text: #0F172A;
      --text-muted: #64748B;
      --border: rgba(14, 165, 233, 0.15);

      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
      --shadow-glass: 0 8px 32px 0 rgba(15, 23, 42, 0.07);

      --font-english: 'Outfit', sans-serif;
      --font-tamil: 'Noto Sans Tamil', sans-serif;
      --font-heading: 'Outfit', sans-serif;

      --transition-speed: 0.4s;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
      user-select: none;
    }

    body {
      font-family: var(--font-english);
      background-color: var(--text);
      /* Dark background for desktop wrapper */
      color: var(--text);
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      overflow: hidden;
      background-image: radial-gradient(circle at 50% 0%, #1E293B 0%, #0F172A 70%);
    }

    body.lang-tamil .lang-en {
      display: none !important;
    }

    body:not(.lang-tamil) .lang-ta {
      display: none !important;
    }

    body.lang-tamil {
      font-family: var(--font-tamil), var(--font-english);
    }

    .desktop-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 24px;
      padding: 20px;
      z-index: 10;
      height: 100%;
    }

    .desktop-title {
      font-family: var(--font-heading);
      color: #F1F5F9;
      font-size: 24px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 12px;
      text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }

    .desktop-title span {
      font-weight: 400;
      color: #94A3B8;
      font-size: 16px;
    }

    .phone-mockup {
      width: 390px;
      height: 844px;
      background-color: var(--bg);
      border: 12px solid #1E293B;
      border-radius: 50px;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5), inset 0 0 0 2px #334155;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }

    /* ── PWA Standalone Mode: Remove phone frame, go full screen ── */
    @media (display-mode: standalone) {
      body {
        background: var(--bg) !important;
        background-image: none !important;
        align-items: flex-start;
        justify-content: flex-start;
      }

      .desktop-container {
        width: 100vw;
        height: 100vh;
        padding: 0;
        gap: 0;
      }

      .desktop-title {
        display: none !important;
      }

      .phone-mockup {
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
        border-radius: 0 !important;
        box-shadow: none !important;
        max-width: 100% !important;
      }

      .status-bar {
        display: none !important;
      }

      .home-indicator-bar {
        display: none !important;
      }

      .desktop-info-floating {
        display: none !important;
      }
    }

    /* JS fallback class for older browsers */
    body.pwa-mode {
      background: var(--bg) !important;
      background-image: none !important;
      align-items: flex-start;
      justify-content: flex-start;
    }

    body.pwa-mode .desktop-container {
      width: 100vw;
      height: 100vh;
      padding: 0;
      gap: 0;
    }

    body.pwa-mode .desktop-title {
      display: none !important;
    }

    body.pwa-mode .phone-mockup {
      width: 100vw !important;
      height: 100vh !important;
      border: none !important;
      border-radius: 0 !important;
      box-shadow: none !important;
      max-width: 100% !important;
    }

    body.pwa-mode .status-bar {
      display: none !important;
    }

    body.pwa-mode .home-indicator-bar {
      display: none !important;
    }

    body.pwa-mode .desktop-info-floating {
      display: none !important;
    }

    /* Screen Deck & Layout */
    .screen-deck {
      flex: 1;
      position: relative;
      overflow: hidden;
      background-color: var(--bg);
    }

    .screen {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      background-color: var(--bg);
      transform: translateX(100%);
      transition: transform var(--transition-speed) cubic-bezier(0.2, 0.8, 0.2, 1);
      opacity: 0;
      pointer-events: none;
    }

    .screen.active {
      transform: translateX(0);
      opacity: 1;
      pointer-events: auto;
    }

    .screen-content {
      flex: 1;
      overflow-y: auto;
      overflow-x: hidden;
      padding: 24px 20px 100px;
    }

    .screen-content::-webkit-scrollbar {
      display: none;
    }

    /* Smart UI Components */
    .card,
    .glass-card {
      background: var(--surface);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 20px;
      box-shadow: var(--shadow-glass);
      margin-bottom: 16px;
      transition: transform 0.2s, box-shadow 0.2s;
    }

    .card:active,
    .glass-card:active,
    .kpi-glass:active,
    .kpi-card:active {
      transform: scale(0.98);
    }

    .card-title {
      font-family: var(--font-heading);
      font-size: 16px;
      font-weight: 700;
      color: var(--text);
      margin-bottom: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .btn {
      border: none;
      border-radius: 14px;
      padding: 14px 20px;
      font-size: 15px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      width: 100%;
      transition: all 0.2s;
      font-family: var(--font-heading);
    }

    .btn-primary {
      background: var(--primary);
      color: white;
      box-shadow: 0 4px 14px rgba(15, 23, 42, 0.15);
    }

    .btn-primary:active {
      transform: scale(0.96);
      box-shadow: 0 2px 8px rgba(15, 23, 42, 0.1);
    }

    .form-group {
      margin-bottom: 20px;
      text-align: left;
    }

    .form-label {
      display: block;
      font-size: 14px;
      line-height: 1.5;
      font-weight: 600;
      color: var(--text-muted);
      margin-bottom: 8px;
      font-family: var(--font-heading);
    }

    .form-input {
      width: 100%;
      padding: 14px 16px;
      border-radius: 12px;
      border: 1px solid var(--border);
      background-color: var(--surface-solid);
      color: var(--text);
      font-size: 15px;
      font-family: var(--font-english);
      outline: none;
      transition: border-color 0.2s, box-shadow 0.2s;
    }

    .form-input:focus {
      border-color: var(--accent);
      box-shadow: 0 0 0 3px rgba(14, 165, 233, 0.15);
    }

    /* Login Screen Specifics */
    .smart-login-header {
      text-align: center;
      margin-top: 20px;
      margin-bottom: 40px;
      animation: slideDown 0.6s ease-out;
    }

    @keyframes slideDown {
      from {
        opacity: 0;
        transform: translateY(-20px);
      }

      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .login-role-card {
      background: var(--surface-solid);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 16px;
      display: flex;
      align-items: center;
      gap: 16px;
      margin-bottom: 12px;
      cursor: pointer;
      transition: all 0.2s;
      box-shadow: var(--shadow-sm);
      animation: fadeIn 0.5s ease-out forwards;
      opacity: 0;
      transform: translateY(10px);
    }

    @keyframes fadeIn {
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .login-role-card:nth-child(1) {
      animation-delay: 0.1s;
    }

    .login-role-card:nth-child(2) {
      animation-delay: 0.2s;
    }

    .login-role-card:nth-child(3) {
      animation-delay: 0.3s;
    }

    .login-role-card:hover {
      border-color: var(--accent);
      box-shadow: var(--shadow);
      transform: translateY(-2px);
    }

    .login-role-card:active {
      transform: translateY(0) scale(0.98);
    }

    .role-icon {
      width: 48px;
      height: 48px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      background: var(--bg);
    }

    .role-info {
      text-align: left;
      flex: 1;
    }

    .role-title {
      font-family: var(--font-heading);
      font-weight: 700;
      font-size: 16px;
      color: var(--text);
    }

    .role-desc {
      font-size: 14px;
      line-height: 1.5;
      line-height: 1.5;
      color: var(--text-muted);
      margin-top: 2px;
    }

    .login-action-btn {
      background: var(--surface-solid);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 12px 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      color: var(--text);
      cursor: pointer;
      transition: all 0.2s;
      box-shadow: var(--shadow-sm);
      width: 100%;
    }

    .login-action-btn:hover {
      border-color: var(--accent);
    }

    .login-action-btn:active {
      transform: scale(0.96);
    }

    .login-action-btn i {
      color: var(--accent);
      width: 22px;
      height: 22px;
    }

    .login-action-btn .btn-text-col {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
    }

    .login-action-btn .btn-text-col span {
      font-size: 13px;
      font-weight: 700;
      font-family: var(--font-heading);
      line-height: 1.2;
    }

    .login-action-btn .btn-text-col small {
      font-size: 11px;
      color: var(--text-muted);
      font-family: var(--font-tamil);
      line-height: 1.2;
      margin-top: 2px;
    }

    /* App Header */
    .app-header {
      padding: 20px 20px 10px;
      background: var(--bg);
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 50;
    }

    .app-header h1 {
      font-family: var(--font-heading);
      font-size: 22px;
      font-weight: 800;
      color: var(--text);
    }

    .app-header>* {
      grid-row: 1;
    }

    /* Modern Bottom Nav */
    .bottom-nav {
      position: absolute;
      bottom: 30px;
      left: 20px;
      right: 20px;
      background: rgba(255, 255, 255, 0.9);
      backdrop-filter: blur(16px);
      border-radius: 24px;
      display: none;
      justify-content: space-around;
      padding: 12px 8px;
      box-shadow: var(--shadow-glass);
      border: 1px solid var(--border);
      z-index: 200;
    }

    .bottom-nav.active {
      display: flex;
    }

    .nav-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.2s;
      position: relative;
      width: 60px;
    }

    .nav-item i {
      width: 22px;
      height: 22px;
      stroke-width: 2px;
      transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    }

    .nav-item span {
      font-size: 12px;
      line-height: 1.5;
      font-weight: 600;
      font-family: var(--font-heading);
    }

    .nav-item.active {
      color: var(--accent);
    }

    .nav-item.active i {
      transform: translateY(-4px);
      stroke-width: 2.5px;
    }

    .nav-item.active::after {
      content: '';
      position: absolute;
      bottom: -8px;
      width: 4px;
      height: 4px;
      background: var(--accent);
      border-radius: 50%;
    }

    /* KPI Grid Glass */
    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin-bottom: 16px;
    }

    .kpi-glass,
    .kpi-card {
      background: var(--surface);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 16px;
      text-align: center;
      box-shadow: var(--shadow-glass);
      margin-bottom: 16px;
      transition: transform 0.2s, box-shadow 0.2s;
    }

    .kpi-num {
      font-family: var(--font-heading);
      font-size: 28px;
      font-weight: 800;
      color: var(--primary);
      margin-bottom: 4px;
    }

    .kpi-label {
      font-size: 14px;
      line-height: 1.5;
      line-height: 1.5;
      color: var(--text-muted);
      font-weight: 600;
    }

    /* Badge */
    .badge {
      padding: 4px 10px;
      border-radius: 99px;
      font-size: 12px;
      line-height: 1.5;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .badge-success {
      background: var(--success-light);
      color: var(--success);
    }

    .badge-info {
      background: var(--info-light);
      color: var(--info);
    }

    .badge-primary {
      background: rgba(14, 165, 233, 0.08);
      color: var(--accent);
    }

    /* List Items */
    .list-item {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 12px 0;
      border-bottom: 1px solid var(--border);
    }

    .list-item:last-child {
      border-bottom: none;
    }

    /* Utilities */
    .text-gradient {
      background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    /* Hide scrollbars globally */
    ::-webkit-scrollbar {
      display: none;
    }



    /* --- COMBINED PREMIUM LIGHT THEME & UTILITIES --- */

    :root {
      --app-bg: #F8FAFC;
      --app-bg-gradient: linear-gradient(135deg, #e0f2fe 0%, #f1f5f9 50%, #faf5ff 100%);
      --surface: rgba(255, 255, 255, 0.82);
      --surface-solid: #FFFFFF;
      --text: #0F172A;
      --text-muted: #475569;
      --border: rgba(14, 165, 233, 0.12);
      --shadow-glass: 0 10px 40px rgba(15, 23, 42, 0.04);
      --shadow-sm: 0 4px 10px rgba(15, 23, 42, 0.02);
      --primary: #0F172A;
      --primary-light: #1E293B;
      --accent: #0ea5e9;
      --accent-light: rgba(14, 165, 233, 0.08);
    }

    body {
      background-color: #0F172A !important;
      background-image: radial-gradient(circle at 50% 0%, #1E293B 0%, #0F172A 80%) !important;
    }

    /* Premium Mesh/Aura Gradient Background (Light Mode) */
    body:not(.dark-mode) .phone-mockup {
      background: #F8FAFC !important;
      background-image:
        radial-gradient(at 0% 0%, rgba(14, 165, 233, 0.15) 0px, transparent 50%),
        radial-gradient(at 100% 0%, rgba(99, 102, 241, 0.15) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(245, 158, 11, 0.1) 0px, transparent 50%),
        radial-gradient(at 0% 100%, rgba(16, 185, 129, 0.1) 0px, transparent 50%) !important;
    }

    .smartphone {
      background: var(--app-bg-gradient) !important;
    }

    .screen-deck,
    .screen {
      background: transparent !important;
      color: var(--text) !important;
    }

    /* Global Utility Classes (Light Mode) */
    body:not(.dark-mode) .card:not(.bg-primary-gradient):not([style*="background"]),
    body:not(.dark-mode) .glass-card:not([style*="background"]),
    body:not(.dark-mode) .kpi-glass,
    body:not(.dark-mode) .kpi-card {
      background: rgba(255, 255, 255, 0.75) !important;
    }

    body:not(.dark-mode) .card:not(.bg-primary-gradient):not([style*="color"]),
    body:not(.dark-mode) .glass-card:not([style*="color"]) {
      color: var(--text) !important;
    }

    body:not(.dark-mode) .card,
    body:not(.dark-mode) .glass-card,
    body:not(.dark-mode) .kpi-glass,
    body:not(.dark-mode) .kpi-card {
      backdrop-filter: blur(20px) !important;
      -webkit-backdrop-filter: blur(20px) !important;
      border: 1px solid rgba(255, 255, 255, 0.6) !important;
      box-shadow:
        0 4px 6px -1px rgba(15, 23, 42, 0.01),
        0 10px 30px -3px rgba(15, 23, 42, 0.04) !important;
      border-radius: 24px !important;
      padding: 24px;
      margin-bottom: 16px;
    }

    /* Light Mode Custom Pastel Color Accents */
    body:not(.dark-mode) .kpi-card.kpi-blue {
      background: rgba(59, 130, 246, 0.06) !important;
      border: 1px solid rgba(59, 130, 246, 0.15) !important;
    }

    body:not(.dark-mode) .kpi-card.kpi-amber {
      background: rgba(245, 158, 11, 0.06) !important;
      border: 1px solid rgba(245, 158, 11, 0.15) !important;
    }

    body:not(.dark-mode) .kpi-card.kpi-green {
      background: rgba(16, 185, 129, 0.06) !important;
      border: 1px solid rgba(16, 185, 129, 0.15) !important;
    }

    body:not(.dark-mode) .kpi-card.kpi-cyan {
      background: rgba(14, 165, 233, 0.06) !important;
      border: 1px solid rgba(14, 165, 233, 0.15) !important;
    }

    body:not(.dark-mode) .kpi-card.kpi-purple {
      background: rgba(139, 92, 246, 0.06) !important;
      border: 1px solid rgba(139, 92, 246, 0.15) !important;
    }

    body:not(.dark-mode) .card.card-quick-actions {
      background: rgba(14, 165, 233, 0.05) !important;
      border: 1px solid rgba(14, 165, 233, 0.15) !important;
    }

    /* ── Light Mode: Alternating Pastel Card Accents (all screens) ── */
    /* Cards cycle through 4 soft hues: sky, sage, peach, lavender */
    body:not(.dark-mode) .screen-content>.card:nth-child(4n+1):not(.bg-primary-gradient):not([style*="background"]) {
      background: rgba(14, 165, 233, 0.05) !important;
      border: 1px solid rgba(14, 165, 233, 0.12) !important;
    }

    body:not(.dark-mode) .screen-content>.card:nth-child(4n+2):not(.bg-primary-gradient):not([style*="background"]) {
      background: rgba(16, 185, 129, 0.05) !important;
      border: 1px solid rgba(16, 185, 129, 0.12) !important;
    }

    body:not(.dark-mode) .screen-content>.card:nth-child(4n+3):not(.bg-primary-gradient):not([style*="background"]) {
      background: rgba(139, 92, 246, 0.05) !important;
      border: 1px solid rgba(139, 92, 246, 0.12) !important;
    }

    body:not(.dark-mode) .screen-content>.card:nth-child(4n):not(.bg-primary-gradient):not([style*="background"]) {
      background: rgba(245, 158, 11, 0.05) !important;
      border: 1px solid rgba(245, 158, 11, 0.12) !important;
    }

    /* Attendance card on parent home — subtle warm green */
    body:not(.dark-mode) #parent-home .card:first-of-type {
      background: rgba(16, 185, 129, 0.05) !important;
      border: 1px solid rgba(16, 185, 129, 0.12) !important;
    }

    /* Today's class schedule card — subtle blue */
    body:not(.dark-mode) #teacher-home .card:last-of-type {
      background: rgba(59, 130, 246, 0.05) !important;
      border: 1px solid rgba(59, 130, 246, 0.12) !important;
    }

    /* Admin recent approvals card — subtle purple */
    body:not(.dark-mode) #admin-home .card:first-of-type {
      background: rgba(139, 92, 246, 0.05) !important;
      border: 1px solid rgba(139, 92, 246, 0.12) !important;
    }

    /* Soften card-title text color in light mode to pair with color tints */
    body:not(.dark-mode) .card-title {
      color: #0F172A !important;
    }

    /* ── Light Mode: KPI card color accents ── */
    /* KPI cards cycle through 4 accent hues: sky, sage, lavender, peach */
    body:not(.dark-mode) .kpi-grid .kpi-card:nth-child(4n+1) {
      background: rgba(14, 165, 233, 0.07) !important;
      border: 1px solid rgba(14, 165, 233, 0.18) !important;
    }

    body:not(.dark-mode) .kpi-grid .kpi-card:nth-child(4n+2) {
      background: rgba(16, 185, 129, 0.07) !important;
      border: 1px solid rgba(16, 185, 129, 0.18) !important;
    }

    body:not(.dark-mode) .kpi-grid .kpi-card:nth-child(4n+3) {
      background: rgba(139, 92, 246, 0.07) !important;
      border: 1px solid rgba(139, 92, 246, 0.18) !important;
    }

    body:not(.dark-mode) .kpi-grid .kpi-card:nth-child(4n) {
      background: rgba(245, 158, 11, 0.07) !important;
      border: 1px solid rgba(245, 158, 11, 0.18) !important;
    }

    /* KPI numbers vibrant accent colors to match their card tints */
    body:not(.dark-mode) .kpi-grid .kpi-card:nth-child(4n+1) .kpi-num {
      color: #0284c7 !important;
    }

    body:not(.dark-mode) .kpi-grid .kpi-card:nth-child(4n+2) .kpi-num {
      color: #059669 !important;
    }

    body:not(.dark-mode) .kpi-grid .kpi-card:nth-child(4n+3) .kpi-num {
      color: #7c3aed !important;
    }

    body:not(.dark-mode) .kpi-grid .kpi-card:nth-child(4n) .kpi-num {
      color: #d97706 !important;
    }

    /* KPI label text stays readable */
    body:not(.dark-mode) .kpi-label {
      color: #475569 !important;
    }

    /* Login Role Selection Upgrades (Light Mode) */
    body:not(.dark-mode) .login-role-card {
      background: rgba(255, 255, 255, 0.75) !important;
      border: 1px solid rgba(14, 165, 233, 0.12) !important;
      box-shadow: 0 4px 10px rgba(15, 23, 42, 0.02) !important;
      border-radius: 20px !important;
      padding: 16px;
      margin-bottom: 14px;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }

    body:not(.dark-mode) .login-role-card:hover {
      transform: translateY(-3px) scale(1.02);
      box-shadow: 0 16px 36px rgba(15, 23, 42, 0.07) !important;
    }

    body:not(.dark-mode) .login-role-card:nth-child(1):hover {
      border-color: rgba(16, 185, 129, 0.4) !important;
      box-shadow: 0 10px 25px rgba(16, 185, 129, 0.08) !important;
    }

    body:not(.dark-mode) .login-role-card:nth-child(2):hover {
      border-color: rgba(59, 130, 246, 0.4) !important;
      box-shadow: 0 10px 25px rgba(59, 130, 246, 0.08) !important;
    }

    body:not(.dark-mode) .login-role-card:nth-child(3):hover {
      border-color: rgba(245, 158, 11, 0.4) !important;
      box-shadow: 0 10px 25px rgba(245, 158, 11, 0.08) !important;
    }

    body:not(.dark-mode) .role-icon {
      border-radius: 14px !important;
      transition: transform 0.3s ease;
    }

    body:not(.dark-mode) .login-role-card:hover .role-icon {
      transform: scale(1.1);
    }

    /* Login Action buttons & language triggers (Light Mode) */
    body:not(.dark-mode) .login-action-btn {
      background: rgba(255, 255, 255, 0.75) !important;
      border: 1px solid rgba(14, 165, 233, 0.12) !important;
      color: var(--text) !important;
      box-shadow: 0 4px 10px rgba(15, 23, 42, 0.02) !important;
      border-radius: 16px !important;
      transition: all 0.2s ease;
    }

    body:not(.dark-mode) .login-action-btn:hover {
      border-color: var(--accent) !important;
      box-shadow: 0 8px 20px rgba(14, 165, 233, 0.08) !important;
      transform: translateY(-2px);
    }

    body:not(.dark-mode) .card.bg-primary-gradient {
      background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%) !important;
      color: rgba(255, 255, 255, 0.95) !important;
      border: none !important;
      box-shadow: 0 10px 25px rgba(15, 23, 42, 0.15) !important;
    }

    body:not(.dark-mode) .card.bg-primary-gradient h2,
    body:not(.dark-mode) .card.bg-primary-gradient h3,
    body:not(.dark-mode) .card.bg-primary-gradient p,
    body:not(.dark-mode) .card.bg-primary-gradient span {
      color: rgba(255, 255, 255, 0.95) !important;
    }

    /* --- Web App Layout & Navigation (Light Mode Specifics) --- */
    body:not(.dark-mode) .app-header {
      padding: 12px 20px;
      background: rgba(248, 250, 252, 0.8) !important;
      backdrop-filter: blur(16px) !important;
      -webkit-backdrop-filter: blur(16px) !important;
      display: grid !important;
      grid-template-columns: 40px 1fr 40px;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 50;
      border-bottom: 1px solid var(--border) !important;
    }

    body:not(.dark-mode) .app-header h1 {
      grid-column: 2;
      text-align: center;
      font-size: 18px !important;
      font-weight: 700;
      color: var(--text) !important;
      margin: 0;
    }

    body:not(.dark-mode) .header-btn {
      background: #FFFFFF !important;
      border: 1px solid var(--border) !important;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--text) !important;
      cursor: pointer;
      box-shadow: var(--shadow-sm) !important;
      transition: all 0.2s ease;
    }

    body:not(.dark-mode) .header-btn:active {
      transform: scale(0.95);
      background: rgba(14, 165, 233, 0.05) !important;
    }

    .app-header .header-btn[onclick*="backward"] {
      grid-column: 1;
      justify-self: start;
    }

    .app-header .header-btn[onclick*="toggleLanguage"],
    .app-header .header-btn[onclick*="bell"] {
      grid-column: 3;
      justify-self: end;
    }

    body:not(.dark-mode) .bottom-nav {
      background: rgba(255, 255, 255, 0.85) !important;
      backdrop-filter: blur(20px) !important;
      -webkit-backdrop-filter: blur(20px) !important;
      border: 1px solid var(--border) !important;
      box-shadow: 0 -4px 30px rgba(15, 23, 42, 0.05) !important;
    }

    .bottom-nav.active {
      display: flex;
    }

    .nav-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
      color: var(--text-muted) !important;
      cursor: pointer;
      transition: all 0.2s;
      position: relative;
      width: 60px;
    }

    .nav-item.active {
      color: var(--accent) !important;
    }

    .nav-item.active::after {
      content: '';
      width: 6px;
      height: 6px;
      background-color: var(--accent) !important;
      border-radius: 50%;
      position: absolute;
      bottom: -10px;
    }

    body.dark-mode .login-role-card {
      background: var(--surface-solid) !important;
      border: 1px solid var(--border) !important;
      color: var(--text) !important;
      box-shadow: var(--shadow-sm) !important;
      border-radius: 20px !important;
      padding: 16px;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      cursor: pointer;
      transition: all 0.3s ease !important;
    }

    body.dark-mode .login-role-card:hover {
      border-color: var(--accent) !important;
      transform: translateY(-3px);
      box-shadow: var(--shadow-glass) !important;
    }

    .status-bar {
      height: 44px;
      color: #0F172A !important;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 24px;
      font-size: 14px;
      font-weight: 600;
      z-index: 100;
      position: relative;
      margin-top: 6px;
    }

    .status-bar .notch {
      width: 140px;
      height: 30px;
      background-color: #1E293B;
      position: absolute;
      top: -6px;
      left: 50%;
      transform: translateX(-50%);
      border-bottom-left-radius: 20px;
      border-bottom-right-radius: 20px;
      z-index: 99;
    }

    .status-bar .left-indicators {
      display: flex;
      align-items: center;
      gap: 4px;
      z-index: 101;
      margin-top: -6px;
      font-family: -apple-system, BlinkMacSystemFont, sans-serif;
      letter-spacing: -0.2px;
      font-size: 15px;
    }

    .status-bar .right-indicators {
      display: flex;
      align-items: center;
      gap: 6px;
      z-index: 101;
      margin-top: -6px;
    }

    .home-indicator-bar {
      position: absolute;
      bottom: 8px;
      left: 50%;
      transform: translateX(-50%);
      width: 130px;
      height: 5px;
      background-color: #0F172A !important;
      border-radius: 100px;
      z-index: 100;
    }

    @keyframes spin {
      100% {
        transform: rotate(360deg);
      }
    }

    .loading-overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(248, 250, 252, 0.85) !important;
      backdrop-filter: blur(10px);
      z-index: 999;
      display: none;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }

    .spinner {
      width: 44px;
      height: 44px;
      border: 4px solid rgba(14, 165, 233, 0.2);
      border-top-color: var(--accent);
      border-radius: 50%;
      animation: spin 1s linear infinite;
    }

    .loading-overlay p {
      color: var(--accent) !important;
      font-weight: 700;
      margin-top: 16px;
      font-family: var(--font-heading);
    }

    /* Inputs & Buttons (Light Mode Specifics) */
    body:not(.dark-mode) .form-input {
      background: rgba(255, 255, 255, 0.8) !important;
      color: var(--text) !important;
      border: 1.5px solid rgba(14, 165, 233, 0.15) !important;
      width: 100%;
      padding: 14px 16px;
      border-radius: 14px;
      font-size: 14px;
      margin-bottom: 12px;
      transition: all 0.2s ease;
    }

    body:not(.dark-mode) .form-input::placeholder {
      color: var(--text-muted) !important;
    }

    body:not(.dark-mode) .form-input:focus {
      border-color: var(--accent) !important;
      background: #FFFFFF !important;
      box-shadow: 0 0 0 3px rgba(14, 165, 233, 0.15) !important;
    }

    body:not(.dark-mode) .btn-secondary {
      background: rgba(255, 255, 255, 0.85) !important;
      color: var(--text) !important;
      border: 1px solid rgba(14, 165, 233, 0.20) !important;
      border-radius: 14px;
      padding: 14px;
      font-weight: 600;
      transition: all 0.2s ease;
      box-shadow: 0 2px 8px rgba(14, 165, 233, 0.06) !important;
    }

    body:not(.dark-mode) .btn-secondary:hover {
      background: rgba(14, 165, 233, 0.07) !important;
      border-color: rgba(14, 165, 233, 0.35) !important;
    }

    body:not(.dark-mode) .btn-secondary:active {
      transform: scale(0.97);
      background: rgba(14, 165, 233, 0.10) !important;
    }

    body:not(.dark-mode) .btn-accent {
      background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%) !important;
      color: white !important;
      border: none;
      padding: 14px;
      border-radius: 14px;
      font-weight: 700;
      box-shadow: 0 6px 18px rgba(14, 165, 233, 0.2) !important;
      transition: all 0.2s ease;
    }

    body:not(.dark-mode) .btn-accent:active {
      transform: scale(0.97);
      box-shadow: 0 3px 8px rgba(14, 165, 233, 0.12) !important;
    }

    body:not(.dark-mode) .btn-danger {
      background: var(--danger-light) !important;
      color: var(--danger) !important;
      border: 1px solid rgba(239, 68, 68, 0.2) !important;
      border-radius: 14px;
      padding: 14px;
      font-weight: 600;
    }

    /* Dark Mode Fallbacks for older general styles (Not touched dark mode) */
    body.dark-mode .app-header {
      padding: 12px 20px;
      background: rgba(5, 13, 26, 0.8) !important;
      backdrop-filter: blur(16px) !important;
      -webkit-backdrop-filter: blur(16px) !important;
      display: grid !important;
      grid-template-columns: 40px 1fr 40px;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 50;
      border-bottom: 1px solid var(--border) !important;
    }

    body.dark-mode .app-header h1 {
      grid-column: 2;
      text-align: center;
      font-size: 18px !important;
      font-weight: 700;
      color: var(--text) !important;
      margin: 0;
    }

    body.dark-mode .header-btn {
      background: #0b1329 !important;
      color: var(--text) !important;
      border: 1px solid var(--border) !important;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: var(--shadow-sm) !important;
      transition: all 0.2s ease;
    }

    body.dark-mode .bottom-nav {
      background: rgba(11, 19, 41, 0.95) !important;
      border: 1px solid var(--border) !important;
      box-shadow: 0 -4px 30px rgba(15, 23, 42, 0.04) !important;
    }

    body.dark-mode .form-input {
      background: #0b1329 !important;
      color: var(--text) !important;
      border: 1px solid var(--border) !important;
      width: 100%;
      padding: 12px;
      border-radius: 12px;
      font-size: 14px;
      margin-bottom: 12px;
    }

    body.dark-mode .btn-secondary {
      background: #0b1329 !important;
      color: var(--text) !important;
      border: 1px solid var(--border) !important;
    }

    body.dark-mode .btn-accent {
      background: var(--accent);
      color: white;
      border: none;
      padding: 12px;
      border-radius: 12px;
      font-weight: 600;
      cursor: pointer;
    }

    body.dark-mode .btn-danger {
      background: var(--danger-light);
      color: var(--danger);
      border: 1px solid rgba(239, 68, 68, 0.2);
    }

    .badge-danger {
      background: var(--danger-light);
      color: var(--danger);
    }

    .badge-warning {
      background: var(--warning-light);
      color: var(--warning);
    }

    .badge-info {
      background: #DBEAFE;
      color: #1D4ED8;
    }

    .badge-muted {
      background: var(--surface-solid);
      color: var(--text-muted);
      border: 1px solid var(--border);
    }

    .badge-success {
      background: var(--success-light);
      color: var(--success);
    }

    .badge {
      padding: 4px 8px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
    }

    .calendar-grid {
      display: grid;
      grid-template-columns: repeat(7, 1fr);
      gap: 6px;
      margin-top: 10px;
    }

    .calendar-day {
      background: var(--surface-solid) !important;
      border: 1px solid var(--border) !important;
      color: var(--text) !important;
      aspect-ratio: 1;
      border-radius: 10px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-size: 13px;
      font-weight: 600;
      position: relative;
      cursor: pointer;
      box-shadow: var(--shadow-sm);
    }

    body:not(.dark-mode) .calendar-day {
      background: rgba(255, 255, 255, 0.75) !important;
      border: 1px solid rgba(14, 165, 233, 0.1) !important;
      box-shadow: 0 2px 6px rgba(15, 23, 42, 0.01) !important;
    }

    .calendar-day.empty {
      background: transparent !important;
      border: none !important;
      box-shadow: none !important;
    }

    .calendar-day.event::after {
      content: '';
      width: 4px;
      height: 4px;
      background-color: var(--accent);
      border-radius: 50%;
      position: absolute;
      bottom: 4px;
    }

    .calendar-day.holiday {
      background-color: var(--danger-light);
      color: var(--danger);
      border-color: rgba(239, 68, 68, 0.2);
    }

    .segment-bar {
      background: rgba(255, 255, 255, 0.6) !important;
      border: 1px solid var(--border) !important;
      padding: 6px !important;
      border-radius: 16px !important;
      display: flex;
      margin-bottom: 16px;
      backdrop-filter: blur(8px);
    }

    body:not(.dark-mode) .segment-bar {
      background: rgba(255, 255, 255, 0.75) !important;
      border: 1px solid rgba(14, 165, 233, 0.12) !important;
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.02) !important;
    }

    .segment-btn {
      color: var(--text-muted) !important;
      flex: 1;
      border: none;
      background: none;
      padding: 8px;
      font-size: 13px;
      font-weight: 600;
      border-radius: 10px;
      cursor: pointer;
      transition: all 0.2s;
      font-family: var(--font-heading);
    }

    .segment-btn.active {
      background: #FFFFFF !important;
      color: var(--accent) !important;
      box-shadow: var(--shadow-sm) !important;
    }

    body:not(.dark-mode) .segment-btn.active {
      background: #FFFFFF !important;
      color: var(--accent) !important;
      box-shadow: 0 4px 10px rgba(15, 23, 42, 0.04) !important;
    }

    .profile-avatar-circle {
      width: 80px;
      height: 80px;
      background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
      color: white;
      border-radius: 24px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 28px;
      font-weight: 800;
      font-family: var(--font-heading);
      box-shadow: 0 10px 20px rgba(15, 23, 42, 0.15);
      margin: 0 auto 16px;
    }

    body:not(.dark-mode) .profile-avatar-circle {
      background: linear-gradient(135deg, #1d4ed8 0%, #0ea5e9 100%) !important;
      box-shadow: 0 10px 20px rgba(14, 165, 233, 0.2) !important;
    }

    .account-header {
      text-align: center;
      margin-top: 20px;
      margin-bottom: 30px;
    }

    .account-name {
      font-size: 20px;
      font-weight: 700;
      color: var(--text) !important;
      font-family: var(--font-heading);
    }

    .account-email {
      font-size: 12px;
      color: var(--text-muted);
      margin-top: 4px;
    }

    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
      color: var(--text) !important;
      line-height: 1.3;
    }

    p {
      color: var(--text-muted) !important;
      line-height: 1.5;
    }

    .text-gradient {
      background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%) !important;
      -webkit-background-clip: text !important;
      -webkit-text-fill-color: transparent !important;
    }

    body:not(.dark-mode) .text-gradient {
      background: linear-gradient(135deg, #1d4ed8 0%, #0ea5e9 100%) !important;
      -webkit-background-clip: text !important;
      -webkit-text-fill-color: transparent !important;
    }

    .desktop-title,
    .desktop-title span {
      color: #FFFFFF !important;
    }

    .role-title {
      color: var(--text) !important;
      font-weight: 800 !important;
    }

    .role-desc {
      color: var(--text-muted) !important;
    }

    .smart-login-header h2 {
      color: var(--text) !important;
    }

    .smart-login-header p {
      color: var(--text-muted) !important;
    }

    /* --- RESTORED COMPONENT WIDGETS --- */
    /* Child Switcher Banner Pill */
    .child-switcher {
      display: flex;
      gap: 8px;
      background-color: var(--surface-solid);
      border-radius: 20px;
      padding: 4px;
      margin-bottom: 12px;
      border: 1.5px solid var(--border);
    }

    body:not(.dark-mode) .child-switcher {
      background: rgba(255, 255, 255, 0.75) !important;
      border: 1px solid rgba(14, 165, 233, 0.12) !important;
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.02) !important;
    }

    .child-pill {
      flex: 1;
      text-align: center;
      padding: 6px 12px;
      font-size: 13px;
      font-weight: 600;
      border-radius: 16px;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.2s;
    }

    .child-pill.active {
      background-color: var(--accent) !important;
      color: #FFFFFF !important;
    }

    /* Donut chart simulation */
    .attendance-radial-panel {
      display: flex;
      align-items: center;
      gap: 20px;
    }

    .radial-circle {
      width: 80px;
      height: 80px;
      border-radius: 50%;
      background: conic-gradient(var(--accent) 0% 90%, var(--border) 90% 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }

    .radial-circle::before {
      content: '90%' !important;
      position: absolute;
      width: 62px;
      height: 62px;
      background-color: var(--surface-solid) !important;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 16px;
      color: var(--text) !important;
    }

    /* --- DARK MODE TRANSITIONS & OVERRIDES --- */
    body.dark-mode {
      --bg: #050d1a !important;
      --app-bg: #050d1a !important;
      --app-bg-gradient: linear-gradient(135deg, rgba(0, 212, 255, 0.05) 0%, #050d1a 100%) !important;
      --surface: rgba(11, 19, 41, 0.85) !important;
      --surface-solid: #0b1329 !important;
      --text: #f8fafc !important;
      --text-muted: #94a3b8 !important;
      --border: rgba(0, 212, 255, 0.15) !important;
      --shadow-glass: 0 10px 40px rgba(0, 0, 0, 0.4) !important;
      --shadow-sm: 0 4px 10px rgba(0, 0, 0, 0.2) !important;
      --primary: #0ea5e9 !important;
      --primary-light: #1e293b !important;
      --accent: #00d4ff !important;
      --accent-light: rgba(0, 212, 255, 0.08) !important;
    }

    body.dark-mode .app-header {
      background: rgba(5, 13, 26, 0.8) !important;
      border-bottom: 1px solid var(--border) !important;
    }

    body.dark-mode .header-btn {
      background: #0b1329 !important;
      color: var(--text) !important;
      border: 1px solid var(--border) !important;
    }

    body.dark-mode .bottom-nav {
      background: rgba(11, 19, 41, 0.95) !important;
      border: 1px solid var(--border) !important;
    }

    body.dark-mode .chat-bubble.received {
      background: #0b1329 !important;
      color: var(--text) !important;
      border: 1px solid var(--border) !important;
    }

    body.dark-mode .chat-input-bar {
      background: rgba(5, 13, 26, 0.95) !important;
      border-top: 1px solid var(--border) !important;
    }

    body.dark-mode .chat-input-bar .form-input {
      background: #0b1329 !important;
      color: var(--text) !important;
    }

    body.dark-mode .form-input {
      background: #0b1329 !important;
      color: var(--text) !important;
      border: 1px solid var(--border) !important;
    }

    body.dark-mode .btn-secondary {
      background: rgba(255, 255, 255, 0.06) !important;
      color: var(--text) !important;
      border: 1px solid var(--border) !important;
    }

    body.dark-mode .btn-secondary:hover {
      background: rgba(255, 255, 255, 0.12) !important;
    }

    body.dark-mode .home-indicator-bar {
      background-color: #f8fafc !important;
    }

    body.dark-mode .status-bar {
      color: #f8fafc !important;
    }

    body.dark-mode .loading-overlay {
      background: rgba(5, 13, 26, 0.85) !important;
    }

    body.dark-mode .segment-bar {
      background: rgba(11, 19, 41, 0.6) !important;
      border: 1px solid var(--border) !important;
    }

    body.dark-mode .segment-btn.active {
      background: #0d1b32 !important;
      color: var(--accent) !important;
    }

    body.dark-mode .card.bg-primary-gradient {
      background: linear-gradient(135deg, #0b1329 0%, #162545 100%) !important;
      border: 1px solid var(--border) !important;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3) !important;
    }

    body.dark-mode .card.bg-primary-gradient h2,
    body.dark-mode .card.bg-primary-gradient h3,
    body.dark-mode .card.bg-primary-gradient p,
    body.dark-mode .card.bg-primary-gradient span {
      color: rgba(255, 255, 255, 0.95) !important;
    }

    /* Premium Dark Mode Card Layout & Spacing Uniformity */
    body.dark-mode .card,
    body.dark-mode .glass-card,
    body.dark-mode .kpi-glass,
    body.dark-mode .kpi-card {
      background: rgba(11, 19, 41, 0.85) !important;
      backdrop-filter: blur(20px) !important;
      -webkit-backdrop-filter: blur(20px) !important;
      border: 1px solid rgba(0, 212, 255, 0.15) !important;
      box-shadow:
        0 4px 6px -1px rgba(0, 0, 0, 0.2),
        0 10px 30px -3px rgba(0, 0, 0, 0.4) !important;
      border-radius: 24px !important;
      padding: 24px;
      margin-bottom: 16px;
    }

    /* Premium Chat UI */
    .chat-box {
      flex: 1;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 12px;
      padding: 20px;
      padding-bottom: 100px;
      height: 100%;
    }

    .chat-bubble {
      max-width: 80%;
      padding: 12px 16px;
      border-radius: 20px;
      font-size: 14px;
      line-height: 1.4;
      position: relative;
      box-shadow: var(--shadow-sm);
    }

    .chat-bubble p {
      margin: 0;
      color: inherit !important;
    }

    .chat-bubble.received {
      background: #FFFFFF !important;
      color: var(--text) !important;
      align-self: flex-start;
      border-bottom-left-radius: 4px;
      border: 1px solid var(--border);
    }

    .chat-bubble.sent {
      background: var(--primary) !important;
      color: #FFFFFF !important;
      align-self: flex-end;
      border-bottom-right-radius: 4px;
      box-shadow: 0 4px 15px rgba(15, 23, 42, 0.15);
      border: none;
    }

    .chat-time {
      font-size: 11px;
      margin-top: 6px;
      display: block;
      opacity: 0.7;
      text-align: right;
    }

    .chat-bubble.sent .chat-time {
      color: rgba(255, 255, 255, 0.8);
    }

    .chat-input-bar {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      padding: 12px 20px;
      padding-bottom: 24px;
      background: rgba(255, 255, 255, 0.95) !important;
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-top: 1px solid var(--border);
      display: flex;
      gap: 12px;
      align-items: center;
      z-index: 250;
      box-shadow: 0 -10px 30px rgba(15, 23, 42, 0.02);
    }

    .chat-input-bar .form-input {
      margin-bottom: 0;
      background: #F8FAFC !important;
      border: 1px solid rgba(14, 165, 233, 0.2) !important;
      padding: 12px 16px;
      border-radius: 24px;
      box-shadow: none;
      color: var(--text) !important;
    }

    .chat-input-bar .form-input:focus {
      border-color: var(--accent) !important;
      box-shadow: 0 0 0 3px rgba(14, 165, 233, 0.15) !important;
    }

    .chat-input-bar .header-btn {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: var(--accent) !important;
      color: white !important;
      border: none !important;
      box-shadow: 0 4px 10px rgba(14, 165, 233, 0.3) !important;
      transition: transform 0.2s;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .chat-input-bar .header-btn:active {
      transform: scale(0.9);
    }

    .chat-input-bar .header-btn i {
      color: white !important;
    }

    /* Ensure screen content fills space properly for absolute positioning of input */
    #parent-chat .screen-content,
    #teacher-chat .screen-content {
      padding: 0 !important;
      height: 100%;
      position: relative;
      background: transparent !important;
    }

    /* ── TOAST NOTIFICATION SYSTEM ── */
    #toast-container {
      position: absolute;
      top: 60px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 9999;
      display: flex;
      flex-direction: column;
      gap: 8px;
      align-items: center;
      width: 92%;
      pointer-events: none;
    }

    .toast {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 12px 16px;
      border-radius: 14px;
      font-size: 13px;
      font-weight: 600;
      font-family: var(--font-heading);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.18);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      pointer-events: auto;
      width: 100%;
      max-width: 320px;
      animation: toastIn 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #fff;
    }

    .toast.toast-success {
      background: linear-gradient(135deg, #10b981ee 0%, #059669ee 100%);
    }

    .toast.toast-error {
      background: linear-gradient(135deg, #ef4444ee 0%, #dc2626ee 100%);
    }

    .toast.toast-info {
      background: linear-gradient(135deg, #0ea5e9ee 0%, #0284c7ee 100%);
    }

    .toast.toast-warning {
      background: linear-gradient(135deg, #f59e0bee 0%, #d97706ee 100%);
    }

    .toast .toast-icon {
      width: 20px;
      height: 20px;
      flex-shrink: 0;
    }

    .toast .toast-msg {
      flex: 1;
      line-height: 1.35;
    }

    .toast .toast-close {
      background: none;
      border: none;
      color: rgba(255, 255, 255, 0.7);
      cursor: pointer;
      padding: 0;
      display: flex;
      font-size: 16px;
    }

    .toast .toast-close:hover {
      color: #fff;
    }

    @keyframes toastIn {
      from {
        opacity: 0;
        transform: translateY(-16px) scale(0.94);
      }

      to {
        opacity: 1;
        transform: translateY(0) scale(1);
      }
    }

    @keyframes toastOut {
      from {
        opacity: 1;
        transform: translateY(0) scale(1);
      }

      to {
        opacity: 0;
        transform: translateY(-12px) scale(0.94);
      }
    }

    .toast.removing {
      animation: toastOut 0.28s cubic-bezier(0.4, 0, 1, 1) forwards;
    }

    /* ── CUSTOM CONFIRM DIALOG ── */
    #toast-confirm-overlay {
      position: absolute;
      inset: 0;
      background: rgba(0, 0, 0, 0.45);
      backdrop-filter: blur(6px);
      z-index: 10000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }

    #toast-confirm-overlay.open {
      display: flex;
    }

    #toast-confirm-box {
      background: var(--surface-solid);
      border-radius: 20px;
      padding: 24px 20px 20px;
      width: 100%;
      max-width: 300px;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.35);
      border: 1px solid var(--border);
      animation: toastIn 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    #toast-confirm-icon {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: rgba(239, 68, 68, 0.12);
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto 12px;
    }

    #toast-confirm-title {
      font-size: 16px;
      font-weight: 700;
      color: var(--text);
      text-align: center;
      margin-bottom: 6px;
      font-family: var(--font-heading);
    }

    #toast-confirm-msg {
      font-size: 13px;
      color: var(--text-muted);
      text-align: center;
      line-height: 1.5;
      margin-bottom: 20px;
    }

    .confirm-btns {
      display: flex;
      gap: 10px;
    }

    .confirm-btns button {
      flex: 1;
      border: none;
      border-radius: 12px;
      padding: 12px;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      font-family: var(--font-heading);
      transition: transform 0.15s, opacity 0.15s;
    }

    .confirm-btns button:active {
      transform: scale(0.96);
      opacity: 0.85;
    }

    #toast-confirm-cancel {
      background: var(--bg, #F8FAFC);
      color: var(--text-muted);
      border: 1px solid var(--border) !important;
    }

    #toast-confirm-ok {
      background: linear-gradient(135deg, #ef4444, #dc2626);
      color: #fff;
    }

    /* Responsive styles to hide smartphone mockup frame on mobile viewports/PWAs */
    @media (max-width: 768px) {
      body {
        background-color: var(--bg);
        background-image: none;
      }

      .desktop-container {
        padding: 0 !important;
        gap: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
      }

      .desktop-title {
        display: none !important;
      }

      .phone-mockup {
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
        border-radius: 0 !important;
        box-shadow: none !important;
        padding-top: env(safe-area-inset-top, 20px) !important;
      }

      .status-bar {
        display: none !important;
      }
    }

    /* Segmented Control */
    .segment-control {
      display: flex;
      background: var(--bg-color);
      border-radius: 12px;
      padding: 4px;
      gap: 4px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }

    .segment-btn {
      flex: 1;
      text-align: center;
      padding: 10px 0;
      font-size: 14px;
      font-weight: 600;
      color: var(--text-muted);
      border-radius: 8px;
      transition: all 0.2s ease;
    }

    .segment-btn.active {
      background: var(--primary);
      color: white;
      box-shadow: 0 2px 6px rgba(11, 87, 208, 0.3);
    }

    /* PWA Install Banner styles (adaptable for light and dark modes) */
    #pwa-install-banner {
      display: none;
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      z-index: 9999;
      padding: 14px 20px;
      align-items: center;
      gap: 12px;
      transition: all 0.3s ease;
    }

    body:not(.dark-mode) #pwa-install-banner {
      background: rgba(255, 255, 255, 0.85) !important;
      backdrop-filter: blur(20px) !important;
      -webkit-backdrop-filter: blur(20px) !important;
      border-top: 1px solid rgba(14, 165, 233, 0.15) !important;
      box-shadow: 0 -10px 30px rgba(15, 23, 42, 0.05) !important;
    }

    body.dark-mode #pwa-install-banner {
      background: linear-gradient(135deg, #1A2E55, #0F172A) !important;
      border-top: 1px solid rgba(14, 165, 233, 0.3) !important;
      box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.4) !important;
    }

    body:not(.dark-mode) .pwa-banner-title {
      color: var(--text) !important;
    }

    body.dark-mode .pwa-banner-title {
      color: #fff !important;
    }

    body:not(.dark-mode) .pwa-banner-desc {
      color: var(--text-muted) !important;
    }

    body.dark-mode .pwa-banner-desc {
      color: rgba(255, 255, 255, 0.6) !important;
    }

    body:not(.dark-mode) .pwa-banner-close {
      color: var(--text-muted) !important;
    }

    body.dark-mode .pwa-banner-close {
      color: rgba(255, 255, 255, 0.5) !important;
    }

    /* ── FLOATING GLASS BACK BUTTON ── */
    .floating-back-btn {
      position: absolute;
      bottom: 104px;
      /* Positioned close to the navbar without touching or merging */
      right: 24px;
      width: 52px;
      height: 52px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.35);
      backdrop-filter: blur(20px) saturate(180%);
      -webkit-backdrop-filter: blur(20px) saturate(180%);
      border: 1px solid var(--border);
      /* Sync border color with other glass cards */
      box-shadow: 0 8px 32px 0 rgba(15, 23, 42, 0.08), inset 0 0 0 1px rgba(255, 255, 255, 0.3);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--text);
      cursor: pointer;
      z-index: 100;
      transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
      opacity: 0;
      pointer-events: none;
      transform: translateY(12px) scale(0.8);

      /* Completely reset native mobile button borders & appearance */
      appearance: none;
      -webkit-appearance: none;
      outline: none;
    }

    .floating-back-btn.visible {
      opacity: 1;
      pointer-events: auto;
      transform: translateY(0) scale(1);
    }

    .floating-back-btn:active {
      transform: scale(0.92);
      background: rgba(255, 255, 255, 0.55);
      border-color: rgba(255, 255, 255, 0.7);
    }

    /* Dark Mode styling for Floating Back Button */
    body.dark-mode .floating-back-btn {
      background: rgba(11, 19, 41, 0.35) !important;
      backdrop-filter: blur(20px) saturate(180%) !important;
      -webkit-backdrop-filter: blur(20px) saturate(180%) !important;
      border: 1px solid var(--border) !important;
      color: #00d4ff !important;
      box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.05) !important;
    }

    body.dark-mode .floating-back-btn:active {
      background: rgba(11, 19, 41, 0.55) !important;
      border-color: rgba(0, 212, 255, 0.4) !important;
    }

    /* Theme-specific logo visibility */
    body.dark-mode .logo-light {
      display: none !important;
    }
    body:not(.dark-mode) .logo-dark {
      display: none !important;
    }

    /* Splash Screen Premium Styling */
    #splash {
      background: radial-gradient(circle at 50% 50%, #1e293b 0%, #0f172a 100%) !important;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
    }
    .splash-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 16px;
      animation: fadeIn 1.2s ease-out;
    }
    .splash-logo {
      width: 120px;
      height: 120px;
      margin-bottom: 8px;
      filter: drop-shadow(0 8px 24px rgba(0, 212, 255, 0.2));
      animation: pulseLogo 2s infinite ease-in-out;
    }
    @keyframes pulseLogo {
      0%, 100% { transform: scale(1); filter: drop-shadow(0 8px 24px rgba(0, 212, 255, 0.2)); }
      50% { transform: scale(1.05); filter: drop-shadow(0 12px 32px rgba(0, 212, 255, 0.45)); }
    }
  </style>"""

    html = html[:style_start] + new_css + html[style_end + 8:]

    # 2. Replace Login Screen HTML
    login_start = html.find('<div class="screen" id="login">')
    login_end = html.find('<!-- ════ SCREEN 3: PARENT HOME SCREEN ════ -->')
    if login_start != -1 and login_end != -1:
        new_login = """<div class="screen" id="login">
          <div class="loading-overlay" id="login-spinner">
            <div class="spinner"></div>
            <p style="margin-top:16px;font-weight:700;font-family:var(--font-heading);color:var(--text);">
              Authenticating...</p>
          </div>

          <div class="screen-content"
            style="padding: 24px; display: flex; flex-direction: column; justify-content: center; height: 100%;">

            <!-- VIEW A: ROLE SELECTION -->
            <div id="login-role-select-view" style="display: flex; flex-direction: column; width: 100%;">
              <div class="smart-login-header">
                <div class="logo-light"
                  style="width: 80px; height: 80px; background: var(--surface-solid); border: 1.5px solid var(--border); border-radius: 24px; display: inline-flex; align-items: center; justify-content: center; box-shadow: var(--shadow-glass); margin-bottom: 20px; padding: 6px; box-sizing: border-box;">
                  <img src="logo-blue.png?v=13" alt="MTS Logo" style="width: 100%; height: 100%; object-fit: contain;">
                </div>
                <div class="logo-dark"
                  style="width: 80px; height: 80px; background: var(--surface-solid); border: 1.5px solid var(--border); border-radius: 24px; display: inline-flex; align-items: center; justify-content: center; box-shadow: var(--shadow-glass); margin-bottom: 20px; padding: 6px; box-sizing: border-box;">
                  <img src="logo-silver.png?v=13" alt="MTS Logo" style="width: 100%; height: 100%; object-fit: contain;">
                </div>
                <h2 style="font-family: var(--font-heading); font-weight: 800; font-size: 28px; color: var(--text);">
                  Welcome to <br><span class="text-gradient">MTS Connect</span></h2>
                <p style="font-size: 14px; color: var(--text-muted); margin-top: 8px;" class="lang-en">Select your role
                  to explore the smart campus.</p>
                <p style="font-size: 14px; color: var(--text-muted); margin-top: 8px;" class="lang-ta">ஸ்மார்ட் வளாகத்தை
                  ஆராய உங்கள் பாத்திரத்தைத் தேர்ந்தெடுக்கவும்.</p>
              </div>

              <div class="demo-login-cards" style="margin-top: 20px;">
                <div class="login-role-card" onclick="selectLoginRole('parent')">
                  <div class="role-icon" style="background: rgba(16, 185, 129, 0.1); color: #10B981;">👨‍👩‍👦</div>
                  <div class="role-info">
                    <div class="role-title">Parent Portal</div>
                    <div class="role-desc">View attendance, homework & news</div>
                  </div>
                  <i data-lucide="chevron-right" style="color: #CBD5E1;"></i>
                </div>

                <div class="login-role-card" onclick="selectLoginRole('teacher')">
                  <div class="role-icon" style="background: rgba(59, 130, 246, 0.1); color: #3B82F6;">👩‍🏫</div>
                  <div class="role-info">
                    <div class="role-title">Teacher Dashboard</div>
                    <div class="role-desc">Manage classes & grading</div>
                  </div>
                  <i data-lucide="chevron-right" style="color: #CBD5E1;"></i>
                </div>

                <div class="login-role-card" onclick="selectLoginRole('admin')">
                  <div class="role-icon" style="background: rgba(245, 158, 11, 0.1); color: #F59E0B;">👑</div>
                  <div class="role-info">
                    <div class="role-title">Admin Console</div>
                    <div class="role-desc">School oversight & approvals</div>
                  </div>
                  <i data-lucide="chevron-right" style="color: #CBD5E1;"></i>
                </div>
              </div>
            </div>

            <!-- VIEW B: CREDENTIALS INPUT -->
            <div id="login-credentials-view" style="display: none; flex-direction: column; width: 100%;">
              <div class="smart-login-header" style="margin-bottom: 24px; text-align: left;">
                <button type="button" onclick="goBackToRoles()"
                  style="margin-left: -4px; margin-bottom: 16px; display: inline-flex; align-items: center; gap: 6px; border: none; background: none; color: var(--accent); font-weight: 700; font-size: 14px; cursor: pointer; padding: 4px 0;">
                  <i data-lucide="arrow-left" style="width: 18px; height: 18px;"></i>
                  <span class="lang-en">Back to Roles</span>
                  <span class="lang-ta">திரும்புக</span>
                </button>
                <h2 id="login-form-title"
                  style="font-family: var(--font-heading); font-weight: 800; font-size: 26px; color: var(--text);">Login
                </h2>
                <p id="login-form-subtitle" style="font-size: 14px; color: var(--text-muted); margin-top: 4px;">Please
                  enter your credentials below.</p>
              </div>

              <form onsubmit="event.preventDefault(); processLogin();"
                style="display: flex; flex-direction: column; gap: 16px; width: 100%;">
                <div class="form-group" style="margin-bottom: 16px; text-align: left; width: 100%;">
                  <label class="form-label" for="login-email" style="margin-bottom: 6px;">Email Address</label>
                  <input type="email" id="login-email" class="form-input" placeholder="e.g. user@mts.edu" required
                    style="box-sizing: border-box; width: 100%;">
                </div>

                <div class="form-group" style="margin-bottom: 8px; text-align: left; width: 100%;">
                  <label class="form-label" for="login-password" style="margin-bottom: 6px;">Password</label>
                  <div style="position: relative; width: 100%;">
                    <input type="password" id="login-password" class="form-input" placeholder="••••••••" required
                      style="box-sizing: border-box; padding-right: 48px; width: 100%;">
                    <button type="button" onclick="togglePasswordInput()"
                      style="position: absolute; right: 12px; top: 50%; transform: translateY(-50%); background: none; border: none; color: var(--text-muted); cursor: pointer; display: flex; align-items: center; justify-content: center; padding: 4px;">
                      <i data-lucide="eye" id="eye-icon" style="width: 20px; height: 20px;"></i>
                    </button>
                  </div>
                </div>

                <button type="submit" class="btn btn-accent"
                  style="width: 100%; padding: 14px; border-radius: 12px; font-weight: 700; font-size: 16px; margin-top: 8px;">Sign
                  In</button>

                <div style="text-align: center; margin-top: 8px; width: 100%;">
                  <a href="#" onclick="event.preventDefault(); autoFillDemoCreds();"
                    style="color: var(--accent); font-size: 13.5px; font-weight: 600; text-decoration: none;">Auto-fill
                    Demo Credentials</a>
                </div>
              </form>
            </div>

            <!-- Language/Theme Controls -->
            <div
              style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 32px; animation: fadeIn 0.5s ease-out forwards; opacity: 0; animation-delay: 0.4s; transform: translateY(10px); width: 100%;">
              <button onclick="toggleLanguage()" class="login-action-btn">
                <i data-lucide="languages"></i>
                <div class="btn-text-col">
                  <span>Language</span>
                  <small>மொழி</small>
                </div>
              </button>
              <button onclick="toggleTheme()" class="login-action-btn">
                <i data-lucide="moon" id="login-theme-icon"></i>
                <div class="btn-text-col">
                  <span id="login-theme-text-en">Theme</span>
                  <small id="login-theme-text-ta">தீம்</small>
                </div>
              </button>
            </div>
          </div>
        </div>

        """
        html = html[:login_start] + new_login + html[login_end:]

    # 3. Replace Parent Home Screen to use Glass Cards
    phome_start = html.find('<div class="screen" id="parent-home">')
    phome_end = html.find('<!-- ════ SCREEN 4: PARENT CHILDREN LIST ════ -->')
    
    if phome_start != -1 and phome_end != -1:
        new_phome = """<div class="screen" id="parent-home">
          <div class="app-header">
            <h1 class="lang-en">Parent Portal</h1>
            <h1 class="lang-ta">பெற்றோர் தளம்</h1>
            <button class="header-btn" onclick="toggleLanguage()"><i data-lucide="globe"></i></button>
          </div>
          <div class="screen-content">
            <!-- Active Child Selector pill -->
            <div class="child-switcher" id="parent-child-toggle">
              <div class="child-pill active" onclick="switchChild('Anika Kumar')">Anika</div>
              <div class="child-pill" onclick="switchChild('Rohan Kumar')">Rohan</div>
            </div>

            <!-- Todays Word Card -->
            <div class="card bg-primary-gradient">
              <span class="badge badge-success" style="margin-bottom:8px;">Word of the Day / இன்றைய சொல்</span>
              <h2 style="font-size:20px;font-weight:700;font-family:var(--font-tamil);">வணக்கம் (Vanakkam)</h2>
              <p style="font-size:14px;line-height:1.5;opacity:0.9;margin-top:4px;" class="lang-en">Greeting meaning
                "Hello" or "Welcome" in Tamil.</p>
              <p style="font-size:14px;line-height:1.5;opacity:0.9;margin-top:4px;" class="lang-ta">தமிழில் "ஹலோ" அல்லது
                "வரவேற்பு" என்று பொருள்படும் வாழ்த்துச் சொல்.</p>
            </div>

            <div class="kpi-grid">
              <div class="kpi-card kpi-green" onclick="showScreen('parent-attendance')">
                <div class="kpi-num" id="parent-kpi-att">90%</div>
                <div class="kpi-label lang-en">Attendance</div>
                <div class="kpi-label lang-ta">வருகைப்பதிவு</div>
              </div>
              <div class="kpi-card kpi-amber" onclick="showScreen('parent-homework')">
                <div class="kpi-num" id="parent-kpi-hw">1 / 2</div>
                <div class="kpi-label lang-en">Homework Done</div>
                <div class="kpi-label lang-ta">வீட்டுப்பாடம்</div>
              </div>
            </div>

            <!-- Attendance Donut widget -->
            <div class="card">
              <div class="card-title">
                <span class="lang-en">Attendance Overview</span>
                <span class="lang-ta">வருகை கண்ணோட்டம்</span>
              </div>
              <div class="attendance-radial-panel">
                <div class="radial-circle" id="parent-radial-chart"></div>
                <div>
                  <h4 style="font-size:14px;color:var(--text);" id="parent-attendance-class">Grade 3-A</h4>
                  <p style="font-size:14px;line-height:1.5;line-height:1.5;color: var(--text-muted);margin-top:4px;"
                    class="lang-en">Consistently present. Goal is 95%.</p>
                  <p style="font-size:14px;line-height:1.5;line-height:1.5;color: var(--text-muted);margin-top:4px;"
                    class="lang-ta">தொடர்ந்து வருகை தந்துள்ளார். இலக்கு 95%.</p>
                </div>
              </div>
            </div>

            <!-- Recent Broadcast announcements panel -->
            <div class="card">
              <div class="card-title">
                <span class="lang-en">Latest Broadcasts</span>
                <span class="lang-ta">சமீபத்திய அறிவிப்புகள்</span>
                <button
                  style="border:none;background:none;color:var(--accent);font-size:14px;line-height:1.5;line-height:1.5;font-weight:600;"
                  onclick="showScreen('parent-announcements')">See All</button>
              </div>
              <div id="parent-home-announcements-list">
                <!-- Seeding dynamic announcements list -->
              </div>
            </div>

            <!-- Quick PT meeting banner info -->
            <div class="card" style="border-left:4px solid var(--accent);" onclick="showScreen('parent-calendar')">
              <div style="display:flex;align-items:center;gap:12px;">
                <div
                  style="background-color:var(--accent-light);color:var(--accent);width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;">
                  <i data-lucide="handshake" style="width:20px;height:20px;"></i>
                </div>
                <div>
                  <h4 style="font-size:14px;line-height:1.5;color:var(--text);" class="lang-en">PT Meeting Slot Open
                  </h4>
                  <h4 style="font-size:14px;line-height:1.5;color:var(--text);" class="lang-ta">பெற்றோர்-ஆசிரியர்
                    கூட்டம்</h4>
                  <p style="font-size:14px;line-height:1.5;line-height:1.5;line-height:1.5;color: var(--text-muted);margin-top:2px;"
                    class="lang-en">Book slots for June 21 now</p>
                  <p style="font-size:14px;line-height:1.5;line-height:1.5;line-height:1.5;color: var(--text-muted);margin-top:2px;"
                    class="lang-ta">ஜூன் 21 க்கான நேரத்தை பதிவு செய்யவும்</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        """
        html = html[:phome_start] + new_phome + html[phome_end:]

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("Successfully overhauled UI!")

if __name__ == '__main__':
    rebuild()
