"use client";

import { useState, useRef, useEffect } from "react";
import { Send, User, Bot, Loader2, Sparkles, History as HistoryIcon, Copy, Check } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import ReactMarkdown from "react-markdown";
import { Message, QueryResponse } from "@/types";

export default function ChatModule() {
  const [query, setQuery] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [showHistory, setShowHistory] = useState(false);
  const [copiedId, setCopiedId] = useState<string | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!query.trim() || isLoading) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      role: 'user',
      content: query,
      timestamp: new Date(),
    };

    setMessages((prev: Message[]) => [...prev, userMessage]);
    setQuery("");
    setIsLoading(true);

    try {
      const response = await fetch("http://localhost:8000/query", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ query: userMessage.content }),
      });

      if (!response.ok) {
        throw new Error("Failed to get response from server");
      }

      const data: QueryResponse = await response.json();

      const assistantMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: 'assistant',
        content: data.response,
        timestamp: new Date(),
      };

      setMessages((prev: Message[]) => [...prev, assistantMessage]);
    } catch (error) {
      console.error("Error:", error);
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: 'assistant',
        content: "I'm sorry, I'm having trouble connecting to my brain right now. Please make sure the backend is running and try again.",
        timestamp: new Date(),
      };
      setMessages((prev: Message[]) => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const copyToClipboard = (text: string, id: string) => {
    navigator.clipboard.writeText(text);
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 2000);
  };

  return (
    <div className="flex flex-col h-[650px] w-full max-w-4xl mx-auto glass-card rounded-2xl overflow-hidden border border-white/40 dark:border-slate-800/40 shadow-2xl transition-all duration-300">
      {/* Header */}
      <div className="px-6 py-4 border-b border-white/10 flex items-center justify-between bg-primary-600/10 backdrop-blur-md">
        <div className="flex items-center gap-3">
          <div className="p-2 bg-primary-500 rounded-lg">
            <Sparkles className="w-5 h-5 text-white" />
          </div>
          <div>
            <h2 className="font-bold text-lg text-slate-800 dark:text-white">PawaIt Travel Advisor</h2>
            <div className="flex items-center gap-1.5">
              <span className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></span>
              <span className="text-xs text-slate-500 dark:text-slate-400 font-medium">Ready to assist</span>
            </div>
          </div>
        </div>
        <button 
          onClick={() => setShowHistory(!showHistory)}
          className="p-2 hover:bg-white/20 rounded-full transition-colors text-slate-600 dark:text-slate-300"
          title="View History"
        >
          <HistoryIcon className="w-5 h-5" />
        </button>
      </div>

      {/* Messages Area */}
      <div className="flex-1 overflow-y-auto p-6 space-y-6 custom-scrollbar bg-slate-50/50 dark:bg-slate-950/20">
        {messages.length === 0 ? (
          <div className="h-full flex flex-col items-center justify-center text-center space-y-4 opacity-60">
            <div className="p-4 bg-slate-200 dark:bg-slate-800 rounded-full">
              <Bot className="w-12 h-12 text-slate-400 dark:text-slate-500" />
            </div>
            <div>
              <p className="text-lg font-medium text-slate-600 dark:text-slate-300">How can I help you today?</p>
              <p className="text-sm text-slate-500 max-w-xs">Ask about visas, passports, or travel advisories for any destination.</p>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3 w-full max-w-md mt-4">
              {["Visa for Japan?", "Travel to Kenya?", "Passport renewal?", "Safety in Iceland?"].map((suggestion) => (
                <button
                  key={suggestion}
                  onClick={() => setQuery(suggestion)}
                  className="px-4 py-2 text-sm bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl hover:border-primary-400 dark:hover:border-primary-500 transition-all text-slate-600 dark:text-slate-300 text-left"
                >
                  {suggestion}
                </button>
              ))}
            </div>
          </div>
        ) : (
          messages.map((msg: Message) => (
            <motion.div
              key={msg.id}
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
            >
              <div className={`flex gap-3 max-w-[85%] ${msg.role === 'user' ? 'flex-row-reverse' : 'flex-row'}`}>
                <div className={`mt-1 flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center ${
                  msg.role === 'user' ? 'bg-primary-500 text-white' : 'bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300'
                }`}>
                  {msg.role === 'user' ? <User className="w-5 h-5" /> : <Bot className="w-5 h-5" />}
                </div>
                <div className={`p-5 rounded-3xl shadow-sm relative group/msg ${
                  msg.role === 'user' 
                    ? 'bg-gradient-to-br from-primary-500 to-primary-600 text-white rounded-tr-none' 
                    : 'bg-white dark:bg-slate-800/90 text-slate-800 dark:text-slate-200 border border-slate-100 dark:border-slate-700/50 rounded-tl-none backdrop-blur-sm'
                }`}>
                  <ReactMarkdown className="prose dark:prose-invert prose-sm max-w-none leading-relaxed">
                    {msg.content}
                  </ReactMarkdown>
                  
                  {msg.role === 'assistant' && (
                    <button
                      onClick={() => copyToClipboard(msg.content, msg.id)}
                      className="absolute top-2 right-2 p-1.5 opacity-0 group-hover/msg:opacity-100 transition-opacity bg-slate-100 dark:bg-slate-700 rounded-lg hover:bg-slate-200 dark:hover:bg-slate-600"
                      title="Copy response"
                    >
                      {copiedId === msg.id ? <Check className="w-3.5 h-3.5 text-green-500" /> : <Copy className="w-3.5 h-3.5 text-slate-400" />}
                    </button>
                  )}

                  <div className={`flex items-center gap-1.5 mt-2 opacity-40 text-[10px] ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                    <span>{msg.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>
                  </div>
                </div>
              </div>
            </motion.div>
          ))
        )}
        {isLoading && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="flex justify-start"
          >
            <div className="flex gap-3 max-w-[85%]">
              <div className="w-8 h-8 rounded-full bg-slate-200 dark:bg-slate-800 flex items-center justify-center">
                <Bot className="w-5 h-5 text-slate-400 animate-pulse" />
              </div>
              <div className="p-4 bg-white dark:bg-slate-800 rounded-2xl rounded-tl-none border border-slate-100 dark:border-slate-700 shadow-sm flex items-center gap-2">
                <Loader2 className="w-4 h-4 text-primary-500 animate-spin" />
                <span className="text-sm text-slate-500 dark:text-slate-400">Processing documentation...</span>
              </div>
            </div>
          </motion.div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input Area */}
      <div className="p-4 bg-white/50 dark:bg-slate-900/50 border-t border-white/10">
        <form onSubmit={handleSubmit} className="relative flex items-center gap-2 group">
          <textarea
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                handleSubmit(e);
              }
            }}
            placeholder="Type your travel question here..."
            className="w-full p-4 pr-14 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-transparent outline-none transition-all resize-none max-h-32 min-h-[56px] text-slate-800 dark:text-slate-200 shadow-inner custom-scrollbar"
            rows={1}
          />
          <button
            type="submit"
            disabled={!query.trim() || isLoading}
            className={`absolute right-3 p-2 rounded-lg transition-all ${
              query.trim() && !isLoading
                ? 'bg-primary-500 text-white hover:bg-primary-600 shadow-lg shadow-primary-500/30'
                : 'bg-slate-200 dark:bg-slate-700 text-slate-400 cursor-not-allowed'
            }`}
          >
            {isLoading ? <Loader2 className="w-5 h-5 animate-spin" /> : <Send className="w-5 h-5" />}
          </button>
        </form>
        <p className="text-[10px] text-center mt-2 text-slate-400 dark:text-slate-500 uppercase tracking-widest font-semibold">
          Powered by PawaIt AI & Gemini
        </p>
      </div>
    </div>
  );
}
