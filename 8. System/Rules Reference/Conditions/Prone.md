---
type: condition
source-type: "Remaster"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

You're lying on the ground. You are [[Off Guard]] and take a –2 circumstance penalty to attack rolls. The only move actions you can use while you're prone are [[Crawl]] and [[Stand]]. Standing up ends the prone condition. You can [[Take Cover]] while prone to hunker down and gain greater cover against ranged attacks, even if you don't have an object to get behind, which grants you a +4 circumstance bonus to AC against ranged attacks (but you remain off-guard).

If you would be knocked prone while you're [[Climbing]] or [[Flying]], you fall. You can't be knocked prone when [[Swimming]].

**Source:** `= this.source` (`= this.source-type`)
