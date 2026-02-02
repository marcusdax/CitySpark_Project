/**
 * 📊 CitySpark Dashboard
 * Main dashboard component for the CitySpark platform
 */

import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import {
  BookOpen,
  Palette,
  Brain,
  Github,
  TrendingUp,
  Award,
  Clock,
  Users,
  BarChart3,
  Activity,
  Zap,
  Target,
  Star
} from 'lucide-react';

const Dashboard = ({ activeSection }) => {
  const [stats, setStats] = useState({
    learningProgress: 0,
    artCreated: 0,
    aiInteractions: 0,
    githubRepos: 0
  });

  const [recentActivity, setRecentActivity] = useState([]);
  const [featuredContent, setFeaturedContent] = useState([]);

  useEffect(() => {
    // Simulate loading dashboard data
    const loadDashboardData = async () => {
      try {
        // In a real app, these would be API calls
        setStats({
          learningProgress: 75,
          artCreated: 12,
          aiInteractions: 48,
          githubRepos: 6
        });

        setRecentActivity([
          {
            id: 1,
            type: 'learning',
            title: 'Completed AI Basics Module',
            time: '2 hours ago',
            icon: BookOpen,
            color: 'text-blue-600'
          },
          {
            id: 2,
            type: 'art',
            title: 'Generated Urban Skyline Art',
            time: '4 hours ago',
            icon: Palette,
            color: 'text-purple-600'
          },
          {
            id: 3,
            type: 'ai',
            title: 'Received Learning Recommendations',
            time: '6 hours ago',
            icon: Brain,
            color: 'text-green-600'
          },
          {
            id: 4,
            type: 'github',
            title: 'New Repository Added',
            time: '1 day ago',
            icon: Github,
            color: 'text-gray-600'
          }
        ]);

        setFeaturedContent([
          {
            id: 1,
            title: 'Introduction to Machine Learning',
            type: 'course',
            difficulty: 'Beginner',
            duration: '6 weeks',
            enrolled: 1250,
            rating: 4.8
          },
          {
            id: 2,
            title: 'Digital Urban Art Collection',
            type: 'art',
            style: 'Modern',
            pieces: 15,
            likes: 342,
            featured: true
          },
          {
            id: 3,
            title: 'Python Data Science Resources',
            type: 'github',
            stars: 1500,
            forks: 450,
            updated: '2 days ago'
          }
        ]);
      } catch (error) {
        console.error('Error loading dashboard data:', error);
      }
    };

    loadDashboardData();
  }, []);

  const StatCard = ({ title, value, icon: Icon, color, trend }) => (
    <motion.div
      whileHover={{ scale: 1.02 }}
      className="bg-white rounded-xl shadow-sm border border-gray-200 p-6"
    >
      <div className="flex items-center justify-between">
        <div>
          <p className="text-sm font-medium text-gray-600">{title}</p>
          <p className="text-2xl font-bold text-gray-900 mt-1">{value}</p>
          {trend && (
            <div className="flex items-center mt-2 text-sm">
              <TrendingUp className="w-4 h-4 text-green-500 mr-1" />
              <span className="text-green-500">{trend}</span>
            </div>
          )}
        </div>
        <div className={`p-3 rounded-lg ${color}`}>
          <Icon className="w-6 h-6 text-white" />
        </div>
      </div>
    </motion.div>
  );

  const ActivityItem = ({ activity }) => {
    const Icon = activity.icon;
    return (
      <div className="flex items-center gap-4 p-4 bg-white rounded-lg border border-gray-200">
        <div className={`p-2 rounded-lg bg-gray-50 ${activity.color}`}>
          <Icon className="w-5 h-5" />
        </div>
        <div className="flex-1">
          <p className="font-medium text-gray-900">{activity.title}</p>
          <p className="text-sm text-gray-500">{activity.time}</p>
        </div>
      </div>
    );
  };

  const ContentCard = ({ content }) => {
    const getIcon = (type) => {
      switch (type) {
        case 'course': return BookOpen;
        case 'art': return Palette;
        case 'github': return Github;
        default: return Activity;
      }
    };

    const Icon = getIcon(content.type);

    return (
      <motion.div
        whileHover={{ y: -2 }}
        className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 cursor-pointer"
      >
        <div className="flex items-start justify-between mb-4">
          <div className={`p-2 rounded-lg ${content.type === 'course' ? 'bg-blue-100 text-blue-600' :
            content.type === 'art' ? 'bg-purple-100 text-purple-600' : 'bg-gray-100 text-gray-600'
          }`}>
            <Icon className="w-5 h-5" />
          </div>
          {content.featured && (
            <div className="flex items-center text-yellow-500">
              <Star className="w-4 h-4 fill-current" />
              <span className="text-xs ml-1">Featured</span>
            </div>
          )}
        </div>

        <h3 className="font-semibold text-gray-900 mb-2">{content.title}</h3>
        
        <div className="space-y-1 text-sm text-gray-600">
          {content.difficulty && (
            <p>Difficulty: <span className="font-medium">{content.difficulty}</span></p>
          )}
          {content.duration && (
            <p>Duration: <span className="font-medium">{content.duration}</span></p>
          )}
          {content.style && (
            <p>Style: <span className="font-medium">{content.style}</span></p>
          )}
          {content.enrolled && (
            <p>Enrolled: <span className="font-medium">{content.enrolled.toLocaleString()}</span></p>
          )}
          {content.likes && (
            <p>Likes: <span className="font-medium">{content.likes.toLocaleString()}</span></p>
          )}
          {content.stars && (
            <p>Stars: <span className="font-medium">{content.stars.toLocaleString()}</span></p>
          )}
        </div>

        {content.rating && (
          <div className="flex items-center mt-3">
            <div className="flex items-center">
              {[...Array(5)].map((_, i) => (
                <Star
                  key={i}
                  className={`w-4 h-4 ${i < Math.floor(content.rating) ? 'text-yellow-400 fill-current' : 'text-gray-300'
                    }`}
                />
              ))}
            </div>
            <span className="ml-2 text-sm text-gray-600">{content.rating}</span>
          </div>
        )}
      </motion.div>
    );
  };

  return (
    <div className="space-y-6">
      {/* Stats Overview */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <StatCard
          title="Learning Progress"
          value={`${stats.learningProgress}%`}
          icon={BookOpen}
          color="bg-blue-500"
          trend="+5% this week"
        />
        <StatCard
          title="Art Created"
          value={stats.artCreated}
          icon={Palette}
          color="bg-purple-500"
          trend="+3 today"
        />
        <StatCard
          title="AI Interactions"
          value={stats.aiInteractions}
          icon={Brain}
          color="bg-green-500"
          trend="+12 this week"
        />
        <StatCard
          title="GitHub Repos"
          value={stats.githubRepos}
          icon={Github}
          color="bg-gray-500"
          trend="+2 new"
        />
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Recent Activity */}
        <div className="lg:col-span-1">
          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <h2 className="text-lg font-semibold text-gray-900 mb-4">Recent Activity</h2>
            <div className="space-y-3">
              {recentActivity.map((activity) => (
                <ActivityItem key={activity.id} activity={activity} />
              ))}
            </div>
          </div>
        </div>

        {/* Featured Content */}
        <div className="lg:col-span-2">
          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <h2 className="text-lg font-semibold text-gray-900 mb-4">Featured Content</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {featuredContent.map((content) => (
                <ContentCard key={content.id} content={content} />
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Quick Actions */}
      <div className="bg-gradient-to-r from-blue-600 to-purple-600 rounded-xl p-6 text-white">
        <h2 className="text-xl font-bold mb-4">Quick Actions</h2>
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <button className="bg-white/20 backdrop-blur-sm rounded-lg p-4 text-center hover:bg-white/30 transition-colors">
            <Target className="w-8 h-8 mx-auto mb-2" />
            <span className="text-sm">Set Learning Goals</span>
          </button>
          <button className="bg-white/20 backdrop-blur-sm rounded-lg p-4 text-center hover:bg-white/30 transition-colors">
            <Zap className="w-8 h-8 mx-auto mb-2" />
            <span className="text-sm">Generate Art</span>
          </button>
          <button className="bg-white/20 backdrop-blur-sm rounded-lg p-4 text-center hover:bg-white/30 transition-colors">
            <BarChart3 className="w-8 h-8 mx-auto mb-2" />
            <span className="text-sm">View Analytics</span>
          </button>
          <button className="bg-white/20 backdrop-blur-sm rounded-lg p-4 text-center hover:bg-white/30 transition-colors">
            <Users className="w-8 h-8 mx-auto mb-2" />
            <span className="text-sm">Join Community</span>
          </button>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;