---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 4}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Popular with lovers, decorators, and sports fans, the seeds of these ephemeral plants grow and bloom immediately into flowers when placed in any warm environment, including a cup of dirt, a bowl of warm water, and a tightly clenched hand. The color of these flowers varies, but each has an internal glow that sheds bright light in a 30-foot radius. The radius of this light shrinks by 10 feet every 20 minutes. At the end of an hour, the plant disintegrates, leaving only a vaguely pleasant scent in the air.

**Source:** `= this.source` (`= this.source-type`)
