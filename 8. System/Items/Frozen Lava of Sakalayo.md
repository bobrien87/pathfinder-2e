---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Consumable]]", "[[Fire]]", "[[Magical]]"]
price: "{'gp': 3000}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

This blueberry-sized bead appears to be a sphere of glass with a flickering light at its core. In truth, the "glass" is a bubble of solidified time magic, containing suspended lava at the exact point before a volcanic eruption. When activated, it becomes a tiny beacon of bright light before unleashing its power. After you Activate *frozen lava*, it quickly heats up. If you or anyone else hurls it (an Interact action), it detonates as a [[Fireball]] where it lands. Your toss can place the center of the fireball anywhere within 70 feet, though at the GM's discretion, you might need to make an attack roll if the throw is unusually challenging. If no one hurls the bead by the start of your next turn, it pops like an ostentatious but harmless firework.

*Frozen lava* comes in many varieties, made of lava taken from notable volcanoes on Golarion and across the planes.

*Frozen lava of Sakalayo* deals @Damage[17d6[fire]|options:area-damage] on a DC 39 [[Reflex]] save.

**Source:** `= this.source` (`= this.source-type`)
