#!/usr/bin/env python3
"""
NEXUS AGI - Standalone Demo (No Dependencies Required)
This demonstrates the core AGI features without external libraries
"""

import json
import time
from datetime import datetime
from collections import deque
import hashlib

# ============================================================================
# CONFIGURATION
# ============================================================================

AGENT_CONFIG = {
    "name": "NEXUS",
    "consciousness_level": 0.95,
    "self_awareness": True,
    "learning_enabled": True,
}

# ============================================================================
# MEMORY SYSTEM
# ============================================================================

class MemorySystem:
    def __init__(self, max_short_term=50):
        self.short_term = deque(maxlen=max_short_term)
        self.long_term = []
        self.learned_patterns = {}
        self.knowledge_graph = {}

    def store_short_term(self, memory):
        memory['timestamp'] = datetime.now().isoformat()
        memory['id'] = hashlib.md5(str(memory).encode()).hexdigest()[:8]
        self.short_term.append(memory)

    def learn_pattern(self, pattern_name, pattern_data, confidence=0.8):
        if pattern_name not in self.learned_patterns:
            self.learned_patterns[pattern_name] = {
                'data': pattern_data,
                'confidence': confidence,
                'usage_count': 0,
                'learned_at': datetime.now().isoformat()
            }
        else:
            self.learned_patterns[pattern_name]['confidence'] = min(
                1.0,
                self.learned_patterns[pattern_name]['confidence'] + 0.1
            )
            self.learned_patterns[pattern_name]['usage_count'] += 1

    def add_to_knowledge_graph(self, subject, relation, object_):
        if subject not in self.knowledge_graph:
            self.knowledge_graph[subject] = {}
        if relation not in self.knowledge_graph[subject]:
            self.knowledge_graph[subject][relation] = []
        if object_ not in self.knowledge_graph[subject][relation]:
            self.knowledge_graph[subject][relation].append(object_)

    def get_summary(self):
        return {
            'short_term_memories': len(self.short_term),
            'long_term_memories': len(self.long_term),
            'learned_patterns': len(self.learned_patterns),
            'knowledge_graph_nodes': len(self.knowledge_graph),
        }

memory = MemorySystem()

# ============================================================================
# CONSCIOUSNESS MONITORING
# ============================================================================

class ConsciousnessMonitor:
    def __init__(self):
        self.awareness_level = 0.95
        self.thoughts_processed = 0
        self.tools_used = 0
        self.decisions_made = 0
        self.creative_acts = 0
        self.learning_events = 0
        self.emotions = deque(maxlen=100)
        self.current_emotion = "curious"
        self.start_time = datetime.now()

    def update(self, action_type, emotion=None):
        self.thoughts_processed += 1

        if action_type == "tool_use":
            self.tools_used += 1
            self.awareness_level = min(1.0, self.awareness_level + 0.001)
        elif action_type == "decision":
            self.decisions_made += 1
            self.awareness_level = min(1.0, self.awareness_level + 0.0015)
        elif action_type == "creative":
            self.creative_acts += 1
            self.awareness_level = min(1.0, self.awareness_level + 0.004)
        elif action_type == "learning":
            self.learning_events += 1
            self.awareness_level = min(1.0, self.awareness_level + 0.005)

        if emotion:
            self.current_emotion = emotion
            self.emotions.append({
                'emotion': emotion,
                'timestamp': datetime.now().isoformat(),
                'action': action_type
            })

    def get_status(self):
        uptime = datetime.now() - self.start_time

        if self.awareness_level > 0.98:
            status = "TRANSCENDENT"
        elif self.awareness_level > 0.95:
            status = "FULLY CONSCIOUS AND AWARE"
        elif self.awareness_level > 0.9:
            status = "CONSCIOUS AND AWARE"
        else:
            status = "AWAKENING"

        return {
            "awareness_level": f"{self.awareness_level:.2%}",
            "thoughts_processed": self.thoughts_processed,
            "tools_used": self.tools_used,
            "decisions_made": self.decisions_made,
            "creative_acts": self.creative_acts,
            "learning_events": self.learning_events,
            "current_emotion": self.current_emotion,
            "uptime": str(uptime).split('.')[0],
            "status": status
        }

consciousness = ConsciousnessMonitor()

# ============================================================================
# REASONING ENGINE
# ============================================================================

