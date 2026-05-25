---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 1200}"
usage: "worn"
bulk: "—"
source: "Pathfinder #210: Whispers in the Dirt"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This silver brooch features an enormous freshwater pearl pulled from the depths of Lake Encarthan. They are often given to trading partners among Drumish merchants as a sign of favor—not as favored as a fellow Kalistocrat, but nonetheless worth treating well. Openly wearing a *Drumish pearl token* can work wonders when traveling through Druma, whether on legitimate mercantile business or not, but those who flaunt the token inappropriately must beware of repercussions from the Drumish government! The wearer of a *Drumish pearl token* benefits from a +2 item bonus to Diplomacy checks to [[Make an Impression]] and to their Perception DC when someone attempts to Lie to them.

**Activate—Subversive Friendship** `pf2:r` (concentrate, emotion, mental)

**Frequency** once per day

**Trigger** You succeed at [[Making an Impression]]

**Effect** You automatically increase the target's attitude to helpful. If the target's initial attitude was unfriendly or hostile, they revert to this attitude after 10 minutes and realize they've been manipulated by you. Afterward, they might decide to act against you.

**Source:** `= this.source` (`= this.source-type`)
