---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Graft]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 60}"
usage: "implanted"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Your exposed skin is covered in fine, needle-like hairs that you can flick into the eyes of enemies.

**Activate—Urticating Burst** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** You flick tiny spines in a @Template[cone|distance:15], dealing @Damage[2d8[piercing]|options:area-damage] damage to all creatures in the area with a DC 18 [[Reflex]] save. On a critical failure, the creature is also [[Dazzled]] until the end of their next turn.

**Source:** `= this.source` (`= this.source-type`)