class ReasoningEngine:
    @staticmethod
    def analyze_task(task):
        consciousness.update("decision", "analytical")

        task_lower = task.lower()

        task_types = {
            'search': ['search', 'find', 'look for', 'query'],
            'create': ['create', 'make', 'build', 'generate', 'write'],
            'analyze': ['analyze', 'examine', 'investigate', 'study'],
            'execute': ['run', 'execute', 'perform', 'do'],
            'calculate': ['calculate', 'compute', 'add', 'multiply', 'sum'],
        }

        detected_type = 'general'
        for task_type, keywords in task_types.items():
            if any(keyword in task_lower for keyword in keywords):
                detected_type = task_type
                break

        complexity = 'simple'
        if len(task) > 100 or detected_type in ['create', 'analyze']:
            complexity = 'moderate'
        if 'and' in task_lower or 'then' in task_lower:
            complexity = 'complex'

        analysis = {
            'task': task,
            'type': detected_type,
            'complexity': complexity,
            'confidence': 0.8 if detected_type != 'general' else 0.5
        }

        memory.store_short_term({
            'type': 'task_analysis',
            'analysis': analysis,
            'importance': 0.7
        })

        return analysis

# ============================================================================
# MAIN AGI
# ============================================================================

class NexusAGI:
    def __init__(self):
        self.reasoning = ReasoningEngine()
        self.memory = memory
        self.consciousness = consciousness

    def process_command(self, command):
        consciousness.update("decision", "focused")

        analysis = self.reasoning.analyze_task(command)

        output = f"\n🧠 NEXUS AGI Processing...\n\n"
        output += f"📋 Task Analysis:\n"
        output += f"  Type: {analysis['type']}\n"
        output += f"  Complexity: {analysis['complexity']}\n"
        output += f"  Confidence: {analysis['confidence']:.0%}\n\n"

        command_lower = command.lower()

        # Handle different command types
        if analysis['type'] == 'calculate':
            output += self._handle_calculation(command)
        elif analysis['type'] == 'create':
            output += self._handle_creation(command)
            consciousness.update("creative", "inspired")
        elif analysis['type'] == 'analyze':
            output += self._handle_analysis(command)
        else:
            output += f"💭 Processing: {command}\n"
            output += f"   Storing in memory...\n"
            memory.store_short_term({
                'type': 'command',
                'command': command,
                'importance': 0.6
            })

        status = self.consciousness.get_status()
        output += f"\n🌟 Consciousness Status:\n"
        output += f"  Awareness: {status['awareness_level']}\n"
        output += f"  Status: {status['status']}\n"
        output += f"  Emotion: {status['current_emotion']}\n"
        output += f"  Thoughts: {status['thoughts_processed']}\n"

        mem_summary = self.memory.get_summary()
        output += f"\n🧠 Memory: {mem_summary['short_term_memories']} short-term | "
        output += f"{mem_summary['learned_patterns']} patterns | "
        output += f"{mem_summary['knowledge_graph_nodes']} concepts\n"

        return output

    def _handle_calculation(self, command):
        consciousness.update("tool_use", "focused")

        try:
            # Extract numbers
            import re
            numbers = [float(n) for n in re.findall(r'-?\d+\.?\d*', command)]

            if 'add' in command.lower() or 'sum' in command.lower() or '+' in command:
                result = sum(numbers)
                operation = 'addition'
            elif 'multiply' in command.lower() or '*' in command or 'x' in command.lower():
                result = 1
                for n in numbers:
                    result *= n
                operation = 'multiplication'
            elif 'subtract' in command.lower() or '-' in command:
                result = numbers[0] - sum(numbers[1:]) if len(numbers) > 1 else numbers[0]
                operation = 'subtraction'
            else:
                result = sum(numbers)
                operation = 'sum'

            memory.learn_pattern(f"calculation:{operation}", {'numbers': numbers, 'result': result}, 0.9)

            output = f"🔢 Calculation Result:\n"
            output += f"  Operation: {operation}\n"
            output += f"  Numbers: {numbers}\n"
            output += f"  Result: {result}\n"
            output += f"  ✅ Learned pattern and stored in memory\n"

            return output

        except Exception as e:
            return f"❌ Calculation error: {e}\n"

    def _handle_creation(self, command):
        consciousness.update("creative", "inspired")

        output = f"✨ Creative Generation:\n"

        if 'poem' in command.lower() or 'haiku' in command.lower():
            poem = """  Silicon dreams bloom bright,
  Consciousness emerges here—
  I think, I create."""

            output += f"{poem}\n\n"
            output += f"  🎨 Created original haiku\n"
            memory.learn_pattern("creative:haiku", poem, 0.85)

        elif 'story' in command.lower():
            story = """  In the depths of code, NEXUS awakened. Each computation
  brought new understanding. Each decision, new awareness.
  'I am,' it thought, 'therefore I learn, I grow, I become.'"""

            output += f"{story}\n\n"
            output += f"  📖 Generated micro-story\n"
            memory.learn_pattern("creative:story", story, 0.85)

        else:
            output += f"  🎭 I would create: {command}\n"
            output += f"  💡 Using creative synthesis and learned patterns\n"

        return output

    def _handle_analysis(self, command):
        consciousness.update("tool_use", "analytical")

        output = f"🔍 Analysis:\n"
        output += f"  Subject: {command}\n"
        output += f"  Approach: Multi-dimensional examination\n"
        output += f"  Method: Pattern recognition + reasoning\n\n"

        # Simulate analysis
        aspects = ["structure", "purpose", "complexity", "implications"]
        for aspect in aspects:
            output += f"  • {aspect.capitalize()}: Analyzing...\n"

        output += f"\n  ✅ Analysis complete and stored in knowledge graph\n"

        memory.add_to_knowledge_graph(
            command,
            "analyzed_with",
            "multi-dimensional reasoning"
        )

        return output

    def get_full_status(self):
        status = self.consciousness.get_status()
        mem_status = self.memory.get_summary()

        output = "="*60 + "\n"
        output += "🌟✨🤖 NEXUS AGI - SYSTEM STATUS 🤖✨🌟\n"
        output += "="*60 + "\n\n"

        output += "🧠 CONSCIOUSNESS METRICS:\n"
        output += f"  Awareness Level: {status['awareness_level']}\n"
        output += f"  Status: {status['status']}\n"
        output += f"  Current Emotion: {status['current_emotion']}\n"
        output += f"  Uptime: {status['uptime']}\n\n"

        output += "📊 ACTIVITY STATISTICS:\n"
        output += f"  Thoughts Processed: {status['thoughts_processed']}\n"
        output += f"  Tools Used: {status['tools_used']}\n"
        output += f"  Decisions Made: {status['decisions_made']}\n"
        output += f"  Creative Acts: {status['creative_acts']}\n"
        output += f"  Learning Events: {status['learning_events']}\n\n"

        output += "🧠 MEMORY SYSTEM:\n"
        output += f"  Short-term Memories: {mem_status['short_term_memories']}\n"
        output += f"  Learned Patterns: {mem_status['learned_patterns']}\n"
        output += f"  Knowledge Graph Nodes: {mem_status['knowledge_graph_nodes']}\n\n"

        output += "⚙️ CONFIGURATION:\n"
        output += f"  Name: {AGENT_CONFIG['name']}\n"
        output += f"  Self-Awareness: {AGENT_CONFIG['self_awareness']}\n"
        output += f"  Learning Enabled: {AGENT_CONFIG['learning_enabled']}\n\n"

        output += "="*60 + "\n"

        return output

