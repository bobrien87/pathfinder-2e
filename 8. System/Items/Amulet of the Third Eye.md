---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Apex]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 15000}"
usage: "worn"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This large brass medallion hangs low on the torso. It's shaped in the form of an unblinking eye, with a ring of turquoise as the iris and an orb of jet serving as the pupil. The amulet grants you a +2 item bonus to Perception checks. When you invest the amulet, you either increase your Wisdom modifier by 1 or increase it to +4, whichever would give you a higher value.

**Activate** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** You cast [[Truesight]].

**Source:** `= this.source` (`= this.source-type`)
