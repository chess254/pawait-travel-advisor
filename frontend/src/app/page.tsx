import ChatModule from "@/components/ChatModule";
import { Globe, ShieldCheck, MapPin, Zap } from "lucide-react";

export default function Home() {
  return (
    <main className="min-height-screen flex flex-col items-center justify-center p-4 md:p-8">
      {/* Background Decorations */}
      <div className="absolute top-0 left-0 w-full h-96 bg-gradient-to-b from-primary-500/10 to-transparent -z-10 blur-3xl rounded-full"></div>
      
      <div className="w-full max-w-6xl flex flex-col items-center gap-12 relative">
        {/* Hero Section */}
        <div className="text-center space-y-4 animate-fade-in">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 bg-primary-100 dark:bg-primary-900/30 text-primary-600 dark:text-primary-400 rounded-full text-xs font-bold uppercase tracking-wider border border-primary-200/50 dark:border-primary-800/30">
            <Zap className="w-3 h-3 fill-current" />
            Next-Gen Travel Intelligence
          </div>
          <h1 className="text-5xl md:text-7xl font-extrabold tracking-tight text-slate-900 dark:text-white">
            Pawa<span className="text-primary-500">It</span> Advisor
          </h1>
          <p className="text-lg md:text-xl text-slate-600 dark:text-slate-400 max-w-2xl mx-auto leading-relaxed">
            Instant guidance on visa documentation, passport requirements, and travel safety powered by advanced LLM integration.
          </p>
        </div>

        {/* Feature Highlights */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 w-full animate-slide-up" style={{ animationDelay: '0.2s' }}>
          {[
            { icon: Globe, title: "Global Coverage", desc: "Documentation for 190+ countries" },
            { icon: ShieldCheck, title: "Verified Advice", desc: "Up-to-date travel protocols" },
            { icon: MapPin, title: "Localized", desc: "Customized for your departure" },
          ].map((feature, i) => (
            <div key={i} className="glass-card p-6 rounded-2xl flex items-center gap-4 group hover:bg-white/90 dark:hover:bg-slate-800/90 transition-all duration-300 transform hover:-translate-y-1">
              <div className="p-3 bg-primary-100 dark:bg-primary-900/30 rounded-xl group-hover:scale-110 transition-transform">
                <feature.icon className="w-6 h-6 text-primary-600 dark:text-primary-400" />
              </div>
              <div>
                <h3 className="font-bold text-slate-800 dark:text-white">{feature.title}</h3>
                <p className="text-sm text-slate-500 dark:text-slate-400 font-medium">{feature.desc}</p>
              </div>
            </div>
          ))}
        </div>

        {/* Main Interface */}
        <div className="w-full animate-slide-up" style={{ animationDelay: '0.4s' }}>
          <ChatModule />
        </div>

        {/* Footer */}
        <footer className="w-full text-center py-8 text-slate-400 dark:text-slate-500 text-sm font-medium">
          <p>© 2024 PawaIt AI. Built with FastAPI, Next.js, and Gemini 1.5 Pro.</p>
        </footer>
      </div>
    </main>
  );
}
