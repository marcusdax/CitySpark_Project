/**
 * 🎨 CitySpark Frontend - Main Application
 * Next.js application for CitySpark Complete Platform
 */

import React from 'react';
import { useState, useEffect } from 'react';
import { QueryClient, QueryClientProvider } from 'react-query';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  BookOpen, 
  Palette, 
  Brain, 
  Github,
  Menu,
  X,
  Home,
  Search,
  User,
  Settings
} from 'lucide-react';
import '../styles/globals.css';

// Create a client for React Query
const queryClient = new QueryClient();

function MyApp({ Component, pageProps }) {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [activeSection, setActiveSection] = useState('dashboard');

  const navigation = [
    { id: 'dashboard', name: 'Dashboard', icon: Home },
    { id: 'learning', name: 'Learning', icon: BookOpen },
    { id: 'art', name: 'Urban Art', icon: Palette },
    { id: 'ai', name: 'AI Features', icon: Brain },
    { id: 'github', name: 'GitHub', icon: Github },
  ];

  return (
    <QueryClientProvider client={queryClient}>
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-purple-50">
        {/* Sidebar */}
        <AnimatePresence>
          {sidebarOpen && (
            <motion.div
              initial={{ x: -300 }}
              animate={{ x: 0 }}
              exit={{ x: -300 }}
              className="fixed inset-y-0 left-0 z-50 w-64 bg-white shadow-xl"
            >
              <div className="flex items-center justify-between p-4 border-b">
                <h1 className="text-xl font-bold text-gray-900">🚀 CitySpark</h1>
                <button
                  onClick={() => setSidebarOpen(false)}
                  className="p-2 rounded-lg hover:bg-gray-100"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>
              
              <nav className="p-4">
                {navigation.map((item) => {
                  const Icon = item.icon;
                  return (
                    <button
                      key={item.id}
                      onClick={() => {
                        setActiveSection(item.id);
                        setSidebarOpen(false);
                      }}
                      className={`w-full flex items-center gap-3 px-4 py-3 rounded-lg mb-2 transition-colors ${
                        activeSection === item.id
                          ? 'bg-blue-100 text-blue-600'
                          : 'hover:bg-gray-100 text-gray-700'
                      }`}
                    >
                      <Icon className="w-5 h-5" />
                      <span>{item.name}</span>
                    </button>
                  );
                })}
              </nav>
            </motion.div>
          )}
        </AnimatePresence>

        {/* Main Content */}
        <div className="flex">
          {/* Mobile Menu Button */}
          <button
            onClick={() => setSidebarOpen(true)}
            className="lg:hidden fixed top-4 left-4 z-40 p-2 bg-white rounded-lg shadow-md"
          >
            <Menu className="w-6 h-6" />
          </button>

          {/* Desktop Sidebar */}
          <aside className="hidden lg:block w-64 bg-white shadow-md h-screen sticky top-0">
            <div className="p-6 border-b">
              <h1 className="text-2xl font-bold text-gray-900">🚀 CitySpark</h1>
              <p className="text-sm text-gray-600 mt-1">AI-Powered Learning Platform</p>
            </div>
            
            <nav className="p-4">
              {navigation.map((item) => {
                const Icon = item.icon;
                return (
                  <button
                    key={item.id}
                    onClick={() => setActiveSection(item.id)}
                    className={`w-full flex items-center gap-3 px-4 py-3 rounded-lg mb-2 transition-colors ${
                      activeSection === item.id
                        ? 'bg-blue-100 text-blue-600'
                        : 'hover:bg-gray-100 text-gray-700'
                    }`}
                  >
                    <Icon className="w-5 h-5" />
                    <span>{item.name}</span>
                  </button>
                );
              })}
            </nav>
          </aside>

          {/* Main Content Area */}
          <main className="flex-1 p-6 lg:p-8">
            <div className="max-w-7xl mx-auto">
              {/* Header */}
              <header className="mb-8">
                <div className="flex items-center justify-between">
                  <div>
                    <h1 className="text-3xl font-bold text-gray-900">
                      {navigation.find(n => n.id === activeSection)?.name || 'Dashboard'}
                    </h1>
                    <p className="text-gray-600 mt-1">
                      {getSectionDescription(activeSection)}
                    </p>
                  </div>
                  
                  <div className="flex items-center gap-4">
                    <button className="p-2 rounded-lg hover:bg-gray-100">
                      <Search className="w-5 h-5" />
                    </button>
                    <button className="p-2 rounded-lg hover:bg-gray-100">
                      <User className="w-5 h-5" />
                    </button>
                    <button className="p-2 rounded-lg hover:bg-gray-100">
                      <Settings className="w-5 h-5" />
                    </button>
                  </div>
                </div>
              </header>

              {/* Content */}
              <AnimatePresence mode="wait">
                <motion.div
                  key={activeSection}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: -20 }}
                  transition={{ duration: 0.3 }}
                >
                  <Component {...pageProps} activeSection={activeSection} />
                </motion.div>
              </AnimatePresence>
            </div>
          </main>
        </div>
      </div>
    </QueryClientProvider>
  );
}

function getSectionDescription(section) {
  const descriptions = {
    dashboard: 'Welcome to your personalized learning dashboard',
    learning: 'Personalized learning paths and educational content',
    art: 'Generate and explore AI-powered urban art',
    ai: 'AI features and intelligent recommendations',
    github: 'GitHub integration and educational resources'
  };
  
  return descriptions[section] || 'Navigate through the platform';
}

export default MyApp;