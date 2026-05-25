---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 175}"
usage: "affixed-to-a-shield"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Usage** affixed to a shield

**Activate** `pf2:f` (concentrate)

**Trigger** You Shield Block a foe's melee attack with the affixed shield.

This miniature Stasian coil talisman emits small sparks when jostled. It uses a combination of Stasian technology and battle magic to erupt in electricity when discharged. When you activate the coil, the foe takes 2d12 electricity damage (DC 27 [[Reflex]] save). On a failed save, the foe is [[Off Guard]] until the start of its next turn.

**Source:** `= this.source` (`= this.source-type`)
