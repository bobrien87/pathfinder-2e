---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Consumable]]", "[[Magical]]", "[[Whetstone]]"]
price: "{'cp': 0, 'gp': 200, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Imbued with a spirit fragment that continually surveys the world around it, this crystalline bar is roughened to form a file at one end. When you apply the *foe-sensing rod* to a weapon, choose aberration, animal, beast, celestial, construct, dragon, elemental, fey, fiend, giant, monitor, ooze, undead, or both fungus and plant. The spirit fragment is transferred into your weapon for 1 hour, keeping watch for creatures with the chosen trait or traits. The affected weapon vibrates slightly if such a creature is within 60 feet of you, unless the creature is disguised or [[Hidden]] and has a Deception or Stealth DC of 26 or higher.

**Source:** `= this.source` (`= this.source-type`)
