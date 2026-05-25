---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 360}"
usage: "wornbelt"
bulk: "—"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This 6-foot-long scarf shimmers with the silvery light of the River of Souls while worn, providing illumination equivalent to that of a candle. You can deactivate or activate this radiance as an Interact action. The dangling lengths of a *ghost scarf* softly billow in the presence of haunts, granting the wearer a +1 item bonus to all Perception checks and Perception DCs to resolve discovering a haunt or rolling initiative when a haunt triggers.

**Activate—Ghost Slayer's Caress** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** The scarf extends silvery threads that wrap around a weapon you carry, granting the effects of a [[Ghost Touch]] property rune to that weapon for 5 minutes. If the weapon already bears a *ghost touch* rune, you instead gain a +1 item bonus to Fortitude saves against effects from incorporeal undead for 5 minutes.

> [!danger] Effect: Ghost Scarf

**Source:** `= this.source` (`= this.source-type`)
