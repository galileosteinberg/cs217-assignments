from notebook import create_app
import os

app = create_app()

if __name__ == "__main__":
    # 0.0.0.0 lets the app receive traffic that is forwarded
    # into the container from the host’s 5000/tcp port
    app.run(host="0.0.0.0",
            port=int(os.environ.get("PORT", 5000)),
            debug=False)