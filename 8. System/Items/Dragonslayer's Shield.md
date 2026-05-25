---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Magical]]"]
price: "{'gp': 670}"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *dragonslayer's shield* is a steel shield covered with dragonhide from a specific dragon, which visually distinguishes each shield from the others. While raised, this steel shield (Hardness 8, HP 32, BT 16) grants its circumstance bonus to Reflex saves against area effects (as well as to AC, as normal).

While you hold the shield, it also grants you a +2 circumstance bonus to Will saves against a dragon's frightful presence ability. The shield has resistance 10 against the damage type corresponding to the dragon breath of the dragon whose hide was used in its creation (for example, a *dragonslayer's shield* made with the hide of a diabolic dragon would grant resistance to fire); this applies after reducing the damage for Hardness, so when you use Shield Block, the *dragonslayer's shield* takes 18 less damage from attacks of that damage type. You can use Shield Block against effects that deal damage of that type.

**Craft Requirements** The initial raw materials must include at least 30 gp of dragonhide.

**Source:** `= this.source` (`= this.source-type`)
