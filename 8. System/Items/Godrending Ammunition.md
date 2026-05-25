---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 440}"
bulk: "—"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Embedded in this piece of ammunition is a shining sliver of a warshard. When an activated godrending ammunition hits a target, the body of the struck creature attempts to tear itself apart, causing nauseating pain. Instead of its normal damage, the ammunition deals 10d8 slashing damage. The target can attempt a DC 30 [[Fortitude]] save saving throw; it takes a –2 circumstance penalty to this save if the Strike was a critical hit.
- **Critical Success** The foe takes the normal damage from the ammunition, instead of the 10d8 slashing damage.
- **Success** The foe takes half damage.
- **Failure** The foe takes full damage and is [[Sickened]] 1.
- **Critical Failure** The foe takes double damage and is [[Sickened]] 2. A creature reduced to 0 HP from this damage is ripped limb from limb, and it instantly dies; its gear remains.

**Source:** `= this.source` (`= this.source-type`)
