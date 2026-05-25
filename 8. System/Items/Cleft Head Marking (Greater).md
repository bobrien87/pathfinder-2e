---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 850}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder #207: The Resurrection Flood"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Caution and misdirection are the hallmarks of your hold. You've encountered more travelers than most of Belkzen's holds ever see, and you need to understand how to deal with them. You're a proud member of the Cleft Head Hold or have been found worthy of wearing their mark. This tattoo is a crooked line that begins high above one eye and zigzags toward your mouth. The tattoo's grim appearance can help mask your true motivations. You gain a +2 item bonus to Deception checks to [[Feint]].

**Activate—Unexpected Strike** `pf2:f` (concentrate)

**Frequency** once per day

**Trigger** You Strike a creature that has the [[Off Guard]] condition with a weapon attack

**Effect** You deal an extra 2d6 precision damage to the target.

**Source:** `= this.source` (`= this.source-type`)
