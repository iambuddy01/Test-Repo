from Nexa.bot import app  
import Nexa.plugins  

def main():

    print("""
███╗░░██╗███████╗██╗░░██╗░█████╗░
████╗░██║██╔════╝╚██╗██╔╝██╔══██╗
██╔██╗██║█████╗░░░╚███╔╝░███████║
██║╚████║██╔══╝░░░██╔██╗░██╔══██║
██║░╚███║███████╗██╔╝╚██╗██║░░██║
╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝
""")
    print("Starting Nexa Bot...")
    print("🔌 Loading plugins...")

    try:
        print("🚀 Bot is now running...")
        app.run()  # Synchronous run
    except KeyboardInterrupt:
        print("🛑 Bot stopped manually (Ctrl+C)")
    except Exception as e:
        print(f"❌ Bot crashed: {e}")
    finally:
        print("⏹ Bot shutdown complete.")

if __name__ == "__main__":
    main()
