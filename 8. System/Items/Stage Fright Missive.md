---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Curse]]", "[[Magical]]", "[[Mental]]", "[[Missive]]"]
price: "{'gp': 22}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (concentrate, manipulate)

Composing a stage fright missive usually involves creating a scathing review, insulting letter, or embarrassing image that ridicules the recipient. The activating creature must succeed at a DC 20 [[Will]] save or be overcome with embarrassment for 1 hour, taking a –1 status penalty to Deception, Diplomacy, Intimidation, and Performance checks. During this time, if the creature attempts to speak or perform in front of an audience, they become [[Sickened]] 1. When they recover from this sickened condition, the missive's effects end. You choose when composing the missive whether it remains as a non-magical document or burns to ash after imparting its magic.

**Source:** `= this.source` (`= this.source-type`)
