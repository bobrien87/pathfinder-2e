---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 625}"
bulk: "L"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 resilient leather armor* is made from drake hide, and includes wing-like membranes that connect the limbs to one another. Originally designed to allow riders of aerial mounts to safely dismount if the need arises, such wingsuits remain uncommon but have gained some popularity among thrill-seeking adventurers and some mountain-dwelling communities.

**Activate—Drake's Glide** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You take 2 move actions, each of which can be a Fly or Stride. If you don't have a fly Speed, you gain a 20-foot fly Speed for Fly actions from this activation.

**Activate—Descend** `pf2:r` (concentrate, manipulate)

**Frequency** once per 10 minutes

**Trigger** You're falling

**Effect** Your fall slows to 60 feet per round for 1 minute, and if you reach the ground during this time you take no damage from the fall.

**Source:** `= this.source` (`= this.source-type`)
