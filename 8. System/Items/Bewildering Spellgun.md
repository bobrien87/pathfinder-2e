---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Attack]]", "[[Consumable]]", "[[Emotion]]", "[[Magical]]", "[[Mental]]", "[[Spellgun]]"]
price: "{'gp': 140}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` Strike

When stared at, a *bewildering spellgun* seems to warp the space around it, creating a mind-bending sensation. Whispers of gibberish arise from it, making their way to nearby ears despite any other sounds in the area. You Activate the spellgun by aiming it at one creature and making your choice of a spell attack roll or a firearm attack roll against the target's AC. This spellgun has a range increment of 15 feet. Once fired, the spellgun twists in your hand and melts away.
- **Critical Success** The target is [[Confused]] for 1 minute.
- **Success** The target is confused for 1 minute but can attempt a DC 25 [[Will]] save at the end of each of its turns to end the effect.

**Source:** `= this.source` (`= this.source-type`)
