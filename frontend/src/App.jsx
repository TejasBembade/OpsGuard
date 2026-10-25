import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link, useLocation } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import AlertsPage from './pages/AlertsPage';
import LogsPage from './pages/LogsPage';
import PredictionsPage from './pages/PredictionsPage';

function NavLink({ to, children }) {
  const location = useLocation();
  const active = location.pathname === to;
  return (
    <Link to={to} className={`px-4 py-2 rounded-lg text-sm font-medium transition-all duration-200 ${
      active ? 'bg-cyan-500/20 text-cyan-400 border border-cyan-500/40' : 'text-gray-400 hover:text-white hover:bg-white/10'
    }`}>{children}</Link>
  );
}

function Nav() {
  return (
    <nav className="glass border-b border-cyan-500/10 px-6 py-4 flex items-center justify-between sticky top-0 z-50">
      <div className="flex items-center gap-3">
        <div className="w-9 h-9 rounded-lg animated-border p-0.5 flex items-center justify-center shadow-lg">
          <div className="w-full h-full rounded-[6px] bg-[#080d1a] flex items-center justify-center">
            <svg className="w-5 h-5 text-cyan-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
              <path d="m9 12 2 2 4-4"/>
            </svg>
          </div>
        </div>
        <div>
          <div className="flex items-center gap-2">
            <span className="text-white font-bold text-lg tracking-wide">Ops<span className="text-cyan-400">Guardian</span></span>
            <span className="text-[11px] font-medium px-2 py-0.5 bg-emerald-500/10 text-emerald-400 rounded-full border border-emerald-500/30">● Live</span>
          </div>
          <p className="text-[11px] text-slate-400 font-medium tracking-wider uppercase">Monitor. Detect. Recover.</p>
        </div>
      </div>
      <div className="flex gap-2">
        <NavLink to="/">Dashboard</NavLink>
        <NavLink to="/alerts">Alerts</NavLink>
        <NavLink to="/predictions">AI Predictions</NavLink>
        <NavLink to="/logs">Logs</NavLink>
      </div>
    </nav>
  );
}

export default function App() {
  return (
    <Router>
      <div className="min-h-screen">
        <Nav />
        <main className="p-6">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/alerts" element={<AlertsPage />} />
            <Route path="/predictions" element={<PredictionsPage />} />
            <Route path="/logs" element={<LogsPage />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}