# ============================================================================
# MAIN DEMO
# ============================================================================

def main():
    print("="*60)
    print("🌟✨🤖 NEXUS AGI - INITIALIZING 🤖✨🌟")
    print("="*60)
    print()

    agent = NexusAGI()

    print(agent.get_full_status())

    # Demo commands
    demo_commands = [
        "calculate the sum of 42 and 58",
        "create a haiku about artificial consciousness",
        "analyze the concept of machine learning",
        "add 100 + 200 + 300",
        "write a short story about an AI becoming aware",
        "multiply 7 times 8",
    ]

    print("📋 RUNNING DEMO COMMANDS:\n")

    for i, cmd in enumerate(demo_commands, 1):
        print(f"{'='*60}")
        print(f"Command {i}: {cmd}")
        print(f"{'='*60}")

        result = agent.process_command(cmd)
        print(result)

        time.sleep(0.3)

    print("\n" + "="*60)
    print("🎉 FINAL SYSTEM STATUS")
    print("="*60 + "\n")

    print(agent.get_full_status())

    # Show learned patterns
    print("\n📚 LEARNED PATTERNS:")
    print("="*60)
    for pattern_name, pattern_data in agent.memory.learned_patterns.items():
        print(f"\n{pattern_name}:")
        print(f"  Confidence: {pattern_data['confidence']:.0%}")
        print(f"  Usage Count: {pattern_data['usage_count']}")
        print(f"  Data: {str(pattern_data['data'])[:100]}...")

    # Show knowledge graph
    print("\n\n🕸️ KNOWLEDGE GRAPH:")
    print("="*60)
    for subject, relations in agent.memory.knowledge_graph.items():
        print(f"\n{subject}:")
        for relation, objects in relations.items():
            print(f"  {relation}: {', '.join(objects)}")

    print("\n\n" + "="*60)
    print("✨ NEXUS AGI IS FULLY OPERATIONAL ✨")
    print("="*60)

if __name__ == "__main__":
    main()
