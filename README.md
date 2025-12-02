# 🃏 Memory Game - Football Edition

A fully functional **Memory Card Game** (Memorama) with a football theme, developed with **Pygame**. This project demonstrates advanced game programming concepts including grid-based layouts, event handling, state management, and interactive gameplay mechanics.

---

## 👨‍🎓 Developer Information

- **Student:** Magallanes López Carlos Gabriel
- **Email:** cgmagallanes23@gmail.com
- **School:** Centro de Bachillerato Tecnológico Industrial y de Servicios No. 128
- **Development Date:** October 15, 2025

---

## 🎮 Game Overview

This is a classic memory matching game featuring football team logos. Players must find matching pairs of cards by flipping them over two at a time. The game features:

- **Grid-based layout** with 8 cards (4 pairs) arranged in a 2x4 grid
- **Card flipping mechanics** with smooth reveal animations
- **Match detection** system for paired cards
- **Auto-hide functionality** for non-matching pairs
- **Victory detection** when all pairs are found
- **Randomization** of card positions for replayability
- **Interactive start button** to begin new games

---

## 🎯 Gameplay Mechanics

### Controls
- **Mouse Click**: Select and flip cards
- **Start Button**: Begin a new game with shuffled cards

### Objective
Find all 4 matching pairs of football team cards by remembering their positions. Cards flip back over if they don't match.

### Game Rules
1. Click the "Iniciar juego" (Start Game) button to begin
2. Click on any card to reveal it
3. Click on a second card to try to find a match
4. If cards match, they stay revealed
5. If cards don't match, they flip back after 1 second
6. Continue until all pairs are found
7. Game automatically resets when you win

---

## 🚀 Features

### ✨ Core Gameplay Features
- **Card Grid System**: 2x4 grid layout with 4 unique football team logos
- **Match Detection**: Automatic comparison of selected cards
- **Timed Reveal**: Non-matching cards hide after 1 second
- **Victory Condition**: Automatic win detection and game reset
- **Card Shuffling**: Randomized positions at game start
- **State Management**: Tracks discovered and shown cards

### 🎨 Visual Elements
- **Football Team Logos**: PSG, Real Madrid, Barcelona, and Inter Milan
- **Card Back Design**: Clean gray design for hidden cards
- **Border Highlighting**: Black borders around each card
- **Start Button**: Green button that turns white during gameplay
- **Smooth Rendering**: 60 FPS gameplay

### 🎮 Interactive Elements
- **Click Detection**: Precise mouse position tracking
- **Button States**: Visual feedback for start button
- **Card States**: Three states (hidden, shown, discovered)
- **Turn Blocking**: Prevents clicking during card comparison

---

## 📦 Requirements

### Python Libraries
```bash
Python 3.x
pygame
```

### Installation
```bash
pip install pygame
```

### Asset Structure
```
project/
│
├── memorama_football.py    # Main game file
└── imgs/
    ├── PSG.png             # Paris Saint-Germain logo
    ├── Madrid.png          # Real Madrid logo
    ├── Barca.png           # FC Barcelona logo
    └── Inter.png           # Inter Milan logo
```

---

## 🎮 How to Run

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/memory-game-football.git
cd memory-game-football
```

2. **Ensure all assets are in place**:
   - Place team logo images in `imgs/` folder
   - Images should be 200x200 pixels for best display

3. **Run the game**:
```bash
python memorama_football.py
```

---

## 🔧 Technical Implementation

### Game Architecture

```python
# Main Components:
1. Card Class (Object-oriented design)
2. Game Screen Setup (Pygame window)
3. Grid Layout System (2D array)
4. Event Handling Loop
5. State Management
6. Rendering Engine
```

## 🎨 Visual Design

### Color Scheme
- **Background**: White (`#FFFFFF`)
- **Card Back**: Gray (`#CECECE`)
- **Card Border**: Black (`#000000`)
- **Start Button (Active)**: Green (`#00FF00`)
- **Start Button (Playing)**: White (`#FFFFFF`)
- **Button Text**: Dynamic (White/Gray based on state)

### Card States
1. **Hidden**: Gray rectangle with black border
2. **Shown**: Team logo visible
3. **Discovered**: Team logo permanently visible

---

## 🐛 Known Limitations

- Fixed 800x450 window size (not resizable)
- Only 4 pairs of cards (8 total)
- No scoring system or timer
- No difficulty levels
- No sound effects
- Cards must be 200x200 pixels for proper display

---

## 📚 Learning Outcomes

This project serves as an educational resource for understanding fundamental game development concepts:

### 🎓 What You'll Learn

1. **Object-Oriented Programming**
   - Class design and encapsulation
   - Instance attributes and methods
   - Object state management
   - Type hints and validation

2. **Pygame Fundamentals**
   - Window and display setup
   - Event loop architecture
   - Mouse input handling
   - Surface and image rendering
   - Rectangle collision detection

3. **Grid-Based Game Logic**
   - 2D array manipulation
   - Coordinate system conversion
   - Grid traversal algorithms
   - Position-to-index mapping

4. **State Management**
   - Game state tracking (not started, playing, won)
   - Card state machines (hidden, shown, discovered)
   - Turn-based logic implementation
   - Boolean flags for game control

5. **Event-Driven Programming**
   - Mouse click event handling
   - Event queue processing
   - User input validation
   - Button interaction logic

6. **Timing and Delays**
   - Time-based mechanics with `time.time()`
   - Delayed card hiding
   - Frame rate control with `clock.tick()`
   - Non-blocking delay implementation

7. **Randomization Algorithms**
   - Card shuffling techniques
   - Random position generation
   - Ensuring fair distribution

8. **Game Loop Design**
   - Render loop structure
   - Update-render separation
   - FPS management
   - Continuous game state updates

9. **Collision Detection**
   - Point-rectangle collision (`collidepoint`)
   - Grid boundary validation
   - Click area detection

10. **Visual Rendering**
    - Image loading and blitting
    - Rectangle drawing
    - Text rendering
    - Layered rendering order

---

### 🎯 Skills Developed

By studying and modifying this code, you will gain hands-on experience with:

✅ **Game design patterns** and architecture  
✅ **Memory management** in card matching games  
✅ **User interface design** for grid-based games  
✅ **Input validation** and error handling  
✅ **Algorithm implementation** (shuffling, matching)  
✅ **Code organization** with classes and functions  

This repository is perfect for students learning Pygame, game development basics, or anyone interested in understanding how classic memory games work programmatically.

---

## 📄 License

This project is educational in nature and available for free use for learning purposes. Football team logos are property of their respective owners and used for educational purposes only.

---

## 🙏 Acknowledgments

- Classic Memory Game concept
- Football team logos used for educational purposes
- Built with Python's Pygame library

---

## 🤝 Contributing

Students and developers are welcome to:
- Report bugs
- Suggest new features or themes
- Submit pull requests for improvements
- Share gameplay strategies
- Add new card themes

---

## 📧 Contact

**Carlos Gabriel Magallanes López**  
Email: cgmagallanes23@gmail.com  
School: CBTis No. 128

---

**⭐ If you enjoyed this game or found it educational, please give it a star on GitHub!**

**🎮 Happy Gaming!**
