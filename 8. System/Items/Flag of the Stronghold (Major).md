---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Aura]]", "[[Magical]]"]
price: "{'gp': 70000}"
usage: "affixed-or-held-in-one-hand"
bulk: "—"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This magical banner is off-white with a depiction of a stronghold that's often colored in a striking blue. Those who stand under the banner are prepared to face the weapons of war and defend their keep until the end. You and allies within the banner's aura gain resistance 10 to damage from siege weapons.

**Source:** `= this.source` (`= this.source-type`)
